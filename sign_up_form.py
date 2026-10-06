while True:
    print("The PRIVÉ Atelier awaits you...")

    name = input("First Name: ").capitalize()
    surname = input("Surname: ").capitalize()
    email = input("Email address: ")
    phone = input("Phone number: ")
    dob = input("Date of Birth: ")
    occupation = input("Occupation: ").title()
    company = input("Company (optional, press enter to skip): ").capitalize()
    styling_for = input("Are you styling for yourself, or on behalf of a company/ someone else? ").lower().capitalize()

    member = {
        "First Name": name,
        "Surname": surname,
        "Email": email,
        "Phone": phone,
        "DOB": dob,
        "Occupation": occupation,
        "Company": company,
        "Styling required for": styling_for,
    }

    print("\nHello, " + name + "!")
    print("Your Details:")

    for key, value in member.items():
        print(f"{key}: {value}")

    confirm_and_submit = input("\nType 'Confirm & Submit' to continue, or type the field name(s) you'd like to edit, separated by commas: ").lower().strip()

    if confirm_and_submit == "confirm & submit":
        print("\nWelcome to PRIVÉ, " + name + "!")
        break
    else:
        print("Uh oh! Let's fix that...")
        fields_to_edit = confirm_and_submit.split(",")

        for field in fields_to_edit:
            field = field.strip()

            if field == "first name":
                name = input("First Name: ").capitalize()
                member["First Name:"] = name
            elif field == "surname":
                surname = input("Surname: ").capitalize()
                member["Surname"] = surname
            elif field == "email":
                email = input("Email address: ")
                member["Email"] = email
            elif field == "phone":
                phone = input("Phone number: ")
                member["Phone"] = phone
            elif field == "dob":
                dob = input("Date of Birth: ")
                member["DOB"] = dob
            elif field == "occupation":
                occupation = input("Occupation: ").title()
                member["Occupation"] = occupation
            elif field == "company":
                company = input("Company (optional, press enter to skip): ").capitalize()
                member["Company"] = company
            elif field == "styling_for":
                styling_for = input("Are you styling for yourself, or on behalf of a company/ someone else? ").lower().capitalize()
                member["Styling required for"] = styling_for

    print("\nHello, " + name + "!")
    print("Your Details:")

    for key, value in member.items():
        print(f"{key}: {value}")

    confirm_and_submit = input("\nType the field name(s) you'd like to edit, separated by commas, or type 'Confirm & Submit' to continue: ").lower().strip()

    if confirm_and_submit == ("confirm & submit"):
        print("\nWelcome to PRIVÉ, " + name + "!")
        print("Loading...")
        break

