"""
Service availability / business hours module.
Author: Member 2 (File Handling Module)

Government offices are open Monday-Friday, 8:00 AM - 6:00 PM, and closed
on Saturdays, Sundays, and public holidays. The holiday list is loaded
from a plain text file (data/holidays.txt) so staff can update it without
touching any code.
"""

import os
from datetime import datetime, time


class BusinessHours:
    OPEN_TIME = time(8, 0)      # 8:00 AM
    CLOSE_TIME = time(18, 0)    # 6:00 PM
    CLOSED_WEEKDAYS = {5, 6}    # Python's weekday(): Monday=0 ... Saturday=5, Sunday=6

    def __init__(self, holidays_file="data/holidays.txt"):
        self.holidays_file = holidays_file
        self._holidays = self._load_holidays()   # {date: "Holiday Name"}

    def _load_holidays(self):
        """Read the holiday list from disk. Missing/corrupt lines are skipped, not fatal."""
        holidays = {}
        if not os.path.exists(self.holidays_file):
            return holidays
        try:
            with open(self.holidays_file, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line or line.startswith("#"):
                        continue
                    parts = line.split("|")
                    date_part = parts[0].strip()
                    name = parts[1].strip() if len(parts) > 1 else "Public Holiday"
                    try:
                        holiday_date = datetime.strptime(date_part, "%Y-%m-%d").date()
                        holidays[holiday_date] = name
                    except ValueError:
                        continue   # skip a malformed line instead of crashing the app
        except OSError:
            pass   # if the file genuinely can't be read, just treat it as "no holidays"
        return holidays

    def is_open(self, check_datetime=None):
        check_datetime = check_datetime or datetime.now()
        if check_datetime.weekday() in self.CLOSED_WEEKDAYS:
            return False
        if check_datetime.date() in self._holidays:
            return False
        return self.OPEN_TIME <= check_datetime.time() <= self.CLOSE_TIME

    def status_message(self, check_datetime=None):
        """Human-readable line describing whether the office is open right now, and why not."""
        check_datetime = check_datetime or datetime.now()
        hours_note = "Office hours: Mon-Fri, 8:00 AM - 6:00 PM (closed Sat, Sun & public holidays)."
        if self.is_open(check_datetime):
            return (f"Office is OPEN. Closes today at {self.CLOSE_TIME.strftime('%I:%M %p')}. "
                    f"{hours_note}")
        return f"Office is CLOSED - {self._closed_reason(check_datetime)}. {hours_note}"

    def _closed_reason(self, check_datetime):
        if check_datetime.weekday() == 5:
            return "today is Saturday"
        if check_datetime.weekday() == 6:
            return "today is Sunday"
        holiday_name = self._holidays.get(check_datetime.date())
        if holiday_name:
            return f"today is a public holiday ({holiday_name})"
        if check_datetime.time() < self.OPEN_TIME:
            return f"office opens at {self.OPEN_TIME.strftime('%I:%M %p')}"
        return f"office closed for the day at {self.CLOSE_TIME.strftime('%I:%M %p')}"
