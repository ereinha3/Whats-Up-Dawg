from random import *
import math
afflictions_dictionary = {
    0: 
        {
          "dog_ate_pizza": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 30,  "time": 1 },
            "health": 0,
            "happiness": 0,
            "description": "Your dog got the runs and you had to do a little extra clean-up as a result. While you shouldn't give you dog pizza, it won't significantly impact its health.",
            }, 
          "accident": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 2 },
            "health": 0,
            "happiness": 0,
            "description": "Your dog had an accident in the house, requiring you to clean it up.",
            },
          "dislikes_friend": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 60,  "time": 0 },
            "health": 0,
            "happiness": -5,
            "description": "Your dog dislikes your friend. You take your friend out to dinner instead of having them over for dinner.",
            },
          "bit_other_dog": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : random.randint(3, 6)*100,  "time": 4},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "brings_rat": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 1},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "singing": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 1},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "growls": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 2},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "dog_on_table": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 4},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "begs": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 2},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "apple_juice": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 150,  "time": 4},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "spin": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "socks": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 1},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "scratched_sofa": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "heel": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 2},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "marigolds": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "car_window": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "trash": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 1},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "let_out": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 1},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "lasagna": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "dirty_dog": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 2},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "doorbell": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 4},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "wrong_word": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 2},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "barber": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "father": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "collar": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 25},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "bonus_tricks": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "mouth_kiss": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "tight collar": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 30,  "time": 1},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "dog_sitter": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 40,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
          "play_date": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 0,  "time": 0},
            "health": 0,
            "happiness": 0,
            "description": "Your dog bit another dog. This is a result of disobedience stemming from poor training.",
            },
        },
    1:
        {
        "fleas": {
            "duration" : 1, #until treatment
            "indefinite": False, #until death
            "cure": { "cost": lambda dog : 150,  "time": 8, },
            "health": -5,
            "happiness": -5,
            "description": "Fleas cause anemia, and may carry eggs from other parasites, particularly tapeworms. Treatment involves medications, specialty shampoos and extermination of fleas from the environment.",
            },
        "ingrown_nail" : {
            "duration" : 1,
            "indefinite": False,
            "cure": { "cost": lambda dog : 100,  "time": 1, }, 
            "health": -1,
            "happiness": -2,
            "description": "Your dog has an ingrown nail on its paw.",
            },
        "bur_in_paw" : {
            "duration" : 1,
            "indefinite": False,
            "cure": { "cost": lambda dog : 100,  "time": 1, }, 
            "health": -1,
            "happiness": -2,
            "description": "Your dog has a burr in its paw.",
            },
        },
    2:
        {
        "allergies" : {
            "duration": math.inf,
            "indefinite": True,
            "cure": { "cost": lambda dog : 60,  "time": 1, }, #this is the recurrent cost... NOT the intitial cost. That will be in the event lookup 
            "health": -1,
            "happiness": -2,
            "description": "Allergies are a lifelong condition. Your dog will need to recieve treatment for it's whole life.",
            },
        "obesity" : {
            "duration": 3,
            "indefinite": False,
            "cure": { "cost": lambda dog : 0,  "time": 10, }, #this is the recurrent cost... NOT the intitial cost. That will be in the event lookup 
            "health": -3,
            "happiness": -2,
            "description": "Obesity is a lasting condition. You will need to walk you dog more frequenlty and feed better food.",
            },
        },
    3:
        {    
        "heartworm" : {
            "duration" : 1,
            "indefinite": False,
            "cure": { "cost": lambda dog : 500 + (200*dog.weight)//50,  "time": 2, }, #WHEN SIZE is implemented, change cost to lambda dog : dog.get_size() to output between $500-1100
            "health": -100,
            "happiness": -8,
            "description": "Heartworms is a very serious parasitic disease affecting the lungs, heart, and other organs. Will result in death if left untreated.",
            },
        },
        
    4: 
        {    
        "cancer" : {
            "duration" : 1,
            "indefinite": False,
            "cure": { "cost": lambda dog : 4100,  "time": 2, }, #WHEN SIZE is implemented, change cost to lambda dog : dog.get_size() to output between $500-1100
            "health": -100,
            "happiness": -8,
            "description": "Dogs are prone to developing an array of different types of cancer. Different breeds are more prone to certain affected areas than other. Consult a guide for your breed to prevent.",
            },
        },



}
