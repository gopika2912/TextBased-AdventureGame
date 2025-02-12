def adventure():
    choice = input("You see a cave. Enter? (yes/no): ")
    if choice.lower() == "yes":
        print("You found treasure!")
    else:
        print("You missed the adventure!")

if __name__ == "__main__":
    adventure()
