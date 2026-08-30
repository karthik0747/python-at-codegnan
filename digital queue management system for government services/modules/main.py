"""
Digital Queue Management System for Government Services
Main entry point - CLI menu.
Author: Member 3 (Functions & Integration Module) - wires all modules together.

Run with:  python main.py   (from inside the src/ folder)
"""

from models import GovernmentQueueSystem
from file_manager import FileManager
from service_hours import BusinessHours
from exceptions import QueueSystemError, InvalidInputError, ServiceClosedError
import utils


def print_menu(business_hours):
    utils.print_divider("=")
    print("   DIGITAL QUEUE MANAGEMENT SYSTEM - GOVERNMENT SERVICES")
    print(f"   {business_hours.status_message()}")
    utils.print_divider("=")
    print("1. Register New Citizen")
    print("2. Serve Next Citizen")
    print("3. View Queue Status (by service + request type)")
    print("4. Search Citizen by Token Number")
    print("5. View All Counters Summary")
    print("6. Export Daily Report")
    print("7. Save & Exit")
    utils.print_divider("=")


def select_service_and_sub(system):
    """Shared helper: prompts for a service, then its request type (sub-service)."""
    service_type = utils.choose_service(list(system.SERVICES.keys()))
    sub_services = system.get_sub_services(service_type)
    sub_service = utils.choose_sub_service(service_type, sub_services)
    return service_type, sub_service


def handle_register(system, file_manager, business_hours):
    try:
        if not business_hours.is_open():
            raise ServiceClosedError(business_hours.status_message())
        name = utils.get_valid_string("Enter citizen name: ")
        age = utils.get_valid_age("Enter age: ")
        contact = utils.get_valid_contact("Enter 10-digit contact number: ")
        service_type, sub_service = select_service_and_sub(system)
        citizen = system.register_citizen(name, age, contact, service_type, sub_service)
        print(f"\n✅ Registration successful! Your token number is: {citizen.token_no}")
        file_manager.log_activity(
            f"Registered citizen {citizen.token_no} for {service_type} - {sub_service}"
        )
    except InvalidInputError as e:
        print(f"\n❌ Input Error: {e}")
    except QueueSystemError as e:
        print(f"\n❌ {e}")


def handle_serve_next(system, file_manager, business_hours):
    try:
        if not business_hours.is_open():
            raise ServiceClosedError(business_hours.status_message())
        service_type, sub_service = select_service_and_sub(system)
        citizen = system.serve_next(service_type, sub_service)
        print(f"\n✅ Now serving: {citizen.display_info()}")
        file_manager.log_activity(
            f"Served citizen {citizen.token_no} at {service_type} - {sub_service}"
        )
    except InvalidInputError as e:
        print(f"\n❌ Input Error: {e}")
    except QueueSystemError as e:
        print(f"\n❌ {e}")


def handle_view_queue(system):
    try:
        service_type, sub_service = select_service_and_sub(system)
        waiting_list = system.get_queue_status(service_type, sub_service)
        print(f"\nQueue for {service_type} - {sub_service}:")
        utils.print_citizen_list(waiting_list)
    except InvalidInputError as e:
        print(f"\n❌ Input Error: {e}")
    except QueueSystemError as e:
        print(f"\n❌ {e}")


def handle_search(system):
    try:
        token_no = utils.get_valid_string("Enter token number: ").upper()
        citizen = system.search_citizen(token_no)
        print(f"\n{citizen.display_info()}")
    except InvalidInputError as e:
        print(f"\n❌ Input Error: {e}")
    except QueueSystemError as e:
        print(f"\n❌ {e}")


def handle_summary(system):
    utils.print_divider()
    print(f"{'Service':<20} | {'Request Type':<25} | {'Waiting':<8} | {'Served'}")
    utils.print_divider()
    for service, sub_service, waiting, served in system.all_counters_summary():
        print(f"{service:<20} | {sub_service:<25} | {waiting:<8} | {served}")
    utils.print_divider()


def handle_export(system, file_manager):
    try:
        path = file_manager.export_report(system)
        print(f"\n✅ Report exported to: {path}")
    except OSError as e:
        print(f"\n❌ Could not export report: {e}")


def main():
    system = GovernmentQueueSystem()
    file_manager = FileManager()
    business_hours = BusinessHours()

    loaded = file_manager.load_all(system)
    if loaded:
        print(f"Loaded {loaded} existing citizen record(s) from previous session.")

    while True:
        print_menu(business_hours)
        choice = input("Enter your choice (1-7): ").strip()

        try:
            if choice == "1":
                handle_register(system, file_manager, business_hours)
            elif choice == "2":
                handle_serve_next(system, file_manager, business_hours)
            elif choice == "3":
                handle_view_queue(system)
            elif choice == "4":
                handle_search(system)
            elif choice == "5":
                handle_summary(system)
            elif choice == "6":
                handle_export(system, file_manager)
            elif choice == "7":
                file_manager.save_all(system.get_all_citizens())
                print("\n✅ Data saved. Goodbye!")
                break
            else:
                print("\n❌ Invalid choice. Please enter a number between 1-7.")
        except KeyboardInterrupt:
            print("\n\nInterrupted. Saving data before exit...")
            file_manager.save_all(system.get_all_citizens())
            break
        except Exception as e:
            print(f"\n❌ Unexpected error occurred: {e}")
            file_manager.log_activity(f"UNEXPECTED ERROR: {e}")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
