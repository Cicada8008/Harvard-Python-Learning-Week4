shopping = {}

while True:
    try:
        item = input().strip().upper()  # Take input and convert to uppercase

        if item in shopping:
            shopping[item] += 1  # Increment count if item already exists
        else:
            shopping[item] = 1  # Add item to dictionary with a count of 1

    except EOFError:  # Handle EOFError to stop input when Ctrl+D is pressed (Linux/macOS) or Ctrl+Z (Windows)
        # Sort the dictionary items alphabetically by the item name (key)
        for item, count in sorted(shopping.items()):
            print(f"{count} {item}")
        break
