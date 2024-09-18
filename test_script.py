from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to test the integration between frontend and backend services
def test_frontend_backend_integration():
    # Set up the WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Define the frontend URL and expected greeting message
    frontend_url = 'http://127.0.0.1:8080/'
    expected_message = "Hello from the Backend!"  # Update this to match the actual message displayed

    try:
        # Navigate to the frontend URL
        driver.get(frontend_url)
        
        # Optional: wait a moment for the page to load
        time.sleep(2)  
        
        # Print page source for debugging
        print(driver.page_source)

        # Wait for the <h1> element to be visible and locate it
        greeting_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
        )
        greeting_message = greeting_element.text

        # Assertion to check if the greeting message matches the expected message
        assert greeting_message == expected_message, f"Expected message '{expected_message}', but got '{greeting_message}'"

        print("Test passed: Greeting message is displayed correctly.")

    except AssertionError as e:
        print("Test failed:", e)
    except Exception as e:
        print("An error occurred:", str(e))  # More informative error output
    finally:
        # Close the WebDriver
        driver.quit()

# Run the test function
if __name__ == "__main__":
    test_frontend_backend_integration()
