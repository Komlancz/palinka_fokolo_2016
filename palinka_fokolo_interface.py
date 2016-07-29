from tkinter import *
from PIL import Image


class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        '''Create one Button, text and three entry field'''

        '''Főzet mennyisége'''
        self.menny_instruc = Label(self, text="Hány liter a főzet?", font=("Helvetica", 12))
        self.menny_instruc.grid(row=0, column=0)

        self.menny = Entry(self, text="nézzük")
        self.menny.grid(row=0, column=1)

        '''Jelenlegi fok'''
        self.jel_fok_instruc = Label(self, text="Hány fokos MOST?", font=("Helvetica", 12))
        self.jel_fok_instruc.grid(row=2, column=0)

        self.jel_fok = Entry(self)
        self.jel_fok.grid(row=2, column=1)

        '''Kívánt fok'''
        self.kivant_fok_instruc = Label(self, text="Hány fokosra szeretnéd készíteni?", font=("Helvetica", 12))
        self.kivant_fok_instruc.grid(row=4, column=0)

        self.kivant_fok = Entry(self)
        self.kivant_fok.grid(row=4, column=1)

        '''Eredmény felirat'''
        self.result_label = Label(self, font=("Helvetica", 18), fg="White")
        self.result_label.grid(row=6, column=0)

        '''Teljes mennyiség'''
        self.teljes_mennyiseg = Label(self, font=("Helvetica", 15), fg="Black")
        self.teljes_mennyiseg.grid(row=7, column=0)

        '''Gomb a számoláshoz'''
        self.count_button = Button(self, fg="Black", font=("Helvetica", 14), bg='#40E0D0')
        self.count_button["text"] = "Fokolás"
        self.count_button["command"] = self.update_count
        self.count_button.grid(row=5, column=1)

        '''Kép hozzáadás'''
        # image = Image.open("barack.jpg")
        # photo = PhotoImage(image)
        # w = Label(self, image=photo)
        # w.image = photo
        # w.pack()

    def update_count(self):
        self.result_label["text"] = str("%.2f liter" % self.fokolas())
        self.result_label["bg"] = "Red"
        self.teljes_mennyiseg["text"] = str("%.2f liter pálinka lesz belőle" % self.teljes_palinka())
        self.count_button["text"] = "Visszaállítás"
        '''Vissza állítás eredeti állapotra'''
        self.count_button["command"] = self.replay

    def replay(self):
        '''Mindent alapértelmezettre állítani'''
        self.result_label["text"]= ""
        self.result_label["bg"] = "#F0F0F0"
        self.teljes_mennyiseg["text"] = ""
        self.count_button["text"] = "Fokolás"
        self.count_button["command"] = self.update_count

    def fokolas(self):
        try:
            menny = float(self.menny.get())
            jel_fok = float(self.jel_fok.get())
            kivant_fok = float(self.kivant_fok.get())
        except ValueError:
            self.result_label["text"] = "Minden mezőt tölts ki!"
            self.result_label["bg"] = "Red"
        VV = menny * jel_fok
        resz = VV / kivant_fok
        kivan_liter = resz - menny
        return kivan_liter

    def teljes_palinka(self):
        total = self.fokolas() + float(self.menny.get())
        return total


root = Tk()
root.title("Pálinka fokolás")
root.geometry("500x200")
app = Application(root)
root.mainloop()
