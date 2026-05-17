class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        if (height < 0):
            height = 0
        if (age < 0):
            age = 0
        self._name: str = name.capitalize()
        self._height: float = height
        self._d_age: int = age
        self._growth: float = 0

    def set_height(self, height: float) -> None:
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            print("Height update rejected")
        else:
            print(f"Height updated: {height}cm")
            self._height = height

    def set_age(self, age: int) -> None:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            print("Age update rejected")
        else:
            print(f"Age updated: {age} days")
            self._d_age = age

    def get_height(self) -> None:
        print(f"Height of plant: {self._height}cm")

    def get_age(self) -> None:
        print(f"Age of plant: {self._d_age} days old")

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,", end=' ')
        print(f"{self._d_age} days old")

    def grow(self, days: int) -> None:
        if (self._d_age < 365):
            self._height += 0.8 * days
            self._growth += 0.8 * days
        else:
            self._height += 0.4 * days
            self._growth += 0.4 * days

    def age(self, days: int) -> None:
        self._d_age += days


def ft_garden_security() -> None:
    plant = Plant("rose", -34, -100000.233)
    print("=== Garden Security System ===")
    print("Plant created:", end=' ')
    plant.show()
    print("")
    plant.set_height(25)
    plant.set_age(30)
    print("")
    plant.set_height(-100)
    plant.set_age(-999)
    print("\nCurrent state:", end=' ')
    plant.show()
    print("")
    plant.get_height()
    plant.get_age()


if __name__ == "__main__":
    ft_garden_security()
