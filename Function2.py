class pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.hunger = 7
        self.happiness = 5
        print(f"Welcome, {self.name} the {self.species} to the family")

    def feed(self):
        if self.hunger > 0:
            self.hunger -= 2  # Decrease hunger by 2
            if self.hunger < 0:
                self.hunger = 0  # don't go below 0

            self.happiness += 1  # increase happiness by 1

            if self.happiness > 10:
                self.happiness = 10  # don't go above 10
            print(
                f"{self.name} is fed. Hunger: {self.hunger}, Happiness: {self.happiness}"
            )
        else:
            print(
                f"{self.name} is not hungry. Hunger: {self.hunger}, Happiness: {self.happiness}"
            )

    def play(self):
        """ "
        this is a method to play with the pet
        """
        if self.happiness < 10:
            self.happiness += 2

            # Nested if 1
            if self.happiness > 10:
                self.happiness = 10

            self.hunger += 1

            # Nested if 2
            if self.hunger > 10:
                self.hunger = 10
            print(
                f"{self.name} is playing. Hunger: {self.hunger}, Happiness: {self.happiness}"
            )
        else:
            print(
                f"{self.name} is too happy. Hunger: {self.hunger}, Happiness: {self.happiness}"
            )


# This is to play with the pet
print("Play with the pet")
mallow = pet("Mallow", "cat")
mallow.feed()
mallow.play()
