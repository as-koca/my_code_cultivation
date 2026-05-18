class Plant:
    def __init__(self, name: str, height: float, age: int) -> None:
        self._name: str = name.capitalize()
        if (self.is_valid(height, "height") is False):
            height = 0
        if (self.is_valid(age, "age") is False):
            age = 0
        self._height: float = height
        self._d_age: int = age
        self._growth: float = 0

    def is_valid(self, p: float, var_name: str) -> bool:
        if (p < 0):
            print(f"{self._name}: Error, {var_name} can't be negative")
            return (False)
        return (True)

    def set_height(self, height: float) -> None:
        if (self.is_valid(height, "height") is False):
            print("Height update rejected")
            return
        print(f"Height updated: {height}cm")
        self._height = height

    def set_age(self, age: int) -> None:
        if (self.is_valid(age, "age") is False):
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
        if (self.is_valid(days, "days") is False):
            return
        if (self._d_age < 365):
            self._height += 0.8 * days
            self._growth += 0.8 * days
        else:
            self._height += 0.4 * days
            self._growth += 0.4 * days

    def age(self, days: int) -> None:
        if (self.is_valid(days, "days") is False):
            return
        self._d_age += days


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float) -> None:
        super().__init__(name=name, height=height, age=age)
        if (self.is_valid(trunk_diameter, "trunk_diameter") is False):
            trunk_diameter = 0
        self._trunk_diameter: float = trunk_diameter
        self._shade: float = 0

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of", end=' ')
        print(f"{round(self._height, 1)}cm long and", end=' ')
        print(f"{round(self._trunk_diameter, 1)}cm wide.")

    def show(self) -> None:
        Plant.show(self)
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name=name, height=height, age=age)
        self._color = color
        self._bloom = f"{self._name} has not bloomed yet"

    def bloom(self) -> None:
        self._bloom = f"{self._name} is blooming beautifully!"

    def show(self) -> None:
        Plant.show(self)
        print(f"Color: {self._color}")
        print(self._bloom)


class Vegetable(Plant):
    def __init__(self, name, height, age, nut_val, harvest_season) -> None:
        super().__init__(name=name, height=height, age=age)
        self._nut_val = nut_val
        self._harvest_season = harvest_season.capitalize()

    def grow(self, days: int) -> None:
        super().grow(days)
        self._nut_val += days / 2

    def age(self, days: int) -> None:
        super().age(days)
        self._nut_val += days / 2

    def show(self) -> None:
        Plant.show(self)
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nut_val, 1)}")


def ft_plant_types() -> None:
    flower = Flower("rose", 15, 10, "red")
    tree = Tree("oak", 200, 365, 5)
    vegetable = Vegetable("tomato", 5, 10, 0, "april")

    print("=== Garden Plant Types ===")
    print("=== Flower")
    flower.show()
    print("[asking flower to bloom]")
    flower.bloom()
    flower.show()

    print("")
    print("=== Tree")
    tree.show()
    print("[asking tree to produce shade]")
    tree.produce_shade()

    print("")
    print("=== Vegetable")
    vegetable.show()
    print("[making vegetable grow and age]")
    vegetable.grow(20)
    vegetable.age(20)
    vegetable.show()


if __name__ == "__main__":
    ft_plant_types()
