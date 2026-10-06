# This sections stand as a placeholder for the animated black/white welcome screen
print("Join PRIVÉ")
print("Log In")
choice = input("Type 'Join PRIVÉ' or 'Log In' to continue: ").lower()
choice = choice.replace("é", "e")

if choice == "join prive":
    print("Let's get you started - taking you to sign up...")
elif choice == "Log In":
    print("Taking you to log in page...")
else:
    print("Invalid choice, please try again.")
