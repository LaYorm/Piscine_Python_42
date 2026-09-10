class Plant:
    def __init__(self, name: str = "Unknown", height: int | str = "Unknown ",
                 age: int | str = "Unknown") -> None:
        self.name = name
        self.height = height
        self.age = age

    def show(self) -> None:
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def ft_garden_data() -> None:
    tulipe = Plant("Tulipe", 28, 62)
    marguerite = Plant("mMarguerite", 12, 6)
    cactus = Plant("Cactus", 112, 359)
    inconnu = Plant()
    print("=== Garden Plant Registry ===")
    tulipe.show()
    marguerite.show()
    cactus.show()
    inconnu.show()


if __name__ == "__main__":
    # Appel et execution si et seulement si le programme
    # est execute directement
    ft_garden_data()
