food = [
    {"meal": "Baja Taco", "price": 4.25},
    {"meal": "Burrito", "price": 7.50},
    {"meal": "Bowl", "price": 8.50},
    {"meal": "Nachos", "price": 11.00},
    {"meal": "Quesadilla", "price": 8.50},
    {"meal": "Super Burrito", "price": 8.50},
    {"meal": "Super Quesadilla", "price": 9.50},
    {"meal": "Taco", "price": 3.00},
    {"meal": "Tortilla Salad", "price": 8.00},
]

total_cost = 0.0  # Initialize total cost to 0

# Infinite loop to take orders until user exits (Control-D)
try:
    while True:
        try:
            user_input = input("meal: ").strip().title()  # Case-insensitive input

            # Search for the meal in the food list
            for item in food:
                if item["meal"] == user_input:
                    total_cost += item["price"]  # Add price to the total cost
                    print(f"${total_cost:.2f}")  # Display formatted total cost
                    break
            else:
                # If item was not found in the menu, ignore it
                pass
        except EOFError:
            # Gracefully exit the loop on Control-D
            print("\nOrder complete.")
            break

except KeyboardInterrupt:
    # Optional handling for Control-C
    print("\nOrder cancelled.")
