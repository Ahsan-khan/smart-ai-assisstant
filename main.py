from CompanionScheduler import CompanionScheduler
from ChatScreenGUI import ChatScreenGUI
from HRScreenGUI import HRScreenGUI
from tkinter import *
hr_screen = HRScreenGUI()
chat_screen = ChatScreenGUI(hr_screen)
scheduler = CompanionScheduler("sample.ics", chat_screen)
chat_screen.root.mainloop()
hr_screen.root.mainloop()