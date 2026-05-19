
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
        self._data = self.Stats()

    class Stats:
        def __init__(self) -> None:
            self.age: int = 0
            self.grow: int = 0
            self.show: int = 0
            self.produce_shade: int = 0

    def show_data(self) -> None:
        print(f"[statistics for {self._name}]")
        print(f"Stats: {self._data.grow} grow, {self._data.age}", end=' ')
        print(f"age, {self._data.show} show")

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

    def grow(self, days: int) -> None:
        if (self.is_valid(days, "days") is False):
            return
        if (self._d_age < 365):
            self._height += 0.8 * days
            self._growth += 0.8 * days
        else:
            self._height += 0.4 * days
            self._growth += 0.4 * days
        self._data.grow += 1

    def age(self, days: int) -> None:
        if (self.is_valid(days, "days") is False):
            return
        self._d_age += days
        self._data.age += 1

    def show(self) -> None:
        print(f"{self._name}: {round(self._height, 1)}cm,", end=' ')
        print(f"{self._d_age} days old")
        self._data.show += 1

    @staticmethod
    def check_year_old(days: int) -> bool:
        if (days > 365):
            return (True)
        return (False)

    @classmethod
    def make_anonymous(cls):
        return cls("Unkown plant", 0, 0)


def show_data(cls) -> None:
    cls.show_data()


class Tree(Plant):
    def __init__(self, name, height, age, trunk_diameter: float) -> None:
        super().__init__(name, height, age)
        if (self.is_valid(trunk_diameter, "trunk_diameter") is False):
            trunk_diameter = 0
        self._trunk_diameter: float = trunk_diameter
        self._shade: float = 0
        self._data = super().Stats()

    def produce_shade(self) -> None:
        print(f"Tree {self._name} now produces a shade of", end=' ')
        print(f"{round(self._height, 1)}cm long and", end=' ')
        print(f"{round(self._trunk_diameter, 1)}cm wide.")
        self._data.produce_shade += 1

    def show(self) -> None:
        super().show()
        print(f"Trunk diameter: {round(self._trunk_diameter, 1)}cm")
        self.show_data()

    def show_data(self) -> None:
        super().show_data()
        print(f"{self._data.produce_shade} shade")


class Flower(Plant):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age)
        self._color = color
        self._bloom = f"{self._name} has not bloomed yet"
        self._data = super().Stats()

    def bloom(self) -> None:
        self._bloom = f"{self._name} is blooming beautifully!"

    def show(self) -> None:
        super().show()
        print(f"Color: {self._color}")
        print(self._bloom)
        self.show_data()


class Seed(Flower):
    def __init__(self, name, height, age, color) -> None:
        super().__init__(name, height, age, color)
        self._seeds: int = 0
        self._data = super().Stats()

    def show(self) -> None:
        super().show()
        print(f"Seeds: {self._seeds}")

    def bloom(self) -> None:
        super().bloom()
        self._seeds += 42


class Vegetable(Plant):
    def __init__(self, name, height, age, nut_val, harvest_season) -> None:
        super().__init__(name, height, age)
        self._nut_val = nut_val
        self._harvest_season = harvest_season.capitalize()
        self._data = super().Stats()

    def grow(self, days: int) -> None:
        super().grow(days)
        self._nut_val += days / 2

    def age(self, days: int) -> None:
        super().age(days)
        self._nut_val += days / 2

    def show(self) -> None:
        super().show()
        print(f"Harvest season: {self._harvest_season}")
        print(f"Nutritional value: {round(self._nut_val, 1)}")
        self.show_data()


def ft_garden_analytics() -> None:
    flower = Flower("rose", 15, 10, "red")
    tree = Tree("oak", 200, 365, 5)
    seed = Seed("sunflower", 80, 45, "yellow")
    anonymous = Plant("", 3, 3).make_anonymous()

    print("=== Garden Statistics ===")
    print("=== Check year-old")
    if (anonymous.check_year_old(30) is False):
        print("Is 30 days more than a year? -> False")
    if (anonymous.check_year_old(400) is True):
        print("Is 400 days more than a year? -> True\n")

    print("== Flower")
    flower.show()
    print("[asking the rose to grow and bloom]")
    flower.grow(8)
    flower.bloom()
    flower.show()
    print("")

    print("=== Tree")
    tree.show()
    print("[asking oak to produce shade]")
    tree.produce_shade()
    tree.show()
    print("")

    print("=== Seed")
    seed.show()
    print("[making sunflower grow, age and bloom]")
    seed.grow(20)
    seed.age(20)
    seed.bloom()
    seed.show()
    print("")

    print("=== Anonymous")
    anonymous.show()
    anonymous.show_data()


if __name__ == "__main__":
    ft_garden_analytics()
