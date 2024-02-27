class Dog:
    def __init__(self, name = "Stitch", age = 0, health = 100, happiness = 100, max_age = 14 * 12, weight = 50, afflictions = {}):
        # Max health attribute to set a cap on the amount of health a dog can have so it does not live forever
        self.max_health = 100
        self.health = min(self.max_health, health)
        self.max_age = max_age #dog cannot live longer than max_age
        self.age = age #dog age in months
        self.weight = weight
        self.afflictions = afflictions
        self.medications = {}
        self.possessions = {}
        self.happiness = happiness
        self.name = name
        self.surrendered = False
        self.default_walk_options = {"short": {"time": 2, "health": 1, "happiness": 0}, "medium": {"time": 7, "health": 2, "happiness": 3}, "long": {"time": 15, "health": 3, "happiness": 5}}
        self.walk_options = self.default_walk_options
        self.walk_schedule = "short"
        self.meal_options = {"cheap": {"display": "Walmart's Finest", "cost": 65, "health": 1}, "vet_recommended": {"display": "Vet Recommended", "cost": 200, "health": 2}}
        self.meal_plan = self.meal_options["cheap"]
    def get_happiness(self) -> float:
        return self.happiness
    def get_health(self) -> float:
        return self.health
    def get_age(self) -> int:
        return self.age
    def get_afflictions(self) -> int:
        return self.afflictions
    def get_name(self) -> str:
        return self.name
    def get_weight(self) -> int:
        return self.weight
    def get_meal_plan(self) -> dict:
        return self.meal_plan
    def get_meal_cost(self) -> float:
        return self.meal_plan["cost"] * self.weight / 100
    def get_meal_options(self) -> dict:
        return self.meal_options
    def set_meal_plan(self, meal_plan: dict) -> None:
        self.meal_plan = self.get_meal_options()[meal_plan]
    def get_med_cost(self) -> float:
        cost = 0.0
        for key, value in self.medications.items():
            cost += value["cost"]
        return cost
    def get_expenses(self) -> float:
       return self.get_meal_cost() + self.get_med_cost()
    def get_medications(self) -> dict:
        return self.medications
    def get_possessions(self) -> dict:
        return self.possessions
    def get_attributes(self) -> list[dict]:
        return [{"max_health": self.max_health}, {"health": self.health}, {"age": self.age}, {"afflictions": self.afflictions}, {"medications": self.medications}, {"possessions": self.possessions}, {"happiness": self.happiness}, {"name": self.name}]
    def get_walk_schedule(self):
        return self.walk_options[self.walk_schedule]
    def get_walk_schedule_name(self):
        return self.walk_schedule
    def walk(self):
        self.update_health(self.get_walk_schedule()["health"])
        self.update_happiness(self.get_walk_schedule()["health"])
    def play(self):
        for key, value in self.get_possessions().items():
            print(key, value)
            if ("happiness" in value):
                self.update_happiness(value["happiness"])
            if ("health" in value):
                self.update_health(value["health"])
            value["duration"] -= 1
        self.possessions = {key: value for key, value in self.get_possessions().items() if value["duration"] > 0}
    def print_attributes(self) -> None:
        for attribute in self.get_attributes():
            print(attribute)
    def update_happiness(self, mod: int) -> None:
        self.happiness += mod
    def update_age(self, mod: int) -> None:
        self.age += mod
        middle_age = self.max_age // 2
        if (self.age > middle_age):
            self.set_max_health = min(self.max_health, middle_age / self.age * 100)
    def update_health(self, mod: int):
        self.health = min(self.health + mod, self.max_health)
    def update_max_health(self, mod: int):
        self.max_health = self.set_max_health(self.max_health + mod)
    def set_name(self, name: str):
        self.name = name
    def set_max_health(self, newMax: int):
        self.max_health = newMax
        self.health = min(self.health, self.max_health)
    def update_walk_schedule(self, schedule: str):
        self.walk_schedule = schedule
    def is_alive(self) -> bool:
        return self.health > 0
    def cure_affliction(self, affliction: str) -> None:
        self.afflictions.remove(affliction)
    def add_afflictions(self, afflictions: dict) -> None:
        self.afflictions = self.afflictions | afflictions
    def get_medications(self) -> dict:
        return self.medications
    def add_medication(self, med: dict) -> None:
        if (med in self.get_medications()):
            self.get_medications()[next(iter(med))] = med[next(iter(med))]
        else:
            self.get_medications()[next(iter(med))]["duration"] += med[next(iter(med))]["duration"]
    def add_possessions(self, new_possessions: dict):
        for key, value in new_possessions.items():
            if key in self.get_possessions():
               self.get_possessions()[key]["duration"] += 1
            else:
                self.get_possessions()[key] = value
    def activate_afflictions(self) -> None:
        for key, value in self.get_afflictions().items():
            if ("harm" in value):
                self.update_health(-value["harm"])
            if ("stress" in value):
                self.update_happiness(-value["stress"])
    def remove_medications(self, med: str) -> None:
        self.medications.remove(med)
    def walk_dog(self):
        if self.health != self.max_health:
            self.health += 1
        if self.happiness != self.max_health:
            self.happiness += 5
    def play_with_dog(self):
        if self.happiness != 100:
            self.happiness += 2
    def surrender(self) -> None:
        self.surrendered = True
    def is_surrendered(self) -> bool:
        return self.surrendered
        
        
class Human:
    def __init__(self):
        # This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
        self.income = 0.
        self.balance = 0.
        self.base_time = 0.
        self.free_time = 0.
        self.upkeep = 0
    def get_income(self) -> float:
        return self.income
    def get_balance(self) -> float:
        return self.balance
    def get_time(self) -> float:
        return self.free_time
    def get_revenue(self) -> float:
        return self.income * 0.05 - self.upkeep
    def get_attributes(self) -> list[dict]:
        return [{"income": self.income}, {"upkeep": self.upkeep}, {"balance": self.balance}, {"time": self.free_time}]
    def init_income(self, income: float) -> None:
        self.income = income
        self.balance = income * 0.05
    def init_time(self, time: float) -> None:
        self.base_time = time
        self.free_time = time
    def print_attributes(self) -> None:
        for attribute in self.get_attributes():
            print(attribute)
    def pay(self, amount: float) -> bool:
        if (self.balance < amount):
            return False
        self.balance -= amount
        return True
    def deposit(self, amount: float):
        self.balance += amount
    def work(self, hours: float) -> bool:
        if (self.free_time < hours):
            return False
        self.free_time -= hours
        return True
    def relax(self) -> None:
        self.free_time += self.base_time
