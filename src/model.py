from data.breeds_dict import breeds
class Dog:
    def __init__(self, 
                 name = "Stitch", 
                 age = 0, 
                 health = 100, 
                 happiness = 100, 
                 max_age = 14 * 12, 
                 weight = 50,
                 breed = "yorkshire terrier"
                 ):
        self.breed = breed 
        # Max health attribute to set a cap on the amount of health a dog can have so it does not live forever
        # Setting max age * 6 to convert to months
        self.max_age = breeds[breed]["max_expectancy"] * 6 #dog cannot live longer than max_age
        self.age = age #dog age in months
        self._health = health
        self.weight = (breeds[breed]["min_weight"] + breeds[breed]["max_weight"]) // 2
        # self.happiness = happiness
        self.name = name
        self.walk_schedule = "Short"
        self.meal_plan = "Normal"
        self.afflictions = set()
        self.medications = set()
        self.items = set()
        self.alive = True
        

    @property
    def max_health(self):
        middle_age = self.max_age / 2
        return 100 if self.age < middle_age else middle_age / self.age * 100

    @property
    def health(self):
        return min(self._health, self.max_health)

    @health.setter
    def health(self, value):
        self._health = min(value, self.max_health)

class Human:
    def __init__(self, income, dog:Dog):
        # This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
        self.income = income
        self._balance = income
        self.time_spent = 0.
        self.dog = dog

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
