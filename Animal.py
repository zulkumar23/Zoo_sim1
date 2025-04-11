class Animal:
    def __init__(self, name, species, age, hunger):
        self.name = name
        self.species = species
        self.age = age
        self.hunger = hunger

    def make_sound(self):
        pass

    def eat(self, food):
       if self.hunger > 0:
           self.hunger -= 1
           print(f"{self.name} ate {food}. Hunger is now {self.hunger}.")
       else:
           print(f"{self.name} is not hungry.")

    def info(self):
        print(f"Name: {self.name}, Species: {self.species}, Age: {self.age}, Hunger: {self.hunger}")



class Mammal(Animal):
    def __init__(self, name, age, hunger):
        super().__init__(name, "Mammal", age, hunger)

class Bird(Animal):
    def __init__(self, name, age, hunger):
        super().__init__(name, "Bird", age, hunger)

class Reptile(Animal):
    def __init__(self, name, age, hunger):
        super().__init__(name, "Reptile", age, hunger)



class Lion(Mammal):
    def make_sound(self):
        print("Ryk")

    def hunt(self):
        print(f"{self.name} is hunting...")

class Eagle(Bird):
    def make_sound(self):
        print("Krik")
    def fly(self):
        print(f"{self.name} is flying high...")

class Snake(Reptile):
    def make_sound(self):
        print("Ship")


class Zoo:
    def __init__(self, name):
        self.name = name
        self.animals =["Lion", "Eagle", "Snake"]

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} жаңы жаныбар {self.name} кошулду.")

    def remove_animal(self, animal_name):
        animal_to_remove = None
        for animal in self.animals:
              self.animals.remove(animal_to_remove)
              print(f"{animal_name} жаныбар {self.name} зоопарктан чыгарылды.")
        else:
            print(f"{animal_name} зоопарктан табылган жок.")

    def list_animals(self):
        if not self.animals:
            print("The zoo is empty.")
        else:
            print(f"\nЗоопарктагы жаныбарлардын {self.name}:")
            for animal in self.animals:
                animal.info()

    def feed_animal(self, food):
        if not self.animals:
            print("Зоопаркта тамактандырганга эч кандай жаныбар жок.")
        else:
            print("\nЖалпы жаныбарларды тамактандыруу:")
            for animal in self.animals:
                animal.eat(food)

        if __name__ == "__man__":
            safari_zoo = Zoo("Safari")

            simba = Lion("Simba", 5,3)
            aquila = Eagle("Aquila", 3,2)
            nagini = Snake("Nagini", 4, 1)

            safari_zoo.add_animal(simba)
            safari_zoo.add_animal(aquila)
            safari_zoo.add_animal(nagini)

            safari_zoo.list_animals_info()

            safari_zoo.feed_all("meat")

            safari_zoo.remove_animal("Aquila")

            safari_zoo.list_animals_info()



