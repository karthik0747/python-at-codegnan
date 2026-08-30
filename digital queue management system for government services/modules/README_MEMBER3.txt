MEMBER 3 — FUNCTIONS & INTEGRATION MODULE (UPDATED)
======================================================

Files: utils.py, main.py, tests/test_queue.py

WHAT CHANGED THIS ROUND:
  - main.py: now creates a BusinessHours instance at startup, shows the
    live open/closed status at the top of the menu every loop, and
    blocks "Register New Citizen" and "Serve Next Citizen" with a
    ServiceClosedError when the office is closed. Viewing queues,
    searching, viewing the summary, and exporting reports still work
    at any time (read-only actions).
  - tests/test_queue.py: added a TestBusinessHours class covering: open
    during weekday hours, closed before opening, closed after closing,
    closed Saturday, closed Sunday, closed on a public holiday. Uses a
    throwaway holidays file in /tmp so it never touches your real
    data/holidays.txt.
  - utils.py is unchanged from the sub-service version.

What to do:
1. Place utils.py and main.py inside src/. Place test_queue.py in tests/.
2. git checkout -b feature/functions-integration
   git add src/utils.py src/main.py tests/test_queue.py
   git commit -m "Enforce business hours in the CLI flow and add coverage"
   git push origin feature/functions-integration
3. Open a PR: base = main, compare = feature/functions-integration. Merge after review.

Note: main.py now imports service_hours.py (Member 2) and exceptions.py
(Member 1's updated version with ServiceClosedError), so all three
members' files need to be in src/ together before this fully runs.

To run:              cd src && python main.py
To run the tests:    python -m unittest discover -s tests -v   (from project root)
