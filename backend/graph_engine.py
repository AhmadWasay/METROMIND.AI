import networkx as nx
import math
from transit_data import (
    METRO_STATIONS, BUS_STOPS, ALL_STOPS, BUS_ROUTES, 
    TRANSFER_HUBS, TIMETABLE, LINE_COLORS
)

class TransitGraph:
    def __init__(self):
        # UPGRADE: MultiDiGraph allows parallel overlapping routes (Bus and Metro sharing tracks)
        self.graph = nx.MultiDiGraph()
        self.metro_lines = {}
        self.bus_routes = {}
        self._build_real_transit_network()

    def _build_real_transit_network(self):
        """Build the full Islamabad/Rawalpindi transit network based on logical topology"""
        
        # 1. Add all nodes
        for station in METRO_STATIONS:
            self.graph.add_node(
                station['code'],
                name=station['name'],
                lat=station['coordinates']['lat'],
                lng=station['coordinates']['lng'],
                line=station['line'],
                type='metro'
            )
            
            line = station['line']
            if line not in self.metro_lines:
                self.metro_lines[line] = []
            self.metro_lines[line].append(station)
        
        for stop in BUS_STOPS:
            self.graph.add_node(
                stop['code'],
                name=stop['name'],
                lat=stop['coordinates']['lat'],
                lng=stop['coordinates']['lng'],
                area=stop.get('area', 'Area'),
                type='bus'
            )
        
        # 2. Connect metro stations on the same line
        for line, stations in self.metro_lines.items():
            for i in range(len(stations) - 1):
                curr = stations[i]
                next_st = stations[i + 1]
                distance = self._calculate_distance(
                    curr['coordinates']['lat'], curr['coordinates']['lng'],
                    next_st['coordinates']['lat'], next_st['coordinates']['lng']
                )
                
                time_mins = max(2, distance * 2.0)
                metro_fare = TIMETABLE.get(line, {}).get('fare', TIMETABLE.get('BRT_Lines', {}).get('fare', 50))
                
                for src, dst in [(curr, next_st), (next_st, curr)]:
                    self.graph.add_edge(
                        src['code'], dst['code'],
                        weight=time_mins,
                        distance=distance,
                        type='metro',
                        line=line,
                        fare=metro_fare
                    )
        
        # 3. Connect bus route stops
        for route in BUS_ROUTES:
            route_code = route['code']
            stops = route['stops']
            self.bus_routes[route_code] = route
            
            for i in range(len(stops) - 1):
                source_code = stops[i]
                target_code = stops[i + 1]
                
                source_stop = self._find_stop(source_code)
                target_stop = self._find_stop(target_code)
                
                if source_stop and target_stop:
                    distance = self._calculate_distance(
                        source_stop['coordinates']['lat'], source_stop['coordinates']['lng'],
                        target_stop['coordinates']['lat'], target_stop['coordinates']['lng']
                    )
                    
                    time_mins = max(3, distance * 4.0)
                    
                    self.graph.add_edge(
                        source_code, target_code,
                        weight=time_mins,
                        distance=distance,
                        type='bus',
                        route=route_code,
                        line=route.get('name', f"Route {route_code}"),
                        fare=route.get('fare', 50)
                    )
        
        # 4. Generate Logical Transfers
        self._add_logical_transfers()
        
        # 5. Add short-distance walking connections
        self._add_feeder_walking_edges()

    def _edge_exists_with_type(self, u, v, e_type):
        """Helper for MultiDiGraph to prevent duplicate transfer/walk edges"""
        if not self.graph.has_edge(u, v):
            return False
        for key, data in self.graph[u][v].items():
            if data.get('type') == e_type:
                return True
        return False

    def _add_logical_transfers(self):
        nodes = list(self.graph.nodes(data=True))
        transfer_penalty_mins = 5.0 

        for i, (code_a, data_a) in enumerate(nodes):
            for code_b, data_b in nodes[i + 1:]:
                is_same_name = data_a.get('name', '').lower() == data_b.get('name', '').lower()
                is_explicit_hub = (code_a, code_b) in TRANSFER_HUBS or (code_b, code_a) in TRANSFER_HUBS

                if is_same_name or is_explicit_hub:
                    if not self._edge_exists_with_type(code_a, code_b, 'transfer'):
                        self.graph.add_edge(
                            code_a, code_b,
                            weight=transfer_penalty_mins, distance=0.0, type='transfer',
                            line=f"Transfer: {data_a.get('line', 'Bus')} ↔ {data_b.get('line', 'Bus')}"
                        )
                        self.graph.add_edge(
                            code_b, code_a,
                            weight=transfer_penalty_mins, distance=0.0, type='transfer',
                            line=f"Transfer: {data_b.get('line', 'Bus')} ↔ {data_a.get('line', 'Bus')}"
                        )

    def _add_feeder_walking_edges(self):
        nodes = list(self.graph.nodes(data=True))
        max_walk_km = 0.3 

        for i, (code_a, data_a) in enumerate(nodes):
            for code_b, data_b in nodes[i + 1:]:
                if self.graph.has_edge(code_a, code_b):
                    continue

                distance = self._calculate_distance(
                    data_a['lat'], data_a['lng'], data_b['lat'], data_b['lng']
                )
                
                if distance <= max_walk_km:
                    walking_time = max(1, self._estimate_walking_time(distance))
                    for src, dst in [(code_a, code_b), (code_b, code_a)]:
                        self.graph.add_edge(
                            src, dst,
                            weight=walking_time, distance=distance,
                            type='walk', line='walk'
                        )

    def _find_stop(self, code):
        for station in METRO_STATIONS:
            if station['code'] == code: return station
        for stop in BUS_STOPS:
            if stop['code'] == code: return stop
        return None
    
    def _calculate_distance(self, lat1, lng1, lat2, lng2):
        R = 6371 
        lat1_rad, lat2_rad = math.radians(lat1), math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lng = math.radians(lng2 - lng1)
        
        a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lng/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    def _estimate_walking_time(self, distance_km):
        if distance_km <= 0.05: return 0
        return (distance_km * 60) / 5.04 
    
    def find_shortest_path(self, source, target, optimization="time"):
        try:
            source_code = self._find_location_code(source)
            target_code = self._find_location_code(target)
            
            if not source_code or not target_code:
                return {'status': 'error', 'message': 'Location not found.'}
            if source_code == target_code:
                return {'status': 'error', 'message': 'Source and destination are the same.'}
            if not nx.has_path(self.graph, source_code, target_code):
                return {'status': 'error', 'message': 'No route found between these locations.'}
            
            path = nx.shortest_path(self.graph, source_code, target_code, weight='weight')
            total_time = nx.shortest_path_length(self.graph, source_code, target_code, weight='weight')
            
            segments = []
            total_fare = 0
            metro_used = False
            current_bus_route = None
            active_line = None
            
            for i in range(len(path) - 1):
                curr_code, next_code = path[i], path[i + 1]
                
                # Retrieve all overlapping edges between these two nodes
                edge_dict = self.graph[curr_code][next_code]
                
                # Sort by weight so the fastest edge is the default choice
                available_edges = sorted(edge_dict.values(), key=lambda x: x.get('weight', float('inf')))
                best_edge = available_edges[0]
                
                # LINE AFFINITY HEURISTIC: Prevent phantom transfers by prioritizing the current line
                if active_line:
                    for e in available_edges:
                        if e.get('line') == active_line:
                            # Accept staying on the line as long as it isn't drastically slower (> 3 mins)
                            if e.get('weight', 0) <= best_edge.get('weight', 0) + 3.0:
                                best_edge = e
                                break
                                
                edge_data = best_edge
                active_line = edge_data.get('line')
                e_type = edge_data['type']
                
                curr_stop = self._find_stop(curr_code)
                next_stop = self._find_stop(next_code)
                
                dist = edge_data.get('distance', 0)
                time = edge_data.get('weight', 0)
                
                if e_type == 'metro':
                    if not metro_used:
                        total_fare += edge_data.get('fare', 50)
                        metro_used = True
                    current_bus_route = None
                    segments.append(self._format_segment(e_type, active_line, curr_stop, next_stop, dist, time))
                    
                elif e_type == 'bus':
                    route = edge_data['route']
                    if current_bus_route != route:
                        total_fare += edge_data.get('fare', 50)
                        current_bus_route = route
                    segments.append(self._format_segment(e_type, active_line, curr_stop, next_stop, dist, time))
                    
                elif e_type in ['walk', 'transfer']:
                    desc = 'Walk' if e_type == 'walk' else active_line
                    segments.append(self._format_segment(e_type, desc, curr_stop, next_stop, dist, time))

            walking_segments = [s for s in segments if s['type'] == 'walk']
            intermediate_walking_km = sum(s['distance_km'] for s in walking_segments)
            
            endpoint_walking_km = 0.6 if len(path) > 0 else 0
            endpoint_walking_time = int(self._estimate_walking_time(endpoint_walking_km))
            
            # Transfer math is now accurate because Line Affinity prevents bouncing
            transit_lines = [s['line'] for s in segments if s['type'] in ['metro', 'bus']]
            transfer_count = sum(1 for i in range(1, len(transit_lines)) if transit_lines[i] != transit_lines[i-1])

            return {
                'status': 'success',
                'packages': [{
                    'name': '⚡ Recommended Route',
                    'description': f'Journey with {transfer_count} transfers, {round(intermediate_walking_km + endpoint_walking_km, 2)}km walking',
                    'path': [self._find_stop(c)['name'] for c in path],
                    'journey_segments': segments,
                    'transfers': transfer_count,
                    'estimated_cost': total_fare,
                    'estimated_time_minutes': int(total_time + endpoint_walking_time)
                }]
            }
            
        except Exception as e:
            return {'status': 'error', 'message': f'Error planning trip: {str(e)}'}

    def _format_segment(self, segment_type, line_desc, curr_stop, next_stop, dist, time):
        return {
            'type': segment_type,
            'line': line_desc,
            'from': curr_stop['name'],
            'to': next_stop['name'],
            'distance_km': round(dist, 2),
            'time_mins': int(time),
            'description': f'{line_desc}' if segment_type != 'walk' else 'Walk / Transfer'
        }

    def _find_location_code(self, location_name):
        search_name = location_name.lower().replace(' ', '_')
        for stop_list in [METRO_STATIONS, BUS_STOPS]:
            for stop in stop_list:
                if stop['code'].lower() == search_name or stop['name'].lower().replace(' ', '_') == search_name:
                    return stop['code']
        return None

transit_engine = TransitGraph()