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


def ft_plant_growth() -> None:
    bamboo = Plant("Bamboo", 28, 62, 80.4)
    cactus = Plant("Cactus", 112, 750, 0.6)
    inconnu = Plant()
    print("=== Garden Plant Registry ===")
    bamboo.show()
    cactus.show()
    inconnu.show()
    for i in range(7):
        print(f"=== Day {i + 1} ===")
        bamboo.grow()
        bamboo.age()
        cactus.grow()
        cactus.age()
        bamboo.show()
        cactus.show()
    print("=== Total growth ===")
    bamboo.total_grow()
    cactus.total_grow()


if __name__ == "__main__":
    # Appel et execution si et seulement si le programme
    # est execute directement
    ft_plant_growth()
