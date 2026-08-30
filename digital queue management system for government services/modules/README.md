# 🏛️ Digital Queue Management System for Government Services

A console-based Python application that digitizes token/queue management
across multiple government service counters (Passport, Driving License,
Aadhar Card, Birth Certificate, Income Certificate).

Each service is further split into **request types** (sub-services), just
like a real government office — e.g. under **Aadhar Card**: New Enrollment,
Date of Birth Update, Address Update, Name Correction, Mobile Number
Update, Photo Update. Each request type has its **own independent queue**
and its **own token sequence**, e.g.:

```
Aadhar Card -> Date of Birth Update   -> tokens AC-DOB-0001, AC-DOB-0002 ...
Aadhar Card -> Address Update         -> tokens AC-ADR-0001, AC-ADR-0002 ...
Passport    -> Passport Renewal       -> tokens PA-REN-0001, PA-REN-0002 ...
```

Built as a 3-member team project to demonstrate:
- ✅ **Object-Oriented Programming** — encapsulation, inheritance, abstraction, polymorphism
- ✅ **Exception Handling** — custom exception hierarchy + built-in exceptions
- ✅ **File Handling** — persistent storage, activity logs, report export
- ✅ **Functions** — clean, reusable, single-purpose helper functions

---

## 📁 Project Structure

```
queue_management_system/
├── README.md
├── requirements.txt
├── .gitignore
├── GITHUB_SETUP_GUIDE.md
├── data/                     # created automatically at runtime
│   ├── holidays.txt          # public holiday calendar (edit this file to update)
│   ├── citizens.txt          # persisted queue data
│   ├── logs.txt              # activity log
│   └── daily_report.txt      # generated report
├── src/
│   ├── exceptions.py         # custom exception classes
│   ├── models.py             # OOP classes (Citizen, ServiceCounter, GovernmentQueueSystem)
│   ├── file_manager.py       # all file I/O + exception handling
│   ├── service_hours.py      # business-hours check (Mon-Fri 8AM-6PM, holidays from file)
│   ├── utils.py              # input validation & display helper functions
│   └── main.py                # CLI menu / entry point
└── tests/
    └── test_queue.py          # unit tests
```

## 👥 Team Member Responsibilities (for GitHub commit history)

| Member | Module(s) | Focus |
|---|---|---|
| **Member 1** | `exceptions.py`, `models.py` | OOP design — classes, inheritance, abstraction |
| **Member 2** | `file_manager.py`, `service_hours.py`, `data/holidays.txt` | File handling — save/load/log, and business-hours logic driven by a data file |
| **Member 3** | `utils.py`, `main.py`, `tests/` | Functions, input validation, CLI integration, testing |

Each member should work on their own **feature branch** and merge via
Pull Request — see `GITHUB_SETUP_GUIDE.md` for the exact commands.

## ⚙️ How to Run

Requires Python 3.8+. No external libraries needed.

```bash
cd src
python main.py
```

On exit (option 7), data is saved to `data/citizens.txt` and automatically
reloaded the next time you start the program.

## 🧪 How to Run Tests

```bash
# from the project root
python -m unittest discover -s tests -v
```

## ✨ Features

1. **Register a citizen** — validated name, age, contact number, service, and request type; auto-generated token (e.g. `AC-DOB-0001` for Aadhar Card / Date of Birth Update).
2. **Serve next citizen** — FIFO dequeue per service **and request type**, so "Aadhar DOB Update" and "Aadhar Address Update" are independent lines.
3. **View queue status** — see everyone waiting for a given service + request type.
4. **Search by token number** — instant lookup.
5. **Counter summary** — waiting count + total served, per service and request type.
6. **Export daily report** — writes a formatted `.txt` report to disk.
7. **Persistent storage** — all data auto-saved/reloaded between runs.
8. **Activity logging** — every action is timestamped in `data/logs.txt`.
9. **Business hours enforcement** — the office is open **Monday-Friday, 8:00 AM - 6:00 PM**, and closed on **Saturdays, Sundays, and public holidays**. Registration and serving are blocked outside these hours, with a clear message explaining why (e.g. "Office is CLOSED - today is Sunday" or "today is a public holiday (Independence Day)"). The holiday calendar lives in `data/holidays.txt` — add or remove a line to update it, no code changes needed. Viewing queues, searching, and exporting reports still work anytime (read-only actions).

## 🛠️ Concepts Demonstrated

- **Encapsulation**: private-ish attributes (`_queue`, `_all_citizens`) accessed via methods/properties.
- **Abstraction**: `Person` is an `ABC` with an abstract `display_info()` method.
- **Inheritance**: `Citizen` inherits from `Person`; all custom exceptions inherit from `QueueSystemError`.
- **Polymorphism**: each exception subclass builds its own message; `display_info()` can be overridden by future subclasses (e.g. `PriorityCitizen`).
- **Exception handling**: custom exceptions (`InvalidServiceError`, `QueueEmptyError`, `CitizenNotFoundError`, `DuplicateTokenError`, `InvalidInputError`) plus built-in ones (`FileNotFoundError`, `PermissionError`, `OSError`, `ValueError`, `KeyboardInterrupt`).
- **File handling**: `with open(...)` context managers throughout, `os.path` checks, structured pipe-delimited storage, append-mode logging.
- **Functions**: small, single-purpose functions in `utils.py` for validation and display, kept separate from business logic.
