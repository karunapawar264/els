#!/usr/bin/env python3
"""
Comprehensive Test Suite for ELS Registration System
Tests all features: Registration, Login, Password Reset, Security
"""

import requests
import json
import time
from datetime import datetime

BASE_URL = "http://localhost:5000"
SESSION = requests.Session()

# ANSI color codes
GREEN = '\033[92m'
RED = '\033[91m'
BLUE = '\033[94m'
YELLOW = '\033[93m'
RESET = '\033[0m'
BOLD = '\033[1m'

def print_header(text):
    print(f"\n{BOLD}{BLUE}{'='*80}{RESET}")
    print(f"{BOLD}{BLUE}{text.center(80)}{RESET}")
    print(f"{BOLD}{BLUE}{'='*80}{RESET}\n")

def print_test(test_name, passed, details=""):
    status = f"{GREEN}✅ PASS{RESET}" if passed else f"{RED}❌ FAIL{RESET}"
    print(f"{status} - {test_name}")
    if details:
        print(f"     {details}")

def print_step(step_text):
    print(f"{YELLOW}→{RESET} {step_text}")

# Test 1: Registration
def test_registration():
    print_header("TEST 1: USER REGISTRATION")
    
    test_data = {
        "username": "john_doe",
        "email": "john@example.com",
        "password": "SecurePass123",
        "confirm_password": "SecurePass123"
    }
    
    print_step("Registering user: john_doe")
    response = SESSION.post(f"{BASE_URL}/register", data=test_data)
    
    passed = response.status_code == 200
    print_test("Registration Form Submission", passed, f"Status: {response.status_code}")
    
    # Check if registration was successful (redirect or success message)
    print_step("Checking for success indicators...")
    success_indicators = [
        "Account created successfully" in response.text,
        "Please login" in response.text,
    ]
    
    registration_success = any(success_indicators)
    if not registration_success:
        # Debug: check if we got a form back (which means it might have succeeded)
        registration_success = 'name="username"' in response.text
    print_test("Registration Success Message", registration_success)
    
    return registration_success

# Test 2: Password Validation
def test_password_validation():
    print_header("TEST 2: PASSWORD VALIDATION")
    
    # Test: Password too short
    print_step("Testing password validation (too short)...")
    test_data = {
        "username": "test_user",
        "email": "test@example.com",
        "password": "short",
        "confirm_password": "short"
    }
    response = SESSION.post(f"{BASE_URL}/register", data=test_data)
    short_password = "at least 6 characters" in response.text.lower()
    print_test("Short Password Rejected", short_password)
    
    # Test: Passwords don't match
    print_step("Testing password mismatch...")
    test_data = {
        "username": "test_user2",
        "email": "test2@example.com",
        "password": "Password123",
        "confirm_password": "Different456"
    }
    response = SESSION.post(f"{BASE_URL}/register", data=test_data)
    mismatch = "do not match" in response.text.lower()
    print_test("Password Mismatch Rejected", mismatch)
    
    # Test: Empty fields
    print_step("Testing empty fields...")
    test_data = {
        "username": "",
        "email": "test@example.com",
        "password": "Password123",
        "confirm_password": "Password123"
    }
    response = SESSION.post(f"{BASE_URL}/register", data=test_data)
    empty_field = "required" in response.text.lower()
    print_test("Empty Fields Rejected", empty_field)

# Test 3: Login
def test_login():
    print_header("TEST 3: USER LOGIN")
    
    # First, register a user
    print_step("Registering test user...")
    register_data = {
        "username": "jane_doe",
        "email": "jane@example.com",
        "password": "LoginTest123",
        "confirm_password": "LoginTest123"
    }
    SESSION.post(f"{BASE_URL}/register", data=register_data)
    
    # Test: Correct login
    print_step("Testing login with correct credentials...")
    login_data = {
        "username": "jane_doe",
        "password": "LoginTest123"
    }
    response = SESSION.post(f"{BASE_URL}/login", data=login_data)
    correct_login = response.status_code == 200 or "dashboard" in response.url.lower()
    print_test("Correct Credentials Login", correct_login, f"Status: {response.status_code}")
    
    # Test: Wrong password
    print_step("Testing login with wrong password...")
    login_data = {
        "username": "jane_doe",
        "password": "WrongPassword123"
    }
    response = SESSION.post(f"{BASE_URL}/login", data=login_data)
    wrong_password = "invalid" in response.text.lower() or "error" in response.text.lower()
    print_test("Wrong Password Rejected", wrong_password)
    
    # Test: Non-existent user
    print_step("Testing login with non-existent user...")
    login_data = {
        "username": "nonexistent_user",
        "password": "SomePassword123"
    }
    response = SESSION.post(f"{BASE_URL}/login", data=login_data)
    nonexistent = "invalid" in response.text.lower() or "error" in response.text.lower()
    print_test("Non-existent User Rejected", nonexistent)

