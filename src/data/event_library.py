import random
event_lookup_table = {
    "fleas": {
        "name": "Flea and Tick Meds",
        "resist": {
            "check": lambda dog: "Flea and Tick Meds" in dog.medications, #().keys(),
            "message": "Your dog was exposed to fleas, but fortunately they were on flea and tick meds and it didn't catch them.",
            },
        "intro": "Your dog is itchy and has little brown dots jumping from its skin. Do you... ?",
        "options": {
            "1": {
                "intro": "Take your dog and get rid of those fleas!", 
                "outro": "Your vet prescribes medication to your dog and flea shampoo. It takes several hours over the next few weeks to completely remove the fleas from your house, and the treatment isn't cheap. Your vet strongly recommends that you begin a medication plan for flea and tick meds. These will prevent your dog from getting fleas or ticks in the future.",
                },
            "2": {
                "intro": "Ignore it for now. It's only fleas right?",
                "outro": "Your dog won't stop scratching themself, and your skin is beginning to crawl.", 
                },
            },
        },


    "heartworm": {
        "name": "Heartworm Meds",
        "resist": {
            "check": lambda dog: "Heartworm Meds" in dog.medications, #().keys(),
            "message": "Your dog was exposed to Heartworm, but luckily has already taken medication for that!",
            },
        "intro": "Your dog is having trouble breathing and is very lethargic. Do you... ?",
        "options": {
            "1": {
                "intro": "Take your dog to the vet!", 
                "outro": "Your vet diagnosis your dog with Heartworms and prescribes a one-time medication: ProHeart. It's a chewable tablet.",
                },
            "2": {
                "intro": "Ignore it for now... it's probably fine?",
                "outro": "Your dog is increasingly unable to breathe, and limps around the house. You think something is really wrong.", 
                },
            },
        },
    
    "ingrown_nail": {
        "name": "ingrown_nail",
        "resist": {
            "check": lambda dog: False,  #
            "message": "n/a",
            },
        "intro": "Your dog is limping around your kitchen and yelping when putting pressure on its paw! Do you... ?",
        "options": {
            "1": {
                "intro": "Take your dog to the vet!", 
                "outro": "Your vet fixes your dogs ingrown nail!",
                },
            "2": { 
                "intro": "Ignore it. That will heal on it's own, right?",
                "outro": "Your dog limps for a couple weeks, but eventually the condition appears to sort itself out.", 
                },
            },
        },

    "bur_in_paw": {
        "name": "bur_in_paw",
        "resist": {
            "check": lambda dog: False,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Your dog is limping around your kitchen and yelping when putting pressure on its paw! Will you... ?",
        "options": {
            "1": {
                "intro": "Go to the vet and try to fix it!", 
                "outro": "Your vet removes the bur from your dogs foot!",
                },
            "2": { 
                "intro": "Ignore it for now. That'll go away, right?",
                "outro": "Eventually, the bur disloges from your dogs foot, and heals on it's own.",  
                },
            },
        },

    "allergies": {
        "name": "allergies",
        "resist": {
            "check": lambda dog: False,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Your dog has watery eyes and has been repeatedly sneezing. Do you... ?",
        "options": {
            "1": {
                "intro": "Take your dog to the vet.", 
                "outro": "Your vet diagnosis your dog with allergies. The treatment is a medication is a recurrent and lifelong.",
                },
            "2": { 
                "intro": "Do nothing, we all get sneezy.",
                "outro": "Your dog continues to sneeze and have very watery eyes.",  
                },
            },
        },

    "obesity": {
        "name": "obesity",
        "resist": {
            "check": lambda dog: (dog.walk_schedule is "Medium" and dog.meal_plan in ["Normal", "Vet Recommended"]) or (dog.walk_schedule is "Long") ,  #add a clause for excersise when this is added to the dog object model
            "message": "Maybe your dog just had a big lunch? Well done for walking you dog consistently and feeding it properly. Your dog has avoided obesity.",
            },
        "intro": "Your dog appears to be gaining weight is having trouble goin to the bathroom. Do you... ?",
        "options": {
            "1": {
                "intro": "Take your dog to the vet.", 
                "outro": "Your vet informs you your dog is obese. You must be consistent about walking your dog frequently and feeding it healthy food.",
                },
            "2": { 
                "intro": "Do nothing, your dog won't die of obesity, right?",
                "outro": "Your dog continues to gain weight and lose mobility.",  
                },
            },
        },
    
    "cancer": {
        "name": "cancer",
        "resist": {
            # This is essentially making it happen if they've made poor lifestyle decisions or giving them 33% chance of resisting in healthy
            "check": lambda dog: random.choice([0, 0, (dog.walk_schedule in ["medium", "long"] and dog.meal_plan in ["normal", "vet_recommended"])]),  #add a clause for excersise when this is added to the dog object model
            "message": "While resisting cancer is difficult, frequent excercise and proper diet are the best mechanisms for prevention.",
            },
        "intro": "Your dog is lethargic and seems to have no motivation to do anything. Do you... ?",
        "options": {
            "1": {
                "intro": "Take your dog to the vet.", 
                "outro": "Your vet informs you your dog has cancer. Treatment involves surgery and encouraging healthy behaviour following recovery.",
                },
            "2": { 
                "intro": "Do nothing, maybe it's a case of seasonal depression?",
                "outro": "Your dog continues to lose energy and is no longer playful.",  
                },
            },
        },
    
    # These are the general events, separate from the "afflictions"

    "dog_ate_pizza": {
        "name": "dog_ate_pizza",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "Your dog didn't eat your pizza",
            },
        "intro": "Your dog ate your pizza while you got up to go to the bathroom. Your dog will be fine... but now you need to find other dinner plans.",
        "options": {
            "1": {
                "intro": "Take your dog to the vet.", 
                "outro": "Your vet says your dog is fine. Try to avoid letting it eat your pizza.",
                },
            "2": { 
                "intro": "Do nothing, your dog seems to have liked it.",
                "outro": "Your dog appears to be fine. Make sure you consult a prohibited foods list whenever your dog eats something.",  
                },
            },
    },
    
    "accident": {
        "name": "accident",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "Your dog didn't have an accident",
            },
        "intro": "You left to go to dinner with friends and stayed out longer than usual. Your dog had an accident in the house while being left at home.",
        "options": {
            "1": {
                "intro": "Take your dog to a trainer", 
                "outro": "Your dog is much more obedient and less likely to have an accident.",
                },
            "2": { 
                "intro": "Do nothing, your dog probably won't do it again.",
                "outro": "You clean up your dog's accident and stay more responsible about returning on time.",  
                },
            },
    },
    
    "dislikes_friend": {
        "name": "dislikes_friend",
        "resist": {
            "check": lambda dog: dog.happiness>60,  #add a clause for excersise when this is added to the dog object model
            "message": "You've been caring for you dog and your dog is well-behaved as a result.'",
            },
        "intro": "Your friend came over for dinner and your dog wouldn't stop barking at them. Do you...?",
        "options": {
            "1": {
                "intro": "Leave your dog inside and go out to dinner with your friend.", 
                "outro": "You feel bad so you offer to pay for their dinner.",
                },
            "2": { 
                "intro": "Lock your dog outside.",
                "outro": "You and your friend enjoy your dinner while your dog whimpers from behind the glass door.",  
                },
            },
    },
     
    "bit_other_dog": {
        "name": "bit_other_dog",
        "resist": {
            "check": lambda dog: dog.happiness>20,  #add a clause for excersise when this is added to the dog object model
            "message": "You've been caring for you dog and your dog is not aggressive as a result.'",
            },
        "intro": "You take your dog to the dog park. It bites another dog. Do you...?",
        "options": {
            "1": {
                "intro": "Pay for the other dogs medical bill and apologize profusely.", 
                "outro": "You feel bad so you offer to pay for their dinner.",
                },
            "2": { 
                "intro": "Say your sorry and leave. You are banned from this dog park, however.",
                "outro": "The other dog is fine. Your dog may bite again though.",  
                },
            },
    }
     

}

