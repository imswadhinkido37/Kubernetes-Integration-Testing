# Kubernetes-Integration-Testing
## QA Automation Testing

# # Problem Statement 1: QA Integration Testing for Frontend and Backend Services

## Overview

This repository contains a comprehensive QA testing setup for verifying the integration between a frontend and backend service. The objective of this task was to ensure that the frontend can successfully communicate with the backend, returning the expected results when the user interacts with the application.

## Technologies Used

- **Kubernetes**: For container orchestration.
- **Docker**: To containerize the application components.
- **Selenium**: For automating browser interactions and testing the integration.
- **Python**: The primary programming language used for writing the test scripts.
- **Webdriver Manager**: For managing the browser driver binaries automatically.
  
## Setup Instructions

### Prerequisites

1. **Docker**: Ensure Docker is installed and running on your machine.
2. **Kubernetes**: Install and configure Minikube or another Kubernetes setup.
3. **Python**: Install Python 3.x on your system.
4. **Selenium**: Install the Selenium package via pip:
   ```bash
   pip install selenium webdriver-manager
   ```

### Deployment

1. **Deploy the Application**: 
   - Clone the repository containing your application code.
   - Deploy the backend and frontend services on Kubernetes:
     ```bash
     kubectl apply -f deployment.yaml
     ```
2. **Verify Pods and Services**:
   - Check that the pods are running:
     ```bash
     kubectl get pods
     ```
   - Check that the services are created:
     ```bash
     kubectl get services
     ```

3. **Port Forwarding**:
   - Use port forwarding to access the frontend service locally:
     ```bash
     kubectl port-forward service/frontend-service 8080:80
     ```

## Testing

### Test Script

The integration test is defined in the `test_script.py` file. The script performs the following actions:

1. Sets up the Selenium WebDriver to launch a Chrome browser.
2. Navigates to the local URL of the frontend service.
3. Waits for the page to load.
4. Locates the element that displays a greeting message.
5. Compares the actual message with the expected message.
6. Outputs whether the test passed or failed.

### Running the Test

To execute the test script, run the following command in your terminal:

```bash
python test_script.py
```

If the test is successful, you will see a confirmation message indicating that the greeting message is displayed correctly. If any assertion fails, an error message will be printed detailing the mismatch.

## Results

During the testing process, the following was observed:

- The application returned the expected greeting message, confirming successful integration between the frontend and backend services.
- All test assertions passed without any errors, demonstrating the reliability of the communication between components.


# Problem Statement 2: QA Automation Scripts

This project includes three scripts aimed at monitoring and analyzing system performance and application health. The scripts developed are:

1. **System Health Monitoring Script**
2. **Log File Analyzer**
3. **Application Health Checker**

### 1. System Health Monitoring Script

This Python script monitors the health of a Linux system by checking CPU usage, memory usage, disk space, and running processes. If any of these metrics exceed predefined thresholds (e.g., CPU usage > 80%), the script sends an alert to the console and logs the information.

#### Key Features:
- Monitors CPU usage and logs warnings if usage exceeds 80%.
- Checks memory usage and logs warnings for high memory consumption.
- Lists the number of running processes and logs this information.

### 2. Log File Analyzer

This Python script analyzes web server logs (e.g., Apache, Nginx) for common patterns. It identifies the number of `404` errors, the most requested pages, and the IP addresses with the most requests.

#### How to Test:
As there wasn’t a log file available, you can create a sample log file to test this script. Follow these steps:

1. Open a text editor (like Notepad).
2. Copy and paste the following sample log entries into the editor:

   ```
   127.0.0.1 - - [24/Apr/2023:13:26:29 +0000] "GET /index.html HTTP/1.1" 200 2326
   127.0.0.1 - - [24/Apr/2023:13:26:30 +0000] "GET /about.html HTTP/1.1" 404 732
   127.0.0.1 - - [24/Apr/2023:13:26:31 +0000] "GET /index.html HTTP/1.1" 200 2326
   192.168.1.1 - - [24/Apr/2023:13:26:32 +0000] "GET /index.html HTTP/1.1" 200 2326
   ```

3. Save the file as `access.log` in the `C:\Users\Avi00\Desktop\QA` directory.

### 3. Application Health Checker

This script checks the uptime of a specified application by sending HTTP requests and analyzing the response status codes. It determines if the application is 'up' (functioning correctly) or 'down' (unavailable).

**Note**: This script is working, but I had to forward the URL for testing purposes, so I couldn't attach the results here.

### Conclusion

The scripts provide valuable tools for monitoring system health and analyzing web server logs, contributing to improved performance and reliability in software applications. Additionally, the integration testing task has been successfully completed, with the frontend application correctly receiving data from the backend service as verified by the Selenium automation tests. Further enhancements can be made by adding more test cases and edge scenarios to ensure comprehensive coverage. Feel free to explore and modify the scripts to fit your specific needs!


imswadhinkido37

