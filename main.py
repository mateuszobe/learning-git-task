print("Zadanie 1")
print()
print("Lista zakupów")

slownik =  {"piekarnia":["chleb","bułki","pączek"],
            "warzywniak":["marchew","seler","rukola"]}
x = 0
for sklep, rzeczy in slownik.items():
    sklep = sklep.title()
    rzeczy = [rzecz.title() for rzecz in rzeczy]
    x +=len(rzeczy)
    print (f"Idę do {sklep}, kupuję tu następujące rzeczy: {rzeczy}")
print(f"W sumie kupuję {x} produktów")