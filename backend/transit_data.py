# Transit data for Islamabad/Rawalpindi public transport system
# Based on official RMBS (Rawalpindi Metro Bus Service) and CDA Feeder Route Network 
# Data extracted from Dec 2025 Map, Route List, and FR Stops data.

# ===== METRO/RAPID TRANSIT STATIONS (BRT Core Network) =====
METRO_STATIONS = [
    # RED LINE (Saddar to Secretariat)
    {'code': 'RED_Saddar', 'name': 'Saddar Station', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.593, 'lng': 73.053}},
    {'code': 'RED_Liaquat', 'name': 'Liaquat Bagh', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.602, 'lng': 73.060}},
    {'code': 'RED_Faizabad', 'name': 'Faizabad', 'line': 'Red Line', 'type': 'metro', 'area': 'IJP Road', 'coordinates': {'lat': 33.640, 'lng': 73.085}},
    {'code': 'RED_FaizAhmad', 'name': 'Faiz Ahmad Faiz', 'line': 'Red Line', 'type': 'metro', 'area': 'H-8', 'coordinates': {'lat': 33.669, 'lng': 73.054}},
    {'code': 'RED_PIMS', 'name': 'PIMS Hospital', 'line': 'Red Line', 'type': 'metro', 'area': 'G-8/F-8', 'coordinates': {'lat': 33.705, 'lng': 73.048}},
    {'code': 'RED_Secretariat', 'name': 'Secretariat Station', 'line': 'Red Line', 'type': 'metro', 'area': 'Red Zone', 'coordinates': {'lat': 33.731, 'lng': 73.097}},
    
    # ORANGE LINE (Faiz Ahmad Faiz to Airport)
    {'code': 'ORG_G10', 'name': 'G-10 Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-10', 'coordinates': {'lat': 33.652, 'lng': 73.012}},
    {'code': 'ORG_NUST', 'name': 'NUST Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'H-12', 'coordinates': {'lat': 33.641, 'lng': 72.986}},
    {'code': 'ORG_Golra', 'name': 'Golra Morh Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'Golra', 'coordinates': {'lat': 33.633, 'lng': 72.973}},
    {'code': 'ORG_N5', 'name': 'N-5 Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'N-5 Highway', 'coordinates': {'lat': 33.612, 'lng': 72.932}},
    {'code': 'ORG_Airport', 'name': 'Islamabad Int. Airport', 'line': 'Orange Line', 'type': 'metro', 'area': 'Airport', 'coordinates': {'lat': 33.551, 'lng': 72.827}},
    
    # BLUE LINE (PIMS to Gulberg)
    {'code': 'BLU_Gulberg', 'name': 'Gulberg', 'line': 'Blue Line', 'type': 'metro', 'area': 'Gulberg Greens', 'coordinates': {'lat': 33.604, 'lng': 73.151}},
    
    # GREEN LINE (PIMS to Bhara Kahu)
    {'code': 'GRN_Jillani', 'name': 'Jillani, Bhara Kahu', 'line': 'Green Line', 'type': 'metro', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.755, 'lng': 73.168}},
]

# ===== BUS STOPS (Feeder Route Nodes) =====
BUS_STOPS = [
    {'code': 'FR_KhannaPul', 'name': 'Khanna Pul', 'type': 'bus', 'area': 'Islamabad Expressway', 'coordinates': {'lat': 33.626, 'lng': 73.111}},
    {'code': 'FR_Saidpur', 'name': 'Saidpur Village / Faisal Masjid', 'type': 'bus', 'area': 'F-7/E-7', 'coordinates': {'lat': 33.743, 'lng': 73.067}},
    {'code': 'FR_BariImam', 'name': 'Bari Imam', 'type': 'bus', 'area': 'Diplomatic Enclave', 'coordinates': {'lat': 33.748, 'lng': 73.116}},
    {'code': 'FR_QAU', 'name': 'Quaid-e-Azam University', 'type': 'bus', 'area': 'QAU Campus', 'coordinates': {'lat': 33.747, 'lng': 73.138}},
    {'code': 'FR_E11', 'name': 'E-11 Markaz / Golra Shareef', 'type': 'bus', 'area': 'E-11', 'coordinates': {'lat': 33.702, 'lng': 72.981}},
    {'code': 'FR_Tramri', 'name': 'Tramri Chowk', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.668, 'lng': 73.154}},
    {'code': 'FR_Nilore', 'name': 'Nilore', 'type': 'bus', 'area': 'Nilore', 'coordinates': {'lat': 33.652, 'lng': 73.256}},
    {'code': 'FR_Taxila', 'name': 'Taxila Highway Stop', 'type': 'bus', 'area': 'Taxila', 'coordinates': {'lat': 33.745, 'lng': 72.805}},
    {'code': 'FR_I16', 'name': 'Noon, I-16', 'type': 'bus', 'area': 'I-16', 'coordinates': {'lat': 33.597, 'lng': 72.946}},
    {'code': 'FR_FatehJang', 'name': 'Fateh Jang', 'type': 'bus', 'area': 'Fateh Jang Road', 'coordinates': {'lat': 33.568, 'lng': 72.645}},
    {'code': 'FR_Rawat', 'name': 'T Chowk / Rawat', 'type': 'bus', 'area': 'Rawat', 'coordinates': {'lat': 33.499, 'lng': 73.195}},
    {'code': 'FR_MediaTown', 'name': 'Media Town', 'type': 'bus', 'area': 'PWD/Media Town', 'coordinates': {'lat': 33.578, 'lng': 73.136}},
    {'code': 'FR_MandiMorh', 'name': 'Mandi Morh', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.761, 'lng': 73.181}},
]

# Combined list of all stops
ALL_STOPS = METRO_STATIONS + BUS_STOPS

# ===== BUS ROUTES (CDA Feeder Routes & BRT) =====
BUS_ROUTES = [
    # BRT Core Routes
    {
        'code': 'BRT_RED', 'name': 'Red Line: Saddar - Secretariat', 'operator': 'RMBS', 'type': 'brt',
        'stops': ['RED_Saddar', 'RED_Liaquat', 'RED_Faizabad', 'RED_FaizAhmad', 'RED_PIMS', 'RED_Secretariat'], 'fare': 50
    },
    {
        'code': 'BRT_ORANGE', 'name': 'Orange Line: Faiz Ahmad Faiz - Airport', 'operator': 'RMBS', 'type': 'brt',
        'stops': ['RED_FaizAhmad', 'ORG_G10', 'ORG_NUST', 'ORG_Golra', 'ORG_N5', 'ORG_Airport'], 'fare': 50
    },
    
    # Islamabad Feeder Routes (FR)
    {
        'code': 'FR_1', 'name': 'FR-1: Khanna Pul - NUST Metro Station', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['FR_KhannaPul', 'ORG_NUST'], 'fare': 50
    },
    {
        'code': 'FR_3A', 'name': 'FR-3A: PIMS Gate - Saidpur/Faisal Masjid', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['RED_PIMS', 'FR_Saidpur'], 'fare': 50
    },
    {
        'code': 'FR_4', 'name': 'FR-4: PIMS Gate - Bari Imam', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['RED_PIMS', 'FR_BariImam'], 'fare': 50
    },
    {
        'code': 'FR_4A', 'name': 'FR-4A: Bari Imam - Quaid-e-Azam University', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['FR_BariImam', 'FR_QAU'], 'fare': 50
    },
    {
        'code': 'FR_6', 'name': 'FR-6: PIMS Gate - E-11 Markaz', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['RED_PIMS', 'FR_E11'], 'fare': 50
    },
    {
        'code': 'FR_7', 'name': 'FR-7: PIMS Gate - G-10 Metro Station', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['RED_PIMS', 'ORG_G10'], 'fare': 50
    },
    {
        'code': 'FR_8A', 'name': 'FR-8A: PIMS Gate - Tramri Chowk', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['RED_PIMS', 'FR_Tramri'], 'fare': 50
    },
    {
        'code': 'FR_8B', 'name': 'FR-8B: Khanna Pul - Nilore', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['FR_KhannaPul', 'FR_Nilore'], 'fare': 50
    },
    {
        'code': 'FR_9', 'name': 'FR-9: Khanna Pul - Golra Morh Station', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['FR_KhannaPul', 'ORG_Golra'], 'fare': 50
    },
    {
        'code': 'FR_10_5', 'name': 'FR-10 & 5: Golra Morh Station - Taxila', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['ORG_Golra', 'FR_Taxila'], 'fare': 50
    },
    {
        'code': 'FR_11', 'name': 'FR-11: Golra Morh Station - Noon, I-16', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['ORG_Golra', 'FR_I16'], 'fare': 50
    },
    {
        'code': 'EX_16', 'name': 'EX-16: PIMS Gate - Media Town', 'operator': 'CDA', 'type': 'feeder',
        'stops': ['RED_PIMS', 'FR_MediaTown'], 'fare': 50
    }
]

