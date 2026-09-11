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
            print(f"Plant created: {name}: {height:.1f}cm, {age} days old")

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
        print(
            "Current state: "
            f"{self.name}: {self._height:.1f}cm, {self._age} days old"
        )


def ft_plant_types() -> None:
    garden = [
        Plant("Rose", 20.6, 75),
        Plant("Bamboo", 1, 1)
    ]
    print("\n=== Garden Security System ===")
    for plant in garden:
        plant.show()
    print()
    garden[0].set_height(-10.3)
    print()
    garden[0].set_height(10.3)
    garden[1].set_age(12)
    print()
    for plant in garden:
        plant.show()


if __name__ == "__main__":
    # Appel et execution si et seulement si le programme
    # est execute directement
    ft_plant_types()
