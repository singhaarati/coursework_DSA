from tkinter import *
from tkinter.ttk import *
# from turtle import right

# from pyparsing import col
import waterSystem as WS
import auth as Auth


class popupWindow(object):
    def __init__(self, master, query):
        top = self.top = Toplevel(master)
        self.l = Label(top, text=query, font=("", 13))
        self.l.pack(padx=10, pady=10)
        if query != "Cycle Detected":
            self.e = Entry(top)
            self.e.pack(padx=10, pady=10, ipadx=8, ipady=8)
            self.b = Button(top, text='Ok', command=self.cleanupPopup)
            self.b.pack(padx=10, pady=10, ipadx=8, ipady=8)

    def cleanupPopup(self):
        self.value = self.e.get()
        self.top.destroy()


class LoginWindow(object):
    def __init__(self, master):
        self.master = master
        self.master.geometry("500x400")
        self.master.title("Water Supply System")

        self.emailEntry = Entry(master, width=200)
        # self.on_click_id = self.emailEntry.bind('<Button-1>', self.on_click)
        self.emailEntry.insert(0, "Enter Email")
        self.emailEntry.pack(ipadx=8, ipady=8, padx=5, pady=5)

        self.passwordEntry = Entry(master, width=200)
        # self.on_click_id = self.passwordEntry.bind('<Button-1>', self.on_click)
        self.passwordEntry.insert(0, "Enter Password")
        self.passwordEntry.pack(ipadx=8, ipady=8, padx=5, pady=5)

        self.login = Button(
            master, text="Login", command=self.validateLogin)
        self.login.pack(ipadx=10, ipady=10, padx=10, pady=10)
        self.signUp = Button(
            master, text="Sign Up", command=lambda: self.validateLogin(signUp=True))
        self.signUp.pack(ipadx=10, ipady=10, padx=10, pady=10)

    def validateLogin(self, signUp=False):
        self.email = self.emailEntry.get()
        self.password = self.passwordEntry.get()
        if signUp:
            Auth.signUp(self.email, self.password)
            self.lauchMainWindow()
        elif Auth.login(self.email, self.password):
            self.lauchMainWindow()
        else:
            print("Invalid")

    def on_click(self, event):
        self.emailEntry.configure(state=NORMAL)
        self.emailEntry.delete(0, END)

        self.emailEntry.unbind('<Button-1>', self.on_click_id)

        self.passwordEntry.configure(state=NORMAL)
        self.passwordEntry.delete(0, END)

        self.passwordEntry.unbind('<Button-1>', self.on_click_id)

    def lauchMainWindow(self):
        self.master.destroy()  # close the current window
        self.master = Tk()  # create another Tk instance
        self.app = mainWindow(self.master)  # create Demo2 window


class mainWindow(object):
    def __init__(self, master):
        self.master = master
        self.master.title("Water Supply System")
        self.master.geometry("205x450")

        self.menu_label = Label(master, text="Menu")
        self.view_pipelines = Button(
            master, text="View Water Supply Connections", command=WS.displayPipeSystem)
        self.add_house = Button(
            master, text="Add New House", command=self.popupNewHouse)
        self.add_pipe = Button(
            master, text="Add Pipe Connection", command=self.popupAddPipe)
        self.shortest_path = Button(
            master, text="Show Shortest Path", command=self.popupShortestPath)
        self.add_vulnerable = Button(
            master, text="Add Vulnerable House", command=self.popupVulnerableHouse)
        self.reset = Button(
            master, text="Reset", command=WS.reset)

        self.menu_label.grid(row=0, column=0, pady=15, padx=5)
        self.view_pipelines.grid(row=1, column=0, pady=5, padx=5,
                                 sticky=W+E, ipadx=8, ipady=8)
        self.add_house.grid(row=2, column=0, pady=5, padx=5,
                            sticky=W+E, ipadx=8, ipady=8)
        self.add_pipe.grid(row=3, column=0, pady=5, padx=5,
                           sticky=W+E, ipadx=8, ipady=8)
        self.shortest_path.grid(row=4, column=0, pady=5, padx=5,
                                sticky=W+E, ipadx=8, ipady=8)
        self.add_vulnerable.grid(row=5, column=0, pady=5, padx=5,
                                 sticky=W+E, ipadx=8, ipady=8)
        self.reset.grid(row=6, column=0, pady=50, ipadx=10, ipady=10)

    # def addNewPipe(self):
    def popupShortestPath(self):
        self.w = popupWindow(
            self.master, "Enter Respective House Numbers Separated By '-'")
        self.add_pipe["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.add_pipe["state"] = "normal"
        # WS.addNewHouse(self.entryValue())
        src, dest = self.entryValue().split('-')
        WS.displayPipeSystem(plotShortestPath=True, src=src, dest=dest)

    def popupNewHouse(self):
        self.w = popupWindow(self.master, "Enter New House Number")
        self.add_house["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.add_house["state"] = "normal"
        WS.addNewHouse(str(self.entryValue()).strip())

    def popupVulnerableHouse(self):
        self.w = popupWindow(self.master, "Enter Vulnerable House Number")
        self.add_house["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.add_house["state"] = "normal"
        WS.vulnerable_house(str(self.entryValue()).strip())

    def popupAddPipe(self):
        self.w = popupWindow(
            self.master, "Enter Respective House Numbers Separated By '-'")
        self.add_pipe["state"] = "disabled"
        self.master.wait_window(self.w.top)
        self.add_pipe["state"] = "normal"
        # WS.addNewHouse(self.entryValue())
        h1, h2 = self.entryValue().split('-')
        if WS.addPipeConnection(str(h1).strip(), str(h2).strip()) == False:
            self.w = popupWindow(self.master, "Cycle Detected")

    def entryValue(self):
        return self.w.value


if __name__ == "__main__":
    window = Tk()
    m = LoginWindow(window)
    window.mainloop()
