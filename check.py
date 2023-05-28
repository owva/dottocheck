import requests

def check_github_username_availability(username):
    url = f"https://github.com/{username}"
    response = requests.get(url)

    if response.status_code == 200 and "manifest.json" in response.text:
        return False  # Username is taken
    else:
        return True  # Username is available

# Example usage: Check availability of a GitHub username
username = "livyork"
is_available = check_github_username_availability(username)

# Visual output
if is_available:
    print(f"The GitHub username '{username}' is available.")
else:
    print(f"The GitHub username '{username}' is not available.")