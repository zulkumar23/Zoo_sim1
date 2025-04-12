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
           print(f"{self.name} eat {food}. Hunger is now {self.hunger}.")
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
        self.animals = []

    def add_animal(self, animal):
        self.animals.append(animal)
        print(f"{animal.name} зоопарка кошулду.")

    def remove_animal(self, animal_name):
        for animal in self.animals:
            if animal.name == animal_name:
                self.animals.remove(animal)
                print(f"{animal_name} зоопарктан чыгарылды.")
                return
        print(f"{animal_name} табылган жок.")

    def list_animals(self):
        if not self.animals:
            print("Зоопарк бош.")
        else:
            for animal in self.animals:
                animal.info()

    def feed_animal(self, food):
        for animal in self.animals:
            animal.eat(food)

    def make_all_sounds(self):
        for animal in self.animals:
            animal.make_sound()


def zoo_menu():
    zoo = Zoo("Jungle Park")
    while True:
        print("\n--- ZOO MENU ---")
        print("1. Add Animal")
        print("2. Remove Animal")
        print("3. Show All Animals")
        print("4. Feed All Animals")
        print("5. Make All Animals Sound")

        choice = input("Choose (1-5): ")

        if choice == "1":
            print("a. Lion\nb. Eagle\nc. Snake")
            animal_type = input("Type (a/b/c): ")
            name = input("Animal name: ")
            age = int(input("Age: "))
            hunger = int(input("Hunger (0-5): "))

            if animal_type == "a":
                zoo.add_animal(Lion(name, age, hunger))
            elif animal_type == "b":
                zoo.add_animal(Eagle(name, age, hunger))
            elif animal_type == "c":
                zoo.add_animal(Snake(name, age, hunger))
            else:
                print("Type not recognized.")

        elif choice == "2":
            name = input("Animal name to remove: ")
            zoo.remove_animal(name)

        elif choice == "3":
            zoo.list_animals()

        elif choice == "4":
            food = input("Food name: ")
            zoo.feed_animal(food)

        elif choice == "5":
            zoo.make_all_sounds()



if __name__ == "__main__":
                zoo_menu()








