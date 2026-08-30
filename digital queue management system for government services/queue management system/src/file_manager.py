"""
File Handling module for the Digital Queue Management System.
Author: Member 2 (File Handling Module)

Handles saving/loading citizen data and activity logging, with
exception handling around every disk operation.
"""

import os
from datetime import datetime

from models import Citizen


class FileManager:
    def __init__(self, data_file="data/citizens.txt", log_file="data/logs.txt"):
        self.data_file = data_file
        self.log_file = log_file
        self._ensure_data_folder()

    def _ensure_data_folder(self):
        folder = os.path.dirname(self.data_file)
        if folder and not os.path.exists(folder):
            os.makedirs(folder)

    def save_all(self, citizens_dict):
        """Overwrite the data file with the current state of all citizens."""
        try:
            with open(self.data_file, "w", encoding="utf-8") as f:
                for citizen in citizens_dict.values():
                    f.write(citizen.to_record() + "\n")
            self.log_activity("Data saved successfully.")
        except PermissionError:
            self.log_activity("ERROR: Permission denied while saving data.")
            raise
        except OSError as e:
            self.log_activity(f"ERROR: OS error while saving data - {e}")
            raise

    def load_all(self, system):
        """Load citizens from file into the running GovernmentQueueSystem."""
        if not os.path.exists(self.data_file):
            self.log_activity("No existing data file found. Starting fresh.")
            return 0

        loaded_count = 0
        try:
            with open(self.data_file, "r", encoding="utf-8") as f:
                for line_num, line in enumerate(f, start=1):
                    line = line.strip()
                    if not line:
                        continue
                    try:
                        citizen = Citizen.from_record(line)
                        system.restore_citizen(citizen)
                        loaded_count += 1
                    except ValueError as ve:
                        self.log_activity(f"WARNING: Skipped corrupted line {line_num}: {ve}")
            self.log_activity(f"Loaded {loaded_count} citizen record(s) from file.")
        except FileNotFoundError:
            self.log_activity("ERROR: Data file missing during load.")
        except PermissionError:
            self.log_activity("ERROR: Permission denied while reading data file.")
            raise
        return loaded_count

    def log_activity(self, message):
        """Append a timestamped log entry to the log file. Never crashes the app."""
        try:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            with open(self.log_file, "a", encoding="utf-8") as f:
                f.write(f"[{timestamp}] {message}\n")
        except OSError:
            print(f"(logging failed) {message}")

    def export_report(self, system, report_path="data/daily_report.txt"):
        """Generate a readable summary report of the day's queue activity."""
        try:
            with open(report_path, "w", encoding="utf-8") as f:
                f.write("DAILY QUEUE REPORT\n")
                f.write(f"Generated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
                f.write("=" * 65 + "\n")
                for service, sub_service, waiting, served in system.all_counters_summary():
                    f.write(f"{service:<20} | {sub_service:<25} | Waiting: {waiting:<3} | Served: {served}\n")
            self.log_activity(f"Report exported to {report_path}")
            return report_path
        except OSError as e:
            self.log_activity(f"ERROR: Could not export report - {e}")
            raise
