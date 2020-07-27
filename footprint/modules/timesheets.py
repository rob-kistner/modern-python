from datetime import *

"""
now = datetime.now()
print(now)
print(now.hour)
print(now.minute)
print(now.strftime("%a %B %d %I:%M%p").lower())
"""


class Timesheet:

    worktypes = {
        "PM": "Project Management",
        "CON": "Concept",
        "DES": "Design",
        "PRO": "Production",
        "GTH": "Gathering",
        "UNB": "Unbillable"
    }

    def __repr__(self):
        info = (
           f"{self.entry_date}",
           f"{self.job_id}",
           f"{self.get_time_range()}"
        )
        return "\n".join(info)

    def __init__(self):
        self.job_id = 0
        self.entry_date = date.now()
        self.start_time = "09:00"
        self.end_time = "09:30"
        self.worktype = "DES"
    
    def format_time(self, time):
        return time.strftime("%I:%M%p").lower()

    def get_time_range(self):
        return f"{format_time(self.start_time)} – {format_time(self.end_time)}"

ts1 = Timesheet()