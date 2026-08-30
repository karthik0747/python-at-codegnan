"""
Core OOP models for the Digital Queue Management System.
Author: Member 1 (OOP Module)

Each government service (Passport, Aadhar Card, etc.) now has multiple
REQUEST TYPES / sub-services (e.g. Aadhar Card -> Date of Birth Update,
Address Update, Name Correction ...). Each request type has its own
queue and its own token sequence, e.g.:

    Aadhar Card -> Date of Birth Update  -> tokens AC-DOB-0001, AC-DOB-0002 ...
    Passport    -> Passport Renewal      -> tokens PA-REN-0001, PA-REN-0002 ...

Demonstrates: Encapsulation, Inheritance, Abstraction, Polymorphism,
              composition (GovernmentQueueSystem is built from SubServiceCounters).
"""

from datetime import datetime
from abc import ABC, abstractmethod

from exceptions import (
    InvalidServiceError, InvalidSubServiceError, QueueEmptyError,
    CitizenNotFoundError, DuplicateTokenError
)


class Person(ABC):
    """Abstract base class demonstrating abstraction."""

    def __init__(self, name, age, contact):
        self._name = name
        self._age = age
        self._contact = contact

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @abstractmethod
    def display_info(self):
        """Every subclass must define how it presents itself."""
        pass


class Citizen(Person):
    """Represents a citizen waiting in a government service queue."""

    def __init__(self, name, age, contact, service_type, sub_service, token_no):
        super().__init__(name, age, contact)
        self.service_type = service_type
        self.sub_service = sub_service
        self.token_no = token_no
        self.status = "WAITING"            # WAITING, SERVED
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.served_time = None

    def mark_served(self):
        self.status = "SERVED"
        self.served_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def display_info(self):
        return (f"Token: {self.token_no} | Name: {self._name} | Age: {self._age} | "
                f"Service: {self.service_type} ({self.sub_service}) | Status: {self.status} | "
                f"Registered: {self.timestamp}")

    def to_record(self):
        """Convert citizen object to a pipe-separated line for file storage."""
        return "|".join([
            self.token_no, self._name, str(self._age), self._contact,
            self.service_type, self.sub_service, self.status, self.timestamp,
            self.served_time if self.served_time else "NA"
        ])

    @staticmethod
    def from_record(record_line):
        """Recreate a Citizen object from a stored file record (factory method)."""
        parts = record_line.strip().split("|")
        if len(parts) != 9:
            raise ValueError("Corrupted citizen record in data file.")
        (token_no, name, age, contact, service_type, sub_service,
         status, timestamp, served_time) = parts
        citizen = Citizen(name, int(age), contact, service_type, sub_service, token_no)
        citizen.status = status
        citizen.timestamp = timestamp
        citizen.served_time = None if served_time == "NA" else served_time
        return citizen

    def __str__(self):
        return self.display_info()


class SubServiceCounter:
    """
    Represents ONE specific request-type queue,
    e.g. "Aadhar Card -> Date of Birth Update".
    """

    def __init__(self, service_type, sub_service, abbrev):
        self.service_type = service_type
        self.sub_service = sub_service
        self.abbrev = abbrev
        self._queue = []            # FIFO queue for this specific request type
        self.total_served = 0

    def enqueue(self, citizen):
        self._queue.append(citizen)

    def dequeue(self):
        if not self._queue:
            raise QueueEmptyError(self.service_type, self.sub_service)
        citizen = self._queue.pop(0)
        citizen.mark_served()
        self.total_served += 1
        return citizen

    def queue_length(self):
        return len(self._queue)

    def get_waiting_list(self):
        return list(self._queue)


