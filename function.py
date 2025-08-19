import os

base_dir = "./Note/"

# TODO: try excepte for filepath
def create_new_note(title, text):
    filepath = os.path.join(base_dir, title)
    if not os.path.exists("./Note/"):
        os.makedirs("./Note/")
    
    note = open(f"{filepath}.txt", "a") # "a" filepath erstellt die Datei schon
    note.write(text)

def open_note(title):
    full_path = os.path.join(base_dir, f"{title}.txt")

    with open(full_path, "r") as note:
        content = note.read()
        print(content)

def delete_note():
    pass
def list_all_notes() -> None:
    print("Hier sind alle deine Notizen:")
    all_notes = os.listdir(base_dir)
    for i in all_notes:
        print(i)