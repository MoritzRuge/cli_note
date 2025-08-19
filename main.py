from function import create_new_note, open_note, list_all_notes

def main():
    while True:
        print("1. Neue Notiz")
        print("2. Notiz öffnen")
        print("3. Alle Notizen anzeigen")
        print("n. Beenden\n")
        user_input = int(input("Bitte wähle Sie die Funktion aus :): "))
        match user_input:
            case 1:
                title = input("Bitte Titel eingeben: ")
                text = input ("Text: ")
                create_new_note(title, text)
            case 2:
                title = input("Bitte Titel eingeben: ")
                open_note(title)
            case 3:
                list_all_notes()
            case _:
                break

if __name__ == "__main__":
    main()