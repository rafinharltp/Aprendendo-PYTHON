frutas = ["maca", "banana", "laranja"]

frutas.append("uva")
print(frutas)

frutas.insert(0,"pera")
print(frutas)

frutas.remove("maca")
print(frutas)

fruta_removida = frutas.pop(1)
print(frutas)
print("Foi removida a fruta:",fruta_removida)

frutas.sort()
print(frutas)

frutas.sort(reverse=True)
print(frutas)