# Transit data for Islamabad/Rawalpindi public transport system
# Based on official RMBS (Rawalpindi Metro Bus Service) and CDA Feeder Route Network 

# ===== METRO/RAPID TRANSIT STATIONS (BRT Core Network) =====
METRO_STATIONS = [
    # RED LINE (Saddar to Secretariat)
    {'code': 'RED_Saddar', 'name': 'Saddar Station', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.593, 'lng': 73.053}},
    {'code': 'RED_Marrir_Chowk', 'name': 'Marrir Chowk', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.597, 'lng': 73.056}},
    {'code': 'RED_Liaquat_Bagh', 'name': 'Liaquat Bagh', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.602, 'lng': 73.060}},
    {'code': 'RED_Committe_Chowk', 'name': 'Committe Chowk', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.607, 'lng': 73.064}},
    {'code': 'RED_Waris_Khan', 'name': 'Waris Khan', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.612, 'lng': 73.068}},
    {'code': 'RED_Chandni_Chowk', 'name': 'Chandni Chowk', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.621, 'lng': 73.073}},
    {'code': 'RED_Rehmanabad', 'name': 'Rehmanabad', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.626, 'lng': 73.076}},
    {'code': 'RED_6th_Road', 'name': '6th Road', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.632, 'lng': 73.079}},
    {'code': 'RED_Shamsabad', 'name': 'Shamsabad', 'line': 'Red Line', 'type': 'metro', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.637, 'lng': 73.082}},
    {'code': 'RED_Faizabad', 'name': 'Faizabad', 'line': 'Red Line', 'type': 'metro', 'area': 'IJP Road', 'coordinates': {'lat': 33.640, 'lng': 73.085}},
    {'code': 'RED_IJP', 'name': 'IJP', 'line': 'Red Line', 'type': 'metro', 'area': 'I-8/I-9', 'coordinates': {'lat': 33.648, 'lng': 73.078}},
    {'code': 'RED_Potohar', 'name': 'Potohar', 'line': 'Red Line', 'type': 'metro', 'area': 'I-9', 'coordinates': {'lat': 33.654, 'lng': 73.071}},
    {'code': 'RED_Khayaban', 'name': 'Khayaban', 'line': 'Red Line', 'type': 'metro', 'area': 'H-8', 'coordinates': {'lat': 33.662, 'lng': 73.063}},
    {'code': 'RED_Faiz_Ahmad_Faiz', 'name': 'Faiz Ahmad Faiz', 'line': 'Red Line', 'type': 'metro', 'area': 'H-8', 'coordinates': {'lat': 33.669, 'lng': 73.054}},
    {'code': 'RED_Kashmir_Highway', 'name': 'Kashmir Highway', 'line': 'Red Line', 'type': 'metro', 'area': 'G-8', 'coordinates': {'lat': 33.678, 'lng': 73.047}},
    {'code': 'RED_Chaman', 'name': 'Chaman', 'line': 'Red Line', 'type': 'metro', 'area': 'G-8/G-9', 'coordinates': {'lat': 33.685, 'lng': 73.042}},
    {'code': 'RED_Ibn_e_Sina', 'name': 'Ibn-e-Sina', 'line': 'Red Line', 'type': 'metro', 'area': 'G-9', 'coordinates': {'lat': 33.693, 'lng': 73.045}},
    {'code': 'RED_Kachery', 'name': 'Kachery', 'line': 'Red Line', 'type': 'metro', 'area': 'F-8/G-8', 'coordinates': {'lat': 33.699, 'lng': 73.047}},
    {'code': 'RED_PIMS', 'name': 'PIMS Hospital', 'line': 'Red Line', 'type': 'metro', 'area': 'G-8/F-8', 'coordinates': {'lat': 33.705, 'lng': 73.048}},
    {'code': 'RED_Stock_Exchange', 'name': 'Stock Exchange', 'line': 'Red Line', 'type': 'metro', 'area': 'Blue Area', 'coordinates': {'lat': 33.711, 'lng': 73.056}},
    {'code': 'RED_7th_Avenue', 'name': '7th Avenue', 'line': 'Red Line', 'type': 'metro', 'area': 'Blue Area', 'coordinates': {'lat': 33.716, 'lng': 73.067}},
    {'code': 'RED_Shaheed_e_Millat', 'name': 'Shaheed-e-Millat', 'line': 'Red Line', 'type': 'metro', 'area': 'Blue Area', 'coordinates': {'lat': 33.721, 'lng': 73.078}},
    {'code': 'RED_Parade_Ground', 'name': 'Parade Ground', 'line': 'Red Line', 'type': 'metro', 'area': 'Blue Area', 'coordinates': {'lat': 33.726, 'lng': 73.089}},
    {'code': 'RED_Secretariat', 'name': 'Secretariat Station', 'line': 'Red Line', 'type': 'metro', 'area': 'Red Zone', 'coordinates': {'lat': 33.731, 'lng': 73.097}},
    
    # ORANGE LINE (Faiz Ahmad Faiz to Airport)
    {'code': 'ORG_NHA', 'name': 'NHA', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-10/H-10', 'coordinates': {'lat': 33.664, 'lng': 73.038}},
    {'code': 'ORG_High_Court', 'name': 'High Court', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-10', 'coordinates': {'lat': 33.658, 'lng': 73.025}},
    {'code': 'ORG_G10', 'name': 'G-10 Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-10', 'coordinates': {'lat': 33.652, 'lng': 73.012}},
    {'code': 'ORG_Police_Foundation', 'name': 'Police Foundation', 'line': 'Orange Line', 'type': 'metro', 'area': 'H-11', 'coordinates': {'lat': 33.647, 'lng': 73.000}},
    {'code': 'ORG_NUST', 'name': 'NUST Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'H-12', 'coordinates': {'lat': 33.641, 'lng': 72.986}},
    {'code': 'ORG_G13', 'name': 'G-13', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-13', 'coordinates': {'lat': 33.637, 'lng': 72.980}},
    {'code': 'ORG_Golra_Morh', 'name': 'Golra Morh Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'Golra', 'coordinates': {'lat': 33.633, 'lng': 72.973}},
    {'code': 'ORG_N5', 'name': 'N-5 Station', 'line': 'Orange Line', 'type': 'metro', 'area': 'N-5 Highway', 'coordinates': {'lat': 33.612, 'lng': 72.932}},
    {'code': 'ORG_G15', 'name': 'G-15', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-15', 'coordinates': {'lat': 33.605, 'lng': 72.915}},
    {'code': 'ORG_G16', 'name': 'G-16', 'line': 'Orange Line', 'type': 'metro', 'area': 'G-16', 'coordinates': {'lat': 33.595, 'lng': 72.902}},
    {'code': 'ORG_Masjid_Abul_Qasim', 'name': 'Masjid Abul Qasim', 'line': 'Orange Line', 'type': 'metro', 'area': 'Srinagar Hwy', 'coordinates': {'lat': 33.585, 'lng': 72.885}},
    {'code': 'ORG_Top_City_Interchange', 'name': 'Top City Interchange', 'line': 'Orange Line', 'type': 'metro', 'area': 'Top City', 'coordinates': {'lat': 33.575, 'lng': 72.868}},
    {'code': 'ORG_Rakh_Pind_Ranjha', 'name': 'Rakh Pind Ranjha', 'line': 'Orange Line', 'type': 'metro', 'area': 'Airport Road', 'coordinates': {'lat': 33.565, 'lng': 72.852}},
    {'code': 'ORG_Islamabad_International_Airport', 'name': 'Islamabad Int. Airport', 'line': 'Orange Line', 'type': 'metro', 'area': 'Airport', 'coordinates': {'lat': 33.551, 'lng': 72.827}},
    
    # BLUE LINE (PIMS to Gulberg)
    {'code': 'BLU_Gulberg', 'name': 'Gulberg', 'line': 'Blue Line', 'type': 'metro', 'area': 'Gulberg Greens', 'coordinates': {'lat': 33.604, 'lng': 73.151}},
    
    # GREEN LINE (PIMS to Bhara Kahu)
    {'code': 'GRN_Jillani', 'name': 'Jillani, Bhara Kahu', 'line': 'Green Line', 'type': 'metro', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.755, 'lng': 73.168}},
]

# ===== BUS STOPS (Feeder Route Nodes - Comprehensive Data) =====
# Using representative coordinates derived from sector layouts for minor stops
BUS_STOPS = [
    # Core Anchors
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

    # Expressway & Connectivity Stops (FR-1 & FR-16)
    {'code': 'FR_Zia_Masjid', 'name': 'Zia Masjid', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.632, 'lng': 73.102}},
    {'code': 'FR_Kuri_Road', 'name': 'Kuri Road', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.638, 'lng': 73.095}},
    {'code': 'FR_Iqbal_Town', 'name': 'Iqbal Town', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.642, 'lng': 73.090}},
    {'code': 'FR_Dhoke_Kala_Khan', 'name': 'Dhoke Kala Khan', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.646, 'lng': 73.085}},
    {'code': 'FR_Sohan', 'name': 'Sohan', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.650, 'lng': 73.080}},
    {'code': 'FR_I8_Markaz_West', 'name': 'I-8 Markaz West', 'type': 'bus', 'area': 'I-8', 'coordinates': {'lat': 33.668, 'lng': 73.072}},
    {'code': 'FR_MCI_School', 'name': 'MCI Model School', 'type': 'bus', 'area': 'I-8', 'coordinates': {'lat': 33.670, 'lng': 73.075}},
    {'code': 'FR_CDA_Complaint', 'name': 'CDA Complaint Center', 'type': 'bus', 'area': 'I-9', 'coordinates': {'lat': 33.655, 'lng': 73.065}},
    {'code': 'FR_OGTI', 'name': 'OGTI Stop', 'type': 'bus', 'area': 'I-9', 'coordinates': {'lat': 33.658, 'lng': 73.060}},
    {'code': 'FR_Sui_Gas', 'name': 'Sui Gas Stop', 'type': 'bus', 'area': 'I-9', 'coordinates': {'lat': 33.660, 'lng': 73.055}},
    {'code': 'FR_PTCL_I10', 'name': 'PTCL I-10', 'type': 'bus', 'area': 'I-10', 'coordinates': {'lat': 33.645, 'lng': 73.045}},
    {'code': 'FR_IESCO_I10', 'name': 'IESCO I-10 Markaz', 'type': 'bus', 'area': 'I-10', 'coordinates': {'lat': 33.640, 'lng': 73.040}},
    {'code': 'FR_Korang_Road', 'name': 'Korang Road', 'type': 'bus', 'area': 'I-10', 'coordinates': {'lat': 33.635, 'lng': 73.035}},
    {'code': 'FR_Sabzi_Mandi', 'name': 'Sabzi Mandi', 'type': 'bus', 'area': 'I-11', 'coordinates': {'lat': 33.630, 'lng': 73.030}},
    {'code': 'FR_Metro_CC', 'name': 'Metro Cash and Carry', 'type': 'bus', 'area': 'I-11', 'coordinates': {'lat': 33.625, 'lng': 73.025}},
    {'code': 'FR_IMC', 'name': 'Islamabad Medical Complex', 'type': 'bus', 'area': 'H-11', 'coordinates': {'lat': 33.635, 'lng': 73.015}},
    {'code': 'FR_PAEC', 'name': 'PAEC General Hospital', 'type': 'bus', 'area': 'H-11', 'coordinates': {'lat': 33.640, 'lng': 73.010}},
    {'code': 'FR_IIUI', 'name': 'Islamic International University', 'type': 'bus', 'area': 'H-10', 'coordinates': {'lat': 33.650, 'lng': 73.015}},
    {'code': 'FR_FAST', 'name': 'FAST University', 'type': 'bus', 'area': 'H-11', 'coordinates': {'lat': 33.655, 'lng': 73.005}},
    {'code': 'FR_Police_Lines', 'name': 'Police Lines', 'type': 'bus', 'area': 'H-11', 'coordinates': {'lat': 33.645, 'lng': 72.995}},

    # Sectorial Internal Stops (FR-2, 3A, 6, 7)
    {'code': 'FR_Rescue_15', 'name': 'Rescue 15', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.695, 'lng': 73.055}},
    {'code': 'FR_TNT', 'name': 'TNT Stop', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.690, 'lng': 73.060}},
    {'code': 'FR_PTCL_HQ', 'name': 'PTCL HQ', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.685, 'lng': 73.065}},
    {'code': 'FR_Sarya_Chowk', 'name': 'Sarya Chowk', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.680, 'lng': 73.070}},
    {'code': 'FR_Taqwa_Market', 'name': 'Taqwa Market', 'type': 'bus', 'area': 'G-9', 'coordinates': {'lat': 33.688, 'lng': 73.038}},
    {'code': 'FR_G9_4_Park', 'name': 'G-9/4 Park', 'type': 'bus', 'area': 'G-9', 'coordinates': {'lat': 33.690, 'lng': 73.035}},
    {'code': 'FR_Karachi_Company', 'name': 'Karachi Company', 'type': 'bus', 'area': 'G-9', 'coordinates': {'lat': 33.692, 'lng': 73.030}},
    {'code': 'FR_Shifa', 'name': 'Shifa International Hospital', 'type': 'bus', 'area': 'H-8', 'coordinates': {'lat': 33.675, 'lng': 73.065}},
    {'code': 'FR_FBISE', 'name': 'FBISE', 'type': 'bus', 'area': 'H-8', 'coordinates': {'lat': 33.670, 'lng': 73.068}},
    {'code': 'FR_Sahibza_Road', 'name': 'Sahibza Abdul Qayuum Road', 'type': 'bus', 'area': 'I-8', 'coordinates': {'lat': 33.665, 'lng': 73.070}},
    {'code': 'FR_Sangam_Market', 'name': 'Sangam Market', 'type': 'bus', 'area': 'I-8', 'coordinates': {'lat': 33.660, 'lng': 73.075}},
    {'code': 'FR_I8_East', 'name': 'I-8 Markaz East', 'type': 'bus', 'area': 'I-8', 'coordinates': {'lat': 33.662, 'lng': 73.080}},
    {'code': 'FR_F8_Katchery', 'name': 'F-8 Katchery', 'type': 'bus', 'area': 'F-8', 'coordinates': {'lat': 33.708, 'lng': 73.042}},
    {'code': 'FR_F8_Markaz', 'name': 'F-8 Markaz', 'type': 'bus', 'area': 'F-8', 'coordinates': {'lat': 33.712, 'lng': 73.038}},
    {'code': 'FR_F9_Ravi_Gate', 'name': 'Ravi Gate F-9', 'type': 'bus', 'area': 'F-9', 'coordinates': {'lat': 33.715, 'lng': 73.030}},
    {'code': 'FR_Shaheen_Chowk', 'name': 'Shaheen Chowk', 'type': 'bus', 'area': 'F-9', 'coordinates': {'lat': 33.718, 'lng': 73.025}},
    {'code': 'FR_Bahria_Univ', 'name': 'Bahria University', 'type': 'bus', 'area': 'E-8', 'coordinates': {'lat': 33.725, 'lng': 73.020}},
    {'code': 'FR_Naval_Complex', 'name': 'Naval Complex', 'type': 'bus', 'area': 'E-8', 'coordinates': {'lat': 33.728, 'lng': 73.015}},
    {'code': 'FR_Faisal_Masjid', 'name': 'Faisal Masjid', 'type': 'bus', 'area': 'E-7/E-8', 'coordinates': {'lat': 33.730, 'lng': 73.038}},
    {'code': 'FR_Parveen_Shakir', 'name': 'Parveen Shakir Road', 'type': 'bus', 'area': 'F-7', 'coordinates': {'lat': 33.725, 'lng': 73.050}},
    {'code': 'FR_Kohsar', 'name': 'Kohsar Road', 'type': 'bus', 'area': 'F-6', 'coordinates': {'lat': 33.728, 'lng': 73.065}},
    {'code': 'FR_Zoo', 'name': 'Zoo', 'type': 'bus', 'area': 'F-6', 'coordinates': {'lat': 33.732, 'lng': 73.070}},
    {'code': 'FR_F6_2', 'name': 'F-6/2', 'type': 'bus', 'area': 'F-6', 'coordinates': {'lat': 33.735, 'lng': 73.062}},
    {'code': 'FR_Childrens_Hospital', 'name': 'Children Hospital', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.700, 'lng': 73.050}},
    {'code': 'FR_Bank_Colony', 'name': 'Bank Colony', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.705, 'lng': 73.065}},
    {'code': 'FR_Salai_Centre', 'name': 'Salai Centre', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.708, 'lng': 73.070}},
    {'code': 'FR_Sitara_Market', 'name': 'Sitara Market', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.710, 'lng': 73.075}},
    {'code': 'FR_Pully_Stop', 'name': 'Pully Stop', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.712, 'lng': 73.080}},
    {'code': 'FR_Iqbal_Hall', 'name': 'Iqbal Hall', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.715, 'lng': 73.085}},
    {'code': 'FR_G6_1_2', 'name': 'G-6/1,2', 'type': 'bus', 'area': 'G-6', 'coordinates': {'lat': 33.718, 'lng': 73.090}},
    {'code': 'FR_Melody', 'name': 'Melody Market', 'type': 'bus', 'area': 'G-6', 'coordinates': {'lat': 33.720, 'lng': 73.095}},
    {'code': 'FR_Aabpara', 'name': 'Aabpara Market', 'type': 'bus', 'area': 'G-6', 'coordinates': {'lat': 33.715, 'lng': 73.100}},
    {'code': 'FR_Youth_Hostel', 'name': 'Youth Hostel', 'type': 'bus', 'area': 'G-6', 'coordinates': {'lat': 33.710, 'lng': 73.105}},
    {'code': 'FR_MCI', 'name': 'Metropolitan Corporation', 'type': 'bus', 'area': 'G-6', 'coordinates': {'lat': 33.708, 'lng': 73.110}},
    {'code': 'FR_ICB', 'name': 'ICB College', 'type': 'bus', 'area': 'G-6', 'coordinates': {'lat': 33.705, 'lng': 73.115}},
    {'code': 'FR_NADRA_Chowk', 'name': 'NADRA Chowk', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.725, 'lng': 73.095}},
    {'code': 'FR_Lodges', 'name': 'Lodges Park', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.728, 'lng': 73.100}},
    {'code': 'FR_Sukh_Chayn', 'name': 'Sukh Chayn Park', 'type': 'bus', 'area': 'F-5', 'coordinates': {'lat': 33.732, 'lng': 73.095}},
    {'code': 'FR_MOFA', 'name': 'Ministry of Foreign Affairs', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.730, 'lng': 73.102}},
    {'code': 'FR_Radio_Pak', 'name': 'Radio Pakistan', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.725, 'lng': 73.105}},
    {'code': 'FR_Nat_Library', 'name': 'National Library', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.728, 'lng': 73.110}},
    {'code': 'FR_Sec_Police', 'name': 'Secretariate Police Station', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.732, 'lng': 73.115}},
    {'code': 'FR_Diplomatic_Enclave', 'name': 'Diplomatic Enclave Gate 4', 'type': 'bus', 'area': 'Diplomatic Enclave', 'coordinates': {'lat': 33.735, 'lng': 73.120}},
    {'code': 'FR_Aiwan_e_Sadar', 'name': 'Aiwan e Sadar Colony', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.728, 'lng': 73.125}},
    {'code': 'FR_Muslim_Colony', 'name': 'Muslim Colony', 'type': 'bus', 'area': 'Bari Imam', 'coordinates': {'lat': 33.740, 'lng': 73.118}},
    
    # QAU Route (FR-4A)
    {'code': 'FR_Noori_Bagh', 'name': 'Muhallah Noori Bagh', 'type': 'bus', 'area': 'QAU Campus', 'coordinates': {'lat': 33.742, 'lng': 73.125}},
    {'code': 'FR_Community_Health', 'name': 'Community Health Centre', 'type': 'bus', 'area': 'QAU Campus', 'coordinates': {'lat': 33.743, 'lng': 73.128}},
    {'code': 'FR_D_Type', 'name': 'D-Type Quaid-e-Azam Colony', 'type': 'bus', 'area': 'QAU Campus', 'coordinates': {'lat': 33.744, 'lng': 73.130}},
    {'code': 'FR_C_Type', 'name': 'C-Type Quaid-e-Azam Colony', 'type': 'bus', 'area': 'QAU Campus', 'coordinates': {'lat': 33.745, 'lng': 73.133}},
    {'code': 'FR_Babul_Quaid', 'name': 'Babul Quaid', 'type': 'bus', 'area': 'QAU Campus', 'coordinates': {'lat': 33.746, 'lng': 73.135}},

    # Western Sectors (FR-6, 7, 10, 11)
    {'code': 'FR_Tipu_Market', 'name': 'Tipu Market', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.692, 'lng': 73.048}},
    {'code': 'FR_G9_Markaz', 'name': 'G-9 Markaz', 'type': 'bus', 'area': 'G-9', 'coordinates': {'lat': 33.690, 'lng': 73.028}},
    {'code': 'FR_F9_Khyber', 'name': 'F-9 Khyber Gate', 'type': 'bus', 'area': 'F-9', 'coordinates': {'lat': 33.705, 'lng': 73.025}},
    {'code': 'FR_PAF_Hospital', 'name': 'PAF Hospital', 'type': 'bus', 'area': 'E-9', 'coordinates': {'lat': 33.715, 'lng': 73.018}},
    {'code': 'FR_DCI', 'name': 'Pakistan Gate DCI', 'type': 'bus', 'area': 'E-9', 'coordinates': {'lat': 33.712, 'lng': 73.012}},
    {'code': 'FR_Maroof', 'name': 'Maroof International Hospital', 'type': 'bus', 'area': 'F-10', 'coordinates': {'lat': 33.695, 'lng': 73.008}},
    {'code': 'FR_F10_Markaz', 'name': 'F-10 Markaz', 'type': 'bus', 'area': 'F-10', 'coordinates': {'lat': 33.692, 'lng': 73.005}},
    {'code': 'FR_IMCB_F10', 'name': 'IMCB F-10/4', 'type': 'bus', 'area': 'F-10', 'coordinates': {'lat': 33.690, 'lng': 73.002}},
    {'code': 'FR_F10_F11_Greenbelt', 'name': 'F-10/ F-11 Greenbelt', 'type': 'bus', 'area': 'F-10/F-11', 'coordinates': {'lat': 33.688, 'lng': 72.998}},
    {'code': 'FR_Barki_Road', 'name': 'Barki Road F-11', 'type': 'bus', 'area': 'F-11', 'coordinates': {'lat': 33.685, 'lng': 72.995}},
    {'code': 'FR_F11_Markaz', 'name': 'F-11 Markaz', 'type': 'bus', 'area': 'F-11', 'coordinates': {'lat': 33.682, 'lng': 72.990}},
    {'code': 'FR_OPF_Colony', 'name': 'OPF Colony', 'type': 'bus', 'area': 'F-11', 'coordinates': {'lat': 33.680, 'lng': 72.985}},
    {'code': 'FR_Golra_Shareef', 'name': 'Golra Shareef F-11', 'type': 'bus', 'area': 'F-11', 'coordinates': {'lat': 33.678, 'lng': 72.980}},
    {'code': 'FR_NPF_Society', 'name': 'NPF Society', 'type': 'bus', 'area': 'E-11', 'coordinates': {'lat': 33.698, 'lng': 72.985}},
    {'code': 'FR_NORI', 'name': 'NORI Hospital', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.698, 'lng': 73.045}},
    {'code': 'FR_Dental', 'name': 'Dental Hospital', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.695, 'lng': 73.042}},
    {'code': 'FR_G8_Markaz', 'name': 'G-8 Markaz', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.692, 'lng': 73.040}},
    {'code': 'FR_Dev_Park', 'name': 'Development Park', 'type': 'bus', 'area': 'G-8', 'coordinates': {'lat': 33.688, 'lng': 73.035}},
    {'code': 'FR_Police_Flats', 'name': 'Police Flats', 'type': 'bus', 'area': 'G-9', 'coordinates': {'lat': 33.680, 'lng': 73.025}},
    {'code': 'FR_College_Morh', 'name': 'College Morh', 'type': 'bus', 'area': 'G-10', 'coordinates': {'lat': 33.675, 'lng': 73.020}},
    {'code': 'FR_G10_Markaz', 'name': 'G-10 Markaz', 'type': 'bus', 'area': 'G-10', 'coordinates': {'lat': 33.670, 'lng': 73.015}},
    {'code': 'FR_PHA_Flats', 'name': 'PHA Flats', 'type': 'bus', 'area': 'G-10/G-11', 'coordinates': {'lat': 33.665, 'lng': 73.008}},
    {'code': 'FR_Tanki_Stop', 'name': 'Tanki Stop', 'type': 'bus', 'area': 'G-11', 'coordinates': {'lat': 33.662, 'lng': 73.005}},
    {'code': 'FR_G10_G11_Greenbelt', 'name': 'Greenbelt G-10/G-11', 'type': 'bus', 'area': 'G-10/G-11', 'coordinates': {'lat': 33.660, 'lng': 73.002}},
    {'code': 'FR_IMS', 'name': 'Institute of Modern Studies', 'type': 'bus', 'area': 'G-11', 'coordinates': {'lat': 33.658, 'lng': 72.998}},
    {'code': 'FR_G11_Markaz', 'name': 'G-11 Markaz', 'type': 'bus', 'area': 'G-11', 'coordinates': {'lat': 33.655, 'lng': 72.995}},
    {'code': 'FR_Mehrabad', 'name': 'Mehrabad', 'type': 'bus', 'area': 'G-11', 'coordinates': {'lat': 33.652, 'lng': 72.990}},
    {'code': 'FR_Bar_Council', 'name': 'Bar Council', 'type': 'bus', 'area': 'G-10', 'coordinates': {'lat': 33.655, 'lng': 73.015}},
    {'code': 'FR_DC_Office', 'name': 'DC Office', 'type': 'bus', 'area': 'G-10', 'coordinates': {'lat': 33.653, 'lng': 73.013}},

    # Rural & Eastern Routes (FR-8A, 8B, 8C, 14, 14A)
    {'code': 'FR_Fire_Brigade', 'name': 'Fire Brigade', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.702, 'lng': 73.085}},
    {'code': 'FR_CDA_Stop', 'name': 'CDA Stop', 'type': 'bus', 'area': 'G-7', 'coordinates': {'lat': 33.700, 'lng': 73.088}},
    {'code': 'FR_Foreign_Office', 'name': 'Foreign Office', 'type': 'bus', 'area': 'G-5', 'coordinates': {'lat': 33.728, 'lng': 73.100}},
    {'code': 'FR_Kashmir_Chowk', 'name': 'Kashmir Chowk', 'type': 'bus', 'area': 'Kashmir Hwy', 'coordinates': {'lat': 33.715, 'lng': 73.120}},
    {'code': 'FR_Rawal_Chowk', 'name': 'Rawal Chowk', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.710, 'lng': 73.125}},
    {'code': 'FR_Rawal_Town', 'name': 'Rawal Town', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.705, 'lng': 73.130}},
    {'code': 'FR_School_Board', 'name': 'School Board Stop', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.700, 'lng': 73.135}},
    {'code': 'FR_Rawal_Dam_Colony', 'name': 'Rawal Dam Colony', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.695, 'lng': 73.140}},
    {'code': 'FR_NARC', 'name': 'NARC Colony', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.690, 'lng': 73.145}},
    {'code': 'FR_NIH', 'name': 'NIH Allergy Center', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.685, 'lng': 73.150}},
    {'code': 'FR_Shahzad_Town', 'name': 'Shahzad Town', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.680, 'lng': 73.155}},
    {'code': 'FR_Park_View', 'name': 'Park View (Kuri Road)', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.675, 'lng': 73.160}},
    {'code': 'FR_Green_Avenue', 'name': 'Green Avenue', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.670, 'lng': 73.165}},
    {'code': 'FR_Chatta_Bakhtawar', 'name': 'Chatta Bakhtawar', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.665, 'lng': 73.170}},
    {'code': 'FR_Hostel_City', 'name': 'Hostel City', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.660, 'lng': 73.175}},
    {'code': 'FR_COMSATS', 'name': 'COMSATS University', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.655, 'lng': 73.180}},
    {'code': 'FR_Tamma_Stop', 'name': 'Tamma Stop', 'type': 'bus', 'area': 'Park Road', 'coordinates': {'lat': 33.650, 'lng': 73.185}},
    {'code': 'FR_Rawal_Gen', 'name': 'Rawal General Hospital', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.635, 'lng': 73.125}},
    {'code': 'FR_Sanam_Chowk', 'name': 'Sanam Chowk', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.638, 'lng': 73.130}},
    {'code': 'FR_Burma_Town', 'name': 'Burma Town', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.642, 'lng': 73.135}},
    {'code': 'FR_Ghauri_Gardens', 'name': 'Ghauri Gardens', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.645, 'lng': 73.140}},
    {'code': 'FR_Tarlai_Farms', 'name': 'Tarlai Farms', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.648, 'lng': 73.145}},
    {'code': 'FR_PO_Tarlai', 'name': 'Post Office Tarlai', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.650, 'lng': 73.150}},
    {'code': 'FR_Dak_Khana', 'name': 'Dak Khana Stop', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.652, 'lng': 73.155}},
    {'code': 'FR_Tarlai_School', 'name': 'Tarlai Kalan School', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.655, 'lng': 73.160}},
    {'code': 'FR_HBS_College', 'name': 'HBS Medical and Dental College', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.658, 'lng': 73.165}},
    {'code': 'FR_HBS_Hospital', 'name': 'HBS General Hospital', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.660, 'lng': 73.170}},
    {'code': 'FR_Ali_Pur', 'name': 'Ali Pur Bank Stop', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.662, 'lng': 73.175}},
    {'code': 'FR_Khaula_Shaheed', 'name': 'Khaula Shaheed Model College', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.665, 'lng': 73.180}},
    {'code': 'FR_Punjgran', 'name': 'Punjgran', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.668, 'lng': 73.185}},
    {'code': 'FR_Farash_Town', 'name': 'Farash Town', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.670, 'lng': 73.190}},
    {'code': 'FR_Sultana', 'name': 'Sultana Foundation', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.672, 'lng': 73.195}},
    {'code': 'FR_Jhang_Sayedan', 'name': 'Jhang Sayedan', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.675, 'lng': 73.200}},
    {'code': 'FR_Arslan_Town', 'name': 'Arslan Town', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.678, 'lng': 73.205}},
    {'code': 'FR_Shaheen_Town', 'name': 'Shaheen Town', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.680, 'lng': 73.210}},
    {'code': 'FR_Thanda_Pani', 'name': 'Thanda Pani', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.685, 'lng': 73.220}},
    {'code': 'FR_IMCG_Thanda', 'name': 'IMCG Thanda Pani', 'type': 'bus', 'area': 'Lehtrar Road', 'coordinates': {'lat': 33.688, 'lng': 73.225}},
    {'code': 'FR_Aziz_Market', 'name': 'Aziz Market', 'type': 'bus', 'area': 'Nilore', 'coordinates': {'lat': 33.660, 'lng': 73.250}},
    {'code': 'FR_Shakarparian', 'name': 'Shakarparian', 'type': 'bus', 'area': 'Shakarparian', 'coordinates': {'lat': 33.685, 'lng': 73.080}},
    {'code': 'FR_Faizabad_IC', 'name': 'Faizabad Interchange', 'type': 'bus', 'area': 'IJP Road', 'coordinates': {'lat': 33.642, 'lng': 73.082}},

    # Extended Feeder Routes (FR-12, 13, 14, 15, 17)
    {'code': 'FR_Pindora', 'name': 'Pindora Chungi', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.645, 'lng': 73.070}},
    {'code': 'FR_Katarian_Chungi', 'name': 'Katarian Chungi', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.640, 'lng': 73.065}},
    {'code': 'FR_Katarian_Pull', 'name': 'Katarian Pull', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.638, 'lng': 73.060}},
    {'code': 'FR_Fauji_Colony', 'name': 'Fauji Colony', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.625, 'lng': 73.040}},
    {'code': 'FR_Carriage', 'name': 'Carriage Factory', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.620, 'lng': 73.035}},
    {'code': 'FR_Westridge', 'name': 'Westridge', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.615, 'lng': 73.030}},
    {'code': 'FR_CTTI', 'name': 'CTTI', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.610, 'lng': 73.025}},
    {'code': 'FR_Social_Sec', 'name': 'Social Security Hospital', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.605, 'lng': 73.020}},
    {'code': 'FR_British_Homes', 'name': 'British Homes', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.600, 'lng': 73.015}},
    {'code': 'FR_Pir_Wadhai', 'name': 'Pir Wadhai Morh', 'type': 'bus', 'area': 'Rawalpindi', 'coordinates': {'lat': 33.615, 'lng': 73.045}},
    {'code': 'FR_Malaal_Morh', 'name': 'Malaal Morh', 'type': 'bus', 'area': 'Golra', 'coordinates': {'lat': 33.630, 'lng': 72.980}},
    {'code': 'FR_AK_Brohi', 'name': 'A. K. Brohi Road', 'type': 'bus', 'area': 'H-11/G-11', 'coordinates': {'lat': 33.650, 'lng': 72.990}},
    {'code': 'FR_FGC_F11', 'name': 'Federal Government College F-11', 'type': 'bus', 'area': 'F-11', 'coordinates': {'lat': 33.680, 'lng': 72.990}},
    {'code': 'FR_NPF_Gate', 'name': 'NPF Society Gate', 'type': 'bus', 'area': 'E-11', 'coordinates': {'lat': 33.695, 'lng': 72.980}},
    {'code': 'FR_Multy_Gate', 'name': 'Multy Gate', 'type': 'bus', 'area': 'E-11', 'coordinates': {'lat': 33.700, 'lng': 72.975}},
    {'code': 'FR_IIH_E11', 'name': 'Islamabad International Hospital (E-11/2)', 'type': 'bus', 'area': 'E-11', 'coordinates': {'lat': 33.705, 'lng': 72.970}},
    {'code': 'FR_D12_Service', 'name': 'D-12 Service Road', 'type': 'bus', 'area': 'D-12', 'coordinates': {'lat': 33.710, 'lng': 72.965}},
    {'code': 'FR_IESCO_D12', 'name': 'IESCO D-12', 'type': 'bus', 'area': 'D-12', 'coordinates': {'lat': 33.715, 'lng': 72.960}},
    {'code': 'FR_D12_Markaz', 'name': 'D-12 Markaz', 'type': 'bus', 'area': 'D-12', 'coordinates': {'lat': 33.720, 'lng': 72.950}},
    {'code': 'FR_Sangjani', 'name': 'Sangjani', 'type': 'bus', 'area': 'Sangjani', 'coordinates': {'lat': 33.680, 'lng': 72.880}},
    {'code': 'FR_B17_Gate1', 'name': 'B-17 Gate No. 1', 'type': 'bus', 'area': 'B-17', 'coordinates': {'lat': 33.695, 'lng': 72.850}},
    {'code': 'FR_B17_Gate2', 'name': 'B-17 Gate No. 2', 'type': 'bus', 'area': 'B-17', 'coordinates': {'lat': 33.690, 'lng': 72.845}},
    {'code': 'FR_Taxilla_Bypass', 'name': 'Taxilla Bypass', 'type': 'bus', 'area': 'Taxila', 'coordinates': {'lat': 33.730, 'lng': 72.820}},
    {'code': 'FR_Wahdat', 'name': 'Wahdat Colony', 'type': 'bus', 'area': 'Taxila', 'coordinates': {'lat': 33.735, 'lng': 72.815}},
    {'code': 'FR_Timber', 'name': 'Timber Market', 'type': 'bus', 'area': 'Taxila', 'coordinates': {'lat': 33.740, 'lng': 72.810}},
    {'code': 'FR_Kohinoor_Colony', 'name': 'Kohinoor Mill Colony', 'type': 'bus', 'area': 'Taxila', 'coordinates': {'lat': 33.748, 'lng': 72.800}},
    {'code': 'FR_Kohinoor_Mill', 'name': 'Kohinoor Mill', 'type': 'bus', 'area': 'Taxila', 'coordinates': {'lat': 33.750, 'lng': 72.795}},
    {'code': 'FR_Golra_Morh_Chowk', 'name': 'Golra Morh Chowk', 'type': 'bus', 'area': 'Golra', 'coordinates': {'lat': 33.630, 'lng': 72.970}},
    {'code': 'FR_IMCG_I14', 'name': 'IMCG I-14', 'type': 'bus', 'area': 'I-14', 'coordinates': {'lat': 33.615, 'lng': 72.955}},
    {'code': 'FR_Riphah', 'name': 'Riphah Int University', 'type': 'bus', 'area': 'I-14', 'coordinates': {'lat': 33.610, 'lng': 72.950}},
    {'code': 'FR_MainRd_St32', 'name': 'Main Road - St 32 Chowk', 'type': 'bus', 'area': 'I-14', 'coordinates': {'lat': 33.608, 'lng': 72.948}},
    {'code': 'FR_Mian_Chowk', 'name': 'Mian Chowk', 'type': 'bus', 'area': 'I-14', 'coordinates': {'lat': 33.605, 'lng': 72.945}},
    {'code': 'FR_Shaheed_Chowk_I14', 'name': 'Shaheed Chowk I-14', 'type': 'bus', 'area': 'I-14', 'coordinates': {'lat': 33.602, 'lng': 72.942}},
    {'code': 'FR_I15_Hail', 'name': '(Hail & Ride in I-15)', 'type': 'bus', 'area': 'I-15', 'coordinates': {'lat': 33.595, 'lng': 72.935}},
    {'code': 'FR_Rana_Chowk', 'name': 'Rana Chowk', 'type': 'bus', 'area': 'I-16', 'coordinates': {'lat': 33.590, 'lng': 72.940}},
    {'code': 'FR_Univ_Wah', 'name': 'University of Wah', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.765, 'lng': 72.740}},
    {'code': 'FR_Wah_B2', 'name': 'Wah Barrier 2', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.770, 'lng': 72.730}},
    {'code': 'FR_Gulshan_Anwar', 'name': 'Gulshan-e-Anwar', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.775, 'lng': 72.725}},
    {'code': 'FR_Jinnah_Colony', 'name': 'Jinnah Colony', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.780, 'lng': 72.720}},
    {'code': 'FR_New_City_1', 'name': 'New City Phase 1', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.785, 'lng': 72.715}},
    {'code': 'FR_Losar_Sharfo', 'name': 'Losar Sharfo', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.790, 'lng': 72.710}},
    {'code': 'FR_New_City_2', 'name': 'New City Phase 2', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.795, 'lng': 72.705}},
    {'code': 'FR_Bahtar_Morh', 'name': 'Bahtar Morh', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.800, 'lng': 72.700}},
    {'code': 'FR_Wah_Model_1', 'name': 'Wah Model Town Phase 1', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.805, 'lng': 72.695}},
    {'code': 'FR_Wah_Model_2', 'name': 'Wah Model Town Phase 2', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.810, 'lng': 72.690}},
    {'code': 'FR_Swedish_College', 'name': 'Swedish College, PECHS', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.815, 'lng': 72.685}},
    {'code': 'FR_Malakand', 'name': 'Malakand Stop', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.820, 'lng': 72.680}},
    {'code': 'FR_Basti', 'name': 'Basti', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.825, 'lng': 72.675}},
    {'code': 'FR_Sabri_Gali', 'name': 'Sabri Gali', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.830, 'lng': 72.670}},
    {'code': 'FR_Wah_B3', 'name': 'Wah Barrier 3', 'type': 'bus', 'area': 'Wah', 'coordinates': {'lat': 33.835, 'lng': 72.665}},
    {'code': 'FR_Ahmad_Nagar', 'name': 'Ahmad Nagar, Doiyan', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.840, 'lng': 72.660}},
    {'code': 'FR_Shah_Wali', 'name': 'Shah Wali Colony Road', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.845, 'lng': 72.655}},
    {'code': 'FR_Cement_Factory', 'name': 'Cement Factory Road, Bangu Chowk', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.850, 'lng': 72.650}},
    {'code': 'FR_Dhok_Dhollian', 'name': 'Dhok Dhollian', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.855, 'lng': 72.645}},
    {'code': 'FR_WAPDA', 'name': 'WAPDA Colony', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.860, 'lng': 72.640}},
    {'code': 'FR_Tipu_Sultan', 'name': 'Tipu Sultan Chowk', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.865, 'lng': 72.635}},
    {'code': 'FR_Avanue03', 'name': 'The Avanue 03', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.870, 'lng': 72.630}},
    {'code': 'FR_Akram_City', 'name': 'Akram City', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.875, 'lng': 72.625}},
    {'code': 'FR_Civil_City', 'name': 'Civil City Road', 'type': 'bus', 'area': 'Hassan Abdal', 'coordinates': {'lat': 33.880, 'lng': 72.620}},
    {'code': 'FR_G16_1', 'name': 'G-16/1', 'type': 'bus', 'area': 'G-16', 'coordinates': {'lat': 33.590, 'lng': 72.905}},
    {'code': 'FR_Airport_Enclave', 'name': 'Airport Enclave', 'type': 'bus', 'area': 'Airport Road', 'coordinates': {'lat': 33.560, 'lng': 72.845}},
    {'code': 'FR_Madni_Chowk', 'name': 'Madni Chowk', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.555, 'lng': 72.835}},
    {'code': 'FR_Dhuma', 'name': 'Dhuma', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.550, 'lng': 72.825}},
    {'code': 'FR_Mohri_Patak', 'name': 'Mohri Patak', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.545, 'lng': 72.815}},
    {'code': 'FR_Dhoke_Miskeen', 'name': 'Dhoke Miskeen', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.540, 'lng': 72.805}},
    {'code': 'FR_Mangial', 'name': 'Mangial', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.535, 'lng': 72.795}},
    {'code': 'FR_Graceland', 'name': 'Graceland Housing Society', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.530, 'lng': 72.785}},
    {'code': 'FR_Qutbal', 'name': 'Qutbal', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.525, 'lng': 72.775}},
    {'code': 'FR_Garhi_Hasu', 'name': 'Garhi Hasu Khan', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.520, 'lng': 72.765}},
    {'code': 'FR_Hattar_Choki', 'name': 'Hattar Choki', 'type': 'bus', 'area': 'Fateh Jang Rd', 'coordinates': {'lat': 33.515, 'lng': 72.755}},
    {'code': 'FR_Shahdara', 'name': 'Shahdara', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.765, 'lng': 73.185}},
    {'code': 'FR_Malpur', 'name': 'Malpur', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.750, 'lng': 73.175}},
    {'code': 'FR_Lake_View', 'name': 'Lake View Point', 'type': 'bus', 'area': 'Murree Road', 'coordinates': {'lat': 33.725, 'lng': 73.140}},
    {'code': 'FR_Garden_Avenue', 'name': 'Garden Avenue', 'type': 'bus', 'area': 'Shakarparian', 'coordinates': {'lat': 33.695, 'lng': 73.100}},
    {'code': 'FR_Margalla_Town', 'name': 'Margalla Town', 'type': 'bus', 'area': 'Margalla Town', 'coordinates': {'lat': 33.685, 'lng': 73.110}},
    {'code': 'FR_ITP_Centre', 'name': 'ITP Centre', 'type': 'bus', 'area': 'Margalla Town', 'coordinates': {'lat': 33.680, 'lng': 73.105}},
    {'code': 'FR_Punjab_College', 'name': 'Punjab College', 'type': 'bus', 'area': 'Faizabad', 'coordinates': {'lat': 33.645, 'lng': 73.080}},
    {'code': 'FR_Col_Ammanullah', 'name': 'Col. Ammanullah Road', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.758, 'lng': 73.170}},
    {'code': 'FR_Athal_Chowk', 'name': 'Athal Chowk', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.765, 'lng': 73.190}},
    {'code': 'FR_Bharakau_Bazar', 'name': 'Bharakau Bazar', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.760, 'lng': 73.185}},
    {'code': 'FR_Jhugi', 'name': 'Jhugi', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.768, 'lng': 73.195}},
    {'code': 'FR_Bhera_Pul', 'name': 'Bhera Pul', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.770, 'lng': 73.200}},
    {'code': 'FR_Imtiaz_Mart', 'name': 'Imtiaz Mart', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.772, 'lng': 73.205}},
    {'code': 'FR_Akbar_Niazi', 'name': 'Akbar Niazi', 'type': 'bus', 'area': 'Bhara Kahu', 'coordinates': {'lat': 33.775, 'lng': 73.210}},
    {'code': 'FR_Phulgran', 'name': 'Phulgran', 'type': 'bus', 'area': 'Murree Road', 'coordinates': {'lat': 33.780, 'lng': 73.215}},
    {'code': 'FR_Dhok_Badam', 'name': 'Dhok Badam', 'type': 'bus', 'area': 'Murree Road', 'coordinates': {'lat': 33.785, 'lng': 73.220}},
    {'code': 'FR_Alwadi_Colony', 'name': 'Alwadi Colony', 'type': 'bus', 'area': 'Murree Road', 'coordinates': {'lat': 33.790, 'lng': 73.225}},
    {'code': 'FR_Satra_Meel', 'name': 'Satra Meel', 'type': 'bus', 'area': 'Murree Road', 'coordinates': {'lat': 33.795, 'lng': 73.230}},
    {'code': 'FR_Tuth_Stop', 'name': 'Tuth Stop', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.595, 'lng': 73.140}},
    {'code': 'FR_PWD', 'name': 'PWD Housing society', 'type': 'bus', 'area': 'PWD', 'coordinates': {'lat': 33.585, 'lng': 73.145}},
    {'code': 'FR_Sohan_E', 'name': 'Sohan garden E block', 'type': 'bus', 'area': 'Sohan Garden', 'coordinates': {'lat': 33.580, 'lng': 73.150}},
    {'code': 'FR_Sohan_G', 'name': 'Sohan garden G block', 'type': 'bus', 'area': 'Sohan Garden', 'coordinates': {'lat': 33.578, 'lng': 73.152}},
    {'code': 'FR_Sohan_H', 'name': 'Sohan garden H block', 'type': 'bus', 'area': 'Sohan Garden', 'coordinates': {'lat': 33.576, 'lng': 73.154}},
    {'code': 'FR_River_Garden', 'name': 'River Garden', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.570, 'lng': 73.155}},
    {'code': 'FR_Kaak_Pul', 'name': 'Kaak Pul', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.560, 'lng': 73.160}},
    {'code': 'FR_DHA_G8', 'name': 'DHA Gate 8', 'type': 'bus', 'area': 'DHA Phase 2', 'coordinates': {'lat': 33.550, 'lng': 73.165}},
    {'code': 'FR_DHA_G7', 'name': 'DHA Gate 7', 'type': 'bus', 'area': 'DHA Phase 2', 'coordinates': {'lat': 33.545, 'lng': 73.170}},
    {'code': 'FR_Suparco', 'name': 'Suparco', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.535, 'lng': 73.175}},
    {'code': 'FR_Doctor_Town', 'name': 'Doctor Town', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.525, 'lng': 73.180}},
    {'code': 'FR_Watim', 'name': 'Watim Hospital', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.515, 'lng': 73.185}},
    {'code': 'FR_DHA_G5', 'name': 'DHA Gate 5', 'type': 'bus', 'area': 'DHA Phase 2', 'coordinates': {'lat': 33.505, 'lng': 73.190}},
    {'code': 'FR_Karal_Chowk', 'name': 'Karal Chowk', 'type': 'bus', 'area': 'Expressway', 'coordinates': {'lat': 33.615, 'lng': 73.130}},
    {'code': 'FR_PWD_Barrier', 'name': 'PWD Barrier', 'type': 'bus', 'area': 'PWD', 'coordinates': {'lat': 33.588, 'lng': 73.142}},
    {'code': 'FR_DD_Block', 'name': 'DD Block', 'type': 'bus', 'area': 'PWD', 'coordinates': {'lat': 33.586, 'lng': 73.140}},
    {'code': 'FR_London_Bakers', 'name': 'London Bakers', 'type': 'bus', 'area': 'PWD', 'coordinates': {'lat': 33.584, 'lng': 73.138}},
    {'code': 'FR_Bara_Plaza', 'name': 'Bara Plaza', 'type': 'bus', 'area': 'PWD', 'coordinates': {'lat': 33.582, 'lng': 73.135}},
    {'code': 'FR_Sihala', 'name': 'Sihala', 'type': 'bus', 'area': 'Kahuta Road', 'coordinates': {'lat': 33.540, 'lng': 73.180}},
    {'code': 'FR_Her_Do_Gher', 'name': 'Her Do Gher', 'type': 'bus', 'area': 'Kahuta Road', 'coordinates': {'lat': 33.535, 'lng': 73.190}},
    {'code': 'FR_Aari_Syedan', 'name': 'Aari Syedan', 'type': 'bus', 'area': 'Kahuta Road', 'coordinates': {'lat': 33.530, 'lng': 73.200}},
]

