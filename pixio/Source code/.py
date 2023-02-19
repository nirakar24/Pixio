import tkinter as tk

class MainApplication(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # Create a container for the frames
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        # Create the two frames
        self.frame1 = Frame1(container, self)
        self.frame2 = Frame2(container, self)

        # Show the first frame by default
        self.frame1.tkraise()

    def switch_to_frame1(self):
        self.frame1.tkraise()

    def switch_to_frame2(self):
        self.frame2.tkraise()

class Frame1(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create widgets for frame 1
        label = tk.Label(self, text="Frame 1")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Switch to Frame 2", command=controller.switch_to_frame2)
        button.pack()

class Frame2(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Create widgets for frame 2
        label = tk.Label(self, text="Frame 2")
        label.pack(pady=10, padx=10)

        button = tk.Button(self, text="Switch to Frame 1", command=controller.switch_to_frame1)
        button.pack()

app = MainApplication()
app.mainloop()
