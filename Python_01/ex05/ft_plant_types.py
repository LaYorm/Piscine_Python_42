class Plant:
    def __init__(self, name: str = "Unknown", height: float = 0.0,
                 age: int = 0) -> None:
        self.name = name
        self.__height = 0.0
        self.__age = 0

        if age < 0:
            print(f"{name}: Error, age can't be negative")
        elif height < 0:
            print(f"{name}: Error, height can't be negative")
        else:
            self.__height = height
            self.__age = age
            print(f"Plant created: {name}: {height:.1f}cm, {age} days old")

    def get_height(self) -> float:
        return self.__height

    def get_age(self) -> int:
        return self.__age

    def set_height(self, new_h: float) -> None:
        if new_h < 0:
            print(
                f"{self.name}: Error, height can't be negative\n"
                "Height update rejected"
            )
        else:
            self.__height = new_h
            print(f"Height updated: {new_h}cm")

    def set_age(self, new_a: int) -> None:
        if new_a < 0:
            print(
                f"{self.name}: Error, age can't be negative\n"
                "Age update rejected"
            )
        else:
            self.__age = new_a
            print(f"Age updated: {new_a} days")

    def show(self) -> None:
        print(
            "Current state: "
            f"{self.name}: {self.__height:.1f}cm, {self.__age} days old"
        )

    def age(self) -> None:
        self.__age += 1


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