# Combined list of all stops
ALL_STOPS = METRO_STATIONS + BUS_STOPS

# ===== BUS ROUTES (CDA Feeder Routes & BRT fully populated) =====
BUS_ROUTES = [
    # BRT Core Routes
    {
        'code': 'BRT_RED', 'name': 'Red Line: Saddar - Secretariat', 'operator': 'RMBS', 'type': 'brt',
        'stops': [
            'Saddar', 'Marrir Chowk', 'Liaquat Bagh', 'Committe Chowk', 'Waris Khan', 
            'Chandni Chowk', 'Rehmanabad', '6th Road', 'Shamsabad', 'Faizabad', 'IJP', 
            'Potohar', 'Khayaban', 'Faiz Ahmad Faiz', 'Kashmir Highway', 'Chaman', 'Ibn-e-Sina', 
            'Kachery', 'PIMS', 'Stock Exchange', '7th Avenue', 'Shaheed-e-Millat', 'Parade Ground', 
            'Secretariat'
        ], 'fare': 30
    },
    {
        'code': 'BRT_ORANGE', 'name': 'Orange Line: Faiz Ahmad Faiz - Airport', 'operator': 'RMBS', 'type': 'brt',
        'stops': [
            'Faiz Ahmad Faiz', 'NHA', 'High Court', 'Police Foundation', 'NUST', 'G-13', 
            'Golra Morh', 'N-5', 'G-15', 'G-16', 'Masjid Abul Qasim', 'Top City Interchange', 
            'Rakh Pind Ranjha', 'Islamabad Intenational Airport'
        ], 'fare': 50
    },
    
    # Islamabad Feeder Routes (FR)
    {
        'code': 'FR_1', 'name': 'FR-1: Khanna Pul - NUST Metro Station', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Khanna Pul', 'Zia Masjid', 'Kuri Road', 'Iqbal Town', 'Dhoke Kala Khan', 'Sohan', 
            'Faizabad Metro Station', 'I-8 Markaz West', 'Potohar Metro Station', 'MCI Model School', 
            'CDA Complaint Center', 'OGTI Stop', 'Sui Gas Stop', 'PTCL I-10', 'IESCO I-10 Markaz', 
            'Korang Road', 'Mandi Morh', 'Sabzi Mandi', 'Metro Cash and Carry', 'Islamabad Medical Complex', 
            'PAEC General Hospital', 'Islamic International University', 'FAST University', 'Police Lines', 
            'Police Foundation Metro Station', 'NUST Metro Station'
        ], 'fare': 50
    },
    {
        'code': 'FR_2', 'name': 'FR-2: PIMS Gate - Faizabad (Suspended)', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', 'Rescue 15', 'TNT Stop', 'PTCL HQ', 'Sarya Chowk', 'Kashmir Highway Metro Station', 
            'Chaman Metro Station', 'Taqwa Market', 'G-9/4 Park', 'Karachi Company', 'Faiz Ahmad Faiz', 
            'Khayaban-e-Johar', 'Shifa International Hospital', 'FBISE', 'Sahibza Abdul Qayuum Road', 
            'Sangam Market', 'I-8 Markaz East', 'Faizabad'
        ], 'fare': 50
    },
    {
        'code': 'FR_3A', 'name': 'FR-3A: PIMS Gate - Saidpur/Faisal Masjid', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', 'PIMS Metro Station', 'F-8 Katchery', 'F-8 Markaz', 'Ravi Gate F-9', 
            'Shaheen Chowk', 'Bahria University', 'Naval Complex', 'Faisal Masjid', 'Parveen Shakir Road', 
            'Kohsar Road', 'Zoo', 'F-6/2', 'Saidpur Village'
        ], 'fare': 50
    },
    {
        'code': 'FR_4', 'name': 'FR-4: PIMS Gate - Bari Imam', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', 'Children Hospital', 'Rescue 15', 'Bank Colony', 'Salai Centre', 
            'Sitara Market', 'Pully Stop', 'Iqbal Hall', 'G-6/1,2', 'Melody Market', 
            'Aabpara Market', 'Youth Hostel', 'Metropolitan Corporation', 'ICB College', 
            'NADRA Chowk', 'Lodges Park', 'Sukh Chayn Park', 'Ministry of Foreign Affairs', 
            'Radio Pakistan', 'National Library', 'Secretariate Police Station', 
            'Diplomatic Enclave Gate 4', 'Aiwan e Sadar Colony', 'Muslim Colony', 'Bari Imam'
        ], 'fare': 50
    },
    {
        'code': 'FR_4A', 'name': 'FR-4A: Bari Imam - Quaid-e-Azam University', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Bari Imam', 'Muhallah Noori Bagh', 'Community Health Centre', 'D-Type Quaid-e-Azam Colony', 
            'C-Type Quaid-e-Azam Colony', 'Babul Quaid', 'Quaid-e-Azam University'
        ], 'fare': 50
    },
    {
        'code': 'FR_6', 'name': 'FR-6: PIMS Gate - E-11 Markaz', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', 'Tipu Market', 'Ibn-e-Sina Metro Station', 'G-9/4 Park', 'G-9 Markaz', 
            'F-9 Park Ravi Gate', 'Shaheen Chowk', 'F-9 Khyber Gate', 'PAF Hospital', 
            'Pakistan Gate DCI', 'Maroof International Hospital', 'F-10 Markaz', 'IMCB F-10/4', 
            'F-10/ F-11 Greenbelt', 'Barki Road F-11', 'F-11 Markaz', 'OPF Colony', 
            'Golra Shareef F-11', 'NPF Society', 'E-11 Markaz'
        ], 'fare': 50
    },
    {
        'code': 'FR_7', 'name': 'FR-7: PIMS Gate - G-10 Metro Station', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', 'Children Hospital', 'NORI Hospital', 'Dental Hospital', 'G-8 Markaz', 
            'Development Park', 'Chaman Metro Station', 'G-9/4 Park', 'Karachi Company', 'G-9 Markaz', 
            'Police Flats', 'College Morh', 'G-10 Markaz', 'PHA Flats', 'Tanki Stop', 
            'Greenbelt G-10/G-11', 'Institute of Modern Studies', 'G-11 Markaz', 'Mehrabad', 
            'NUST Metro Station', 'Bar Council', 'DC Office', 'G-10 Metro Station'
        ], 'fare': 50
    },
    {
        'code': 'FR_8A', 'name': 'FR-8A: PIMS Gate - Tramri Chowk', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', "Children's Hospital", 'T&T Stop', 'Fire Brigade', 'CDA Stop', 'Aabpara', 
            'Foreign Office', 'Kashmir Chowk', 'Rawal Chowk', 'Rawal Town', 'School Board Stop', 
            'Rawal Dam Colony', 'NARC Colony', 'NIH Allergy Center', 'Shahzad Town', 
            'Park View (Kuri Road)', 'Green Avenue', 'Chatta Bakhtawar', 'Hostel City', 
            'COMSATS University', 'Tamma Stop', 'Tramri Chowk'
        ], 'fare': 50
    },
    {
        'code': 'FR_8B', 'name': 'FR-8B: Khanna Pul - Nilore', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Khanna Pul', 'Rawal General Hospital', 'Sanam Chowk', 'Burma Town', 'Ghauri Gardens', 
            'Tarlai Farms', 'Post Office Tarlai', 'Dak Khana Stop', 'Tarlai Kalan School', 
            'HBS Medical and Dental College', 'Tramri Chowk', 'HBS General Hospital', 
            'Ali Pur Bank Stop', 'Khaula Shaheed Model College', 'Punjgran', 'Farash Town', 
            'Sultana Foundation', 'Jhang Sayedan', 'Arslan Town', 'Shaheen Town', 'Thanda Pani', 
            'IMCG Thanda Pani', 'Aziz Market', 'Nilore'
        ], 'fare': 50
    },
    {
        'code': 'FR_8C', 'name': 'FR-8C: PIMS Gate - Tramri Chowk', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', "Children's Hospital", 'T&T Stop', 'Shakarparian', 'Parade Ground', 
            'Faizabad Interchange', 'Rawal Chowk', 'Rawal Town', 'School Board Stop', 
            'Rawal Dam Colony', 'NARC Colony', 'NIH Allergy Center', 'Shahzad Town', 
            'Park View (Kuri Road)', 'Green Avenue', 'Chatta Bakhtawar', 'Hostel City', 
            'COMSATS University', 'Tamma Stop', 'Tramri Chowk'
        ], 'fare': 50
    },
    {
        'code': 'FR_9', 'name': 'FR-9: Khanna - Golra Morh Metro Station', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Khanna Pul', 'Zia Masjid', 'Kuri Road', 'Iqbal Town', 'Dhoke Kala Khan', 'Sohan', 
            'Faizabad Metro Station', 'IJP Metro Station', 'Pindora Chungi', 'Katarian Chungi', 
            'Katarian Pull', 'CDA Stop', 'Pully Stop', 'Mandi Morh', 'Fauji Colony', 
            'Carriage Factory', 'Westridge', 'CTTI', 'Social Security Hospital', 'British Homes', 
            'Pir Wadhai Morh', 'Malaal Morh', 'Golra Morh Metro Station'
        ], 'fare': 50
    },
    {
        'code': 'FR_10_5', 'name': 'FR-10 & 5: Golra Morh Metro Station - Taxila', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Golra Morh Metro Station', 'G-13 Metro Station', 'NUST Metro Station', 'A. K. Brohi Road', 
            'G-11 Markaz', 'Federal Government College F-11', 'F-11 Markaz', 'OPF Colony', 
            'Golra Shareef F-11', 'NPF Society Gate', 'Multy Gate', 
            'Islamabad International Hospital (E-11/2)', 'D-12 Service Road', 'IESCO D-12', 
            'D-12 Markaz', 'Sangjani', 'B-17 Gate No. 1', 'B-17 Gate No. 2', 'Taxilla Bypass', 
            'Wahdat Colony', 'Timber Market', 'Kohinoor Mill Colony', 'Kohinoor Mill', 
            'Golra Morh Chowk', 'Taxilla Highway Stop'
        ], 'fare': 50
    },
    {
        'code': 'FR_11', 'name': 'FR-11: Golra Morh Metro Station - I-16', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Golra Morh Metro Station', 'Golra Morh Chowk', 'IMCG I-14', 'Riphah Int University', 
            'Main Road - St 32 Chowk', 'Mian Chowk', 'Shaheed Chowk I-14', '(Hail & Ride in I-15)', 
            'Rana Chowk', 'PHA Flats', 'Noon (S. R. W. I-16)'
        ], 'fare': 50
    },
    {
        'code': 'FR_12', 'name': 'FR-12: Taxilla Highway Stop - Hassan Abdal', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Taxilla Highway Stop', 'University of Wah', 'Wah Barrier 2', 'Gulshan-e-Anwar', 
            'Jinnah Colony', 'New City Phase 1', 'Losar Sharfo', 'New City Phase 2', 'Bahtar Morh', 
            'Wah Model Town Phase 1', 'Wah Model Town Phase 2', 'Swedish College, PECHS', 
            'Malakand Stop', 'Basti', 'Sabri Gali', 'Wah Barrier 3', 'Ahmad Nagar, Doiyan', 
            'Shah Wali Colony Road', 'Cement Factory Road, Bangu Chowk', 'Dhok Dhollian', 
            'WAPDA Colony', 'Tipu Sultan Chowk', 'The Avanue 03', 'Akram City', 'Civil City Road', 
            'Fateh Jang', 'Hassan Abdal'
        ], 'fare': 50
    },
    {
        'code': 'FR_13', 'name': 'FR-13: Golra Morh Metro Station - Fateh Jang', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Golra Morh Metro Station', 'N-5 Metro Station', 'G-15 / H-15', 'G-16 / H-16', 'G-16/1', 
            'Masjid Abu Al Qasim', 'Top City', 'Mumtaz City', 'Airport Enclave', 'Madni Chowk', 
            'Dhuma', 'IJP Metro Station', 'Mohri Patak', 'Dhoke Miskeen', 'Mangial', 
            'Graceland Housing Society', 'Pully Stop', 'Qutbal', 'Garhi Hasu Khan', 'Hattar Choki'
        ], 'fare': 50
    },
    {
        'code': 'FR_14', 'name': 'FR-14: Jillani Stop - Mandi Morh', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Jillani Stop', 'Shahdara', 'Malpur', 'Lake View Point', 'Kashmir Chowk', 'Rawal Chowk', 
            'Garden Avenue', 'Margalla Town', 'ITP Centre', 'Sohan', 'Faizabad Metro Station', 
            'Punjab College', 'Pindora Chungi', 'Katarian Chungi', 'Katarian Pull', 'CDA Stop', 
            'Mandi Morh'
        ], 'fare': 50
    },
    {
        'code': 'FR_14A', 'name': 'FR-14A: Jillani Stop - Satra Meel', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Jillani Stop', 'Col. Ammanullah Road', 'Athal Chowk', 'Bharakau Bazar', 'Athal Chowk', 
            'Jhugi', 'Bhera Pul', 'Imtiaz Mart', 'Akbar Niazi', 'Phulgran', 'Dhok Badam', 'T-Chowk', 
            'Alwadi Colony', 'Satra Meel'
        ], 'fare': 50
    },
    {
        'code': 'FR_15', 'name': 'FR-15: Gulberg - Rawat', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'Gulberg', 'Tuth Stop', 'PWD Housing society', 'Sohan garden E block', 'Sohan garden G block', 
            'Sohan garden H block', 'River Garden', 'Kaak Pul', 'DHA Gate 8', 'DHA Gate 7', 
            'Suparco', 'Doctor Town', 'Watim Hospital', 'DHA Gate 5', 'Rawat'
        ], 'fare': 50
    },
    {
        'code': 'EX_16', 'name': 'EX-16: PIMS Gate - Media Town', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'PIMS Gate', 'Sohan', 'Khanna Pul', 'Karal Chowk', 'Gulberg', 'Tuth Stop', 
            'PWD Housing society', 'PWD Barrier', 'DD Block', 'London Bakers', 'Bara Plaza', 'Media Town'
        ], 'fare': 50
    },
    {
        'code': 'FR_17', 'name': 'FR-17: T Chowk - Aari Syedan', 'operator': 'CDA', 'type': 'feeder',
        'stops': [
            'T-Chowk', 'Suparco', 'DHA Gate 7', 'DHA Gate 8', 'Kaak Pul', 'Sihala', 
            'Her Do Gher', 'Aari Syedan'
        ], 'fare': 50
    }
]

