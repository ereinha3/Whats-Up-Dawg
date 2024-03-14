import random
from data.breeds_dict import breeds
from data.shop import meal_options, walk_options
from data.config import config

class Dog():
    '''
    A class to represent a dog, the main object of the game is to care for this dog.

    Attributes
    ----------

    name : str
        Name of the dog

    age  : float
        Dog's age in years

    max_age : float
        Varies by breed. If the dog's age ever exceeds its max age the dog dies.

    health : float
        A value representing the dogs current physical wellness. If health is reduced to 0 the dog is killed.

    max_health : float
        A cap on health available to the dog. The max_health decreases as the dog ages.

    happiness : float
        A value representing the dogs joy and mental health. A happy dog is likely to act out and of course, keeping your dog happy is one of the implicit goals of the game.

    weight : float
        The dogs weight varies by breed and impacts meal expenses and some medical expenses.

    breed  : str
        Compared against a public database of information on dog breeds to inform dog weight, max_age, etc.

    training : float
        A well trained dog, similar to happiness is less likely to act out in certain ways.

    walk_schedule : str
        Compared against a walk_schedule dictionary to grab walk_schedule values. These values include health and happiness benefits for the dog, and time required by the human.

    meal_plan : str
        Compared against a meal_plan dictionary to grab meal_plan values. These values include health and happiness benefits for the dog, and cost required by the human to sustain.

    afflictions : dict
        A dictionary of afflictions the dog is currently experiencing. These afflictions are copied over from an afflictions_library, and the copy is updated within the dog model to represent a changes in the afflictions duration (and possible treatment).

    items : dict
        A dictionary of items owned by the dog. These items are mostly toys which increase dog happiness, although some common dog toys (such as bones) are actually unhealthy for dogs and may decrease health.

    medications : dict
        A dictionary of medications given to the dog. These medications are used to resist certain events (such as fleas, ticks or heartworm).

    tags : set[str]
        A set of events the user has experienced this playthrough. Used to filter events so you don't continuously get the same whacky events. Affliction based events (such as fleas) can occur many times and are not included in tags.

    alive : bool
        A bool representing whether or not the dog is currently alive.

    surrendered : bool
        A bool representing whether or not the dog has been surrendered.

    walk_time : int
        Time during a round spent walking a dog.

    meal_expense : float
        Cost of the dogs meals for the round.
    '''


    def __init__(self, 
                 name = "Stitch", 
                 age = 0, 
                 health = 75, 
                 happiness = 75, 
                 max_age = 14,
                 weight = 50,
                 breed = "yorkshire terrier",
                 training = 10
                 ):
        '''Creates a new Dog object.'''

        self.breed = breed 
        self.happiness = happiness
        self.training = training
        #self._trainability = breeds[breed]["trainability_value"] * 10
        self.max_age = breeds[breed]["max_expectancy"]
        self._age = age #dog age in years
        self._health = health
        self.max_health = 100
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
        '''Returns the time spent walking this dog in the past round, given the current walk_schedule.'''
        return walk_options[self.walk_schedule]["time"] * 30 * config["months_per_round"]

    @property
    def meal_expense(self):
        '''Returns the expenses required to pay for the dogs meals in the given round. The formula is derived from a linear regression on dog food required by weight, and multiplied by the amount of cups consumed in a day. Because the meal_plan costs are listed in pounds, and there are 4 cups of dry kibble in a pound, the daily_cost divides the meal_plan cost by 4.'''
        cups_per_day = 0.045 * self.weight + 0.81
        daily_cost = cups_per_day * (meal_options[self.meal_plan]["cost"] / 4) #Divide by 4 to convert from cost/pound to cost/cup (approx 4 ounces per cup).
        return round(daily_cost * 30 * config["months_per_round"], 2)

    def __str__(self):
        return f"{self.name} is a {self.breed} with {self._health} health and is {self.age} years old.\
                \nMedication are {[item for item in self.medications.keys()]} with respective durations of {[val for val in self.medications.values()]}.\
                \nItems are {[item for item in self.items.keys()]} with respective durations of {[val for val in self.items.values()]}.\
                \n{self.name} currently suffers from {[key for key in self.afflictions]} with respective durations of {[val for val in self.afflictions.values()]}"

    @property
    def age(self):
        '''Returns the dogs current age.'''
        return self._age

    @age.setter
    def age(self, value):
        '''Setter for the dogs age property. As the dog ages their max_health and happiness may be decreased.'''
        
        if self.age > self.max_age:
            self.alive = False
        middle_age = self.max_age / 2
        age_difference = value - self._age
        self._age = value

        health_loss = random.randint(6, 12) * age_difference if self._age > middle_age else 0
        
        self.max_health -= health_loss
        self.happiness -= health_loss #Happiness also drops as dog nears the end of their life

        #Health drops more quickly and earlier than max health
        #Health needs to be maintained with good diet and exercise, it is not a given
        #The dog will become unhealthy if not properly cared for
        self.health -= (health_loss + random.randint(1, 12) * age_difference)

    @property
    def health(self):
        '''Returns the dogs current health.'''
        return round(min(self._health, self.max_health), 2)

    @health.setter
    def health(self, value):
        '''Setter for dog health. If reduced below 1 the dog dies.'''
        self._health = min(value, self.max_health)
        if (self._health < 1):
            self.alive = False

