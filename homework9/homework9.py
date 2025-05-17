import re
def split_email(email):
    # Регулярное выражение для разделения на две части
    pattern = r"([a-zA-Z0-9._%+-]+)@([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})"
    match = re.match(pattern, email)
    
    if match:
        username = match.group(1)
        domain = match.group(2)
        return username, domain
    else:
        return None, None
email = input("Введите email: ")
username, domain = split_email(email)

if username and domain:
    print(f"Username: {username}")
    print(f"Domain: {domain}")
else:
    print("Неверный формат email.")
