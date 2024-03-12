#shop menu numbers are mocked
#need research to support specific costs
care_items = {
    "Doggy Treat": {
        "name": "Doggy Treat",
        "cost": 5,
        "display": "Doggy Treat",
        "happiness": 0.25,
        "duration": 1,
        "health": 0
        },
    "Doggy Puzzle": {
        "name": "Doggy Puzzle",
        "cost": 20,
        "display": "Doggy Puzzle",
        "happiness": 0.5,
        "duration": 5,
        "health": 0
        },
    "Plushy Toy": {
        "name": "Plushy Toy",
        "cost": 10,
        "display": "Plushy Toy",
        "happiness": 0.5,
        "duration": 2,
        "health": 0
        },
    "Nylabone": {
        "name": "Nylabone",
        "cost": 5,
        "display": "Nylabone",
        "happiness": 0.5,
        "duration": 3,
        "health": -1,
        },
    "Butcher Bone": {
        "name": "Butcherbone",
        "cost": 5,
        "display": "Butcher Bone",
        "happiness": 0.5,
        "health": -2,
        "duration": 1,
        },
    "Kong Toy": {
        "name": "Kong Toy",
        "cost": 10,
        "display": "Kong Toy",
        "duration": 10,
        "happiness": 0.25,
        "health": 0
        },
    "Doggy Bed": {
        "name": "Doggy Bed",
        "cost": 20,
        "display": "Doggy Bed",
        "duration": 5,
        "happiness": 2,
        "health": 0
        },
    }

medications = {
        "Flea and Tick Meds": {
            "treatment": "fleas",
            "cost": 150, #cost from chewy: https://www.chewy.com/nexgard-chew-dogs-241-60-lbs-purple/dp/173254
            "duration": 1,
            "display": "Flea and Tick Meds",
            },
        "Heartworm Meds": {
            "treatment": "heartworm",
            "cost": 150, #cost from chewy: https://www.chewy.com/nexgard-chew-dogs-241-60-lbs-purple/dp/173254
            "duration": 1,
            "display": "Heartworm Meds",
            },
    }

walk_options = {
        "short": {
            "name": "short",
            "display": "Short", 
            "time": 0.5, 
            "health": 1, 
            "happiness": 0
        }, 
        "medium": {
            "name": "medium",
            "display": "Medium", 
            "time": 1, 
            "health": 2, 
            "happiness": 3
        }, 
        "long": {
            "name": "long",
            "display": "Long", 
            "time": 2, 
            "health": 3, 
            "happiness": 5,
            }
        }

meal_options = {
        "cheap": {
            "name": "cheap",
            "display": "Walmart's\nCheapest", 
            "cost": 1.07, 
            "health": 1,
            }, 
        "normal": {
            "name": "normal",
            "display": "Walmart's\nFinest",
            "cost": 1.84, 
            "health": 2,
        }, 
        "vet_recommended": {
            "name": "vet_recommended",
            "display": "Vet\nRecommended", 
            "cost": 2.15, 
            "health": 3,
        }
    }
