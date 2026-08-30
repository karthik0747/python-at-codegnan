"""
Basic unit tests for the Digital Queue Management System.
Run from the project root with:  python -m unittest discover -s tests -v
"""

import sys
import os
import unittest
from datetime import datetime

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from models import GovernmentQueueSystem
from service_hours import BusinessHours
from exceptions import (
    InvalidServiceError, InvalidSubServiceError,
    QueueEmptyError, CitizenNotFoundError
)


class TestGovernmentQueueSystem(unittest.TestCase):

    def setUp(self):
        self.system = GovernmentQueueSystem()

    def test_register_citizen_success(self):
        citizen = self.system.register_citizen(
            "Ravi Kumar", 34, "9876543210", "Passport", "New Passport Application"
        )
        self.assertEqual(citizen.status, "WAITING")
        self.assertTrue(citizen.token_no.startswith("PA-NEW-"))

    def test_register_invalid_service_raises(self):
        with self.assertRaises(InvalidServiceError):
            self.system.register_citizen("Ravi", 34, "9876543210", "Voter ID", "New")

    def test_register_invalid_sub_service_raises(self):
        with self.assertRaises(InvalidSubServiceError):
            self.system.register_citizen(
                "Ravi", 34, "9876543210", "Passport", "Nonexistent Request Type"
            )

    def test_aadhar_dob_update_token_format(self):
        citizen = self.system.register_citizen(
            "Anita Sharma", 28, "9123456789", "Aadhar Card", "Date of Birth Update"
        )
        self.assertTrue(citizen.token_no.startswith("AC-DOB-"))

    def test_serve_next_empty_queue_raises(self):
        with self.assertRaises(QueueEmptyError):
            self.system.serve_next("Passport", "New Passport Application")

    def test_serve_next_success(self):
        self.system.register_citizen(
            "Ravi Kumar", 34, "9876543210", "Passport", "New Passport Application"
        )
        citizen = self.system.serve_next("Passport", "New Passport Application")
        self.assertEqual(citizen.status, "SERVED")

    def test_search_missing_citizen_raises(self):
        with self.assertRaises(CitizenNotFoundError):
            self.system.search_citizen("XX-XXX-9999")

    def test_search_found_citizen(self):
        registered = self.system.register_citizen(
            "Anita", 28, "9123456789", "Aadhar Card", "Date of Birth Update"
        )
        found = self.system.search_citizen(registered.token_no)
        self.assertEqual(found.name, "Anita")

    def test_separate_queues_per_sub_service(self):
        # DOB Update and Address Update under the same service must be independent queues
        self.system.register_citizen("A", 30, "9000000001", "Aadhar Card", "Date of Birth Update")
        self.system.register_citizen("B", 31, "9000000002", "Aadhar Card", "Address Update")
        dob_queue = self.system.get_queue_status("Aadhar Card", "Date of Birth Update")
        address_queue = self.system.get_queue_status("Aadhar Card", "Address Update")
        self.assertEqual(len(dob_queue), 1)
        self.assertEqual(len(address_queue), 1)
        self.assertEqual(dob_queue[0].name, "A")
        self.assertEqual(address_queue[0].name, "B")


class TestBusinessHours(unittest.TestCase):

    def setUp(self):
        # a throwaway holidays file so tests don't depend on the real data/holidays.txt
        self.holidays_path = "/tmp/_test_holidays.txt"
        with open(self.holidays_path, "w", encoding="utf-8") as f:
            f.write("2026-10-02|Gandhi Jayanti\n")
        self.bh = BusinessHours(holidays_file=self.holidays_path)

    def tearDown(self):
        if os.path.exists(self.holidays_path):
            os.remove(self.holidays_path)

    def test_open_on_weekday_during_hours(self):
        monday_10am = datetime(2026, 8, 31, 10, 0)   # a Monday
        self.assertTrue(self.bh.is_open(monday_10am))

    def test_closed_before_opening(self):
        monday_7am = datetime(2026, 8, 31, 7, 0)
        self.assertFalse(self.bh.is_open(monday_7am))

    def test_closed_after_closing(self):
        monday_7pm = datetime(2026, 8, 31, 19, 0)
        self.assertFalse(self.bh.is_open(monday_7pm))

    def test_closed_on_saturday(self):
        saturday = datetime(2026, 9, 5, 12, 0)
        self.assertFalse(self.bh.is_open(saturday))

    def test_closed_on_sunday(self):
        sunday = datetime(2026, 9, 6, 12, 0)
        self.assertFalse(self.bh.is_open(sunday))

    def test_closed_on_public_holiday(self):
        holiday = datetime(2026, 10, 2, 12, 0)   # Friday, Gandhi Jayanti
        self.assertFalse(self.bh.is_open(holiday))


if __name__ == "__main__":
    unittest.main()
