#shop menu numbers are mocked
#need research to support specific costs
care_items = {
    "treats": {
        "cost": 5,
        "display": "Doggy Treat",
        "happiness": 0.25,
        "duration": 1,
        },
    "puzzle": {
        "cost": 20,
        "display": "Doggy Puzzle",
        "happiness": 0.5,
        "duration": 5,
        },
    "plushy": {
        "cost": 10,
        "display": "Plushy Toy",
        "happiness": 0.5,
        "duration": 2
        },
    "nylabone": {
        "cost": 5,
        "display": "Nylabone",
        "happiness": 0.5,
        "duration": 3,
        "health": -1,
        },
    "butcherbone": {
        "cost": 5,
        "display": "Butcher Bone",
        "happiness": 0.5,
        "health": -2,
        "duration": 1,
        },
    "kong": {
        "cost": 10,
        "display": "Kong Toy",
        "duration": 10,
        "happiness": 0.25,
        },
    "bed": {
        "cost": 20,
        "display": "Doggy Bed",
        "duration": 5,
        "happiness": 2,
        },
    }

medications = {
        "flea_and_tick": {
            "cost": 150, #cost from chewy: https://www.chewy.com/nexgard-chew-dogs-241-60-lbs-purple/dp/173254
            "duation": 1,
            "display": "Flea and Tick Meds",
            },
    }
default_walk_options = {"short": {"time": 2, "health": 1, "happiness": 0}, "medium": {"time": 7, "health": 2, "happiness": 3}, "long": {"time": 15, "health": 3, "happiness": 5}}

meal_options = {"cheap": {"display": "Walmart's Finest", "cost": 65, "health": 1}, "vet_recommended": {"display": "Vet Recommended", "cost": 200, "health": 2}}
