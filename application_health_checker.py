import requests

# Define the application URL
APP_URL = 'http://127.0.0.1:62123/'  # Replace with your app URL

def check_application_status():
    try:
        response = requests.get(APP_URL)
        if response.status_code == 200:
            print("Application is UP")
        else:
            print(f"Application is DOWN, Status Code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Error checking application status: {e}")

def main():
    check_application_status()

if __name__ == "__main__":
    main()
