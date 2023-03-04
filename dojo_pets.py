class Pet:
    def __init__(self, name, type, tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.noise = noise
        self.energy = 100
        self.health = 100
        
    def sleep(self):
        if self.energy == 200:
            print("You have maximum energy!")
        else:    
            self.energy += 25
            print(f"Your energy is:{self.energy}")
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"Your health is:{self.health}")
        print(f"Your energy is:{self.energy}")
        return self
    def play(self):
        self.health += 5
        print(f"Your health is:{self.health}")
        return self
    def make_noise(self):
        print(self.noise)
        return self

class Cat(Pet):
    def make_noise(self):
        print("Where's my food human")
        return 

class Ninja:
    def __init__(self,first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.make_noise()
        return self
  

zinnia = Cat("Zinnia", "Cat", "Roll Over", "Meow")
ross = Ninja("Ross", "Palmer", "Beefy Bits","Crunchy Bits", zinnia)

ross.feed().walk().bathe()



        