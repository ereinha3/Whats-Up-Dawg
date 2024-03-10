import random
event_lookup_table = {
    "fleas": {
        "name": "fleas",
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
        "name": "heartworm",
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
            "check": lambda dog: (dog.walk_schedule is "Medium" and dog.meal_plan is "Vet Recommended") or (dog.walk_schedule is "Long" and dog.meal_plan in []) ,  #add a clause for excersise when this is added to the dog object model
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
        "singing": {
         "name": "singing",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "Your dog didn't sing.",
            },
        "intro": "You start humming to yourself and see that your dog starts singing along to Twinkle Twinkle Little Star. You manage to catch some of it on video! Do you… ?",
        "options": {
            "1": {
                "intro": "Submit that video to America's Got Talent!", 
                "outro": "You submit the video to America's Got Talent. Unfortunately you never hear back.",
                },
            "2": { 
                "intro": "Decide not to submit the video.",
                "outro": "You keep your dogs talents hidden.",  
                },
            },
    },
        "brings_rat": {
         "name": "brings_rat",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "Your dog didn't bring rat.",
            },
        "intro": "After letting your dog out to pee, you are brought back a present of a little dead critter. How lovely! Do you… ?",
        "options": {
            "1": {
                "intro": "Say thank you and bury the sweet thing in the back yard. It deserves a proper send off.", 
                "outro": "You and your dog attend the service. It was beautiful.",
                },
            "2": { 
                "intro": "Scream and kick it away. Hello!? Diseases?",
                "outro": "Your dog appears disgruntled by your lack of appreciation for the gift.",  
                },
            },
    },
        "growls": {
         "name": "growls",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "Your dog didn't growl when the mailman comes.",
            },
        "intro": "Your dog growls when the pizza guy comes to the door. Uh oh! Do you... ?",
        "options": {
            "1": {
                "intro": "Scold your dog and appologize profusely.", 
                "outro": "You give your dog a stern talking to.",
                },
            "2": { 
                "intro": "Let the pizza guy know that he only growls at cute delivery men.",
                "outro": "The pizza man does not return your interest.",  
                },
            },
    },

        "dog_on_table": {  #        7
         "name": "dog_on_table",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "During a play fight, your dog gets rambunctious and decides to jump on the kitchen table. Do you… ?",
        "options": {
            "1": {
                "intro": "Say 'DOWN' sternly and wait for your dog to hop down.", 
                "outro": "After a couple times of firmly repeating yourself, your dog eventually hops down. Problem solved!",
                },
            "2": { 
                "intro": "Scoop your dog off of the table yourself.",
                "outro": "Your dog gets a little sassy with you, but doesn't hop back onto the table. ",  
                },
            },
    },

    "begs": {  #        8
         "name": "begs",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You notice your dog begging for some chicken alfredo from one of your house guests at the dinner table. Do you... ? ",
        "options": {
            "1": {
                "intro": "Let them know that they can give your dog a liiiitle bit of food! But not too much!", 
                "outro": "They take you up on your offer, and your dog doesn't leave the dinnertable all night longer.",
                },
            "2": { 
                "intro": "Kindly ask your guest not to feed your dog from the dinnertable.",
                "outro": "Your dog sticks around for a while longer, but eventually walks off. ",  
                },
            },
    },

    "apple_juice": {  #        9
         "name": "apple_juice",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "While kicking back and watching How to Lose a Guy in 10 Days with your buddies, you spill some of your apple juice on the floor, quickly lapped up by your dog. Uh oh! Do you... ?",
        "options": {
            "1": {
                "intro": "Take him to the vet. Better safe than sorry!", 
                "outro": "You call off movie night to take your dog to the vet. The vet tells you your dog will be fine.",
                },
            "2": { 
                "intro": "It's only apple juice. Do nothing.",
                "outro": "Your dog vibes our with you and your homies to one of the greatest movies of all time. Your dog is fine.",  
                },
            },
    },


    "spin": {  #        10
         "name": "spin",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "At the dog park, you are confided in by another dog owner named Linda that she can't get her dog to do a spin trick. Do you... ?",
        "options": {
            "1": {
                "intro": "Lament with her about her dog's shortcomings.", 
                "outro": "You made a new dog park friend! Linda appreciates your understanding.",
                },
            "2": { 
                "intro": "Brag, and show her your dog's perfect spin.",
                "outro": "Your dog does a beautiful spin. Linda looks at you enviously.",  
                },
            },
    },


    "socks": {  #        11
         "name": "socks",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "While getting ready in the morning, you notice that some of your socks appear to be missing. You can't find a single 'right' sock. Do you... ?",
        "options": {
            "1": {
                "intro": "Take time to go investigating for where they could be / where your dog could have put them.", 
                "outro": "You find a hidden stache of maimed socks under your bed after only a minute of looking. You bite the bullet and slip one on before work.",
                },
            "2": { 
                "intro": "Wear two 'left' socks to work today.",
                "outro": "Somehow, your work day goes on, even though you are wearing 2 'left' socks. ",  
                },
            },
    },


    "scratched_sofa": {  #        12
         "name": "scratched_sofa",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "After coming home from a longer than usual work day, you notice little claw marks on the sofa. Do you... ?",
        "options": {
            "1": {
                "intro": "Repremand your dog!", 
                "outro": "You scold your dog for the damage.",
                },
            "2": { 
                "intro": "Put a throw blanket over the damage. What's done is done.",
                "outro": "You cuddle up next to your dog as usual. He gives you a big kiss on the face.",  
                },
            },
    },


    "heel": {  #        13
         "name": "heel",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You notice your dog really tugging on the leash during walks. Do you... ?",
        "options": {
            "1": {
                "intro": "Teach my dog the word 'heel.'", 
                "outro": "You spend the week trying to make your dog understand the command 'heel.' It doesn't help much.",
                },
            "2": { 
                "intro": "Walk faster to match my dogs pace.",
                "outro": "You've basically become a runner. Perhaps you should sign up for a local race?",  
                },
            },
    },


    "marigolds": {  #        14
         "name": "marigolds",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You notice a hole that has been dug into your backyard by your dog at some point. Do you... ?",
        "options": {
            "1": {
                "intro": "Fill the damage with exess soil from the surrounding earth.", 
                "outro": "You spend 20 minutes fixing up the eveness of your backyard terrain. Good as new!",
                },
            "2": { 
                "intro": "Take this opportunity to plant some marigolds into the excavated area.",
                "outro": "The marigolds are beautiful. Just in time for Spring!",  
                },
            },
    },

    "car_window": {  #        15
         "name": "car_window",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "While driving to a friend's house, your dog is peeking out the window. You want to roll it down. Do you... ?",
        "options": {
            "1": {
                "intro": "Roll the window down 1 inch to let some air in.", 
                "outro": "You get some fresh air circulating in the car, and it smells lovely and fresh.",
                },
            "2": { 
                "intro": "Roll the window down enough so your dog can feel the breeze.",
                "outro": "Your dog's whole head sticks out the window! People on the street stop and exclaim 'awww!'",  
                },
            },
    },


    "trash": {  #        16
         "name": "trash",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You notice your dog sniffing the trash bin. Do you... ?",
        "options": {
            "1": {
                "intro": "Leave it be.", 
                "outro": "30 minutes later, your entire trash can contents are strewn about across the kitchen floor. YUCK!",
                },
            "2": { 
                "intro": "Take out the trash.",
                "outro": "You take out the trash, and your dogs interest about it's contents is put to rest. ",  
                },
            },
    },


    "let_out": {  #        17
         "name": "let_out",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You're watching your favorite show, when your dog begs to be let out (again.) You've already gotten up to let your dog out twice in the past hour, and you dog didn't use the restroom either time. Do you... ?",
        "options": {
            "1": {
                "intro": "Get up and let your dog out again.", 
                "outro": "You get up and let your dog out. What a good dog owner!",
                },
            "2": { 
                "intro": "Tell your dog 'give me 20 minutes to watch my show.'",
                "outro": "Your dog takes this opportunity to use the restroom inside. Yeesh.",  
                },
            },
    },

    "lasagna": {  #        18
         "name": "lasagna",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "After making a killer lasagna, your dogs mouth drools badly all over the floor. Do you... ?",
        "options": {
            "1": {
                "intro": "Give my dog a little bit of lasagna, the poor thing!", 
                "outro": "Your dog happily eats up some lasagna. Your furry friend now sits at your feet during every mealtime.",
                },
            "2": { 
                "intro": "Clean up the drool with a paper towl, but don't give your dog any human food. You know your dog is eating enough!",
                "outro": "You clean up the mess, and your dog doesn't beg for any food, instead just wanders off. ",  
                },
            },
    },

    "dirty_dog": {  #        19
         "name": "dirty_dog",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "After a long hike, your dog is covered in dirt. Do you... ?",
        "options": {
            "1": {
                "intro": "Hose my dog off with the garden hose. It's important to keep the house clean!", 
                "outro": "Your dog does NOT take kindly to being hosed off, but the warm towel afterwards definitely makes up for it!",
                },
            "2": { 
                "intro": "Try to brush off any excessive dirt from your dog's fir using your hands before going back inside.",
                "outro": "Quick and easy fix! You do end up having to vaccum in about a week.",  
                },
            },
    },

    "doorbell": {  #        20
         "name": "doorbell",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Every time your doorbell goes off, your dog starts going berzerk. (Making lots of noise, and jumping at the windows.) Do you... ?",
        "options": {
            "1": {
                "intro": "Try to calm your dog down whenever this happens. It hurts my ears!", 
                "outro": "You successfully manage to calm your dog a little bit, whenever this happens.",
                },
            "2": { 
                "intro": "Ignore it. That's what dogs do!",
                "outro": "Your dog continues to bark furiously any time the doorbell is rung, or there's evidence of any people outside. ",  
                },
            },
    },

    "wrong_word": {  #        21
         "name": "wrong_word",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You slip up, and use the word 'walk' when having a phone conversation with your mother. You weren't planning on walking right now, but your dog is super wound up by the word. ",
        "options": {
            "1": {
                "intro": "Bite the bullet and go for another walk. You can't let your dog down!", 
                "outro": "Your dog is extremely appreciative, and you both have a wonderful walk.",
                },
            "2": { 
                "intro": "Try to calm my dog down, and be careful to avoid this word in the future!",
                "outro": "It certainly doesn't work fully, but you manage to deescalate your dog's enthusiasm. ",  
                },
            },
    },


    "barber": {  #        22
         "name": "barber",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Your dog appears to have made a new ladyfriend at the dog park. The other dog's name is Mable. Wanting to help your dog out, do you... ? ",
        "options": {
            "1": {
                "intro": "Go to the dog park the same time the next week. Maybe Mable will be there again!", 
                "outro": "You indeed see Mable again. You take down her owner's number so that they can hang out more. Success!",
                },
            "2": { 
                "intro": "Bring my dog to the barber to get a fresh cut. Maybe it'll impress Mable.",
                "outro": "Absolutely awful haircut. All of your dog's mojo is gone. You avoid public places for a week.",  
                },
            },
    },

    "father": {  #        23
         "name": "father",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Your father comes to visit, and your dog is very hesistant to say hi! Do you... ?",
        "options": {
            "1": {
                "intro": "Coax your dog out of the corner, and try to introduce them in a gentle manner.", 
                "outro": "After 20 minutes of trying, your dog is a little less nervous.",
                },
            "2": { 
                "intro": "Let you dog hang out alone for a little bit. No big!",
                "outro": "You let your dog chillax, and spend some quality time with your Dad. Win win!",  
                },
            },
    },

    "collar": {  #        24
         "name": "collar",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You notice the collar is getting a little worn in. Maybe it's time for a new one! Do you purchase... ?",
        "options": {
            "1": {
                "intro": "A red one with a hand embroidered name on it & phone number. $25 dollars.", 
                "outro": "Your dog looks rad in the new style!",
                },
            "2": { 
                "intro": "A simple blue one with a little circular charm with all essential information on it. $20.",
                "outro": "Your dog looks rad in the new style!",  
                },
            },
    },

    "bonus_tricks": {  #        25
         "name": "bonus_tricks",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Any time you have a treat in hand, you notice your dog starts doing tricks at random, hoping to maybe score a bonus treat! Do you... ?",
        "options": {
            "1": {
                "intro": "Give a little treat for the entertainment. How cute!", 
                "outro": "Unfortunatly this becomes a pattern. Your dog is now a trick machine, but doesn't necessarily do them on queue!",
                },
            "2": { 
                "intro": "Don't reward the uncalled for tricks. ",
                "outro": "Your dog learns to do the tricks on command instead of at random. Big win!",  
                },
            },
    },

    "mouth_kiss": {  #        26
         "name": "mouth_kiss",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Your dog gives you a biiiiiig kiss on the face when you get home from work. Do you let him lick over your mouth? ",
        "options": {
            "1": {
                "intro": "Yes. You have a heart.", 
                "outro": "You let your dog kiss your face. You even give out some back scratches. How cute!",
                },
            "2": { 
                "intro": "Absolutely not.",
                "outro": "It's just not the way some people roll. You give your dog plenty of tummy rubs.",  
                },
            },
    },

    "tight collar": {  #        27
         "name": "tight collar",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "On walks, your dog is pulling so hard at the leash that it's nearly a choking hazard. Do you... ?",
        "options": {
            "1": {
                "intro": "Switch to a 30 dollar harness that will fit my dog.", 
                "outro": "You make the switch, and it works great!",
                },
            "2": { 
                "intro": "Your dog will stop if it hurts. Do nothing.",
                "outro": "You don't purchase the harness, and your dog continues to pull hard at the leash. Hopefully everything turns out fine... ",  
                },
            },
    },

    "dog_sitter": {  #        28
         "name": "dog_sitter",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "You have to be out of town for a night. Who do you pick as the dog sitter?",
        "options": {
            "1": {
                "intro": "Your 13 year old neighbor named Levi. He seems like a sweet kid, and you and his dad are already friends. You will pay Levi 30 bucks.", 
                "outro": "Levi is very happy to have made the money. Win win!",
                },
            "2": { 
                "intro": "Drop off your dog at your parent's home, that's an hour away. They'll do it for free!",
                "outro": "You get to see your parents AND a free dog sitter? Win win!",  
                },
            },
    },

    "play_date": {  #        29
         "name": "play_date",
        "resist": {
            "check": lambda dog: 0,  #add a clause for excersise when this is added to the dog object model
            "message": "n/a",
            },
        "intro": "Your dog hits it off with a dog named Cooper at the park, but Cooper's owner is a Cheif's fan. Do you... ?",
        "options": {
            "1": {
                "intro": "Set up a play date with Cooper's owner! Your dog could use some socializing.", 
                "outro": "You manage to get over the Cheif's thing. The two dogs really get along.",
                },
            "2": { 
                "intro": "Don't set up a play date. Can't trust a Cheif's fan.",
                "outro": "Resolute that you've made the right decision, you never see Cooper or his owner again. ",  
                },
            },
    }

}

