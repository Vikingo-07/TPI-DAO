import datetime



fecha_1 = datetime.datetime.strptime("2023-11-20", "%Y-%m-%d")
print(fecha_1)
fecha_2 = datetime.datetime.strptime("2023-12-25", "%Y-%m-%d")

print((fecha_2 - fecha_1).days)