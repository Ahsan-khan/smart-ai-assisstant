from tkinter import *
class HRScreenGUI:
    def __init__(self) -> None:
        BG_GRAY = "#E4E1E1"
        BG_COLOR = "#E4E1E1"
        
        # self.splash_root.destroy()
        self.root = Tk()
        self.root.title("HR Dashboard")
        self.root['background'] = BG_COLOR
        initialvalues = [["S.No", "Employee Name", "Happiness Score", "Employee State"], 
                       [1, "Mike", 0, "Neutral"], [2, "Scott", 0.45, "Happy"], [3, "Jim", -0.2, "Sad"]]
        self.textEntries = []
        
        self.createTable(initialvalues)
        # self.txt = Text(self.root, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT, width=60)
        # self.txt.grid(row=3, column=0, columnspan=1)
        
        scrollbar = Scrollbar()
        scrollbar.place(relheight=1, relx=0.974)
    
    def createTable(self, initialValues):
        TEXT_COLOR = "#EF9882"
        FONT_BOLD = "Nunito 13 bold"
        for i in range(4):
            for j in range(4):
                self.e = Entry(self.root, width=20, fg=TEXT_COLOR,
                               font=FONT_BOLD)
                self.e.grid(row=i, column=j)
                self.e.insert(END, initialValues[i][j])
                self.textEntries.append(self.e)
        
    
    def insert_chat_bot_response(self, score, state):
        self.textEntries[6].delete(0, END)
        self.textEntries[7].delete(0, END)
        self.textEntries[6].insert(END, f"{score}")
        self.textEntries[7].insert(END, f"{state}")