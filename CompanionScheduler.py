import time
from datetime import timedelta
from icalendar import Calendar, Event
import threading
class CompanionScheduler:
    def __init__(self, fileName, gui) -> None:
        self.icsFileName = fileName
        self.gui = gui
        self.meetNames = []
        self.meetTimes = []
        self.notifTimes = []
        self.scheduler = []
        self.parse_ics()
        self.schedule_notifications()
        self.schedule_alert()

    def parse_ics(self):
        g = open(self.icsFileName,'rb')
        gcal = Calendar.from_ical(g.read())
        for component in gcal.walk():
            if component.name == "VEVENT":
                st = component.get('dtstart')
                end = component.get('dtend')
                self.meetNames.append(component.get('summary').to_ical().decode("utf-8"))
                self.meetTimes.append((st.dt, end.dt))
        print(self.meetNames, self.meetTimes)
        g.close()
    
    def schedule_notifications(self):
        for (start, end) in self.meetTimes:
            print(start.time(), end.time())
            st_time = start - timedelta(minutes=10)
            end_time  = end + timedelta(minutes=10)
            print(st_time.time(), end_time.time())
            self.notifTimes.append((st_time, end_time))
    
    def upcoming_meet_alert(self, meetName):
        self.gui.insert_chat_bot_response(f"you have {meetName} meeting coming up in 10 minutes")
    
    def meet_feedback_alert(self, meetName):
        self.gui.insert_chat_bot_response(f"How did your {meetName} meeting go")

    def schedule_alert(self):
        loop_counter = 0
        for (start_times, end_times) in self.notifTimes:
            print(f"aaaa {start_times.timestamp()-time.time()}")
            print(f"aaaa {end_times.timestamp()-time.time()}")
            threading.Timer(start_times.timestamp()-time.time(), self.upcoming_meet_alert, [self.meetNames[loop_counter]]).start()
            threading.Timer(end_times.timestamp()-time.time(), self.meet_feedback_alert, [self.meetNames[loop_counter]]).start()
            loop_counter+=1

