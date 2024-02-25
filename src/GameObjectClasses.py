class Dog:
    def __init__(self, age : int = 0, health : int = 100, happiness : int = 100, illness : list = [], fertility : bool = 1):
        # Max health attribute to set a cap on the amount of health a dog can have so it does not live forever
        self.max_health = 100
        self.age = age
        self.illness = illness
        self.health = health
        self.happiness = happiness
        self.fertility = fertility
    def get_happiness(self):
        return self.happiness
    def get_health(self):
        return self.health
    def get_age(self):
        return self.age
    def get_illness(self):
        return self.illness
    def update_illnesses(self):
        # Illness class needs to be created but decrement round counter and call this funtion at the end of a round
        pass
    def walk_dog(self):
        if self.health != self.max_health:
            self.health += 1
        if self.happiness != self.max_health:
            self.happiness += 5
    def play_with_dog(self):
        if self.happiness != 100:
            self.happiness += 2
    def take_to_vet(self):
        if self.health != self.max_health:
            self.health += 5
    def reduce_max_health(self):
        # This will be called every round to ensure dog will live forever
        # Essentially reducing health by ratio of previous health to max previous health
        self.health = (self.get_health()/self.max_health) * 0.9
        self.max_health -= 10
        
        
class Human:
    def __init__(self, income, free_time = 5, happiness = 100):
        # This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
        self.dispoable_income = income * 0.05
        self.happiness = happiness
        self.free_time = free_time
        self.vet = 0
    def get_happiness(self):
        return self.happiness
    def get_income(self):
        return self.income
    def get_free_time(self):
        return self.free_time
    def get_vet(self, quality):
        # Quality : 1, 2, 3 depending on how good of a vet you want.
        self.vet = quality
    def change_vet(self, interval):
        if self.vet:
            new_vet = self.vet + interval
            if 0<new_vet<=2:
                self.vet = new_vet
            else :
                print("Vet cannot be changed! Cannot upgrade from max or downgrade from min.")
        else:
            print("Vet must be first chosen (used get_vet())")
    def bill_vet(self):
        self.bill += 250 + self.vet*100
    def neuter_dog(self):
        if self.fertility == 0:
            print("Dog has already been neutered or was purchased from a breeder.")
        else:
            self.fertility == 0
            self.bill += 250
    
        

