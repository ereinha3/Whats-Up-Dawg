'''
{
        n: "an integer representing the severity/commonality class used by the event loader to organize events." {
        "event_name": {
            "intro": "Description that prints when the event loads."
            "options": {
                "vet": {
                    "message": "Description of what happens when you take your dog to the vet to resolve this event.",
                    "cost": "A float representing the financial cost imposed on the human for choosing this option.",
                    "time": "A float representing the amount of time spent by the human in choosing this option.",
                    "health": "A float representing the net change in the dogs health as a result of this event.",
                    "happiness": "A float representing the net change in the dogs happiness as a result of this event.",
                    "afflictions": "Any afflictions that this event imparts on the dog.",
                },
                "ignore": {
                    "...": "message and all of the same key value pairs for the vet option"
                    },
                },
            },
        },
        #...etc.
},

i.e.

1: {
    "fleas": {
        "intro": "Your dog has fleas. Do you?",
        "options": {
            "vet": {
                "message": "Your vet prescribes medication to your dog and flea shampoo. It takes several hours over the next few weeks to completely remove the fleas from your house, and the treatment isn't cheap. Your vet strongly recommends that you begin a medication plan for flea and tick meds. These will prevent your dog from getting fleas or ticks in the future.",
                "cost": 150,
                "time": 8,
                },
            "ignore": {
                "message": "Your dog won't stop scratching themself, and your skin is beginning to crawl.", 
                "health": -5, 
                "happiness": -5, 
            },
        },
    },
},
'''
