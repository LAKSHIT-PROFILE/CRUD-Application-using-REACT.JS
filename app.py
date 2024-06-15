# Dictionary to store notes
notes = {}

# Function to add a note
def add_note(title, content):
    if title in notes:
        print("Note with the same title already exists. Please choose a different title.")
    else:
        notes[title] = content
        print("Note added successfully!")

# Function to view all notes
def view_notes():
    if notes:
        print("Your Notes:")
        for title, content in notes.items():
            print(f"Title: {title}")
            print(f"Content: {content}")
            print("---------------------")
    else:
        print("No notes found.")

# Function to delete a note
def delete_note(title):
    if title in notes:
        del notes[title]
        print("Note deleted successfully!")
    else:
        print("Note not found.")

# Main loop for the app
while True:
    print("\nNote-taking App")
    print("1. Add Note")
    print("2. View Notes")
    print("3. Delete Note")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        title = input("Enter note title: ")
        content = input("Enter note content: ")
        add_note(title, content)
    elif choice == '2':
        view_notes()
    elif choice == '3':
        title = input("Enter title of note to delete: ")
        delete_note(title)
    elif choice == '4':
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
