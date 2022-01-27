class Doggy:
    num_of_dogs = 0
    birth_of_dogs = 0
    
    def __init__(self, name, variety):
        self.name = name
        self.variety = variety        
        Doggy.birth_of_dogs += 1
        Doggy.num_of_dogs += 1
    
    def bark(self):
        print('왈왈!')
        
    def get_status():
        print(f'Birth : {Doggy.birth_of_dogs}, Current : {Doggy.num_of_dogs}')
    
    def __del__(self):
        Doggy.num_of_dogs -= 1    
        
        
d3 = Doggy('별이', '시츄')
print(Doggy.num_of_dogs)
d2 = Doggy('꽁이', '말티즈')
print(Doggy.num_of_dogs)
d1 = Doggy('초코', '푸들')
print(Doggy.num_of_dogs)
Doggy.get_status()