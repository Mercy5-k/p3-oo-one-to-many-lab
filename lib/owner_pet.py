class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        """Return all pets belonging to this owner"""
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        """Assign this owner to the given pet"""
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet")
        pet.owner = self  # single source of truth

    def get_sorted_pets(self):
        """Return pets sorted alphabetically by name"""
        return sorted(self.pets(), key=lambda pet: pet.name)
        pass

class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []   # <-- must be indented inside the class, not at top of file!

    def __init__(self, name, pet_type, owner=None):
        self.name = name

        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"{pet_type} is not a valid pet type")
        self.pet_type = pet_type

        if owner is not None and not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner or None")
        self.owner = owner

        Pet.all.append(self) 
        pass