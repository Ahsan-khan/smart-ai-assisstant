from tkinter import *
from tkcalendar import *
from PIL import ImageTk, Image  
import calendar
from chatbot_and_sentiment_analysis import BotAIandAnalyzer
class ChatScreenGUI:
    # GUI
    def __init__(self, hrscreen) -> None:
        self.splash_root = None
        self.root = None
        self.txt = None
        self.e = None
        self.analyzer = BotAIandAnalyzer()
        self.hrscreen = hrscreen
        self.show_main_screen()

    
    def show_splash_screen(self):
        self.splash_root = Tk()
        self.splash_root.geometry("500x300")
        self.splash_root['background'] = '#EF9882'
        self.splash_root.overrideredirect(True)
        self.splash_root.after(3000, self.show_main_screen)
    
    # def run(self):
    #     mainloop()

    def show_main_screen(self):
        BG_GRAY = "#E4E1E1"
        BG_COLOR = "#E4E1E1"
        TEXT_COLOR = "#000000"
        
        FONT = "Nunito 14"
        FONT_BOLD = "Nunito 13 bold"
        # self.splash_root.destroy()
        self.root = Tk()
        self.root.title("GINI")
        self.root['background'] = "#EF9882"
        
        lable1 = Label(self.root, bg="#EF9882", fg=TEXT_COLOR, text="Onboarding Companion", font=FONT_BOLD, pady=10, width=20, height=1).grid(
        row=0)
    
        self.txt = Text(self.root, bg="#EF9882", fg=TEXT_COLOR, font=FONT, width=60)
        self.txt.grid(row=1, column=0, columnspan=2)

        self.txt.tag_configure('bot', justify='left')
        self.txt.tag_configure('user', justify='right')
        # scrollbar = Scrollbar(self.txt)
        # scrollbar.place(relheight=1, relx=0.974)
        
        self.e = Entry(self.root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=55)
        self.e.grid(row=2, column=0)
        
        send = Button(self.root, text="Send", font=FONT_BOLD, bg=BG_GRAY,
                    command=self.send).grid(row=2, column=1)
        
        # img = Image.open("images.png")
        # bg = ImageTk.PhotoImage(img, master=self.root)

        # label = Label(self.root, image=bg, width=50).grid(row=0, column=2, rowspan=2)
        # scheduler = CompanionScheduler("sample.ics", chat_screen)
        self.welcome_new_comer()
    
    def welcome_new_comer(self):
        msg = "Hi I'm GINI your onboarding companion. I welcome you to GSoft. I will be with you in every step, feel free to ask me any questions."
        self.txt.insert(END, f"\n {msg}", "bot")
    # Send function
    def send(self):
        send = self.e.get()
        
        self.txt.insert(END, "\n" + send, 'user')
    
        user = self.e.get()
        response = self.analyzer.get_bot_reply(user)

       
        self.txt.insert(END, "\n" + f"GINI -> {response}", 'bot')
        new_score, new_state = self.analyzer.get_score_and_employee_state(user)
        self.hrscreen.insert_chat_bot_response(new_score, new_state)
        self.e.delete(0, END)
    
    def insert_chat_bot_response(self, text):
        self.txt.insert(END, f"\nGINI -> {text}", 'bot')