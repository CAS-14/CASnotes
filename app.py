from tkinter import *
import notes


class App(Tk):
    def __init__(self):
        super().__init__()

        self.title("CASnotes")

        self.label = Label(self, text="Enter note name")
        self.box = Entry(self)
        self.btn = Button(self, text="click", command=self.getnote(self.box.get()))
        
        self.label.pack()
        self.box.pack()
        self.btn.pack()

    def getnote(self, name):
        win = NoteWindow(notes.accessNote(name))
        win.mainloop()
        

class NoteWindow(Tk):
    def __init__(self, note):
        super().__init__()

        self.title("CASnotes: "+note.name)

        self.label = Label(self, text=note.title+"\n\n"+note.content)
        self.label.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop