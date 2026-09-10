def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if (seed_type != "carrot" and seed_type != "lettuce" and seed_type != "tomato"):
		print("Unknown seed type")
		return
	if (unit == "packets"):
		print(seed_type.capitalize(), f"seeds: {quantity} packets available")
	elif (unit == "grams"):
		print(seed_type.capitalize(), f"seeds: {quantity} grams total")
	elif (unit == "area"):
		print(seed_type.capitalize(), f"seeds: {quantity} square meters")
	else:
		print("Unknown unit type")
