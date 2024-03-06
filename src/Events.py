from utils import percentCheck
from random import randint
from event_library import event_lookup_table
from model import Dog, Human
import sys

def load_event():
    return event_lookup_table[list(event_lookup_table)[randint(0, len(event_lookup_table) - 1)]]

def determine_event_outcome(options: dict, human: Human):
    for key, value in options.items():
        print(key + ".", value["intro"])
    choice = sys.stdin.readline().strip()
    if (choice not in options.keys()):
        print("Please enter a valid option number.\n")
        return determine_event_outcome(options, human)
    
    selection = options[choice]
    if ("cost" in selection and selection["cost"] > human.get_balance()):
        print("It is good of you to try but you cannot afford the expense. You'll have to pick another option.")
        return determine_event_outcome({key: value for key, value in options.items() if key != selection}, human)
    if ("work" in selection and selection["work"] > human.get_time()):
        print("Unfortunately you do not have enough time. You'll have to pick another option.")
        return determine_event_outcome({key: value for key, value in options.items() if key != selection}, human)

    return selection

def play_event(dog: Dog, human: Human, event: dict) -> None:
    print(event["intro"] + "\n")
    if (event["resist"]["check"](dog)):
        print(event["resist"]["message"])
        return
    
    outcome = determine_event_outcome(event["options"], human)
    
    if "cost" in outcome:
        human.pay(outcome["cost"])
    if "work" in outcome:
        human.work(outcome["work"])
    if "harm" in outcome:
        dog.update_health(-outcome["harm"])
    if "stress" in outcome:
        dog.update_happiness(-outcome["stress"])
    if "afflictions" in outcome:
        dog.add_afflictions(outcome["afflictions"])
    
    print(outcome["outro"])
