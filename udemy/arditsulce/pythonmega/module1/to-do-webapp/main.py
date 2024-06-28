from functions import file_operations

action_list = []

while True:
    user_action = input(
        "What do you want to do? (add, show, edit, complete, exit, quit, delete): "
    )
    user_action.strip().lower()

    match user_action:
        case "add":
            action = input("Enter a todo: ")
            action_list.append(action)

            action_list = file_operations("output-files/todolist.txt", action_list, "w")

        case "delete":
            action = input("Enter a todo: ")
            action_list.remove(action)

            action_list = file_operations("output-files/todolist.txt", action_list, "w")

        case "show" | "display":
            print("Your todo list: ")

            action_list = file_operations("output-files/todolist.txt", action_list, "r")

        case "edit":
            action_list = file_operations("output-files/todolist.txt", action_list, "r")

            number = int(input("Number of the todo to edit: "))
            new_action = input("Enter a new todo: ")
            action_list[number - 1] = new_action

            action_list = file_operations("output-files/todolist.txt", action_list, "w")

        case "complete":
            action_list = file_operations("output-files/todolist.txt", action_list, "r")

            number = int(input("Number of the todo to complete: "))
            action_list.pop(number - 1)

            action_list = file_operations("output-files/todolist.txt", action_list, "w")

        case "clear":
            action_list.clear()
            with open("output-files/todolist.txt", "w") as file:
                file.write("")

            print("Your todo list is now empty.")

        case "exit" | "quit":
            break

        case whatever:
            print("invalid input")

print("Goodbye!")
