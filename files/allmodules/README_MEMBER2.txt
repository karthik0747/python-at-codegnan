MEMBER 2 — FILE HANDLING MODULE (UPDATED)
============================================

Files in this folder:
  - file_manager.py

WHAT CHANGED:
  - export_report() now unpacks (service, sub_service, waiting, served)
    instead of (service, waiting, served), since summaries are now
    grouped by request type too. Report lines look like:

      Aadhar Card          | Date of Birth Update      | Waiting: 2 | Served: 5

What to do:
1. Replace the old file_manager.py inside src/ with this one.
2. In your terminal:
     git checkout -b feature/file-handling
     git add src/file_manager.py
     git commit -m "Update report export to include sub-service breakdown"
     git push origin feature/file-handling
3. Open a Pull Request on GitHub: base = main, compare = feature/file-handling.
4. Tag a teammate to review, then merge once approved.

Note: this file still imports Citizen from models.py (Member 1's file),
so make sure the updated models.py is in src/ too.
