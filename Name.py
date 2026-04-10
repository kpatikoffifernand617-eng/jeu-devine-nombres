mport random

def jeu_devine_nombre():
    nombre_secret = random.randint(1, 100)
    tentatives = 0

    print("🎮 Bienvenue dans le jeu Devine le Nombre !")
    print("Je pense à un nombre entre 1 et 100.")

    while True:
        try:
            guess = int(input("👉 Entre ton nombre : "))
            tentatives += 1

            if guess < nombre_secret:
                print("📉 Trop petit !")
            elif guess > nombre_secret:
                print("📈 Trop grand !")
            else:
                print(f"🎉 Bravo ! Tu as trouvé en {tentatives} tentatives !")
                break
        except ValueError:
            print("⚠️ Entre un nombre valide !")

jeu_devine_nombre()
