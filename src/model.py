from data.breeds_dict import breeds
class Dog:
    def __init__(self, 
                 name = "Stitch", 
                 age = 0, 
                 health = 100, 
                 happiness = 100, 
                 max_age = 14 * 12, 
                 weight = 50,
                 breed = "yorkshire terrier",
                 trained = 10
                 ):
        self.breed = breed 
        self.happiness = happiness
        self.trained = trained
        self.trainability = breeds[breed]["trainability_value"] * 10
        # Max health attribute to set a cap on the amount of health a dog can have so it does not live forever
        self.max_age = breeds[breed]["max_expectancy"] #dog cannot live longer than max_age
        self.age = age #dog age in months
        self.max_health = health
        self._health = health
        self.weight = (breeds[breed]["min_weight"] + breeds[breed]["max_weight"]) // 2
        # self.happiness = happiness
        self.name = name
        self.walk_schedule = "short"
        self.meal_plan = "normal"
        self.afflictions = set()
        self.medications = set()
        self.items = set()
        self.alive = True
        self.surrendered = False
        self.calculate_food_per_day = lambda w=self.weight: 0.045*w + 0.81
        
    def __str__(self):
        return f"{self.name} is a {self.breed} with {self._health} health and is {self.age} years old.\nMedication are {[item for item in self.medications]}.\nItems are {[item for item in self.items]}"

    """@property
    def max_health(self):
        middle_age = self.max_age / 2
        return 100 if self.age < middle_age else middle_age / self.age * 100"""

    @property
    def health(self):
        return min(self._health, self.max_health)

    @health.setter
    def health(self, value):
        self._health = min(value, self.max_health)
        if (self._health <= 0):
            self.alive = False

class Human:
    def __init__(self, income, dog:Dog, name="John"):
        # This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
        self.income = int(income)
        self._balance = int(income)
        self.time_spent = 0
        self.name = name
        self.dog = dog
        
    def __str__(self):
        return f"{self.name} currently has a balance of ${self._balance} and has spent {self.time_spent} hours on {self.dog.name}"

    @property
    def upkeep(self):
        meal_cost = 65 #not yet implemented, something like: data.meals[self.dog.meal_plan]["cost"]
        affliction_cost = 0. #not yet implemented
        return meal_cost + affliction_cost


    @property
    def revenue(self):
        return self.income * 0.05

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        self._balance = value
        if (self._balance < -(self.revenue() * 4)):
            self.dog.surrender = True
