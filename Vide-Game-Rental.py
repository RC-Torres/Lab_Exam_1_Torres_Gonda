#GAME DICTIONARIES
game_library = {
    "Donkey Kong": {"quantity": 3, "cost": 2},
    "Super Mario Bros": {"quantity": 5, "cost": 3},
    "Tetris": {"quantity": 2, "cost": 1},
    "Minecraft": {"quantity": 3, "cost": 2},
    "Elden Ring": {"quantity": 1, "cost": 5}
}

# LIST FOR INVENTORY
inventory = []

# DICTIONARIES FOR USER ACCOUNTS
user_database = {}

# DEFAULT ADMIN USERNAME AND PASSWORD
admin_username = "admin"
admin_password = "adminpass"

# USER SIGN UP
def user_sign_up():
    while True:
        try:
            username = input("Enter username: ")
            password = input("Enter Password (must be at least 8 characters long): ")
            user_database[username] = {
                'username': username,
                'password': password,
                'money': 0  # Starting money is zero
            }
            if not username:
                main()
            if username in user_database[username]:
                print("Username already exists. Input another one.")
                user_sign_up()
            if len(password) >= 8:
                print("Sign up successful!")
                main()
            else:
                print("Password must be 8 characters long.")
                user_sign_up()
        except ValueError as e:
            print(e)

# USER LOG IN
def user_log_in():
    while True:
        try:
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            if username in user_database and user_database[username]['password'] == password:
                print("Log in successful!")
                logged_in_menu(username)
            else:
                print("Wrong username or password.")
        except ValueError as e:
            print(e)

# LOGGED IN MENU
def logged_in_menu(username):
    while True:
        print(f'Logged in as {username}')
        print(f'Current balance: ${user_database[username]["money"]}')
        print("""
            1. Rent a Game
            2. Return Game
            3. Top-up Account
            4. Display Inventory
            5. Redeem free Game Rental
            6. Check Points
            7. Logout
            """)
        choice = int(input("Enter a number: "))
        if choice == 1:
            rent_game(username)
        elif choice == 2:
            return_game(username)
        elif choice == 3:
            top_up_acc(username)
        elif choice == 4:
            display_inventory(username)
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            main()
        else:
            "Enter a valid input."

# RENT GAME
def rent_game(username):
    print(f"Available games for rent. Your current balance: ${user_database[username]['money']}:")
    for i, (game, details) in enumerate(game_library.items(), start=1):
        print(f"{i}. {game} - Quantity: {details['quantity']}, Cost: ${details['cost']}")
    choice = int(input("Enter the number of the game you want to rent: "))
    if choice in range(1, len(game_library) + 1):
        game_name = list(game_library.keys())[choice - 1]
        quantity = int(input("How many copies?: "))
        if game_library[game_name]["quantity"] >= quantity:
            total_cost = game_library[game_name]["cost"] * quantity
            if user_database[username]['money'] >= total_cost:  # Check if user has enough money
                user_database[username]['money'] -= total_cost  # Deduct cost from user's money
                inventory.append({"game_name": game_name, "quantity": quantity, "username": username})
                game_library[game_name]["quantity"] -= quantity
                print(f"Total Cost: ${total_cost}")
            else:
                print("Insufficient funds.")
        else:
            print("Insufficient quantity.")
    else:
        print("Enter a valid input.")

# RETURN GAME
def return_game(username):
    print("Games you can return:")
    for i, item in enumerate(inventory, start=1):
        if item["username"] == username:
            print(f"{i}. {item['game_name']} - Quantity: {item['quantity']}")
    choice = int(input("Enter the number of the game you want to return: "))
    if choice in range(1, len(inventory) + 1):
        returned_game = inventory[choice - 1]
        game_name = returned_game["game_name"]
        max_quantity = returned_game["quantity"]
        return_quantity = int(input(f"How many copies of {game_name} do you want to return? (1-{max_quantity}): "))
        if return_quantity in range(1, max_quantity + 1):
            returned_game["quantity"] -= return_quantity
            game_library[game_name]["quantity"] += return_quantity
            print(f"{return_quantity} copy/copies of {game_name} returned successfully.")
        else:
            print("Invalid quantity.")
    else:
        print("Enter a valid input.")

# TOP UP ACCOUNT
def top_up_acc(username):
    try:
        amount = float(input("Enter the amount you want to top up: "))
        if amount > 0:
            user_database[username]['money'] += amount
            print(f"Successfully topped up ${amount}. Total balance: ${user_database[username]['money']}")
        else:
            print("Invalid amount.")
    except ValueError:
        print("Invalid input.")

# DISPLAY GAMES IN INVENTORY
def display_inventory(username):
    print("Your rented games:")
    for i, item in enumerate(inventory, start=1):
        if item["username"] == username:
            for _ in range(item["quantity"]):
                print(f"{i}. {item['game_name']}")
                i += 1

# REDEEM FREE GAMES USING POINTS
def redeem_free_game():
    pass

# CHECK POINTS
def check_points():
    pass


# ADMIN LOG IN
def admin_log_in():
    admin_check_username = input("Enter username: ")
    admin_check_password = input("Enter password: ")
    if admin_check_password == admin_password and admin_check_username == admin_username:
        print("Admin logged in.")
        admin_menu()
    else:
        main()
    choice = int(input("Enter a number: "))
    if choice == 1:
        pass
    if choice == 2:
        main()

# CHANGE GAME DETAILS
def change_game_details():
    print("Change Game Details")
    print("Select a game to update:")
    for i, (game, details) in enumerate(game_library.items(), start=1):
        print(f"{i}. {game}")
    choice = int(input("Enter the number of the game you want to update: "))
    if choice in range(1, len(game_library) + 1):
        game_name = list(game_library.keys())[choice - 1]
        new_quantity = int(input(f"Enter the new quantity for {game_name}: "))
        new_cost = float(input(f"Enter the new cost for {game_name}: $"))
        game_library[game_name]["quantity"] = new_quantity
        game_library[game_name]["cost"] = new_cost
        print(f"{game_name} details updated successfully.")
        admin_menu()
    else:
        print("Invalid input.")


# ADMIN MENU
def admin_menu():
    print("""
        ADMIN MENU
        1. Update Game Details
        2. Logout
        """)
    choice = int(input("Enter a number: "))
    if choice == 1:
        change_game_details()
    elif choice == 2:
        main()

# DISPLAY AVAILABLE GAMES
def display_available_games():
    print("Available games for rent:")
    for i, (game, details) in enumerate(game_library.items(), start=1):
        print(f"{i}. {game} - Quantity: {details['quantity']}, Cost: ${details['cost']}")
    input("Press enter to continue")

# MAIN MENU
def main():
    print("""
        Welcome to Game Rental System
        1. User Sign up
        2. User Log in
        3. Admin Log in
        4. Display available games
        5. Exit
        """)
    choice = int(input("Enter choice: "))
    if choice == 1:
        user_sign_up()
    elif choice == 2:
        user_log_in()
    elif choice == 3:
        admin_log_in()
    elif choice == 4:
        display_available_games()
    elif choice == 5:
        exit()
    else:
        print("Enter a valid input.")
        main()

main()
