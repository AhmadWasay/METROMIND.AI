# backend/graph_engine.py - Transit routing engine for Islamabad-Rawalpindi
import networkx as nx
import math
from transit_data import (
    METRO_STATIONS, BUS_STOPS, ALL_STOPS, BUS_ROUTES, 
    TRANSFER_HUBS, TIMETABLE, LINE_COLORS
)

class TransitGraph:
    def __init__(self):
        self.graph = nx.DiGraph()
        self.metro_lines = {}
        self.bus_routes = {}
        self._build_real_transit_network()

    def _build_real_transit_network(self):
        """Build the full Islamabad/Rawalpindi transit network"""
        
        # Add all nodes (metro stations + bus stops)
        for station in METRO_STATIONS:
            self.graph.add_node(
                station['code'],
                name=station['name'],
                lat=station['coordinates']['lat'],
                lng=station['coordinates']['lng'],
                line=station['line'],
                type='metro'
            )
        
        for stop in BUS_STOPS:
            self.graph.add_node(
                stop['code'],
                name=stop['name'],
                lat=stop['coordinates']['lat'],
                lng=stop['coordinates']['lng'],
                area=stop.get('area', 'Area'),
                type='bus'
            )
        
        # Organize metro stations by line
        for station in METRO_STATIONS:
            line = station['line']
            if line not in self.metro_lines:
                self.metro_lines[line] = []
            self.metro_lines[line].append(station)
        
        # Connect metro stations on the same line
        for line, stations in self.metro_lines.items():
            for i in range(len(stations) - 1):
                curr = stations[i]
                next_st = stations[i + 1]
                distance = self._calculate_distance(
                    curr['coordinates']['lat'], curr['coordinates']['lng'],
                    next_st['coordinates']['lat'], next_st['coordinates']['lng']
                )
                # Transit time estimate: ~2 minutes per km on metro
                time_mins = max(2, distance * 2)
                
                # Bidirectional metro
                # Use specific line fare if present, otherwise fall back to BRT_Lines or default 50
                metro_fare = TIMETABLE.get(line, {}).get('fare', TIMETABLE.get('BRT_Lines', {}).get('fare', 50))
                self.graph.add_edge(
                    curr['code'], next_st['code'],
                    weight=time_mins,
                    distance=distance,
                    type='metro',
                    line=line,
                    fare=metro_fare
                )
                self.graph.add_edge(
                    next_st['code'], curr['code'],
                    weight=time_mins,
                    distance=distance,
                    type='metro',
                    line=line,
                    fare=metro_fare
                )
        
        # Add transfer connections between metro lines at nearby stations
        metro_list = list(self.metro_lines.values())
        for i, line1_stations in enumerate(metro_list):
            for j, line2_stations in enumerate(metro_list):
                if i < j:  # Avoid duplicate connections
                    for st1 in line1_stations:
                        for st2 in line2_stations:
                            distance = self._calculate_distance(
                                st1['coordinates']['lat'], st1['coordinates']['lng'],
                                st2['coordinates']['lat'], st2['coordinates']['lng']
                            )
                            # Consider transfers if within 1.5 km (walking distance)
                            if distance < 1.5:
                                walking_time = self._estimate_walking_time(distance)
                                transfer_time = max(3, walking_time)  # Min 3 mins transfer
                                self.graph.add_edge(
                                    st1['code'], st2['code'],
                                    weight=transfer_time,
                                    distance=distance,
                                    type='transfer',
                                    line=f"{st1['line']} ↔ {st2['line']}"
                                )
                                self.graph.add_edge(
                                    st2['code'], st1['code'],
                                    weight=transfer_time,
                                    distance=distance,
                                    type='transfer',
                                    line=f"{st2['line']} ↔ {st1['line']}"
                                )
        
        # Connect bus route stops
        for route in BUS_ROUTES:
            route_code = route['code']
            stops = route['stops']
            self.bus_routes[route_code] = route
            
            for i in range(len(stops) - 1):
                source_code = stops[i]
                target_code = stops[i + 1]
                
                # Find actual stop info to get coordinates
                source_stop = self._find_stop(source_code)
                target_stop = self._find_stop(target_code)
                
                if source_stop and target_stop:
                    distance = self._calculate_distance(
                        source_stop['coordinates']['lat'], source_stop['coordinates']['lng'],
                        target_stop['coordinates']['lat'], target_stop['coordinates']['lng']
                    )
                    # Bus time: ~4 minutes per km
                    time_mins = max(3, distance * 4)
                    
                    self.graph.add_edge(
                        source_code, target_code,
                        weight=time_mins,
                        distance=distance,
                        type='bus',
                        route=route_code,
                        line=route['name'],
                        fare=route['fare']
                    )
        
        # Add walking transfer connections between nearby stops and stations
        self._add_transfer_edges()

    def _add_transfer_edges(self):
        nodes = list(self.graph.nodes(data=True))
        for i, (code_a, data_a) in enumerate(nodes):
            for code_b, data_b in nodes[i + 1:]:
                if code_a == code_b:
                    continue
                if self.graph.has_edge(code_a, code_b) or self.graph.has_edge(code_b, code_a):
                    continue

                distance = self._calculate_distance(
                    data_a['lat'], data_a['lng'],
                    data_b['lat'], data_b['lng']
                )
                if distance <= 2.0:
                    walking_time = max(1, self._estimate_walking_time(distance))
                    self.graph.add_edge(
                        code_a, code_b,
                        weight=walking_time,
                        distance=distance,
                        type='walk',
                        line='walk'
                    )
                    self.graph.add_edge(
                        code_b, code_a,
                        weight=walking_time,
                        distance=distance,
                        type='walk',
                        line='walk'
                    )

    def _find_stop(self, code):
        """Find a stop by code in either metros or bus stops"""
        for station in METRO_STATIONS:
            if station['code'] == code:
                return station
        for stop in BUS_STOPS:
            if stop['code'] == code:
                return stop
        return None
    
    def _calculate_distance(self, lat1, lng1, lat2, lng2):
        """Calculate distance in km using Haversine formula"""
        R = 6371
        lat1_rad = math.radians(lat1)
        lat2_rad = math.radians(lat2)
        delta_lat = math.radians(lat2 - lat1)
        delta_lng = math.radians(lng2 - lng1)
        
        a = math.sin(delta_lat/2)**2 + math.cos(lat1_rad) * math.cos(lat2_rad) * math.sin(delta_lng/2)**2
        c = 2 * math.asin(math.sqrt(a))
        return R * c
    
    def _estimate_walking_time(self, distance_km):
        """Estimate walking time in minutes (1.4 m/s = 5.04 km/h)"""
        if distance_km <= 0.05:
            return 0
        return (distance_km * 60) / 5.04
    
    def find_shortest_path(self, source, target, optimization="time"):
        """Find optimal trip between two locations"""
        try:
            # Normalize location names
            source_code = self._find_location_code(source)
            target_code = self._find_location_code(target)
            
            if not source_code or not target_code:
                return {
                    'status': 'error',
                    'message': 'Location not found. Please select from available stops.'
                }
            
            if source_code == target_code:
                return {
                    'status': 'error',
                    'message': 'Source and destination are the same.'
                }
            
            # Find path
            if not nx.has_path(self.graph, source_code, target_code):
                return {
                    'status': 'error',
                    'message': 'No route found between these locations.'
                }
            
            path = nx.shortest_path(self.graph, source_code, target_code, weight='weight')
            total_time = nx.shortest_path_length(self.graph, source_code, target_code, weight='weight')
            
            # Build journey segments
            segments = []
            total_fare = 0
            metro_used = False
            walking_details = []
            
            for i in range(len(path) - 1):
                curr_code = path[i]
                next_code = path[i + 1]
                edge_data = self.graph[curr_code][next_code]
                
                curr_stop = self._find_stop(curr_code)
                next_stop = self._find_stop(next_code)
                
                distance = edge_data.get('distance', 0)
                time = edge_data.get('weight', 0)
                
                # Check if we can collapse with the previous continuous segment
                if segments and segments[-1].get('line') == edge_data.get('line') and segments[-1]['type'] != 'walk':
                    segments[-1]['to'] = next_stop['name']
                    segments[-1]['distance_km'] = round(segments[-1]['distance_km'] + distance, 2)
                    segments[-1]['time_mins'] += int(time)
                    
                    if 'intermediate_stops' not in segments[-1]:
                        segments[-1]['intermediate_stops'] = []
                    
                    # Add the intermediate station we just passed through
                    segments[-1]['intermediate_stops'].append(curr_stop['name'])
                    
                    stops_list = segments[-1]['intermediate_stops']
                    base_desc = f"{segments[-1]['line']} Metro" if segments[-1]['type'] == 'metro' else f"Bus Route {segments[-1].get('route', '')}"
                    
                    # Show specific station names if it's a short hop, otherwise show total stop count
                    if len(stops_list) <= 3:
                        stops_str = ", ".join(stops_list)
                        segments[-1]['description'] = f"{base_desc} (via {stops_str})"
                    else:
                        segments[-1]['description'] = f"{base_desc} ({len(stops_list)} stops)"
                        
                else:
                    # Create a new segment branch
                    if edge_data['type'] == 'metro':
                        line = edge_data['line']
                        if not metro_used:
                            # Metro fare: prefer line-specific fare, otherwise use BRT_Lines fallback
                            total_fare += TIMETABLE.get(line, {}).get('fare', TIMETABLE.get('BRT_Lines', {}).get('fare', 50))
                            metro_used = True
                        
                        segments.append({
                            'type': 'metro',
                            'line': line,
                            'from': curr_stop['name'],
                            'to': next_stop['name'],
                            'distance_km': round(distance, 2),
                            'time_mins': int(time),
                            'description': f'{line} Metro'
                        })
                    
                    elif edge_data['type'] == 'bus':
                        route = edge_data['route']
                        fare = edge_data.get('fare', 25)
                        segments.append({
                            'type': 'bus',
                            'route': route,
                            'line': edge_data['line'],
                            'from': curr_stop['name'],
                            'to': next_stop['name'],
                            'distance_km': round(distance, 2),
                            'time_mins': int(time),
                            'description': f'Bus Route {route}'
                        })
                        total_fare += fare  # Only charges once per continuous bus ride now!
                    
                    elif edge_data['type'] == 'walk':
                        segments.append({
                            'type': 'walk',
                            'line': 'walk',
                            'from': curr_stop['name'],
                            'to': next_stop['name'],
                            'distance_km': round(distance, 2),
                            'time_mins': int(time),
                            'description': 'Walk'
                        })
            
            # Total fare is metro flat fare + bus fares
            
            # Calculate walking distances
            walking_km = 0
            if len(path) > 0:
                # Walking from source to first transit stop (estimate)
                source_stop = self._find_stop(source_code)
                if source_stop:
                    walking_km += 0.3  # Assume walking to first stop
                
                # Walking from last transit stop to destination
                target_stop = self._find_stop(target_code)
                if target_stop:
                    walking_km += 0.3
            
            walking_time = self._estimate_walking_time(walking_km)
            
            transfer_count = sum(
                1 for i in range(1, len(segments))
                if segments[i]['line'] != segments[i-1]['line']
            )
            return {
                'status': 'success',
                'packages': [{
                    'name': '⚡ Recommended Route',
                    'description': f'Journey with {transfer_count} transfers, {round(walking_km, 2)}km walking',
                    'path': [self._find_stop(c)['name'] for c in path],
                    'journey_segments': segments,
                    'lines_used': list({s['line'] for s in segments}),
                    'transfers': transfer_count,
                    'estimated_cost': total_fare,
                    'estimated_time_minutes': int(total_time + walking_time),
                    'transit_time_mins': int(total_time),
                    'walking_time_mins': int(walking_time),
                    'walking_details': [
                        {
                            'type': 'to_first_station',
                            'distance_km': 0.3,
                            'time_mins': int(self._estimate_walking_time(0.3))
                        },
                        {
                            'type': 'from_last_station',
                            'distance_km': 0.3,
                            'time_mins': int(self._estimate_walking_time(0.3))
                        }
                    ]
                }]
            }
        
        except Exception as e:
            return {
                'status': 'error',
                'message': f'Error planning trip: {str(e)}'
            }
    
    def _find_location_code(self, location_name):
        """Find location code by name"""
        search_name = location_name.lower().replace(' ', '_')
        
        for station in METRO_STATIONS:
            if station['code'].lower() == search_name or station['name'].lower().replace(' ', '_') == search_name:
                return station['code']
        
        for stop in BUS_STOPS:
            if stop['code'].lower() == search_name or stop['name'].lower().replace(' ', '_') == search_name:
                return stop['code']
        
        return None

# Initialize global transit graph
transit_engine = TransitGraph()
