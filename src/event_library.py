event_lookup_table = {
    "fleas": {
        "resist": {
            "check": lambda dog: "flea_and_tick" in dog.get_meds().keys(),
            "message": "Your dog was exposed to fleas, but fortunately they were on flea and tick meds and didn't catch them."\
            },
        "intro": "Your dog has fleas. Do you?",
        "options": {
            "1": {
                "intro": "Take your dog and get rid of those fleas!", 
                "outro": "Your vet prescribes medication to your dog and flea shampoo. It takes several hours over the next few weeks to completely remove the fleas from your house, and the treatment isn't cheap. Your vet strongly recommends that you begin a medication plan for flea and tick meds. These will prevent your dog from getting fleas or ticks in the future.",
                "cost": 150,
                "work": 8,
                },
            "2": {
                "intro": "Ignore it for now. It's only fleas right?",
                "outro": "Your dog won't stop scratching themself, and your skin is beginning to crawl.", 
                "harm": 5, 
                "stress": 5, 
                "afflictions": {
                    "fleas": {
                    "persistent": True,
                    "cure": {
                        "cost": 150, 
                        "work": 8,
                        },
                    "harm": 5,
                    "stress": 5,
                    "description": "Fleas cause anemia, and may carry eggs from other parasites, particularly tapeworms. Treatment involves medications, specialty shampoos and extermination of fleas from the environment.",
                             },
                         },
                },
            },
        },
    }
