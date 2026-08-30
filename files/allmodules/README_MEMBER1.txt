MEMBER 1 — OOP MODULE (UPDATED)
=================================

Files in this folder:
  - exceptions.py
  - models.py

WHAT CHANGED:
  - Each service now has multiple REQUEST TYPES (sub-services), e.g.
    Aadhar Card -> New Enrollment, Date of Birth Update, Address Update,
    Name Correction, Mobile Number Update, Photo Update.
  - Each request type is its own independent queue (SubServiceCounter)
    with its own token sequence, e.g. AC-DOB-0001, AC-ADR-0001.
  - New exception: InvalidSubServiceError, raised if someone picks a
    request type that doesn't exist under the chosen service.
  - Citizen objects now store a `sub_service` field too.

What to do:
1. Replace the old exceptions.py and models.py inside src/ with these.
2. In your terminal:
     git checkout -b feature/oop-models
     git add src/exceptions.py src/models.py
     git commit -m "Add sub-service (request type) support: per-type queues and token sequences"
     git push origin feature/oop-models
3. Open a Pull Request on GitHub: base = main, compare = feature/oop-models.
4. Tag a teammate to review, then merge once approved.
