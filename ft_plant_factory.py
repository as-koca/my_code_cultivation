class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self.height: float = height
        self.d_age: int = age
        self.growth: float = 0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm,", end=' ')
        print(f"{self.d_age} days old")

    def grow(self, days: int) -> None:
        if (self.d_age < 365):
            self.height += 0.8 * days
            self.growth += 0.8 * days
        else:
            self.height += 0.4 * days
            self.growth += 0.4 * days

    def age(self, days: int) -> None:
        self.d_age += days


def ft_plant_factory() -> None:
    plants = [Plant("rose", 25, 30), Plant("oak", 200, 365),
              Plant("cactus", 5, 90), Plant("sunflower", 80, 45),
              Plant("fern", 15, 120)]

    print("=== Plant Factory Output ===")
    for i in range(0, 5):
        print("Created: ", end=' ')
        plants[i].show()


if __name__ == "__main__":
    ft_plant_factory()