class GovernmentQueueSystem:
    """
    Central controller class - composed of many SubServiceCounters,
    grouped under their parent service.
    """

    # service_name -> list of (request_type_name, token_abbreviation)
    SERVICES = {
        "Passport": [
            ("New Passport Application", "NEW"),
            ("Passport Renewal", "REN"),
            ("Reissue - Lost or Damaged", "RIS"),
            ("Address Change", "ADR"),
        ],
        "Driving License": [
            ("New License", "NEW"),
            ("License Renewal", "REN"),
            ("Duplicate License", "DUP"),
            ("Address Update", "ADR"),
        ],
        "Aadhar Card": [
            ("New Enrollment", "NEW"),
            ("Date of Birth Update", "DOB"),
            ("Address Update", "ADR"),
            ("Name Correction", "NAME"),
            ("Mobile Number Update", "MOB"),
            ("Photo Update", "PHO"),
        ],
        "Birth Certificate": [
            ("New Registration", "NEW"),
            ("Correction", "COR"),
            ("Duplicate Copy", "DUP"),
        ],
        "Income Certificate": [
            ("New Application", "NEW"),
            ("Certificate Renewal", "REN"),
            ("Correction", "COR"),
        ],
    }

    # short prefix used at the front of every token for this service
    SERVICE_PREFIXES = {
        "Passport": "PA",
        "Driving License": "DL",
        "Aadhar Card": "AC",
        "Birth Certificate": "BC",
        "Income Certificate": "IC",
    }

    def __init__(self):
        # nested structure: { service_name: { sub_service_name: SubServiceCounter } }
        self._counters = {
            service: {
                sub_name: SubServiceCounter(service, sub_name, abbrev)
                for sub_name, abbrev in sub_list
            }
            for service, sub_list in self.SERVICES.items()
        }
        self._all_citizens = {}                 # token_no -> Citizen (O(1) lookup)
        self._token_counters = {}                # (service, sub_service) -> running int

    # ---------- lookups / validation ----------

    def get_sub_services(self, service_type):
        if service_type not in self.SERVICES:
            raise InvalidServiceError(service_type)
        return [name for name, _ in self.SERVICES[service_type]]

    def _get_abbrev(self, service_type, sub_service):
        for name, abbrev in self.SERVICES[service_type]:
            if name == sub_service:
                return abbrev
        raise InvalidSubServiceError(sub_service, service_type)

    def _validate(self, service_type, sub_service):
        if service_type not in self._counters:
            raise InvalidServiceError(service_type)
        if sub_service not in self._counters[service_type]:
            raise InvalidSubServiceError(sub_service, service_type)

    # ---------- token generation ----------

    def generate_token(self, service_type, sub_service):
        prefix = self.SERVICE_PREFIXES.get(service_type, service_type[:2].upper())
        abbrev = self._get_abbrev(service_type, sub_service)
        key = (service_type, sub_service)
        self._token_counters[key] = self._token_counters.get(key, 0) + 1
        token_no = f"{prefix}-{abbrev}-{self._token_counters[key]:04d}"
        if token_no in self._all_citizens:
            raise DuplicateTokenError(token_no)
        return token_no

    # ---------- core operations ----------

    def register_citizen(self, name, age, contact, service_type, sub_service):
        self._validate(service_type, sub_service)
        token_no = self.generate_token(service_type, sub_service)
        citizen = Citizen(name, age, contact, service_type, sub_service, token_no)
        self._counters[service_type][sub_service].enqueue(citizen)
        self._all_citizens[token_no] = citizen
        return citizen

    def serve_next(self, service_type, sub_service):
        self._validate(service_type, sub_service)
        return self._counters[service_type][sub_service].dequeue()

    def get_queue_status(self, service_type, sub_service):
        self._validate(service_type, sub_service)
        return self._counters[service_type][sub_service].get_waiting_list()

    def search_citizen(self, token_no):
        if token_no not in self._all_citizens:
            raise CitizenNotFoundError(token_no)
        return self._all_citizens[token_no]

    def all_counters_summary(self):
        """Returns a flat list of (service, sub_service, waiting, served) tuples."""
        summary = []
        for service, sub_counters in self._counters.items():
            for sub_service, counter in sub_counters.items():
                summary.append((service, sub_service, counter.queue_length(), counter.total_served))
        return summary

    def get_all_citizens(self):
        return self._all_citizens

    def restore_citizen(self, citizen):
        """Used while loading saved data back into memory at startup."""
        self._all_citizens[citizen.token_no] = citizen
        service, sub_service = citizen.service_type, citizen.sub_service
        if service in self._counters and sub_service in self._counters[service]:
            if citizen.status == "WAITING":
                self._counters[service][sub_service].enqueue(citizen)
            else:
                self._counters[service][sub_service].total_served += 1
        # keep the token counter in sync so newly generated tokens never collide
        key = (service, sub_service)
        num_part = citizen.token_no.split("-")[-1]
        if num_part.isdigit():
            self._token_counters[key] = max(self._token_counters.get(key, 0), int(num_part))
