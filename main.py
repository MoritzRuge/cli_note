import click
import os

def main():


    def menu():
        print("1. New Note\n2. Exit\n")

        user_input = int(input("Bitte wähle Sie die Funktion aus :)"))

        match user_input:
            case 1:
                title = input("Bitte Titel eingeben: ")
                text = input ("Text: ")
                create_new_note(title, text)
            case _:
                exit()

    def create_new_note(title, text):
        filepath = os.path.join("./Note/", title)
        if not os.path.exists("./Note/"):
            os.makedirs("./Note/")
        note = open(f"{filepath}.txt", "a") # "a" filepath erstellt die Datei schon
        note.write(text)

    def open_note():
        pass
    def delete_note():
        pass
    def list_all_notes():
        pass


    ### MAIN ###
    menu()
    




if __name__ == "__main__":
    main()
