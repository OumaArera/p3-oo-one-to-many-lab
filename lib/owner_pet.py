class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []
    def __init__(self, name, pet_type, owner=None):
        if pet_type not in self.PET_TYPES:
            raise Exception(f"Invalid pet_type. Supported types are: {', '.join(self.PET_TYPES)}")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner 

        if owner:
            owner.pet_list.append(self)

        self.__class__.all.append(self)

class Owner:
    def __init__(self, name):
        self.name = name
        self.pet_list = []

    def pets(self):
        return self.pet_list
    
    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise TypeError("Only instances of Pet can be added to the owner's pets list.")
        pet.owner = self
        self.pet_list.append(pet)

        if self not in pet.all:
            pet.all.append(self)

    def get_sorted_pets(self):
        return sorted(self.pet_list, key=lambda pet: pet.name)
    

