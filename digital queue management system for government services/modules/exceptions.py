"""
Custom Exception classes for the Digital Queue Management System.
Author: Member 1 (OOP Module)

Demonstrates: Inheritance (custom exceptions inherit from Exception),
              polymorphism (each overrides __init__ / message).
"""


class QueueSystemError(Exception):
    """Base exception class for all custom exceptions in this system."""
    pass


class InvalidServiceError(QueueSystemError):
    """Raised when an invalid/unregistered service type is requested."""

    def __init__(self, service_name):
        self.service_name = service_name
        super().__init__(f"Invalid service type: '{service_name}' is not offered at this center.")


class InvalidSubServiceError(QueueSystemError):
    """Raised when an invalid request type (sub-service) is requested under a valid service."""

    def __init__(self, sub_service, service_name):
        self.sub_service = sub_service
        self.service_name = service_name
        super().__init__(f"'{sub_service}' is not a valid request type under '{service_name}'.")


class QueueEmptyError(QueueSystemError):
    """Raised when trying to serve a citizen from an empty queue."""

    def __init__(self, service_name, sub_service=None):
        label = f"{service_name} - {sub_service}" if sub_service else service_name
        super().__init__(f"No citizens waiting in the '{label}' queue.")


class CitizenNotFoundError(QueueSystemError):
    """Raised when a citizen's token number is not found in the system."""

    def __init__(self, token_no):
        super().__init__(f"Citizen with token number '{token_no}' was not found.")


class DuplicateTokenError(QueueSystemError):
    """Raised when a duplicate token number is generated/assigned."""

    def __init__(self, token_no):
        super().__init__(f"Token number '{token_no}' already exists in the system.")


class InvalidInputError(QueueSystemError):
    """Raised when user-provided input fails validation."""
    pass


class ServiceClosedError(QueueSystemError):
    """Raised when a citizen/admin action is attempted outside business hours."""
    pass
