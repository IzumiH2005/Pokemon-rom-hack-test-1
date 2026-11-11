"""Tables écrites à la main pour la bascule des extérieurs."""

# Portes : case Rouge Feu -> case HnS. None = bâtiment absent du Kanto de HnS.
PORTES = {
 'PewterCity': {(17,6):(19,8), (25,4):(27,6), (15,16):(16,18), (28,18):(30,22), (33,11):(35,15),
                (17,25):(19,29), (9,30):(11,34)},
 'CeruleanCity': {(10,11):(18,11), (30,11):(38,11), (15,17):(23,17), (22,19):(30,19), (31,21):(39,21),
                  (13,28):(21,28), (29,28):(37,28), (1,12):(9,12), (10,8):None, (31,8):None, (31,9):None,
                  (14,28):(22,28), (23,28):None, (17,11):None},
 'LavenderTown': {(18,6):(22,6), (6,5):(10,5), (10,11):(12,11), (5,16):(5,16), (10,16):(12,16), (20,15):(4,6)},
 'VermilionCity': {(22,34):None, (23,34):None, (24,34):None, (9,6):(15,4), (15,6):(22,4), (12,17):(18,16),
                   (19,17):(25,16), (29,17):(38,16), (28,24):(38,22), (14,25):(21,23)},
 'CeladonCity': {(34,21):(35,21), (11,14):(11,14), (15,14):(15,14), (30,11):(30,11), (48,11):(48,11),
                 (39,20):None, (11,30):(12,30), (37,29):(37,29), (41,29):(41,29), (49,29):None,
                 (29,5):(30,4), (30,4):(30,4), (31,5):(30,4)},
 'FuchsiaCity': {(24,5):(26,5), (33,31):None, (11,15):(11,15), (28,16):None, (9,32):(9,32), (14,31):(14,31),
                 (25,31):(25,31), (38,31):(38,31), (39,28):(39,28), (39,29):(39,28), (19,31):(19,30)},
 'CinnabarIsland': {(8,3):None, (20,4):None, (8,9):None, (14,11):(45,29), (19,11):None},
 'SaffronCity': {(33,30):(25,30), (22,14):(19,21), (40,12):(32,12), (46,12):(38,12), (27,21):None,
                 (40,21):(32,21), (24,38):(16,38), (43,38):(35,38), (8,27):(0,27), (34,5):(26,5),
                 (58,27):(50,27), (34,46):(26,46), (35,46):(27,46), (35,5):(27,5), (47,21):None},
 'Route2': {(5,13):(5,13), (6,13):(6,13), (5,51):(5,51), (17,11):(17,11), (17,22):(17,22), (18,46):(18,46),
            (18,41):(18,40), (19,41):(19,40), (19,46):(19,46), (6,51):(6,51)},
 'Route4': {(19,5):(18,9), (32,5):(32,5), (12,5):(12,5)},
 'Route5': {(31,31):(31,31), (23,25):(23,25), (24,32):(24,32), (25,32):(25,32)},
 'Route6': {(19,13):(49,13), (12,5):(42,5), (13,5):(43,5)},
 'Route7': {(7,14):(7,33), (15,10):(15,30)},
 'Route8': {(13,4):(9,3), (7,10):(3,9)},
 'Route10': {(8,19):(16,19), (8,57):(16,57), (7,40):(15,40), (13,20):(21,20), (2,37):(10,37)},
 'Route11': {(6,7):None, (58,10):None, (65,10):None},
 'Route12': {(12,86):(12,85), (14,15):None, (15,15):None, (14,21):None},
 'Route15': {(9,11):(9,11), (16,11):(16,11)},
 'Route16': {(10,5):(10,5), (20,6):(20,13), (27,6):(27,13), (20,13):(20,13), (27,13):(27,13)},
 'Route18': {(41,9):(41,9), (48,9):(48,9)},
 'Route20': {(60,8):(60,8), (72,14):(72,14)},
 'Route22': {(8,5):(12,9), (9,5):(12,9)},
 'Route25': {(51,4):(51,8)},
}
# La Cave Taupiqueur sort à Carmin dans HnS, plus sur la Route 11.
PORTE_DEPLACEE = ('Route11', (6, 7), 'VermilionCity', (61, 10), 'DiglettsCave_SouthEntrance')

