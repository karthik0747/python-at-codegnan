MEMBER 3 — FUNCTIONS & INTEGRATION MODULE (UPDATED)
======================================================

Files in this folder:
  - utils.py
  - main.py
  - tests/test_queue.py

WHAT CHANGED:
  - New function in utils.py: choose_sub_service() — shows the list of
    request types under whichever service was picked (e.g. under Aadhar
    Card: New Enrollment, Date of Birth Update, Address Update, ...).
  - main.py: every menu action (register, serve, view queue) now asks
    for the request type after the service, via a shared helper
    select_service_and_sub(). The summary screen shows one row per
    service + request type.
  - tests/test_queue.py: updated to call register_citizen(...) with the
    new sub_service argument, checks the new token format
    (e.g. "PA-NEW-0001", "AC-DOB-0001"), and adds a test confirming
    different request types under the same service get independent
    queues.

What to do:
1. Replace the old utils.py and main.py inside src/, and test_queue.py
   inside tests/, with these updated versions.
2. In your terminal:
     git checkout -b feature/functions-integration
     git add src/utils.py src/main.py tests/test_queue.py
     git commit -m "Add request-type selection to CLI flow and update tests for sub-services"
     git push origin feature/functions-integration
3. Open a Pull Request on GitHub: base = main, compare = feature/functions-integration.
4. Tag a teammate to review, then merge once approved.

To run:              cd src && python main.py
To run the tests:    python -m unittest discover -s tests -v   (from project root)
