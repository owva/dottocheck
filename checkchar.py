import requests
import random
import string

def check_github_username_availability(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)

    if response.status_code == 200 and "manifest.json" in response.text:
        return False  # Username is taken
    else:
        return True  # Username is available

# Prompt user for input
character_length = int(input("Enter the character length: "))

# Generate and check usernames
available_usernames = []
while len(available_usernames) < 10 ** character_length:
    username = ''.join(random.choice(string.ascii_letters) for _ in range(character_length))
    is_available = check_github_username_availability(username)
    print(f"Generated: {username} - Available: {is_available}")
    if is_available:
        available_usernames.append(username)

# Visual output
print(f"Available GitHub usernames with {character_length} characters:") 
print(available_usernames) 