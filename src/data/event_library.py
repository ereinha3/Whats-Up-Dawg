event_lookup_table = {
    "fleas": {
        "name": "fleas",
        "resist": {
            "check": lambda dog: "fleas" in dog.medications, #().keys(),
            "message": "Your dog was exposed to fleas, but fortunately they were on flea and tick meds and it didn't catch them.",
            },
        "intro": "Your dog has fleas. Do you... ?",
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


    "heartworms": {
        "name": "heartworm",
        "resist": {
            "check": lambda dog: "ProHeart" in dog.medications, #().keys(),
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
        "intro": "Your dog has an ingrown nail! Do you... ?",
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
        "intro": "Your dog has a bur in it's paw! Will you... ?",
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
    }