class Human():
    '''
    A class to represent a Human, a stand in object for the player themselves.

    Attributes
    ----------
    monthly_income : float
        Total monthly income set by the player

    balance : float
        Funds the human has set aside to pay for their dog's expenses. If balance runs too low the human is forced to surrender their dog.

    revenue : float
        Money the human receives after every round to add to their balance, smaller than income because only a small portion of a persons income is available to pay for pet expenses (5%).

    time_spent : int
        A number of hours spent by the human player in caring for their dog, tracked only for educational and viewing purposes.

    name : str
        Name assigned by the player to their human

    dog : Dog
        A Dog object, the human is the parent of the dog both philosophically and literally, they need to access dog attributes in order to pay for the dogs expenses, etc.

    round_expenses : float
        Expenses accumulated throughout each round and used to inform the user of their expenses for the round. Reset at the beginning of each round.

    total_expenses : float
        Expenses accumulated throughout the entire game. Summarized for the user at the end.

    log : str
        A string concatenated by any event or update that gets displayed to the user. Reset at the end of every round.

    '''

    def __init__(self, monthly_income, dog:Dog, name="John"):
        self.monthly_income = float(monthly_income)
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
        '''Returns a nicely rounded set of expenses for the user during a given round.'''
        return round(self._round_expenses, 2)

    @round_expenses.setter
    def round_expenses(self, value):
        '''Setter for updating a users expenses over a given round.'''
        self._round_expenses = value

    @property
    def total_expenses(self):
        '''Returns a nicely rounded set of expenses for the user accumulated throughout the game.'''
        return round(self._total_expenses, 2)

    @total_expenses.setter
    def total_expenses(self, value):
        '''Setter for updating a users expenses accumulated throughout the game.'''
        self._total_expenses = value

    @property
    def revenue(self):
        '''Returns a nicely rounded revenue generated by the user during the last round. This revenue is explicitly reduced to represent disposable income for pet care, not the humans total income.'''
        return round(self.monthly_income * 0.05 * config["months_per_round"], 2)

    @property
    def balance(self):
        '''Returns the humans current available balance for spending on the pet care.'''
        return round(self._balance, 2)

    @balance.setter
    def balance(self, value):
        '''Setter for updating the humans available balance for pet care. If the balance is reduced too low they are forced to surrender their dog for lack of funds.'''
        loss = max((self._balance - value), 0)
        self.round_expenses += loss
        self.total_expenses += loss

        self._balance = value
        if (self._balance < -(self.revenue / 6 * 4)):
            self.dog.surrendered = True
