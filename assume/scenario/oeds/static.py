# SPDX-FileCopyrightText: ASSUME Developers
#
# SPDX-License-Identifier: AGPL-3.0-or-later

fuel_translation = {
    "Wind": "wind",
    "Wasser": "hydro",
    "Solar": "solar",
    "Braunkohle": "lignite",
    "Biomasse": "biomass",
    "Geothermie": "geothermal",
    "Grubengas": "landfill gas",
    "andere Gase": "landfill gas",
    "nicht biogener Abfall": "waste",
    "Steinkohle": "hard coal",
    "Erdgas": "gas",
    "Mineralölprodukte": "oil",
    "Kernenergie": "nuclear",
    "Speicher": "storage",
}


# SolarLage
mastr_solar_codes = {
    "free_area": "852",
    "roof_top": "853",
    "other": "2484",
    "balcony": "2961",
    "water": "3002",
    "parking_lot": "3058",
}

mastr_solar_azimuth = {
    "695": "0",
    "696": "45",
    "697": "90",
    "698": "135",
    "699": "180",
    "700": "225",
    "701": "270",
    "702": "315",
    "703": "360",
    "704": "-1",
    "806": "90",
    "807": "75",
    "808": "50",
    "809": "30",
    "810": "10",
    "811": "0",
    "802": "100",
    "803": "70",
    "804": "60",
    "805": "50",
    "1535": "100",
}

mastr_storage = {
    "Niederwartha": 591,
    "Bleiloch": 753,
    "Hohenwarte 1": 795,
    "Hohenwarte 2": 2087,
    "Wendefurth": 532,
    "Markersbach": 4018,
    "Geesthacht": 600,
    "Waldeck 1": 478,
    "Waldeck 2": 3428,
    "Bringhausen": 0,
    "Hemfurth": 0,
    "illwerke": 0,
    "Glems": 560,
    "Schwarzenbach": 198,
    "Witznau": 220,
    "Säckingen": 2064,
    "Häusern": 463,
    "Waldshut": 402,
    "Wehr": 6073,
    "Walchenseekraftwerk": 0,
    "Happurg": 900,
    "Schnitzel": 0,
    "Langenprozelten": 950,
    "E2307101": 0,
    "Goldisthal": 8480,
}

# start cost given in [€/MW]
# chi in [t CO2/MWh therm.]
# Set technical parameter corresponding to the type (0, 2000, 2024)
technical_parameter = {
    "hard coal": {
        0: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 1,
            "ramp_down": 1,
            "eta": 36,
            "chi": 0.355,
            "min_down_time": 9,
            "min_operating_time": 8,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
        2000: {
            "maxPower": 100,
            "minPower": 33,
            "ramp_up": 4,
            "ramp_down": 4,
            "eta": 40,
            "chi": 0.355,
            "min_down_time": 7,
            "min_operating_time": 6,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
        2024: {
            "maxPower": 100,
            "minPower": 25,
            "ramp_up": 6,
            "ramp_down": 6,
            "eta": 45,
            "chi": 0.355,
            "min_down_time": 5,
            "min_operating_time": 4,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
    },
    "gas_combined": {
        0: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 2,
            "ramp_down": 2,
            "eta": 45,
            "chi": 0.202,
            "min_down_time": 4,
            "min_operating_time": 4,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
        2000: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 4,
            "ramp_down": 4,
            "eta": 55,
            "chi": 0.202,
            "min_down_time": 3,
            "min_operating_time": 3,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
        2024: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 8,
            "ramp_down": 8,
            "eta": 65,
            "chi": 0.202,
            "min_down_time": 2,
            "min_operating_time": 2,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
    },
    "gas": {
        0: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 8,
            "ramp_down": 8,
            "eta": 40,
            "chi": 0.202,
            "min_down_time": 4,
            "min_operating_time": 4,
            "start_cost": 20,
            "on": 1,
            "off": 0,
        },
        2000: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 12,
            "ramp_down": 12,
            "eta": 45,
            "chi": 0.202,
            "min_down_time": 3,
            "min_operating_time": 3,
            "start_cost": 20,
            "on": 1,
            "off": 0,
        },
        2024: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 15,
            "ramp_down": 15,
            "eta": 50,
            "chi": 0.202,
            "min_down_time": 2,
            "min_operating_time": 2,
            "start_cost": 20,
            "on": 1,
            "off": 0,
        },
    },
    "lignite": {
        0: {
            "maxPower": 100,
            "minPower": 60,
            "ramp_up": 1.0,
            "ramp_down": 1.0,
            "eta": 34,
            "chi": 0.407,
            "min_down_time": 9,
            "min_operating_time": 8,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
        2000: {
            "maxPower": 100,
            "minPower": 50,
            "ramp_up": 2.5,
            "ramp_down": 2.5,
            "eta": 40,
            "chi": 0.407,
            "min_down_time": 7,
            "min_operating_time": 6,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
        2024: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 4.0,
            "ramp_down": 4.0,
            "eta": 45,
            "chi": 0.407,
            "min_down_time": 5,
            "min_operating_time": 4,
            "start_cost": 60,
            "on": 1,
            "off": 0,
        },
    },
    "nuclear": {
        0: {
            "maxPower": 100,
            "minPower": 50,
            "ramp_up": 0.5,
            "ramp_down": 0.5,
            "eta": 33,
            "chi": 0,
            "min_down_time": 22,
            "min_operating_time": 20,
            "start_cost": 250,
            "on": 1,
            "off": 0,
        },
        2000: {
            "maxPower": 100,
            "minPower": 45,
            "ramp_up": 0.5,
            "ramp_down": 0.5,
            "eta": 35,
            "chi": 0,
            "min_down_time": 22,
            "min_operating_time": 15,
            "start_cost": 250,
            "on": 1,
            "off": 0,
        },
        2024: {
            "maxPower": 100,
            "minPower": 40,
            "ramp_up": 0.5,
            "ramp_down": 0.5,
            "eta": 38,
            "chi": 0,
            "min_down_time": 22,
            "min_operating_time": 10,
            "start_cost": 250,
            "on": 1,
            "off": 0,
        },
    },
}
