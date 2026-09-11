class Plant:
    def __init__(self, name: str = "Unknown", height: float = 0.0,
                 age: int = 0) -> None:
        self.name = name
        self._height = 0.0
        self._age = 0

        if age < 0:
            print(f"{name}: Error, age can't be negative")
        elif height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self._height = height
            self._age = age

    def get_height(self) -> float:
        return self._height

    def get_age(self) -> int:
        return self._age

    def set_height(self, new_h: float) -> None:
        if new_h < 0:
            print(
                f"{self.name}: Error, height can't be negative\n"
                "Height update rejected"
            )
        else:
            self._height = new_h
            print(f"Height updated: {new_h}cm")

    def set_age(self, new_a: int) -> None:
        if new_a < 0:
            print(
                f"{self.name}: Error, age can't be negative\n"
                "Age update rejected"
            )
        else:
            self._age = new_a
            print(f"Age updated: {new_a} days")

    def show(self) -> None:
        print(f"{self.name}: {self._height:.1f}cm, {self._age} days old")

    def age(self) -> None:
        self._age += 1

    def grow(self, grow_size: float) -> None:
        self._height += grow_size


class Flower(Plant):
    def __init__(self, name: str, height: float,
                 age: int, color: str = "Unknown"):
        super().__init__(name, height, age)
        self.color = color
        self.has_bloom = False

    def bloom(self) -> None:
        if not self.has_bloom:
            self.has_bloom = True

    def show(self) -> None:
        super().show()
        print(f" Color: {self.color}")
        if self.has_bloom:
            print(f" {self.name} is blooming beautifully!")
        else:
            print(f" {self.name} has not bloomed yet")


class Tree(Plant):
    def __init__(self, name: str, height: float,
                 age: int, trunk: float):
        super().__init__(name, height, age)
        self.trunk_diam = trunk

    def produce_shade(self) -> None:
        print(
            f"Tree {self.name} now produces a shade of "
            f"{self._height:.1f}cm long and {self.trunk_diam:.1f}cm wide."
        )

    def show(self) -> None:
        super().show()
        print(f" Trunk diameter: {self.trunk_diam:.1f}cm")


class Vegetable(Plant):
    def __init__(self, name: str, height: float,
                 age: int, harvest: str):
        super().__init__(name, height, age)
        self.harv_season = harvest
        self.nut_val = 0
        self.nb_aged = 0
        self.nb_grow = 0

    def age(self) -> None:
        super().age()
        self.nb_aged += 1
        self.update_nut_val()

    def grow(self, grow_size: float) -> None:
        super().grow(grow_size)
        self.nb_grow += 1
        self.update_nut_val()

    def update_nut_val(self) -> None:
        if self.nb_aged <= self.nb_grow:
            self.nut_val = self.nb_aged
        else:
            self.nut_val = self.nb_grow

    def show(self) -> None:
        super().show()
        print(f" Harvest season: {self.harv_season}")
        print(f" Nutritional value: {self.nut_val}")


def ft_plant_types() -> None:
    print("=== Garden Plant Types ===")
    print("=== Flower")
    rose = Flower("Rose", 15, 10, "red")
    rose.show()
    print("[asking the rose to bloom]")
    rose.bloom()
    rose.show()
    print("\n=== Tree")
    oak = Tree("Oak", 200, 365, 5)
    oak.show()
    print("[asking the oak to produce shade]")
    oak.produce_shade()
    print("\n=== Vegetable")
    tomato = Vegetable("Tomato", 5, 10, "April")
    tomato.show()
    print("[make tomato grow and age for 20 days]")
    for i in range(20):
        tomato.age()
        tomato.grow(2.1)
    tomato.show()


if __name__ == "__main__":
    # Appel et execution si et seulement si le programme
    # est execute directement
    ft_plant_types()