# ===== TRANSFER HUBS =====
TRANSFER_HUBS = [
    {
        'code': 'PIMS_Hub', 'name': 'PIMS Hospital Transfer Hub',
        'coordinates': {'lat': 33.705, 'lng': 73.048},
        'lines': ['Red Line', 'Blue Line', 'Green Line', 'FR-3A', 'FR-4', 'FR-6', 'FR-7', 'FR-8A', 'EX-16'],
        'facilities': ['Central Interchange', 'Ticketing', 'Waiting Area']
    },
    {
        'code': 'FaizAhmad_Hub', 'name': 'Faiz Ahmad Faiz Hub',
        'coordinates': {'lat': 33.669, 'lng': 73.054},
        'lines': ['Red Line', 'Orange Line'],
        'facilities': ['BRT Transfer Point', 'Ticketing']
    },
    {
        'code': 'Golra_Hub', 'name': 'Golra Morh Station Hub',
        'coordinates': {'lat': 33.633, 'lng': 72.973},
        'lines': ['Orange Line', 'FR-9', 'FR-10 & 5', 'FR-11', 'FR-13'],
        'facilities': ['Western Transfer Point', 'Ticketing']
    },
    {
        'code': 'Khanna_Hub', 'name': 'Khanna Pul Hub',
        'coordinates': {'lat': 33.626, 'lng': 73.111},
        'lines': ['Blue Line', 'FR-1', 'FR-8B', 'FR-9', 'FR-15'],
        'facilities': ['Expressway Transfer Node']
    }
]

# ===== TIMETABLE & SERVICE INFO (From Route List CSV) =====
TIMETABLE = {
    'BRT_Lines': {
        'frequency_minutes': 5, 'operating_hours': '6:00 AM - 10:00 PM', 'fare': 50, 'vehicle_type': 'BRT Articulated'
    },
    'FR_1': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_3A': {'frequency_minutes': 20, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_4': {'frequency_minutes': 10, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_4A': {'frequency_minutes': 30, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_6': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_7': {'frequency_minutes': 10, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_8A': {'frequency_minutes': 20, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_8B': {'frequency_minutes': 30, 'fare': 50, 'vehicle_type': 'Feeder Bus'}
}

# ===== LINE COLORS FOR UI =====
LINE_COLORS = {
    'Red Line': '#E74C3C',    # Saddar - Secretariat
    'Orange Line': '#F39C12', # Faiz Ahmad Faiz - Airport
    'Blue Line': '#3498DB',   # PIMS - Gulberg
    'Green Line': '#27AE60',  # PIMS - Bhara Kahu
    'FR-1': '#95A5A6',
    'FR-3A': '#95A5A6',
    'FR-4': '#95A5A6',
    'FR-6': '#95A5A6',
    'FR-7': '#95A5A6',
    'FR-8A': '#95A5A6',
} 