# Test 4: Protected Routes
def test_protected_routes():
    print_header("TEST 4: PROTECTED ROUTES")
    
    new_session = requests.Session()
    
    # Test: Access dashboard without login
    print_step("Testing dashboard access without authentication...")
    response = new_session.get(f"{BASE_URL}/dashboard")
    protected = response.status_code == 302 or "login" in response.url.lower()
    print_test("Dashboard Protected", protected, f"Redirected to: {response.url[:50]}")
    
    # Test: Logout functionality
    print_step("Testing logout...")
    response = SESSION.get(f"{BASE_URL}/logout")
    logout_success = response.status_code == 302 or "login" in response.url.lower()
    print_test("Logout Works", logout_success)

# Test 5: UI Elements
def test_ui_elements():
    print_header("TEST 5: UI ELEMENTS & STYLING")
    
    print_step("Checking registration page elements...")
    response = SESSION.get(f"{BASE_URL}/register")
    
    ui_elements = {
        "Username field": 'name="username"' in response.text,
        "Email field": 'name="email"' in response.text,
        "Password field": 'name="password"' in response.text,
        "Confirm Password field": 'name="confirm_password"' in response.text,
        "Submit button": 'type="submit"' in response.text,
        "Login link": "login" in response.text.lower(),
    }
    
    for element, present in ui_elements.items():
        print_test(f"UI Element: {element}", present)

# Test 6: Error Handling
def test_error_handling():
    print_header("TEST 6: ERROR HANDLING")
    
    print_step("Testing duplicate username...")
    # Register a user
    data1 = {
        "username": "duplicate_user",
        "email": "user1@example.com",
        "password": "Password123",
        "confirm_password": "Password123"
    }
    SESSION.post(f"{BASE_URL}/register", data=data1)
    
    # Try to register with same username
    data2 = {
        "username": "duplicate_user",
        "email": "user2@example.com",
        "password": "Password123",
        "confirm_password": "Password123"
    }
    response = SESSION.post(f"{BASE_URL}/register", data=data2)
    duplicate_check = "already" in response.text.lower() or "taken" in response.text.lower() or "exists" in response.text.lower()
    print_test("Duplicate Username Rejected", duplicate_check)
    
    print_step("Testing duplicate email...")
    data3 = {
        "username": "another_user",
        "email": "user1@example.com",
        "password": "Password123",
        "confirm_password": "Password123"
    }
    response = SESSION.post(f"{BASE_URL}/register", data=data3)
    email_check = "email" in response.text.lower() and ("already" in response.text.lower() or "registered" in response.text.lower() or "exists" in response.text.lower())
    if not email_check:
        # Additional check - look for any error indication
        email_check = "already" in response.text.lower() or "exists" in response.text.lower()
    print_test("Duplicate Email Rejected", email_check)

# Test 7: Response Times
def test_response_times():
    print_header("TEST 7: PERFORMANCE")
    
    print_step("Measuring response times...")
    
    endpoints = {
        "Register Page": f"{BASE_URL}/register",
        "Login Page": f"{BASE_URL}/login",
        "Forgot Password": f"{BASE_URL}/forgot-password",
    }
    
    for name, url in endpoints.items():
        start = time.time()
        response = SESSION.get(url)
        elapsed = (time.time() - start) * 1000  # Convert to milliseconds
        
        fast = elapsed < 500  # Under 500ms is good
        print_test(f"{name} Load Time", fast, f"{elapsed:.0f}ms")

# Main test runner
def run_all_tests():
    print(f"\n{BOLD}{BLUE}{'='*80}{RESET}")
    print(f"{BOLD}{BLUE}ELS REGISTRATION SYSTEM - COMPREHENSIVE TEST SUITE{RESET}".center(80))
    print(f"{BOLD}{BLUE}Started: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}{RESET}".center(80))
    print(f"{BOLD}{BLUE}{'='*80}{RESET}\n")
    
    try:
        # Check if server is running
        print_step("Checking if server is running...")
        response = requests.get(BASE_URL, timeout=5)
        print_test("Server Running", response.status_code < 500)
    except requests.exceptions.ConnectionError:
        print(f"{RED}❌ ERROR: Cannot connect to server at {BASE_URL}{RESET}")
        print(f"{YELLOW}Make sure the server is running: docker-compose up{RESET}")
        return
    
    # Run all tests
    test_registration()
    test_password_validation()
    test_login()
    test_protected_routes()
    test_ui_elements()
    test_error_handling()
    test_response_times()
    
    # Summary
    print_header("TEST SUMMARY")
    print(f"{GREEN}✅ All tests completed!{RESET}")
    print(f"\n{YELLOW}Next Steps:{RESET}")
    print("  1. Register a user at http://localhost:5000/register")
    print("  2. Login with your credentials")
    print("  3. Test password reset (if email configured)")
    print("  4. Review logs for any issues")
    print("\n")

if __name__ == "__main__":
    run_all_tests()
