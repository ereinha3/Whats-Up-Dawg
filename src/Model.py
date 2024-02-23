class Dog:
	def __init__(self, name = "Stitch", age = 0, health = 100, happiness = 100, illness = {}):
		# Max health attribute to set a cap on the amount of health a dog can have so it does not live forever
		self.max_health = 100
		self.health = min(self.max_health, health)
		self.age = age
		self.illness = illness
		self.meds = {}
		self.happiness = happiness
		self.name = name
	def get_happiness(self) -> int:
		return self.happiness
	def get_health(self) -> int:
		return self.health
	def get_age(self) -> int:
		return self.age
	def get_illness(self) -> int:
		return self.illness
	def get_name(self) -> str:
		return self.name
	def list_attributes(self) -> list[dict]:
		return [{"max_health": self.max_health}, {"health": self.health}, {"age": self.age}, {"illnesses": self.illness}, {"meds": self.meds}, {"happiness": self.happiness}, {"name": self.name}]
	def print_attributes(self) -> None:
		for attribute in self.list_attributes():
			print(attribute)
	def update_happiness(self, mod: int) -> None:
		self.happiness += mod
	def update_age(self, mod: int) -> None:
		self.age += mod
	def update_health(self, mod: int):
		self.health = min(self.health + mod, self.max_health)
	def update_max_health(self, mod: int):
		self.max_health += mod
		self.health = min(self.health, self.max_health)
	def is_alive(self) -> bool:
		return self.health > 0
	def cure_illness(self, affliction: str) -> None:
		self.illness.remove(affliction)
	def add_illness(self, affliction: str) -> None:
		self.illness.add(affliction)
	def add_meds(self, med: str) -> None:
		self.meds.add(med)
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
	def reduce_max_health(self):
		# This will be called every round to ensure dog will live forever
		# Essentially reducing health by ratio of previous health to max previous health
		self.health = (self.get_health()/self.max_health) * 0.9
		self.max_health -= 10
		
		
class Human:
	def __init__(self, income, time = 5):
		# This explicitly needs to be declared as disposable income to the user as they need income for a variety of essentials
		self.income = income * 0.05
		self.balance = income
		self.time = time
	def get_income(self) -> float:
		return self.income
	def get_balance(self) -> float:
		return self.balance
	def get_time(self) -> float:
		return self.time
	def list_attributes(self) -> list[dict]:
		return [{"income": self.income}, {"balance": self.balance}, {"time": self.time}]
	def print_attributes(self) -> None:
		for attribute in self.list_attributes():
			print(attribute)
	def pay(self, amount: float) -> bool:
		if (self.balance < amount):
			return False
		self.balance -= amount
		return True
	def work(self, hours: float) -> bool:
		if (self.time < hours):
			return False
		self.time -= hours
		return True
	def revenue(self) -> None:
		self.balance += self.income * 0.05
