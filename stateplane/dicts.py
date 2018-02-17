STATEFP_TO_EPSG = {
    '45': ('32133'), '54': ('32151', '32150'), '28': ('26994', '26995'),
    '50': ('32145'), '60': ('32116'), '49': ('32143', '32144', '32142'),
    '66': ('4414'), '69': ('6325'), '53': ('32149', '32148'), '04': ('26950', '26948', '26949'),
    '02': ('26936', '26938', '26932', '26934', '26935', '26933', '26940', '26937', '26931'),
    '25': ('26986', '26987'), '26': ('26990', '26988', '26989'), '27': ('26993', '26991', '26992'),
    '06': ('26941', '26946', '26944', '26942', '26943', '26945'), '21': ('26980', '2205'),
    '22': ('26981', '26982'), '23': ('26984', '26983'), '46': ('32135', '32134'), '47': ('32136'),
    '08': ('26955', '26954', '26953'), '09': ('26956'), '42': ('32128', '32129'),
    '29': ('26996', '26998', '26997', '26951'), '40': ('32124', '32125'), '41': ('32126', '32127'),
    '24': ('26985'), '56': ('32157', '32158', '32156', '32155'), '33': ('32110'), '39': ('32123', '32122'),
    '01': ('26930', '26929'), '72': ('32161'), '30': ('32100'), '20': ('26977', '26978'), '78': ('32148'),
    '11': ('26985'), '10': ('26957'), '13': ('26966', '26967'), '38': ('32120', '32121'),
    '15': ('26964', '26961', '26963', '26962'), '48': ('32141', '32138', '32137', '32140', '32139'),
    '17': ('26971', '26972'), '16': ('26969', '26970', '26968'), '55': ('32152', '32154', '32153'),
    '18': ('26974', '26973'), '31': ('32104'), '05': ('26951', '26952'), '51': ('32147', '32146'),
    '36': ('32116', '32115', '32117', '32118'), '35': ('32112', '32114', '32113'), '34': ('32111'),
    '19': ('26975', '26976'), '37': ('32119'), '32': ('32109', '32108', '32107'),
    '12': ('26960', '26958', '26959'), '44': ('32130'), '66': ('27652',),
    '72': ('2820',), '78': ('2820',)
}

FIPS_TO_EPSG = {
    "0101": "26929",
    "0102": "26930",
    "0201": "26948",
    "0202": "26949",
    "0203": "26950",
    "0301": "26951",
    "0302": "26952",
    "0401": "26941",
    "0402": "26942",
    "0403": "26943",
    "0404": "26944",
    "0405": "26945",
    "0406": "26946",
    "0501": "26953",
    "0502": "26954",
    "0503": "26955",
    "0600": "26956",
    "0700": "26957",
    "0901": "26958",
    "0902": "26959",
    "0903": "26960",
    "1001": "26966",
    "1002": "26967",
    "1101": "26968",
    "1102": "26969",
    "1103": "26970",
    "1201": "26971",
    "1202": "26972",
    "1301": "26973",
    "1302": "26974",
    "1401": "26975",
    "1402": "26976",
    "1501": "26977",
    "1502": "26978",
    "1600": "03088",
    "1601": "2205",
    "1602": "26980",
    "1701": "26981",
    "1702": "26982",
    "1703": "32199",
    "1801": "26983",
    "1802": "26984",
    "1900": "26985",
    "2001": "26986",
    "2002": "26987",
    "2111": "26988",
    "2112": "26989",
    "2113": "26990",
    "2201": "26991",
    "2202": "26992",
    "2203": "26993",
    "2301": "26994",
    "2302": "26995",
    "2401": "26996",
    "2402": "26997",
    "2403": "26998",
    "2500": "32100",
    "2600": "32104",
    "2701": "32107",
    "2702": "32108",
    "2703": "32109",
    "2800": "32110",
    "2900": "32111",
    "3001": "32112",
    "3002": "32113",
    "3003": "32114",
    "3101": "32115",
    "3102": "32116",
    "3103": "32117",
    "3104": "32118",
    "3200": "32119",
    "3301": "32120",
    "3302": "32121",
    "3401": "32122",
    "3402": "32123",
    "3501": "32124",
    "3502": "32125",
    "3601": "32126",
    "3602": "32127",
    "3701": "32128",
    "3702": "32129",
    "3800": "32130",
    "3900": "32133",
    "4001": "32134",
    "4002": "32135",
    "4100": "32136",
    "4201": "32137",
    "4202": "32138",
    "4203": "32139",
    "4204": "32140",
    "4205": "32141",
    "4301": "32142",
    "4302": "32143",
    "4303": "32144",
    "4400": "32145",
    "4501": "32146",
    "4502": "32147",
    "4601": "32148",
    "4602": "32149",
    "4701": "32150",
    "4702": "32151",
    "4801": "32152",
    "4802": "32153",
    "4803": "32154",
    "4901": "32155",
    "4902": "32156",
    "4903": "32157",
    "4904": "32158",
    "5001": "26931",
    "5002": "26932",
    "5003": "26933",
    "5004": "26934",
    "5005": "26935",
    "5006": "26936",
    "5007": "26937",
    "5008": "26938",
    "5009": "26939",
    "5010": "26940",
    "5101": "26961",
    "5102": "26962",
    "5103": "26963",
    "5104": "26964",
    "5105": "26965",
    "5200": "32161"
}

