nimi = input("Palun sisesta oma nimi: ")
n = int(input("Sisesta, mitu korda soovid tervitust: "))

for i in range(1, n + 1):
    print(f"Ole tervitatud, {nimi}, {i}. korda.")