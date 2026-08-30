MEMBER 2 — FILE HANDLING MODULE (UPDATED)
============================================

Files: file_manager.py, service_hours.py, data/holidays.txt

WHAT CHANGED THIS ROUND:
  - NEW: service_hours.py — the BusinessHours class. Office hours are
    Monday-Friday, 8:00 AM - 6:00 PM. Closed Saturdays, Sundays, and any
    date listed in data/holidays.txt. Reads the holiday list from disk
    on startup (skips corrupted lines instead of crashing).
  - NEW: data/holidays.txt — plain text holiday calendar, format:
        YYYY-MM-DD|Holiday Name
    Add or remove a line to update the calendar - no code changes needed.
  - file_manager.py is unchanged from the sub-service version.

What to do:
1. Place file_manager.py and service_hours.py inside src/.
   Place holidays.txt inside data/.
2. git checkout -b feature/file-handling
   git add src/file_manager.py src/service_hours.py data/holidays.txt
   git commit -m "Add business-hours check with holiday calendar loaded from file"
   git push origin feature/file-handling
3. Open a PR: base = main, compare = feature/file-handling. Merge after review.

Note: service_hours.py has no dependency on the other modules — you can
test it completely on its own with something like:

    from service_hours import BusinessHours
    bh = BusinessHours(holidays_file="data/holidays.txt")
    print(bh.status_message())
