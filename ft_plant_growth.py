class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self.name: str = name.capitalize()
        self.height: float = height
        self.d_age: int = age
        self.growth: int = 0

    def show(self) -> None:
        print(f"{self.name}: {round(self.height, 1)}cm", end=' ')
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


def ft_plant_growth() -> None:
    plant = Plant("rose", 25, 30)
    days: int = 1
    print("=== Garden Plant Growth ===")
    plant.show()
    while days <= 7:
        print(f"=== Day {days} ===")
        plant.age(1)
        plant.grow(1)
        plant.show()
        days += 1
    print(f"Growth this week: {round(plant.growth, 1)}cm")


if __name__ == "__main__":
    ft_plant_growth()
