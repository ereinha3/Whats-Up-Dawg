from random import *
afflictions_dictionary = {
    "fleas": {
        "persistent": True, #until treatment
        "indefinite": False, #until death
        "cure": { "cost": 150,  "work": 8, },
        "harm": 5,
        "stress": 5,
        "description": "Fleas cause anemia, and may carry eggs from other parasites, particularly tapeworms. Treatment involves medications, specialty shampoos and extermination of fleas from the environment.",
    },
    "heartworms" : {
        "persistent": True,
        "indefinite": False,
        "cure": { "cost": lambda dog : 500 + 600*random.random(),  "work": 2, }, #WHEN SIZE is implemented, change cost to lambda dog : dog.get_size() to output between $500-1100
        "harm": 10,
        "stress": 8,
        "description": "Heartworms is a very serious parasitic disease affecting the lungs, heart, and other organs. Will result in death if left untreated.",
    },
    "ingrown_nail" : {
        "persistent": False,
        "indefinite": False,
        "cure": { "cost": lambda dog : 100,  "work": 1, }, 
        "harm": 1,
        "stress": 2,
        "description": "Your dog has an ingrown nail on its paw.",
    },
    "bur_in_paw" : {
        "persistent": False,
        "indefinite": False,
        "cure": { "cost": lambda dog : 100,  "work": 1, }, 
        "harm": 1,
        "stress": 2,
        "description": "Your dog has a burr in its paw.",
    },
    "allergies" : {
        "persistent": True,
        "indefinite": True,
        "cure": { "cost": lambda dog : 60,  "work": 1, }, #this is the recurrent cost... NOT the intitial cost. That will be in the event lookup 
        "harm": 1,
        "stress": 2,
        "description": "Allergies are a lifelong condition. Your dog will need to recieve treatment for it's whole life.",
    },



}