SHORT_TO_EPSG = {
    "AK_1": "26931",
    "AK_2": "26932",
    "AK_3": "26933",
    "AK_4": "26934",
    "AK_5": "26935",
    "AK_6": "26936",
    "AK_7": "26937",
    "AK_8": "26938",
    "AK_9": "26939",
    "AK_10": "26940",
    "AL_E": "26929",
    "AL_W": "26930",
    "AR_N": "26951",
    "AR_S": "26952",
    "AZ_C": "26949",
    "AZ_E": "26948",
    "AZ_W": "26950",
    "CA_1": "26941",
    "CA_2": "26942",
    "CA_3": "26943",
    "CA_4": "26944",
    "CA_5": "26945",
    "CA_6": "26946",
    "CO_C": "26954",
    "CO_N": "26953",
    "CO_S": "26955",
    "CT": "26956",
    "DE": "26957",
    "FL_E": "26958",
    "FL_N": "26960",
    "FL_W": "26959",
    "GA_E": "26966",
    "GA_W": "26967",
    "HI_1": "26961",
    "HI_2": "26962",
    "HI_3": "26963",
    "HI_4": "26964",
    "HI_5": "26965",
    "IA_N": "26975",
    "IA_S": "26976",
    "ID_C": "26969",
    "ID_E": "26968",
    "ID_W": "26970",
    "IL_E": "26971",
    "IL_W": "26972",
    "IN_E": "26973",
    "IN_W": "26974",
    "KS_N": "26977",
    "KS_S": "26978",
    "KY_N": "2205",
    "KY_S": "26980",
    "LA_N": "26981",
    "LA_S": "26982",
    "MA_I": "26987",
    "MA_M": "26986",
    "MD": "26985",
    "ME_E": "26983",
    "ME_W": "26984",
    "MI_C": "26989",
    "MI_N": "26988",
    "MI_S": "26990",
    "MN_C": "26992",
    "MN_N": "26991",
    "MN_S": "26993",
    "MO_C": "26997",
    "MO_E": "26996",
    "MO_W": "26998",
    "MS_E": "26994",
    "MS_W": "26995",
    "MT": "32100",
    "NC": "32119",
    "ND_N": "32120",
    "ND_S": "32121",
    "NE": "32104",
    "NH": "32110",
    "NJ": "32111",
    "NM_C": "32113",
    "NM_E": "32112",
    "NM_W": "32114",
    "NV_C": "32108",
    "NV_E": "32107",
    "NV_W": "32109",
    "NY_C": "32116",
    "NY_E": "32115",
    "NY_LI": "32118",
    "NY_W": "32117",
    "OH_N": "32122",
    "OH_S": "32123",
    "OK_N": "32124",
    "OK_S": "32125",
    "OR_N": "32126",
    "OR_S": "32127",
    "PA_N": "32128",
    "PA_S": "32129",
    "RI": "32130",
    "SC": "32133",
    "SD_N": "32134",
    "SD_S": "32135",
    "TN": "32136",
    "TX_C": "32139",
    "TX_N": "32137",
    "TX_NC": "32138",
    "TX_S": "32141",
    "TX_SC": "32140",
    "UT_C": "32143",
    "UT_N": "32142",
    "UT_S": "32144",
    "VA_N": "32146",
    "VA_S": "32147",
    "VT": "32145",
    "WA_N": "32148",
    "WA_S": "32149",
    "WI_C": "32153",
    "WI_N": "32152",
    "WI_S": "32154",
    "WV_N": "32150",
    "WV_S": "32151",
    "WY_E": "32155",
    "WY_EC": "32156",
    "WY_W": "32158",
    "WY_WC": "32157",
}

