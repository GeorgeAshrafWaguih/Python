class Person:
    def __init__(self, firstname, lastname, health, status):
        """ initialize attributes to be used in/available for all class methods in this class\
        and for class objects created by this class """

        self.firstname = firstname
        self.lastname = lastname
        self.health = health
        self.status = status

    def introduce(self):
        """All people introduce themselves"""
        print(f'Hello, my name is {self.firstname} {self.lastname}')

    def emote(self):
        emotion = random.randrange(1,3)
        if emotion == 1:
            print(f'{self.firstname} is happy today')
        elif emotion == 2:
            print(f'{self.firstname} is sad right now')

    def status_change(self):
        if self.health == 100:
            print(f'{self.firstname} is totally healthy')
        elif self.health >= 76:
            print(f'{self.firstname} is a little tired today')
        elif self.health >= 51:
            print(f'{self.firstname} feels unwell')
        elif self.health >= 40:
            print(f'{self.firstname} goes to the doctor')
        else:
            print(f'{self.firstname} is unconscious')


Maria = Person("Maria", "Gutierrez", 95, status=True)
Rey = Person("Rey", "Jones", 88, status=False)
Lee = Person("Lee", "Williams", 72, status=True)

print(f'{Maria.firstname} is my friend? {Maria.status}')
print(f'{Rey.firstname} is my friend? {Rey.status}')

Maria.introduce()
Rey.introduce()
Lee.introduce()

Maria.status_change()
Rey.status_change()
Lee.status_change()

