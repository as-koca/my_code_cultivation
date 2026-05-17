class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name.capitalize()
        if (self.is_height_valid(height) is False):
            height = 0
        if (self.is_age_valid(age) is False):
            age = 0
        self._height: float = height
        self._d_age: int = age
        self._growth: float = 0

    def is_height_valid(self, height: float) -> bool:
        if (height < 0):
            print(f"{self._name}: Error, height can't be negative")
            return (False)
        return (True)

    def is_age_valid(self, age: int) -> bool:
        if (age < 0):
            print(f"{self._name}: Error, age can't be negative")
            return (False)
        return (True)

    def set_height(self, height: float) -> None:
        if (self.is_height_valid(height) is False):
            print("Height update rejected")
            return
        print(f"Height updated: {height}cm")
        self._height = height

    def set_age(self, age: int) -> None:
        if (self.is_age_valid(age) is False):
            print("Age update rejected")
            return
        print(f"Age updated: {age} days")
        self._d_age = age

    def get_height(self) -> float:
        # print(f"Height of plant: {self._height}cm")
        return (self._height)

    def get_age(self) -> int:
        # print(f"Age of plant: {self._d_age} days old")
        return (self._d_age)

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
    plant = Plant("rose", -342, -10000)
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
