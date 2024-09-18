from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

# Function to test the integration between frontend and backend services
def test_frontend_backend_integration():
    #WebDriver_Setup
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    
    # Define_the_frontend_URL_and_expected_greeting_message
    frontend_url = 'http://127.0.0.1:8080/'
    expected_message = "Hello from the Backend!" 

    try:
        # Navigate_to_the_frontend-URL
        driver.get(frontend_url)
        time.sleep(2)  
        print(driver.page_source)

        # Wait_for_the_<h1>_element_be_visible
        greeting_element = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.TAG_NAME, 'h1'))
        )
        greeting_message = greeting_element.text

        # Assertion_to check_if_the_greeting_message_matches_the_expected_message
        assert greeting_message == expected_message, f"Expected message '{expected_message}', but got '{greeting_message}'"

        print("Test passed: Greeting message is displayed correctly.")

    except AssertionError as e:
        print("Test failed:", e)
    except Exception as e:
        print("An error occurred:", str(e))  
    finally:
        # Close
        driver.quit()

# Run_the_test_function
if __name__ == "__main__":
    test_frontend_backend_integration()
