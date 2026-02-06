num = [120, 999, 1000, 5000]

for value in num:
	if value >= 1000:
		print(f"{value} -> Premium")
	else:
		print(f"{value} -> Regular")