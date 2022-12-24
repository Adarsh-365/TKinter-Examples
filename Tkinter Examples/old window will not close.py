import tkinter as tk
root=tk.Tk()
class Settings(tk.Toplevel):

    def __init__(self, master=None):
        tk.Toplevel.__init__(self, master)
        self.wm_title("Settings")
        # added grab_set()
        self.grab_set()
        #
        print(Settings.state(self))

        exitButton = tk.Button(self, text="Exit", highlightbackground="#56B426", command=self.destroy)
        exitButton.pack()
mm=Settings()
root.mainloop()