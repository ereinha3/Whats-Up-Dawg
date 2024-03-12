import random
from data.breeds_dict import breeds
from data.shop import meal_options, walk_options

config = {
        "months_per_round": 6
        }

class Dog():
    def __init__(self, 
                 name = "Stitch", 
                 age = 9, 
                 health = 80, 
                 happiness = 50, 
                 max_age = 14,
                 weight = 50,
                 breed = "yorkshire terrier",
                 training = 10
                 ):
        self.breed = breed 
        self.happiness = happiness
        self.training = training
        #self._trainability = breeds[breed]["trainability_value"] * 10
        self.max_age = breeds[breed]["max_expectancy"] #dog will not survive long past max age
        self._age = age #dog age in years
        self._health = health
        self.max_health = health
        self.weight = (breeds[breed]["min_weight"] + breeds[breed]["max_weight"]) // 2
        self.happiness = happiness
        self.name = name
        self.walk_schedule = "short"
        self.meal_plan = "normal"
        self.afflictions = {}
        self.medications = {}
        self.items = {}
        self.tags = set()
        self.alive = True
        self.surrendered = False
 
    @property
    def walk_time(self):
        return walk_options[self.walk_schedule]["time"] * 30 * config["months_per_round"]

    @property
    def meal_expense(self):
        cups_per_day = 0.045 * self.weight + 0.81
        daily_cost = cups_per_day * (meal_options[self.meal_plan]["cost"] / 4)
        return round(daily_cost * 30 * config["months_per_round"], 2)

    def __str__(self):
        return f"{self.name} is a {self.breed} with {self._health} health and is {self.age} years old.\
                \nMedication are {[item for item in self.medications.keys()]} with respective durations of {[val for val in self.medications.values()]}.\
                \nItems are {[item for item in self.items.keys()]} with respective durations of {[val for val in self.items.values()]}.\
                \n{self.name} currently suffers from {[key for key in self.afflictions]} with respective durations of {[val for val in self.afflictions.values()]}"

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        
        if self.age > self.max_age:
            self.alive = False
        middle_age = self.max_age / 2
        age_difference = value - self._age

        health_loss = random.randint(4, 10) * age_difference if self._age > middle_age else 0
        
        self.max_health -= health_loss
        self.happiness -= health_loss #Happiness also drops as dog nears the end of their life

        #Health drops more quickly and earlier than max health
        #Health needs to be maintained with good diet and exercise, it is not a given
        self.health -= (health_loss + random.randint(6, 12) * age_difference)

    @property
    def health(self):
        return round(min(self._health, self.max_health), 2)

    @health.setter
    def health(self, value):
        self._health = min(value, self.max_health)
        if (self._health < 1):
            self.alive = False

class Human:
    def __init__(self, monthly_income, dog:Dog, name="John"):
        # This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
        self.monthly_income = float(monthly_income)
        self.income = float(monthly_income)
        self._balance = self.revenue
        self.time_spent = 0
        self.name = name
        self.dog = dog
        self._round_expenses = 0 #Tracks expenses for a round, controller refreshes on a new round
        self._total_expenses = 0
        self.log = str()
        
    def __str__(self):
        return f"{self.name} currently has a balance of ${self._balance} and has spent {self.time_spent} hours on {self.dog.name}."

    @property
    def round_expenses(self):
        return round(self._round_expenses, 2)

    @round_expenses.setter
    def round_expenses(self, value):
        self._round_expenses = value

    @property
    def total_expenses(self):
        return round(self._total_expenses, 2)

    @total_expenses.setter
    def total_expenses(self, value):
        self._total_expenses = value

    @property
    def revenue(self):
        return round(self.income * 0.05 * config["months_per_round"], 2)

    @property
    def balance(self):
        return round(self._balance, 2)

    @balance.setter
    def balance(self, value):
        loss = max((self._balance - value), 0)
        self.round_expenses += loss
        self.total_expenses += loss

        self._balance = value
        if (self._balance < -(self.revenue / 6 * 4)):
            self.dog.surrendered = True

def update_model(dog, human):
    dog.name = dog.name + "_updated"
    human.income = 5

if __name__ == "__main__":
    Kesey = Dog("Kesey")
    Morgan = Human(2000, Kesey)
    update_model(Kesey, Morgan)
    print(Kesey.name)
    Kesey.health -= 20
    Kesey.max_health -= 20
    print(Kesey.health)
    print(Kesey.max_health)
    print(Morgan.income)