# ===== TRANSFER HUBS =====
TRANSFER_HUBS = [
    {
        'code': 'PIMS_Hub', 'name': 'PIMS Hospital Transfer Hub',
        'coordinates': {'lat': 33.705, 'lng': 73.048},
        'lines': ['Red Line', 'Blue Line', 'Green Line', 'FR-2', 'FR-3A', 'FR-4', 'FR-6', 'FR-7', 'FR-8A', 'FR-8C', 'EX-16'],
        'facilities': ['Central Interchange', 'Ticketing', 'Waiting Area']
    },
    {
        'code': 'FaizAhmad_Hub', 'name': 'Faiz Ahmad Faiz Hub',
        'coordinates': {'lat': 33.669, 'lng': 73.054},
        'lines': ['Red Line', 'Orange Line', 'FR-2'],
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
        'lines': ['Blue Line', 'FR-1', 'FR-8B', 'FR-9', 'EX-16'],
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
    'FR_6': {'frequency_minutes': 30, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_7': {'frequency_minutes': 10, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_8A': {'frequency_minutes': 20, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_8B': {'frequency_minutes': 30, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_8C': {'frequency_minutes': 20, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_9': {'frequency_minutes': 15, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_10_5': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_11': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_12': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_13': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_14': {'frequency_minutes': 15, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_14A': {'frequency_minutes': 30, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_15': {'frequency_minutes': 30, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'EX_16': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
    'FR_17': {'frequency_minutes': 60, 'fare': 50, 'vehicle_type': 'Feeder Bus'},
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
    'FR-4A': '#95A5A6',
    'FR-6': '#95A5A6',
    'FR-7': '#95A5A6',
    'FR-8A': '#95A5A6',
    'FR-8B': '#95A5A6',
    'FR-8C': '#95A5A6',
    'FR-9': '#95A5A6',
    'FR-10_5': '#95A5A6',
    'FR-11': '#95A5A6',
    'FR-12': '#95A5A6',
    'FR-13': '#95A5A6',
    'FR-14': '#95A5A6',
    'FR-14A': '#95A5A6',
    'FR-15': '#95A5A6',
    'EX-16': '#95A5A6',
    'FR-17': '#95A5A6',
}