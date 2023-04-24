# Function to manage motel reservations and view reserved rooms
def motel_management(action, room_number=None):
    if action == "view":
        view_reserved_rooms()
    elif action == "reserve" and room_number is not None:
        reserve_room(room_number)
    else:
        print("Invalid action or missing room number.")

# Function to display the reserved rooms
def view_reserved_rooms():
    print("Occupied Rooms: ", end="")
    for room in reserved_rooms:
        print(room, end=" ")
    print()

# Function to reserve a room if it's available
def reserve_room(room_number):
    room_reserved = False
    for room in reserved_rooms:
        if room == room_number:
            room_reserved = True
            break

    if room_reserved:
        print(f"Room {room_number} is already reserved.")
    else:
        reserved_rooms.append(room_number)
        reserved_rooms.sort()
        print(f"Room {room_number} has been reserved.")

# List to store reserved room numbers
reserved_rooms = [101, 103, 105, 201]

# Main loop for user interaction
def main():
    while True:
        print("\nMotel Management")
        print("1. View reserved rooms")
        print("2. Reserve a room")
        print("3. Quit")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            motel_management("view")
        elif choice == "2":
            room_number = int(input("Enter the room number to reserve: "))
            motel_management("reserve", room_number)
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()
