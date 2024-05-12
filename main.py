import requests
import json

# Constants
BASE_URL = "https://api.spacetraders.io"

# Helper function to make API requests
def make_request(endpoint, method="GET", data=None):
    with open("agent.json") as f:
        config = json.load(f)
    headers = {"Authorization": f"Bearer {config['token']}"}
    print("This is the header: ")
    print(headers)
    
    url = f"{BASE_URL}/{endpoint}"
    response = requests.get("https://api.spacetraders.io/v2/my/agent", headers=headers)
    print("This is response ", response)

    return response.json()


# Example function to get user's account information
def get_account_info():
    with open("agent.json") as f:
        config = json.load(f)
    response = make_request(f"v2/my/agent/{config['token']}")
    return response

# Main function
def main():
    # Get user's account information
    
    account_info = get_account_info()
    print("Account Information:")
    print(account_info)


if __name__ == "__main__":
    main()