# Intérieurs : places fixées à la main (local_id -> case), pour les scènes dont le décor a changé de forme.
PLACES = {
    'PalletTown_ProfessorOaksLab': {
        'LOCALID_OAKS_LAB_PROF_OAK': (13, 11), 'LOCALID_OAKS_LAB_RIVAL': (12, 12),
        'LOCALID_BULBASAUR_BALL': (15, 13), 'LOCALID_SQUIRTLE_BALL': (16, 13), 'LOCALID_CHARMANDER_BALL': (17, 13),
        'LOCALID_POKEDEX_1': (9, 10), 'LOCALID_POKEDEX_2': (10, 10),
    },
    # Clé : local_id, script, ou rang du PNJ dans la carte.
    'FuchsiaCity_SafariZone_Entrance': {0: (2, 5), 'FuchsiaCity_SafariZone_Entrance_EventScript_InfoAttendant': (2, 10)},
    'SafariZone_West': {'SafariZone_SecretHouse_EventScript_Attendant': (9, 8)},      # donne la CS Surf
    'SSAnne_Exterior': {'LOCALID_SS_ANNE': (6, 12)},
}

# Cartes associées à la main : Rouge Feu -> Heart & Soul (zone de la Ligue et donjons redessinés).
# Dans Heart & Soul, la Route Victoire se traverse avant la Route 23 : Portail -> B2F -> B1F -> 1F -> Route 23.
PAIRES_FIXES = {
    'Route22_NorthEntrance': 'ReceptionGate', 'Route23': 'Route23', 'IndigoPlateau_Exterior': 'IndigoPlateau',
    'IndigoPlateau_PokemonCenter_1F': 'IndigoPlateau_PokemonCenter',
    'VictoryRoad_1F': 'VictoryRoadKanto_B2F', 'VictoryRoad_2F': 'VictoryRoadKanto_B1F',
    'VictoryRoad_3F': 'VictoryRoadKanto_1F',
    'PokemonLeague_LoreleisRoom': 'PokemonLeague_WillsRoom', 'PokemonLeague_BrunosRoom': 'PokemonLeague_KogasRoom',
    'PokemonLeague_AgathasRoom': 'PokemonLeague_BrunosRoom', 'PokemonLeague_LancesRoom': 'PokemonLeague_KarensRoom',
    'PokemonLeague_ChampionsRoom': 'PokemonLeague_ChampionsRoom', 'PokemonLeague_HallOfFame': 'PokemonLeague_HallOfFame',
    'ViridianForest': 'ViridianForest', 'Route2_ViridianForest_SouthEntrance': 'Gate_Route2_ViridianForest',
    'Route2_ViridianForest_NorthEntrance': 'Gate_ViridianForest_Route2',
    'MtMoon_1F': 'MtMoon_Cave',
    'DiglettsCave_B1F': 'DiglettsCave_Tunnel', 'DiglettsCave_NorthEntrance': 'DiglettsCave_EntranceNorth',
    'DiglettsCave_SouthEntrance': 'DiglettsCave_EntranceSouth',
    'RockTunnel_1F': 'RockTunnel_1F', 'RockTunnel_B1F': 'RockTunnel_B1F',
    'CeruleanCave_1F': 'CeruleanCave_1F', 'CeruleanCave_2F': 'CeruleanCave_B1F', 'CeruleanCave_B1F': 'CeruleanCave_B2F',
    'SeafoamIslands_1F': 'SeafoamIslands_1F', 'SeafoamIslands_B1F': 'SeafoamIslands_B1F',
    'SeafoamIslands_B4F': 'SeafoamIslands_SecretCave',      # salle d'Artikodin
    'CinnabarIsland_Gym': 'SeafoamIslands_Gym',             # comme dans Or et Argent : l'Arène d'Auguste est aux Îles Écume
    'PowerPlant': 'Route10_PowerPlantEntrance',
    'UndergroundPath_NorthEntrance': 'Route5_TunnelEntrance', 'UndergroundPath_SouthEntrance': 'Route6_TunnelEntrance',
    'UndergroundPath_WestEntrance': 'Route7_TunnelEntrance', 'UndergroundPath_EastEntrance': 'Route8_TunnelEntrance',
    'UndergroundPath_NorthSouthTunnel': 'SaffronCity_Tunnel_NS', 'UndergroundPath_EastWestTunnel': 'SaffronCity_Tunnel_SW',
    # Parc Safari : quatre zones reliées par des connexions, plus une grotte.
    'FuchsiaCity_SafariZone_Entrance': 'FuchsiaCity_SafariZoneEntrance', 'SafariZone_Center': 'FuchsiaCity_SafariZoneBeach',
    'SafariZone_West': 'FuchsiaCity_SafariZoneBrush', 'SafariZone_North': 'FuchsiaCity_SafariZoneMountain',
    'SafariZone_East': 'FuchsiaCity_SafariZoneCave',
    'SSAnne_Exterior': 'VermilionCity_PortInside',          # le quai de l'Océane
}
# Cartes déjà reprises de Heart & Soul par un travail antérieur (Mont Argenté) : elles servent seulement de cible.
DEJA = {'Route28': 'Route28', 'Route28_House': 'Route28_House'}
# Étages de Rouge Feu sans équivalent : leurs dresseurs et leurs objets rejoignent l'étage indiqué.
FUSIONS = {'SeafoamIslands_B1F': ['SeafoamIslands_B2F', 'SeafoamIslands_B3F'],
           'MtMoon_1F': ['MtMoon_B1F', 'MtMoon_B2F']}
