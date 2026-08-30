"""
Utility / helper functions for the Digital Queue Management System.
Author: Member 3 (Functions & Integration Module)

Pure, reusable functions for input validation and console formatting.
"""

from exceptions import InvalidInputError


def get_valid_string(prompt, allow_empty=False):
    value = input(prompt).strip()
    if not value and not allow_empty:
        raise InvalidInputError("This field cannot be empty.")
    return value


def get_valid_age(prompt):
    value = input(prompt).strip()
    try:
        age = int(value)
    except ValueError:
        raise InvalidInputError("Age must be a whole number.")
    if age <= 0 or age > 120:
        raise InvalidInputError("Age must be between 1 and 120.")
    return age


def get_valid_contact(prompt):
    value = input(prompt).strip()
    if not (value.isdigit() and len(value) == 10):
        raise InvalidInputError("Contact number must be exactly 10 digits.")
    return value


def choose_service(valid_services):
    print("\nAvailable Services:")
    for i, service in enumerate(valid_services, start=1):
        print(f"  {i}. {service}")
    choice = input("Choose a service (enter number): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(valid_services)):
        raise InvalidInputError("Invalid service selection.")
    return valid_services[int(choice) - 1]


def choose_sub_service(service_type, sub_services):
    print(f"\nRequest types under {service_type}:")
    for i, name in enumerate(sub_services, start=1):
        print(f"  {i}. {name}")
    choice = input("Choose a request type (enter number): ").strip()
    if not choice.isdigit() or not (1 <= int(choice) <= len(sub_services)):
        raise InvalidInputError("Invalid request type selection.")
    return sub_services[int(choice) - 1]


def print_divider(char="-", length=60):
    print(char * length)


def print_citizen_list(citizens):
    if not citizens:
        print("  (No citizens in this queue)")
        return
    for idx, citizen in enumerate(citizens, start=1):
        print(f"  {idx}. {citizen.display_info()}")
