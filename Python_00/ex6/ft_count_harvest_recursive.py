def ft_count_harvest_recursive() -> None:
    days = int(input("Days until harvest: "))

    def recursive(start: int, days: int) -> None:
        if start > days:
            print("Harvest time!")
            return
        print(f"Day: {start}")
        recursive(start + 1, days)
    recursive(1, days)
