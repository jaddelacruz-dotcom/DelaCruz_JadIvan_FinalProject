import json
import os

class MaintenanceTask:
    def __init__(self, asset_name, task_details, date):
        self.asset_name = asset_name
        self.task_details = task_details
        self.date = date

    def to_dict(self):
        return vars(self)

class TrackerManager:
    def __init__(self, filepath):
        self.filepath = filepath
        self.tasks = self.load_data()

    def load_data(self):
        """Advanced Logic: Context Manager for File Handling"""
        if not os.path.exists(self.filepath):
            return []
        try:
            with open(self.filepath, 'r') as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []

    def add_task(self, asset, detail, date):
        new_task = MaintenanceTask(asset, detail, date)
        self.tasks.append(new_task.to_dict())
        self.save_data()

    def save_data(self):
        with open(self.filepath, 'w') as f:
            json.dump(self.tasks, f, indent=4)

    def search_tasks(self, query):
        """Advanced Concept: List Comprehension for filtering"""
        return [t for t in self.tasks if query.lower() in t['asset_name'].lower()]