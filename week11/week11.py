class Dog:
    def __init__(self, _name, _size, _breed = "unkwown"):           # mandatory 먼저, optional은 뒤에. 이 경우, breed는 optional
        self.name = _name
        self.size = _size
        self.breed = _breed
    
    def get_name(self):
        return self.name
    def get_size(self):
        return self.size
    def get_breed(self):
        return self.breed
    
    def set_name(self, new_name):
        self.name = new_name
    def set_size(self, new_size):
        self.size = new_size

    def speak(self):
        if self.size == 1:
            print('yip')
        elif self.size == 2:
            print('bark')
        elif self.size == 3:
            print('bow wow')




class DogPark:
    def __init__(self, _name):
        self.name = _name
        self.dogs = []

    def add_dog(self, dog):
        self.dogs.append(dog)
    def show_dogs(self):
        for dog in self.dogs:
            print(dog.get_name())
    def change_dog_name(self, old_name, new_name):
        for dog in self.dogs:
            if dog.get_name() == old_name:
                dog.set_name(new_name)
    def find_dog(self, dog_name):
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                dog.speak()
    def call_dog(self, dog_name):
        '''this calls the dogs and removes it from the park'''
        for dog in self.dogs:
            if dog.get_name() == dog_name:
                self.dogs.remove(dog) 
        




park1 = DogPark('Bark Zone')

park1.add_dog(Dog('Spoot', 2, 'lab'))
park1.add_dog(Dog('Rover', 3, 'Mastiff'))
park1.add_dog(Dog('Fluffy', 1))
# dog1 = Dog('Spoot', 2, 'lab')
# park1.add_dog(dog1) 이런식으로 해도 됨
park1.change_dog_name("Spoot", "Spot")

park1.show_dogs()
park1.call_dog("Rover")
park1.show_dogs()
