Explanation:
Importing Libraries:

requests is used to send HTTP requests.
ThreadPoolExecutor from concurrent.futures is used to handle concurrent execution for faster processing.
Function test_ip(ip):

Tries to send a GET request to the given IP address.
If the request is successful and returns a status code of 200, it prints the IP address.
Catches and ignores any exceptions (e.g., connection errors, timeouts).
Function generate_ip_range(base_ip):

Takes a base IP address as input and generates IP addresses from 0 to 254 in the last octet.
Main Block:

Defines the base IP address.
Generates the range of IP addresses.
Uses ThreadPoolExecutor to test multiple IP addresses concurrently (10 threads in this case).






Running the Script:
To run this script, make sure you have Python installed along with the requests library. If you don't have requests installed, you can install it using pip:

sh
Copy code
pip install requests
Then, save the script to a file (e.g., ip_tester.py) and run it:

sh
Copy code
python ip_tester.py
The script will print the working IP addresses to the terminal.
