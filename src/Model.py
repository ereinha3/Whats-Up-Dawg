class Dog:
    def __init__(self, name = "Stitch", age = 0, health = 100, happiness = 100, max_age = 14 * 12, weight = 50, afflictions = {}):
        # Max health attribute to set a cap on the amount of health a dog can have so it does not live forever
        self.max_health = 100
        self.health = min(self.max_health, health)
        self.max_age = max_age #dog cannot live longer than max_age
        self.age = age #dog age in months
        self.afflictions = afflictions
        self.weight = weight
        self.meds = {}
        self.possessions = {}
        self.happiness = happiness
        self.name = name
        self.surrendered = False
        self.default_walk_options = {"short": {"time": 2, "restore": 25, "satisfy": 5}, "medium": {"time": 7, "restore": 50, "satisfy": 35}, "long": {"time": 15, "restore": 75, "satisfy": 90}}
        self.walk_options = self.default_walk_options
        self.walk_schedule = self.walk_options["short"]
        self.meal_options = {"cheap": {"base_cost": 65, "restore": 25}, "vet_recommended": {"base_cost": 150, "restore": 50}}
        self.meal_plan = self.meal_options["cheap"]
    def get_happiness(self) -> int:
        return self.happiness
    def get_health(self) -> int:
        return self.health
    def get_age(self) -> int:
        return self.age
    def get_afflictions(self) -> int:
        return self.afflictions
    def get_name(self) -> str:
        return self.name
    def get_weight(self) -> int:
        return self.weight
    def get_expenses(self) -> float:
       #need to implement actual expenses
       return 100.0
    def get_meds(self) -> dict:
        return self.meds
    def get_attributes(self) -> list[dict]:
        return [{"max_health": self.max_health}, {"health": self.health}, {"age": self.age}, {"afflictions": self.afflictions}, {"meds": self.meds}, {"happiness": self.happiness}, {"name": self.name}]
    def get_walk_schedule(self):
        return self.walk_schedule
    def print_attributes(self) -> None:
        for attribute in self.get_attributes():
            print(attribute)
    def update_happiness(self, mod: int) -> None:
        self.happiness += mod
    def update_age(self, mod: int) -> None:
        self.age += mod
        middle_age = self.max_age / 2
        if (self.age > middle_age):
            self.set_max_health = min(self.max_health, middle_age / self.age * 100)
    def update_health(self, mod: int):
        self.health = min(self.health + mod, self.max_health)
    def update_max_health(self, mod: int):
        self.max_health = self.set_max_health(self.max_health + mod)
    def set_max_health(self, newMax: int):
        self.max_health = newMax
        self.health = min(self.health, self.max_health)
    def is_alive(self) -> bool:
        return self.health > 0
    def cure_affliction(self, affliction: str) -> None:
        self.afflictions.remove(affliction)
    def add_afflictions(self, afflictions: dict) -> None:
        self.afflictions = self.afflictions | afflictions
    def add_meds(self, med: str) -> None:
        self.meds.add(med)
    def activate_afflictions(self) -> None:
        for key, value in self.get_afflictions().items():
            if ("harm" in value):
                self.update_health(-value["harm"])
            if ("stress" in value):
                self.update_happiness(-value["stress"])
    def remove_meds(self, med: str) -> None:
        self.meds.remove(med)
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
    def __init__(self, income, time = 10):
        # This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
        self.income = income
        self.balance = income * 0.05 * 3
        self.base_time = time
        self.free_time = time
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
