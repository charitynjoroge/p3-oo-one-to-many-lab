class Pet:
    all = []

    def __init__(self, name = '', pet_type = '', owner = ''):
        self.name = name
        if pet_type not in self.PET_TYPES:
            raise ValueError("Invalid pet type")
        self.pet_type = pet_type
        self.owner = owner
        self.all.append(self)
        if owner:
            owner.add_pet(self)

    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']

class Owner:
    def __init__(self, name='John'):
        self.name = name
        self._pets = []

    def add_pet(self, pet):
        self._pets.append(pet)
        pet.owner = self

    def pets(self):
        return self._pets
    
    def get_sorted_pets(self):
        return sorted(self._pets, key=lambda pet: pet.name)

