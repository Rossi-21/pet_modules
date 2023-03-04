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