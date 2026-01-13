# Un dizionario associa nomi di studenti a liste di date (stringhe) in cui erano presenti.
# Scrivere funzioni per: (a) contare le presenze di uno studente, (b) trovare chi ha più
# presenze, (c) trovare chi era presente in una certa data.

def contarePresenze(presenze):
    for studente in presenze:
        pr = len(presenze[studente])
        print(f"lo studente {studente} ha un totale di {pr} presenze")

def chi_ha_piu_presenze(presenze):
    max_presenze = 0
    persona_max = None

    for studente in presenze:
        date = presenze[studente]  # prendi la lista di date
        if len(date) > max_presenze:
            max_presenze = len(date)
            persona_max = studente
    print(f"la presona che ha più presenze è {persona_max}, con un totale di {max_presenze} presenze")

def presenza_data(presenza):
    data = input("inserisci la data (anno-mese-giorno): ")

    studente_data = None
    for studente in presenza:
        d = presenza[studente]
        if data in d:
            print(f"{studente} era presente")

def main():
    presenze = {
        "Marco": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15"],
        "Sara": ["2024-01-10", "2024-01-12", "2024-01-15", "2024-01-16", "2024-01-17"],
        "Luca": ["2024-01-10", "2024-01-11"],
        "Elena": ["2024-01-10", "2024-01-11", "2024-01-12", "2024-01-15", "2024-01-16"]
    }
    contarePresenze(presenze)
    print("-------------------------------------------------------------------")
    chi_ha_piu_presenze(presenze)
    print("-------------------------------------------------------------------")
    presenza_data(presenze)

if __name__ == "__main__":
    main()