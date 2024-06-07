import random


def generate_emails(domain="gmail.com", username="paramonov"):
    random_number = random.randint(0, 9999)
    login = f'{username}{random_number}'
    email = f'{login}@{domain}'
    return email