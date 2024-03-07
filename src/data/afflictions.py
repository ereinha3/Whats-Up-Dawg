from random import *
afflictions_dictionary = {
    0: 
        {
          "dog_ate_pizza": {
            "persistent": False, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 30,  "work": 1 },
            "health": 0,
            "stress": 0,
            "description": "Your dog got the runs and you had to do a little extra clean-up as a result. While you shouldn't give you dog pizza, it won't significantly impact its health.",
            }, 
          "accident": {
            "persistent": False, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "work": 2 },
            "health": 0,
            "stress": 0,
            "description": "Your dog had an accident in the house, requiring you to clean it up.",
            },
          "dislikes_friend": {
            "persistent": False, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 60,  "work": 0 },
            "health": 0,
            "stress": -5,
            "description": "Your dog dislikes your friend. You take your friend out to dinner instead of having them over for dinner.",
            },
          "bit_other_dog": {
            "persistent": False, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : random.randint(3, 6)*100,  "work": 4},
            "health": 0,
            "stress": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
        },
    1:
        {
        "fleas": {
            "persistent": True, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 150,  "work": 8, },
            "health": -5,
            "stress": -5,
            "description": "Fleas cause anemia, and may carry eggs from other parasites, particularly tapeworms. Treatment involves medications, specialty shampoos and extermination of fleas from the environment.",
            },
        "ingrown_nail" : {
            "persistent": False,
            "indefinite": False,
            "cure": { "cost": lambda dog : 100,  "work": 1, }, 
            "health": -1,
            "stress": -2,
            "description": "Your dog has an ingrown nail on its paw.",
            },
        "bur_in_paw" : {
            "persistent": False,
            "indefinite": False,
            "cure": { "cost": lambda dog : 100,  "work": 1, }, 
            "health": -1,
            "stress": -2,
            "description": "Your dog has a burr in its paw.",
            },
        },
    2:
        {
        "allergies" : {
            "persistent": True,
            "indefinite": True,
            "cure": { "cost": lambda dog : 60,  "work": 1, }, #this is the recurrent cost... NOT the intitial cost. That will be in the event lookup 
            "health": -1,
            "stress": -2,
            "description": "Allergies are a lifelong condition. Your dog will need to recieve treatment for it's whole life.",
            },
        "obesity" : {
            "persistent": True,
            "indefinite": True,
            "cure": { "cost": lambda dog : 0,  "work": 10, }, #this is the recurrent cost... NOT the intitial cost. That will be in the event lookup 
            "health": -3,
            "stress": -2,
            "description": "Obesity is a lasting condition. You will need to walk you dog more frequenlty and feed better food.",
            },
        },
    3:
        {    
        "heartworm" : {
            "persistent": True,
            "indefinite": False,
            "cure": { "cost": lambda dog : 500 + (200*dog.weight)//50,  "work": 2, }, #WHEN SIZE is implemented, change cost to lambda dog : dog.get_size() to output between $500-1100
            "health": -100,
            "stress": -8,
            "description": "Heartworms is a very serious parasitic disease affecting the lungs, heart, and other organs. Will result in death if left untreated.",
            },
        },
        
    4: 
        {    
        "cancer" : {
            "persistent": True,
            "indefinite": False,
            "cure": { "cost": lambda dog : 4100,  "work": 2, }, #WHEN SIZE is implemented, change cost to lambda dog : dog.get_size() to output between $500-1100
            "health": -100,
            "stress": -8,
            "description": "Dogs are prone to developing an array of different types of cancer. Different breeds are more prone to certain affected areas than other. Consult a guide for your breed to prevent.",
            },
        },



}
