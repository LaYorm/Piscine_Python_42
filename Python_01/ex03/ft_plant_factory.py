class Plant:
    def __init__(self, name: str = "Unknown", height: float = 0,
                 age: int = 0, grow_speed: float = 0) -> None:
        self.name = name
        self.height = height
        self._age = age
        self.height_ini = height
        self.grow_speed = grow_speed

    def show(self) -> None:
        print(f"{self.name}: {self.height:.1f}cm, {self._age} days old")

    def grow(self) -> None:
        self.height += self.grow_speed

    def age(self) -> None:
        self._age += 1

    def total_grow(self) -> None:
        total_growth = self.height - self.height_ini
        print(f"Growth this week of {self.name}: {total_growth:.1f}cm")


def ft_plant_factory() -> None:
    garden = [
        Plant("Bamboo", 245.9, 36),
        Plant("Tulipe", 24, 63),
        Plant("Coquelicot", 18, 45),
        Plant("Cactus", 165.4, 256),
        Plant("Rose", 20.6, 75)
    ]
    for plant in garden:
        print("Created: ", end="")
        plant.show()

if __name__ == "__main__":
    # Appel et execution si et seulement si le programme
    # est execute directement
    ft_plant_factory()
