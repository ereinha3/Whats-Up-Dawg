#shop menu numbers are mocked
#need research to support specific costs
care_items = {
    "Doggy Treat": {
        "cost": 5,
        "display": "Doggy Treat",
        "happiness": 0.25,
        "duration": 1,
        },
    "Doggy Puzzle": {
        "cost": 20,
        "display": "Doggy Puzzle",
        "happiness": 0.5,
        "duration": 5,
        },
    "Plushy Toy": {
        "cost": 10,
        "display": "Plushy Toy",
        "happiness": 0.5,
        "duration": 2
        },
    "Nylabone": {
        "cost": 5,
        "display": "Nylabone",
        "happiness": 0.5,
        "duration": 3,
        "health": -1,
        },
    "Butcher Bone": {
        "cost": 5,
        "display": "Butcher Bone",
        "happiness": 0.5,
        "health": -2,
        "duration": 1,
        },
    "Kong Toy": {
        "cost": 10,
        "display": "Kong Toy",
        "duration": 10,
        "happiness": 0.25,
        },
    "Doggy Bed": {
        "cost": 20,
        "display": "Doggy Bed",
        "duration": 5,
        "happiness": 2,
        },
    }

medications = {
        "Flea and Tick Meds": {
            "cost": 150, #cost from chewy: https://www.chewy.com/nexgard-chew-dogs-241-60-lbs-purple/dp/173254
            "duation": 1,
            "display": "Flea and Tick Meds",
            },
        "Heartworm Meds": {
            "cost": 150, #cost from chewy: https://www.chewy.com/nexgard-chew-dogs-241-60-lbs-purple/dp/173254
            "duation": 1,
            "display": "Heartworm Meds",
            },
    }

walk_options = {"short": {"time": 2, "health": 1, "happiness": 0}, "medium": {"time": 7, "health": 2, "happiness": 3}, "long": {"time": 15, "health": 3, "happiness": 5}}

meal_options = {"cheap": {"display": "Walmart's Finest", "cost": 1.07, "health": 1}, "normal": {"display": "Purina One", "cost": 1.84, "health": 2}, "vet_recommended": {"display": "Vet Recommended", "cost": 2.15, "health": 3}}
