"""
Basic unit tests for the Digital Queue Management System.
Run from the project root with:  python -m unittest discover -s tests -v
"""

import sys
import os
import unittest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from models import GovernmentQueueSystem
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


if __name__ == "__main__":
    unittest.main()
