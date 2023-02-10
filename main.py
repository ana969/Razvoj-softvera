def main():
    print("Dobrodošli u kalkulator recikliranja!")
    print("Ovaj program izračunava broj spašenih stabala i kornjača na temelju količine recikliranog papira i plastičnih boca.")
    print("Počnimo spašavati planet zajedno!")
    print(" ")  
    first_time = input("Jeste li već prije koristili program? (da/ne): ")
    if first_time == "da":
        print(" ")
        mode = int(input("Unesite način rada (1-normalni, 2-mjesečni, 3-godišnji): "))
        if mode == 1:
            print(" ")
            paper = int(input("Unesite broj kilograma recikliranog papira: "))
            bottles = int(input("Unesite broj recikliranih plastičnih boca: "))
            trees = paper / 21
            turtles = bottles / 88
            print("\nČestitamo! Ovo je utjecaj koji ste napravili:")
            print(f"Spasili ste {trees:.2f} drveća i {turtles:.2f} kornjača")
        elif mode == 2:
            print(" ")
            months = int(input("Unesite broj mjeseci: "))
            total_trees = 0
            total_turtles = 0
            for i in range(months):
                paper = int(input(f"Unesite broj kilograma recikliranog papira u mjesecu: {i+1}: "))
                bottles = int(input(f"Unesite broj kilograma recikliranih plastičnih boca u mjesecu: {i+1}: "))
                trees = paper / 21
                turtles = bottles / 88
                total_trees += trees
                total_turtles += turtles
            print("\nČestitamo! Ovo je utjecaj koji ste napravili:")
            print(f"Spasili ste {trees:.2f} drveća i {turtles:.2f} kornjača u {months} mjeseca/mjeseci.")
        elif mode == 3:
            print(" ")
            years = int(input("Unesite broj godina: "))
            total_trees = 0
            total_turtles = 0
            for i in range(years):
                paper = int(input(f"Unesite broj kilograma recikliranog papira u godini: {i+1}: "))
                bottles = int(input(f"Unesite broj kilograma recikliranih plastičnih boca u godini: {i+1}: "))
                trees = paper / 21
                turtles = bottles / 88
                total_trees += trees
                total_turtles += turtles
            print("\nČestitamo! Ovo je utjecaj koji ste napravili:")
            print(f"Spasili ste {total_trees:.2f} drveća i {total_turtles:.2f} kornjača {years} godine/godina.")
    else:
        print(" ")  
        print("Uvijek je dobro početi! ")
        print("Kalkulator recikliranja radi u sklopu web stranice ZG eko priručnik čija je svrha ljudima prikazati sažete informacije o sustavu recikliranja u Zagrebu.")
        print("Namjena mu je povećati svijest ljudi o tome koliko je važno pravilno odvajati otpad i kako su mali doprinosi zapravo jako važni! ")
        print("Krenimo... ")
        print(" ")          
        paper = int(input("Unesite broj kilograma recikliranog papira:"))
        bottles = int(input("Unesite broj recikliranih plastičnih boca:"))
        trees = paper / 21
        turtles = bottles / 88
        print("\nČestitamo! Ovo je utjecaj koji ste napravili:")
        print(f"Spasili ste {trees:.2f} drveća i  {turtles:.2f} kornjača. ")

    print("\nNastavite s recikliranjem. Svako malo djelo pomaže!")

if __name__ == "__main__":
    main()


def main():
    print(" ")
    print(" ")
    play_game = input("Želiš li igrati kviz o recikliranju? (da/ne): ")
    
    if play_game.lower() == 'da':
        print("Dobrodošao u kviz!!")
        print("U ovom kvizu ćeš odgovoriti na 3 kratka pitanja. ")
        print("Pođimo provjeriti koliko znaš!\n")

        questions = [
            {
                "question": "Koliko posto zauzima biootpad u komunalnom otpadu?", 
                "options": ["oko 5%", "oko 20-30%", "više od pola"], 
                "answer": 2
            },
            {
                "question": "Gdje odlažemo namještaj?", 
                "options": ["u plavu kantu", "u poseban kontejner", "nigdje od navedenog"], 
                "answer": 3
            },
            {
                "question": "Što je najmanje prihvatljiv način ophođenja s otpadom?", 
                "options": ["odlaganje otpada", "spaljivanje otpada", "ponovno korištenje"], 
                "answer": 1
            }
        ]

        score = 0
        for question in questions:
            print(f"\n{question['question']}")
            for i, option in enumerate(question['options']):
                print(f"{i+1}. {option}")
            guess = int(input("\nUnesi broj točnog odgovora: "))
            if guess == question['answer']:
                print("Točno!")
                score += 1
            else:
                print("Netočno.")

        print(f"\nDobio si {score} od {len(questions)} točnih")
        if score / len(questions) >= 0.75:
            print("Bravo! Pravi si stručnjak!")
        else:
            print("Nastavi učiti, zajedno možemo napraviti svijet boljim mjestom za život!")
    else:
        print("U redu, ugodan ostatak dana!")

if __name__ == "__main__":
    main()

    print("Doviđenja! Posjetite: zgeko.com")

    input("Pritisni enter za izlazak...")