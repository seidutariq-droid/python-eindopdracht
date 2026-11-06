product1 = "Cola"
prijs1 = 2.50
aantal1 = 40

product2 = "Chips"
prijs2 = 1.75
aantal2 = 25

product3 = "Snoep"
prijs3 = 0.95
aantal3 = 60

omzet1 = prijs1 * aantal1
omzet2 = prijs2 * aantal2
omzet3 = prijs3 * aantal3

totale_omzet = omzet1 + omzet2 + omzet3

print("Product: " + product1 + " | Prijs: " + str(prijs1) + " | Aantal: " + str(aantal1))
print("Product: " + product2 + " | Prijs: " + str(prijs2) + " | Aantal: " + str(aantal2))
print("Product: " + product3 + " | Prijs: " + str(prijs3) + " | Aantal: " + str(aantal3))
print("")
print("Totale omzet: " + str(totale_omzet))

