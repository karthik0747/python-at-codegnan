MEMBER 1 — OOP MODULE
======================

Files: exceptions.py, models.py

WHAT CHANGED THIS ROUND:
  - exceptions.py: added ServiceClosedError, raised when someone tries to
    register or serve a citizen while the office is closed.
  - models.py: unchanged from the sub-service version.

What to do:
1. Place both files inside src/.
2. git checkout -b feature/oop-models
   git add src/exceptions.py src/models.py
   git commit -m "Add ServiceClosedError for out-of-hours actions"
   git push origin feature/oop-models
3. Open a PR: base = main, compare = feature/oop-models. Merge after review.