# Cartes de Heart & Soul sans équivalent dans Rouge Feu, créées vides : nom -> (musique, zone de la carte).
NOUVELLES = {
    'MtMoon_Outside': ('MUS_RG_ROUTE3', 'MAPSEC_MT_MOON'), 'MtMoon_Shop': ('MUS_RG_ROUTE3', 'MAPSEC_MT_MOON'),
    'Route10_PowerPlantBackRoom': ('MUS_RG_POKE_MANSION', 'MAPSEC_POWER_PLANT'),
    'Route26North': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'), 'Route26': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'),
    'Route26_House1': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'), 'Route26_House2': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_26'),
    'Route27': ('MUS_RG_ROUTE24', 'MAPSEC_ROUTE_27'),
    'TohjoFalls_Cavern': ('MUS_RG_MT_MOON', 'MAPSEC_TOHJO_FALLS'),
    'TohjoFalls_GiovanniRoom': ('MUS_RG_MT_MOON', 'MAPSEC_TOHJO_FALLS'),
    'Route19_Cave': ('MUS_RG_MT_MOON', 'MAPSEC_ROUTE_19'),
    'SaffronCity_FightingDojoVIP': ('MUS_RG_GYM', 'MAPSEC_SAFFRON_CITY'),
    'VermilionCity_PortOutside': ('MUS_RG_VERMILLION', 'MAPSEC_VERMILION_CITY'),
}
ZONES = {'MAPSEC_ROUTE_26': ('ROUTE 26', 1, 10), 'MAPSEC_ROUTE_27': ('ROUTE 27', 0, 12),
         'MAPSEC_TOHJO_FALLS': ('CHUTES TOHJO', 0, 12)}
# Scripts de carte de Rouge Feu liés à l'ancien décor (courants, portes) : types retirés de la table de la carte.
SCRIPTS_RETIRES = {'SeafoamIslands_B4F': ('MAP_SCRIPT_ON_LOAD', 'MAP_SCRIPT_ON_WARP_INTO_MAP_TABLE', 'MAP_SCRIPT_ON_FRAME_TABLE')}

# Bâtiments de Rouge Feu absents de Heart & Soul : leurs occupants se tiennent dehors, dans la carte indiquée.
HABITANTS = {'SafariZone_Center': ['SafariZone_Center_RestHouse'],
             'SafariZone_West': ['SafariZone_SecretHouse', 'SafariZone_West_RestHouse'],
             'SafariZone_North': ['SafariZone_North_RestHouse'], 'SafariZone_East': ['SafariZone_East_RestHouse']}
