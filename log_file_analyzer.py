import re
from collections import Counter

# Define a function to analyze the log file
def analyze_log(file_path):
    with open(file_path, 'r') as file:
        logs = file.readlines()

    # Initialize counters
    error_count = 0
    page_count = Counter()
    ip_count = Counter()

    for log in logs:
        # Example log format: '127.0.0.1 - - [24/Apr/2023:13:26:29 +0000] "GET /index.html HTTP/1.1" 200 2326'
        match = re.match(r'(\S+) - - \[\S+ \+\d+\] "GET (\S+) HTTP/\S+" (\d+)', log)

        if match:
            ip, page, status = match.groups()
            # Count 404 errors
            if status == '404':
                error_count += 1
            # Count page requests
            page_count[page] += 1
            # Count IP addresses
            ip_count[ip] += 1

    # Generate report
    print(f"Total 404 Errors: {error_count}")
    print("Most Requested Pages:")
    for page, count in page_count.most_common(5):
        print(f"  {page}: {count} times")
    print("IP Addresses with Most Requests:")
    for ip, count in ip_count.most_common(5):
        print(f"  {ip}: {count} requests")

# Example usage
if __name__ == "__main__":
    log_file_path = 'C:\\Users\\Avi00\\Desktop\\QA\\access.log'  # Replace with your log file path
    analyze_log(log_file_path)
