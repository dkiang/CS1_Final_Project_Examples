def manage_todo_list(action, todo_list=None, item=None, priority=None):
    if action == "add":
        todo_list.append({"item": item, "priority": priority})
    elif action == "display":
        sorted_list = sorted(todo_list, key=lambda x: x["priority"])
        for entry in sorted_list:
            print(f"{entry['item']} (Priority: {entry['priority']})")

def main():
    todo_list = []
    while True:
        print("\nTo-do List Manager")
        print("1. Add item")
        print("2. Display items sorted by priority")
        print("3. Exit")

        choice = int(input("Enter your choice (1/2/3): "))

        if choice == 1:
            item = input("Enter the to-do item: ")
            priority = int(input("Enter the priority (1-5, 1 being highest): "))
            manage_todo_list("add", todo_list, item, priority)
        elif choice == 2:
            print("\nTo-do List Items Sorted by Priority:")
            manage_todo_list("display", todo_list)
        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
