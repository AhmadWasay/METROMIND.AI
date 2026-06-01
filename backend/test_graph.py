from graph_engine import transit_engine
from transit_data import METRO_STATIONS, BUS_STOPS

print(f'Nodes: {transit_engine.graph.number_of_nodes()}')
print(f'Edges: {transit_engine.graph.number_of_edges()}')
# Use available metro station codes from transit data (dynamic)
metro_codes = [s['code'] for s in METRO_STATIONS]
if metro_codes:
    print(f'First metro: {metro_codes[0]}, Last metro: {metro_codes[-1]}')
    try:
        print(f'{metro_codes[0]} neighbors: {list(transit_engine.graph.neighbors(metro_codes[0]))}')
    except Exception:
        print(f'No neighbors for {metro_codes[0]}')
else:
    print('No metro stations defined in METRO_STATIONS')

# Test path finding
import networkx as nx
try:
    if len(metro_codes) >= 2:
        src = metro_codes[0]
        dst = metro_codes[-1]
        has_path = nx.has_path(transit_engine.graph, src, dst)
        print(f'Has path from {src} to {dst}: {has_path}')
        if has_path:
            path = nx.shortest_path(transit_engine.graph, src, dst, weight='weight')
            print(f'Path: {path}')
    else:
        print('Not enough metro stations to test routing')
except Exception as e:
    print(f'Error: {e}')

# Distance checks for transfers
import math

def distance(a, b):
    lat1, lng1 = a
    lat2, lng2 = b
    R = 6371
    return R * 2 * math.asin(math.sqrt(
        math.sin(math.radians(lat2 - lat1) / 2) ** 2 +
        math.cos(math.radians(lat1)) * math.cos(math.radians(lat2)) *
        math.sin(math.radians(lng2 - lng1) / 2) ** 2
    ))

for code in ['RED_PIMS', 'ORG_NUST', 'BLU_Gulberg', 'GRN_Jillani', 'RED_Saddar']:
    item = next((x for x in METRO_STATIONS if x['code'] == code), None)
    if not item:
        continue
    print(f'\nDistances from {code} ({item["name"]}):')
    for stop in BUS_STOPS:
        dist = distance((item['coordinates']['lat'], item['coordinates']['lng']),
                        (stop['coordinates']['lat'], stop['coordinates']['lng']))
        if dist < 2.5:
            print(f'  {stop["code"]} {stop["name"]}: {dist:.2f} km')

print('\nRoute planning test: RED_Saddar -> ORG_NUST')
route_result = transit_engine.find_shortest_path('RED_Saddar', 'ORG_NUST', optimization='time')
print(route_result)