EPSG_TO_NAME = {
    "1034": "NAD83(HARN) / Wisconsin Transverse Mercator",
    "1035": "NAD83 / Maine CS2000 East",
    "1037": "NAD83 / Maine CS2000 West",
    "1038": "NAD83(HARN) / Maine CS2000 East",
    "1040": "NAD83(HARN) / Maine CS2000 West",
    "1269": "NAD83(HARN) / California Albers",
    "1316": "NAD83(HARN) / North Carolina",
    "1318": "NAD83(HARN) / South Carolina",
    "1319": "NAD83(HARN) / South Carolina (ft)",
    "1320": "NAD83(HARN) / Pennsylvania North",
    "1321": "NAD83(HARN) / Pennsylvania North (ftUS)",
    "1322": "NAD83(HARN) / Pennsylvania South",
    "1323": "NAD83(HARN) / Pennsylvania South (ftUS)",
    "1362": "NAD83(HARN) / North Carolina (ftUS)",
    "1375": "NAD83 / Iowa North (ft US)",
    "1376": "NAD83 / Iowa South (ft US)",
    "1377": "NAD83 / Kansas North (ft US)",
    "1378": "NAD83 / Kansas South (ft US)",
    "1379": "NAD83 / Nevada East (ft US)",
    "1380": "NAD83 / Nevada Central (ft US)",
    "1381": "NAD83 / Nevada West (ft US)",
    "1382": "NAD83 / New Jersey (ft US)",
    "1383": "NAD83(HARN) / Iowa North (ft US)",
    "1384": "NAD83(HARN) / Iowa South (ft US)",
    "1385": "NAD83(HARN) / Kansas North (ft US)",
    "1386": "NAD83(HARN) / Kansas South (ft US)",
    "1387": "NAD83(HARN) / Nevada East (ft US)",
    "1388": "NAD83(HARN) / Nevada Central (ft US)",
    "1389": "NAD83(HARN) / Nevada West (ft US)",
    "1390": "NAD83(HARN) / New Jersey (ft US)",
    "1391": "NAD83 / Arkansas North (ftUS)",
    "1392": "NAD83 / Arkansas South (ftUS)",
    "1393": "NAD83 / Illinois East (ftUS)",
    "1394": "NAD83 / Illinois West (ftUS)",
    "1395": "NAD83 / New Hampshire (ftUS)",
    "1396": "NAD83 / Rhode Island (ftUS)",
    "1399": "NAD83(HARN) / Arkansas North (ftUS)",
    "1400": "NAD83(HARN) / Arkansas South (ftUS)",
    "1401": "NAD83(HARN) / Illinois East (ftUS)",
    "1402": "NAD83(HARN) / Illinois West (ftUS)",
    "1403": "NAD83(HARN) / New Hampshire (ftUS)",
    "1404": "NAD83(HARN) / Rhode Island (ftUS)",
    "1409": "NAD83 / Louisiana North (ftUS)",
    "1410": "NAD83 / Louisiana South (ftUS)",
    "1411": "NAD83 / Louisiana Offshore (ftUS)",
    "1412": "NAD83 / South Dakota North (ftUS)",
    "1413": "NAD83 / South Dakota South (ftUS)",
    "1414": "NAD83(HARN) / Louisiana North (ftUS)",
    "1415": "NAD83(HARN) / Louisiana South (ftUS)",
    "1416": "NAD83(HARN) / South Dakota North (ftUS)",
    "1417": "NAD83(HARN) / South Dakota South (ftUS)",
    "1421": "NAD83 / Maine CS2000 Central",
    "1422": "NAD83(HARN) / Maine CS2000 Central",
    "1518": "NAD83 / Utah North (ftUS)",
    "1524": "NAD83 / Utah Central (ftUS)",
    "1525": "NAD83 / Utah South (ftUS)",
    "1526": "NAD83(HARN) / Utah North (ftUS)",
    "1527": "NAD83(HARN) / Utah Central (ftUS)",
    "1528": "NAD83(HARN) / Utah South (ftUS)",
    "1692": "NAD83 / Ohio North (ftUS)",
    "1693": "NAD83 / Ohio South (ftUS)",
    "1694": "NAD83 / Wyoming East (ftUS)",
    "1695": "NAD83 / Wyoming East Central (ftUS)",
    "1696": "NAD83 / Wyoming West Central (ftUS)",
    "1697": "NAD83 / Wyoming West (ftUS)",
    "1711": "NAD83(HARN) / Ohio North (ftUS)",
    "1712": "NAD83(HARN) / Ohio South (ftUS)",
    "1713": "NAD83(HARN) / Wyoming East (ftUS)",
    "1714": "NAD83(HARN) / Wyoming East Central (ftUS)",
    "1715": "NAD83(HARN) / Wyoming West Central (ftUS)",
    "1716": "NAD83(HARN) / Wyoming West (ftUS)",
    "1717": "NAD83 / Hawaii zone 3 (ftUS)",
    "1718": "NAD83(HARN) / Hawaii zone 3 (ftUS)",
    "189": "NAD83 / Kentucky North",
    "204": "NAD83 / Arizona East (ft)",
    "205": "NAD83 / Arizona Central (ft)",
    "206": "NAD83 / Arizona West (ft)",
    "207": "NAD83 / California zone 1 (ftUS)",
    "208": "NAD83 / California zone 2 (ftUS)",
    "209": "NAD83 / California zone 3 (ftUS)",
    "210": "NAD83 / California zone 4 (ftUS)",
    "211": "NAD83 / California zone 5 (ftUS)",
    "212": "NAD83 / California zone 6 (ftUS)",
    "213": "NAD83 / Colorado North (ftUS)",
    "214": "NAD83 / Colorado Central (ftUS)",
    "215": "NAD83 / Colorado South (ftUS)",
    "216": "NAD83 / Connecticut (ftUS)",
    "217": "NAD83 / Delaware (ftUS)",
    "218": "NAD83 / Florida East (ftUS)",
    "219": "NAD83 / Florida West (ftUS)",
    "220": "NAD83 / Florida North (ftUS)",
    "221": "NAD83 / Georgia East (ftUS)",
    "222": "NAD83 / Georgia West (ftUS)",
    "2221": "NAD83 / Maine East (ftUS) (deprecated)",
    "2222": "NAD83 / Maine West (ftUS) (deprecated)",
    "2223": "NAD83 / Minnesota North (ftUS) (deprecated)",
    "2224": "NAD83 / Minnesota Central (ftUS) (deprecated)",
    "2225": "NAD83 / Minnesota South (ftUS) (deprecated)",
    "2226": "NAD83 / Nebraska (ftUS) (deprecated)",
    "2227": "NAD83 / West Virginia North (ftUS) (deprecated)",
    "2228": "NAD83 / West Virginia South (ftUS) (deprecated)",
    "223": "NAD83 / Idaho East (ftUS)",
    "224": "NAD83 / Idaho Central (ftUS)",
    "2245": "NAD83 / Maine East (ftUS)",
    "2246": "NAD83 / Maine West (ftUS)",
    "2247": "NAD83 / Minnesota North (ftUS)",
    "2248": "NAD83 / Minnesota Central (ftUS)",
    "2249": "NAD83 / Minnesota South (ftUS)",
    "225": "NAD83 / Idaho West (ftUS)",
    "2250": "NAD83 / Nebraska (ftUS)",
    "2251": "NAD83 / West Virginia North (ftUS)",
    "2252": "NAD83 / West Virginia South (ftUS)",
    "2253": "NAD83(HARN) / Maine East (ftUS)",
    "2254": "NAD83(HARN) / Maine West (ftUS)",
    "2255": "NAD83(HARN) / Minnesota North (ftUS)",
    "2256": "NAD83(HARN) / Minnesota Central (ftUS)",
    "2257": "NAD83(HARN) / Minnesota South (ftUS)",
    "2258": "NAD83(HARN) / Nebraska (ftUS)",
    "2259": "NAD83(HARN) / West Virginia North (ftUS)",
    "226": "NAD83 / Indiana East (ftUS) (deprecated)",
    "2260": "NAD83(HARN) / West Virginia South (ftUS)",
    "227": "NAD83 / Indiana West (ftUS) (deprecated)",
    "228": "NAD83 / Kentucky North (ftUS)",
    "229": "NAD83 / Kentucky South (ftUS)",
    "230": "NAD83 / Maryland (ftUS)",
    "2301": "NAD83 / Alabama East",
    "2302": "NAD83 / Alabama West",
    "231": "NAD83 / Massachusetts Mainland (ftUS)",
    "2313": "NAD83 / California zone 1",
    "2314": "NAD83 / California zone 2",
    "2315": "NAD83 / California zone 3",
    "2316": "NAD83 / California zone 4",
    "2317": "NAD83 / California zone 5",
    "2318": "NAD83 / California zone 6",
    "2319": "NAD83 / Arizona East",
    "232": "NAD83 / Massachusetts Island (ftUS)",
    "2320": "NAD83 / Arizona Central",
    "2321": "NAD83 / Arizona West",
    "2322": "NAD83 / Arkansas North",
    "2323": "NAD83 / Arkansas South",
    "2324": "NAD83 / Colorado North",
    "2325": "NAD83 / Colorado Central",
    "2326": "NAD83 / Colorado South",
    "2327": "NAD83 / Connecticut",
    "2328": "NAD83 / Delaware",
    "2329": "NAD83 / Florida East",
    "233": "NAD83 / Michigan North (ft)",
    "2330": "NAD83 / Florida West",
    "2331": "NAD83 / Florida North",
    "2332": "NAD83 / Hawaii zone 1",
    "2333": "NAD83 / Hawaii zone 2",
    "2334": "NAD83 / Hawaii zone 3",
    "2335": "NAD83 / Hawaii zone 4",
    "2336": "NAD83 / Hawaii zone 5",
    "2337": "NAD83 / Georgia East",
    "2338": "NAD83 / Georgia West",
    "2339": "NAD83 / Idaho East",
    "234": "NAD83 / Michigan Central (ft)",
    "2340": "NAD83 / Idaho Central",
    "2341": "NAD83 / Idaho West",
    "2342": "NAD83 / Illinois East",
    "2343": "NAD83 / Illinois West",
    "2344": "NAD83 / Indiana East",
    "2345": "NAD83 / Indiana West",
    "2346": "NAD83 / Iowa North",
    "2347": "NAD83 / Iowa South",
    "2348": "NAD83 / Kansas North",
    "2349": "NAD83 / Kansas South",
    "235": "NAD83 / Michigan South (ft)",
    "2350": "NAD83 / Kentucky North (deprecated)",
    "2351": "NAD83 / Kentucky South",
    "2352": "NAD83 / Louisiana North",
    "2353": "NAD83 / Louisiana South",
    "2354": "NAD83 / Maine East",
    "2355": "NAD83 / Maine West",
    "2356": "NAD83 / Maryland",
    "2357": "NAD83 / Massachusetts Mainland",
    "2358": "NAD83 / Massachusetts Island",
    "2359": "NAD83 / Michigan North",
    "236": "NAD83 / Mississippi East (ftUS)",
    "2360": "NAD83 / Michigan Central",
    "2361": "NAD83 / Michigan South",
    "2362": "NAD83 / Minnesota North",
    "2363": "NAD83 / Minnesota Central",
    "2364": "NAD83 / Minnesota South",
    "2365": "NAD83 / Mississippi East",
    "2366": "NAD83 / Mississippi West",
    "2367": "NAD83 / Missouri East",
    "2368": "NAD83 / Missouri Central",
    "2369": "NAD83 / Missouri West",
    "237": "NAD83 / Mississippi West (ftUS)",
    "238": "NAD83 / Montana (ft)",
    "239": "NAD83 / New Mexico East (ftUS)",
    "240": "NAD83 / New Mexico Central (ftUS)",
    "241": "NAD83 / New Mexico West (ftUS)",
    "242": "NAD83 / New York East (ftUS)",
    "243": "NAD83 / New York Central (ftUS)",
    "244": "NAD83 / New York West (ftUS)",
    "245": "NAD83 / New York Long Island (ftUS)",
    "246": "NAD83 / North Carolina (ftUS)",
    "247": "NAD83 / North Dakota North (ft)",
    "248": "NAD83 / North Dakota South (ft)",
    "249": "NAD83 / Oklahoma North (ftUS)",
    "250": "NAD83 / Oklahoma South (ftUS)",
    "251": "NAD83 / Oregon North (ft)",
    "252": "NAD83 / Oregon South (ft)",
    "253": "NAD83 / Pennsylvania North (ftUS)",
    "254": "NAD83 / Pennsylvania South (ftUS)",
    "255": "NAD83 / South Carolina (ft)",
    "256": "NAD83 / Tennessee (ftUS)",
    "257": "NAD83 / Texas North (ftUS)",
    "258": "NAD83 / Texas North Central (ftUS)",
    "259": "NAD83 / Texas Central (ftUS)",
    "260": "NAD83 / Texas South Central (ftUS)",
    "261": "NAD83 / Texas South (ftUS)",
    "262": "NAD83 / Utah North (ft)",
    "263": "NAD83 / Utah Central (ft)",
    "264": "NAD83 / Utah South (ft)",
    "265": "NAD83 / Virginia North (ftUS)",
    "266": "NAD83 / Virginia South (ftUS)",
    "267": "NAD83 / Washington North (ftUS)",
    "268": "NAD83 / Washington South (ftUS)",
    "269": "NAD83 / Wisconsin North (ftUS)",
    "270": "NAD83 / Wisconsin Central (ftUS)",
    "271": "NAD83 / Wisconsin South (ftUS)",
    "27216": "NAD83(HARN) / Mississippi TM",
    "27395": "NAD83(HARN) / Virginia Lambert",
    "27652": "NAD83(HARN) / Guam Map Grid",
    "2768": "NAD83 / Montana",
    "2769": "NAD83 / Nebraska",
    "2770": "NAD83 / Nevada East",
    "2771": "NAD83 / Nevada Central",
    "27714": "NAD83 / South Dakota North (ftUS)",
    "2772": "NAD83 / Nevada West",
    "2773": "NAD83 / New Hampshire",
    "2774": "NAD83 / New Jersey",
    "2775": "NAD83 / New Mexico East",
    "2776": "NAD83 / New Mexico Central",
    "2777": "NAD83 / New Mexico West",
    "2778": "NAD83 / New York East",
    "2779": "NAD83 / New York Central",
    "2780": "NAD83 / New York West",
    "2781": "NAD83 / New York Long Island",
    "2782": "NAD83 / North Carolina",
    "2783": "NAD83 / North Dakota North",
    "2784": "NAD83 / North Dakota South",
    "2785": "NAD83 / Ohio North",
    "2786": "NAD83 / Ohio South",
    "2787": "NAD83 / Oklahoma North",
    "2788": "NAD83 / Oklahoma South",
    "2789": "NAD83 / Oregon North",
    "2790": "NAD83 / Oregon South",
    "2791": "NAD83 / Pennsylvania North",
    "2792": "NAD83 / Pennsylvania South",
    "2793": "NAD83 / Rhode Island",
    "2794": "NAD83 / South Carolina",
    "2795": "NAD83 / South Dakota North",
    "2796": "NAD83 / South Dakota South",
    "2797": "NAD83 / Tennessee",
    "2798": "NAD83 / Texas North",
    "2799": "NAD83 / Texas North Central",
    "2800": "NAD83 / Texas Central",
    "2801": "NAD83 / Texas South Central",
    "2802": "NAD83 / Texas South",
    "2803": "NAD83 / Utah North",
    "2804": "NAD83 / Utah Central",
    "2805": "NAD83 / Utah South",
    "2806": "NAD83 / Vermont",
    "2807": "NAD83 / Virginia North",
    "2808": "NAD83 / Virginia South",
    "2809": "NAD83 / Washington North",
    "2810": "NAD83 / Washington South",
    "2811": "NAD83 / West Virginia North",
    "2812": "NAD83 / West Virginia South",
    "2813": "NAD83 / Wisconsin North",
    "2814": "NAD83 / Wisconsin Central",
    "2815": "NAD83 / Wisconsin South",
    "2816": "NAD83 / Wyoming East",
    "2817": "NAD83 / Wyoming East Central",
    "2818": "NAD83 / Wyoming West Central",
    "2819": "NAD83 / Wyoming West",
    "2820": "NAD83 / Puerto Rico & Virgin Is.",
    "728": "NAD83(HARN) / Alabama East",
    "729": "NAD83(HARN) / Alabama West",
    "730": "NAD83(HARN) / Arizona East",
    "731": "NAD83(HARN) / Arizona Central",
    "732": "NAD83(HARN) / Arizona West",
    "733": "NAD83(HARN) / Arkansas North",
    "734": "NAD83(HARN) / Arkansas South",
    "735": "NAD83(HARN) / California zone 1",
    "736": "NAD83(HARN) / California zone 2",
    "737": "NAD83(HARN) / California zone 3",
    "738": "NAD83(HARN) / California zone 4",
    "739": "NAD83(HARN) / California zone 5",
    "740": "NAD83(HARN) / California zone 6",
    "741": "NAD83(HARN) / Colorado North",
    "742": "NAD83(HARN) / Colorado Central",
    "743": "NAD83(HARN) / Colorado South",
    "744": "NAD83(HARN) / Connecticut",
    "745": "NAD83(HARN) / Delaware",
    "746": "NAD83(HARN) / Florida East",
    "747": "NAD83(HARN) / Florida West",
    "748": "NAD83(HARN) / Florida North",
    "749": "NAD83(HARN) / Georgia East",
    "750": "NAD83(HARN) / Georgia West",
    "751": "NAD83(HARN) / Hawaii zone 1",
    "752": "NAD83(HARN) / Hawaii zone 2",
    "753": "NAD83(HARN) / Hawaii zone 3",
    "754": "NAD83(HARN) / Hawaii zone 4",
    "755": "NAD83(HARN) / Hawaii zone 5",
    "756": "NAD83(HARN) / Idaho East",
    "757": "NAD83(HARN) / Idaho Central",
    "758": "NAD83(HARN) / Idaho West",
    "759": "NAD83(HARN) / Illinois East",
    "760": "NAD83(HARN) / Illinois West",
    "761": "NAD83(HARN) / Indiana East",
    "762": "NAD83(HARN) / Indiana West",
    "763": "NAD83(HARN) / Iowa North",
    "764": "NAD83(HARN) / Iowa South",
    "765": "NAD83(HARN) / Kansas North",
    "766": "NAD83(HARN) / Kansas South",
    "767": "NAD83(HARN) / Kentucky North",
    "768": "NAD83(HARN) / Kentucky South",
    "769": "NAD83(HARN) / Louisiana North",
    "770": "NAD83(HARN) / Louisiana South",
    "771": "NAD83(HARN) / Maine East",
    "772": "NAD83(HARN) / Maine West",
    "773": "NAD83(HARN) / Maryland",
    "774": "NAD83(HARN) / Massachusetts Mainland",
    "775": "NAD83(HARN) / Massachusetts Island",
    "776": "NAD83(HARN) / Michigan North",
    "777": "NAD83(HARN) / Michigan Central",
    "778": "NAD83(HARN) / Michigan South",
    "779": "NAD83(HARN) / Minnesota North",
    "780": "NAD83(HARN) / Minnesota Central",
    "781": "NAD83(HARN) / Minnesota South",
    "782": "NAD83(HARN) / Mississippi East",
    "783": "NAD83(HARN) / Mississippi West",
    "784": "NAD83(HARN) / Missouri East",
    "785": "NAD83(HARN) / Missouri Central",
    "786": "NAD83(HARN) / Missouri West",
    "787": "NAD83(HARN) / Montana",
    "788": "NAD83(HARN) / Nebraska",
    "789": "NAD83(HARN) / Nevada East",
    "790": "NAD83(HARN) / Nevada Central",
    "791": "NAD83(HARN) / Nevada West",
    "792": "NAD83(HARN) / New Hampshire",
    "793": "NAD83(HARN) / New Jersey",
    "794": "NAD83(HARN) / New Mexico East",
    "795": "NAD83(HARN) / New Mexico Central",
    "796": "NAD83(HARN) / New Mexico West",
    "797": "NAD83(HARN) / New York East",
    "798": "NAD83(HARN) / New York Central",
    "799": "NAD83(HARN) / New York West",
    "800": "NAD83(HARN) / New York Long Island",
    "801": "NAD83(HARN) / North Dakota North",
    "802": "NAD83(HARN) / North Dakota South",
    "803": "NAD83(HARN) / Ohio North",
    "804": "NAD83(HARN) / Ohio South",
    "805": "NAD83(HARN) / Oklahoma North",
    "806": "NAD83(HARN) / Oklahoma South",
    "807": "NAD83(HARN) / Oregon North",
    "808": "NAD83(HARN) / Oregon South",
    "809": "NAD83(HARN) / Rhode Island",
    "810": "NAD83(HARN) / South Dakota North",
    "811": "NAD83(HARN) / South Dakota South",
    "812": "NAD83(HARN) / Tennessee",
    "813": "NAD83(HARN) / Texas North",
    "814": "NAD83(HARN) / Texas North Central",
    "815": "NAD83(HARN) / Texas Central",
    "816": "NAD83(HARN) / Texas South Central",
    "817": "NAD83(HARN) / Texas South",
    "818": "NAD83(HARN) / Utah North",
    "819": "NAD83(HARN) / Utah Central",
    "820": "NAD83(HARN) / Utah South",
    "821": "NAD83(HARN) / Vermont",
    "822": "NAD83(HARN) / Virginia North",
    "823": "NAD83(HARN) / Virginia South",
    "824": "NAD83(HARN) / Washington North",
    "825": "NAD83(HARN) / Washington South",
    "826": "NAD83(HARN) / West Virginia North",
    "827": "NAD83(HARN) / West Virginia South",
    "828": "NAD83(HARN) / Wisconsin North",
    "829": "NAD83(HARN) / Wisconsin Central",
    "830": "NAD83(HARN) / Wisconsin South",
    "831": "NAD83(HARN) / Wyoming East",
    "832": "NAD83(HARN) / Wyoming East Central",
    "833": "NAD83(HARN) / Wyoming West Central",
    "834": "NAD83(HARN) / Wyoming West",
    "835": "NAD83(HARN) / Puerto Rico & Virgin Is.",
    "836": "NAD83(HARN) / Arizona East (ft)",
    "837": "NAD83(HARN) / Arizona Central (ft)",
    "838": "NAD83(HARN) / Arizona West (ft)",
    "839": "NAD83(HARN) / California zone 1 (ftUS)",
    "840": "NAD83(HARN) / California zone 2 (ftUS)",
    "841": "NAD83(HARN) / California zone 3 (ftUS)",
    "842": "NAD83(HARN) / California zone 4 (ftUS)",
    "843": "NAD83(HARN) / California zone 5 (ftUS)",
    "844": "NAD83(HARN) / California zone 6 (ftUS)",
    "845": "NAD83(HARN) / Colorado North (ftUS)",
    "846": "NAD83(HARN) / Colorado Central (ftUS)",
    "847": "NAD83(HARN) / Colorado South (ftUS)",
    "848": "NAD83(HARN) / Connecticut (ftUS)",
    "849": "NAD83(HARN) / Delaware (ftUS)",
    "850": "NAD83(HARN) / Florida East (ftUS)",
    "851": "NAD83(HARN) / Florida West (ftUS)",
    "852": "NAD83(HARN) / Florida North (ftUS)",
    "853": "NAD83(HARN) / Georgia East (ftUS)",
    "854": "NAD83(HARN) / Georgia West (ftUS)",
    "855": "NAD83(HARN) / Idaho East (ftUS)",
    "856": "NAD83(HARN) / Idaho Central (ftUS)",
    "857": "NAD83(HARN) / Idaho West (ftUS)",
    "860": "NAD83(HARN) / Kentucky North (ftUS)",
    "861": "NAD83(HARN) / Kentucky South (ftUS)",
    "862": "NAD83(HARN) / Maryland (ftUS)",
    "863": "NAD83(HARN) / Massachusetts Mainland (ftUS)",
    "864": "NAD83(HARN) / Massachusetts Island (ftUS)",
    "865": "NAD83(HARN) / Michigan North (ft)",
    "866": "NAD83(HARN) / Michigan Central (ft)",
    "867": "NAD83(HARN) / Michigan South (ft)",
    "868": "NAD83(HARN) / Mississippi East (ftUS)",
    "869": "NAD83(HARN) / Mississippi West (ftUS)",
    "870": "NAD83(HARN) / Montana (ft)",
    "871": "NAD83(HARN) / New Mexico East (ftUS)",
    "872": "NAD83(HARN) / New Mexico Central (ftUS)",
    "873": "NAD83(HARN) / New Mexico West (ftUS)",
    "874": "NAD83(HARN) / New York East (ftUS)",
    "875": "NAD83(HARN) / New York Central (ftUS)",
    "876": "NAD83(HARN) / New York West (ftUS)",
    "877": "NAD83(HARN) / New York Long Island (ftUS)",
    "878": "NAD83(HARN) / North Dakota North (ft)",
    "879": "NAD83(HARN) / North Dakota South (ft)",
    "880": "NAD83(HARN) / Oklahoma North (ftUS)",
    "881": "NAD83(HARN) / Oklahoma South (ftUS)",
    "882": "NAD83(HARN) / Oregon North (ft)",
    "883": "NAD83(HARN) / Oregon South (ft)",
    "884": "NAD83(HARN) / Tennessee (ftUS)",
    "885": "NAD83(HARN) / Texas North (ftUS)",
    "886": "NAD83(HARN) / Texas North Central (ftUS)",
    "887": "NAD83(HARN) / Texas Central (ftUS)",
    "888": "NAD83(HARN) / Texas South Central (ftUS)",
    "889": "NAD83(HARN) / Texas South (ftUS)",
    "890": "NAD83(HARN) / Utah North (ft)",
    "891": "NAD83(HARN) / Utah Central (ft)",
    "892": "NAD83(HARN) / Utah South (ft)",
    "893": "NAD83(HARN) / Virginia North (ftUS)",
    "894": "NAD83(HARN) / Virginia South (ftUS)",
    "895": "NAD83(HARN) / Washington North (ftUS)",
    "896": "NAD83(HARN) / Washington South (ftUS)",
    "897": "NAD83(HARN) / Wisconsin North (ftUS)",
    "898": "NAD83(HARN) / Wisconsin Central (ftUS)",
    "899": "NAD83(HARN) / Wisconsin South (ftUS)",
    "933": "NAD83 / Indiana East (ftUS)",
    "934": "NAD83 / Indiana West (ftUS)",
    "935": "NAD83(HARN) / Indiana East (ftUS)",
    "936": "NAD83(HARN) / Indiana West (ftUS)",
    "958": "NAD83(HARN) / Oregon Lambert",
    "959": "NAD83(HARN) / Oregon Lambert (ft)",
}
