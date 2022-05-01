from prettytable import PrettyTable

table = PrettyTable()


table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electico", "Water", "Fire"])
print(table.align)
table.align = "l"
print(table)


