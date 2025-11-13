def main():
    email_to_name = {}
    email = input("Email: ").strip()
    while email != "":

        name = extract_name(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()

        if confirmation not in ["", "y", "yes"]:
            name = input("Name: ").strip().title()

        email_to_name[email] = name
        email = input("Email: ").strip()

    # Display stored results
    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def extract_name(email):
    """Extract a formatted name from an email address."""
    prefix = email.split('@')[0]
    parts = prefix.replace('.', ' ').split()
    name = " ".join(parts).title()
    return name