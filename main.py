nom = input("Ton prénom ? ")
age = int(input("Ton âge ? "))

annee = 2026 + (18 - age)

print(f"{nom}, tu auras 18 ans en {annee}")

if age >= 18:
    print("Tu peux déjà viser très haut 😏")
else:
    print("Prépare-toi, ça arrive vite 🚀")