# Déclencheurs gardés : carte -> script -> case dans le décor Heart & Soul.
P = 'FuchsiaCity_SafariZone_Entrance_EventScript_EntryTrigger'
DECLENCHEURS = {'FuchsiaCity_SafariZone_Entrance': {P + 'Mid': (5, 5), P + 'Right': (6, 5), P + 'Left': (4, 5)}}
# Portes ajoutées à un décor Heart & Soul : (x, y, carte, numéro de porte d'arrivée).
PORTES_AJOUTEES = {'SSAnne_Exterior': [(8, 10, 'MAP_SSANNE_1F_CORRIDOR', '2')]}
# PNJ (local_id ou script) et déclencheurs (script) d'un extérieur déplacés dans une autre carte : (source, clé, cible, x, y).
TRANSFERTS = [
    ('VermilionCity', 'LOCALID_VERMILION_FERRY_SAILOR', 'SSAnne_Exterior', 9, 9),
    ('VermilionCity', 'VermilionCity_EventScript_CheckTicketLeft', 'SSAnne_Exterior', 8, 9),
    ('VermilionCity', 'VermilionCity_EventScript_ExitedTicketCheck', 'SSAnne_Exterior', 8, 8),
]
# Scripts ajoutés à la fin du fichier d'une carte.
SCRIPTS_AJOUTES = {'SSAnne_Exterior': """
@ Bout de la passerelle : le décor Heart & Soul n'a pas de case de porte, un déclencheur fait monter à bord.
SSAnne_Exterior_EventScript_Embarquer::
	lockall
	warp MAP_SSANNE_1F_CORRIDOR, 2
	waitstate
	releaseall
	end
"""}
DECLENCHEURS_AJOUTES = {'SSAnne_Exterior': [(8, 10, 'VAR_TEMP_1', 'SSAnne_Exterior_EventScript_Embarquer')]}
# Scripts qui visent une case précise de l'ancien décor : fichier -> [(texte de Rouge Feu, texte adapté)].
E = 'FuchsiaCity_SafariZone_Entrance_'
REMPLACEMENTS = {
    # Ferry des îles Sevii : il accoste au quai du port, là où se tient désormais le marin.
    'src/seagallop.c': [
        ('MAP_GROUP(MAP_VERMILION_CITY), MAP_NUM(MAP_VERMILION_CITY),      0x17, 0x20',
         'MAP_GROUP(MAP_SSANNE_EXTERIOR), MAP_NUM(MAP_SSANNE_EXTERIOR),      8, 8'),
        ('mapGroup == MAP_GROUP(MAP_VERMILION_CITY)', 'mapGroup == MAP_GROUP(MAP_SSANNE_EXTERIOR)'),
        ('mapNum == MAP_NUM(MAP_VERMILION_CITY)', 'mapNum == MAP_NUM(MAP_SSANNE_EXTERIOR)'),
        ('pos.x < 24', 'pos.x < 9'),
    ],
    'data/scripts/safari_zone.inc': [('MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 4, 1', 'MAP_FUCHSIA_CITY_SAFARI_ZONE_ENTRANCE, 5, 2')],
    'data/maps/FuchsiaCity_SafariZone_Entrance_Frlg/scripts.inc': [
        ('MAP_SAFARI_ZONE_CENTER, 26, 30', 'MAP_SAFARI_ZONE_CENTER, 20, 39'),
        ('MAP_SAFARI_ZONE_CENTER, 255, 26, 30', 'MAP_SAFARI_ZONE_CENTER, 255, 20, 39'),
        # L'employé du guichet est à gauche du couloir, et la porte du parc une case plus loin.
        ('Common_Movement_WalkInPlaceFasterRight\n\twaitmovement 0\n\tshowmoneybox',
         'Common_Movement_WalkInPlaceFasterLeft\n\twaitmovement 0\n\tshowmoneybox'),
        (E + 'Movement_Exit::\n', E + 'Movement_Exit::\n\twalk_down\n'),
        (E + 'Movement_EnterSafariZoneMid::\n', E + 'Movement_EnterSafariZoneMid::\n\twalk_up\n'),
        (E + 'Movement_EnterSafariZoneRight::\n', E + 'Movement_EnterSafariZoneRight::\n\twalk_up\n'),
        (E + 'Movement_EnterSafariZoneLeft::\n', E + 'Movement_EnterSafariZoneLeft::\n\twalk_up\n'),
    ],
    'data/maps/SSAnne_Exterior_Frlg/scripts.inc': [
        ('SSAnne_Exterior_Movement_Exit::\n\twalk_up\n', 'SSAnne_Exterior_Movement_Exit::\n'),      # 8 pas jusqu'à la porte
        ('setvar VAR_MAP_SCENE_VERMILION_CITY, 2', 'setvar VAR_MAP_SCENE_VERMILION_CITY, 3'),
        ('warp MAP_VERMILION_CITY, 23, 34', 'warp MAP_VERMILION_CITY_PORT_OUTSIDE, 15, 9'),
    ],
}
