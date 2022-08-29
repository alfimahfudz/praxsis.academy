class Dog:
    kind = 'canine' 
    def __init__(self, name):
        self.name = name
d = Dog('Fido')        
e = Dog('Buddy')
d.kind   
'canine'
e.kind 
'canine'
d.name    
'Fido'
e.name   
'Buddy'

class Dog:

    def __init__(self, name):
        self.name = name
        self.tricks = []
    def add_trick(self, trick):
        self.tricks.append(trick)

d = Dog('Fido')        
e = Dog('Buddy')   
d.add_trick('roll over')    
e.add_trick('play dead') 
d.tricks   
['roll over']
e.tricks
['play dead']

