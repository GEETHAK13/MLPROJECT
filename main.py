import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import joblib
import webbrowser


class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #
        load = Image.open("two.jpg")
        load = load.resize((1500, 1000))
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)


        title_label = tk.Label(self, text="DETECTION SYSTEM", font=("Arial Bold", 55), bg='lavender')
        title_label.place(x=450, y=50)

        amount_label = tk.Label(self, text="Amount", font=("Arial Bold", 20), bg='ivory')
        amount_label.place(x=150, y=200)
        amount_entry = tk.Entry(self, width=30, bd=5)
        amount_entry.place(x=300, y=200)

        title_label = tk.Label(self, text="Amount can be any numeric value", font=("Arial Bold", 15), bg='#FFC5CB')
        title_label.place(x=600, y=200)

        grade_label = tk.Label(self, text="Grade", font=("Arial Bold", 20), bg='ivory')
        grade_label.place(x=150, y=260)
        grade_values = [str(i) for i in range(7)]
        grade_combobox = ttk.Combobox(self, values=grade_values,state="readonly")
        grade_combobox.place(x=300, y=260)

        title_label = tk.Label(self, text="Grade Range: 0-6", font=("Arial Bold", 15), bg='#FFC5CB')
        title_label.place(x=600, y=260)

        years_label = tk.Label(self, text="Years", font=("Arial Bold", 20), bg='ivory')
        years_label.place(x=150, y=320)
        years_entry = tk.Entry(self, width=30, bd=5)
        years_entry.place(x=300, y=320)

        title_label = tk.Label(self, text="Years can be any numeric value", font=("Arial Bold", 15), bg='#FFC5CB')
        title_label.place(x=600, y=320)

        ownership_label = tk.Label(self, text="Ownership", font=("Arial Bold", 20), bg='ivory')
        ownership_label.place(x=150, y=380)
        ownership_values = [str(i) for i in range(4)]
        ownership_combobox = ttk.Combobox(self, values=ownership_values,state="readonly")
        ownership_combobox.place(x=300, y=380)


        title_label = tk.Label(self, text="Ownership Range: 0-3", font=("Arial Bold", 15), bg='#FFC5CB')
        title_label.place(x=600, y=380)

        income_label = tk.Label(self, text="Income", font=("Arial Bold", 20), bg='ivory')
        income_label.place(x=150, y=440)
        income_entry = tk.Entry(self, width=30, bd=5)
        income_entry.place(x=300, y=440)

        title_label = tk.Label(self, text="Income can be any numeric value.", font=("Arial Bold", 15), bg='#FFC5CB')
        title_label.place(x=600, y=440)

        age_label = tk.Label(self, text="Age", font=("Arial Bold", 20), bg='ivory')
        age_label.place(x=150, y=500)
        age_entry = tk.Entry(self, width=30, bd=5)
        age_entry.place(x=300, y=500)

        title_label = tk.Label(self, text="Age can be any numeric value.", font=("Arial Bold", 15), bg='#FFC5CB')
        title_label.place(x=600, y=500)

        def verify():
            try:
                amount = float(amount_entry.get())
                grade = float(grade_combobox.get())
                years = float(years_entry.get())
                ownership = float(ownership_combobox.get())
                income = float(income_entry.get())
                age = float(age_entry.get())

                # Make the prediction using the loaded model
                y_pred = model.predict([[amount, grade, years, ownership, income, age]])
                if grade not in range(7):
                    messagebox.showinfo("Error", "Invalid input! Grade not in range.")
                elif ownership not in range(5):
                    messagebox.showinfo("Error", "Invalid input! Ownership not in range.")

                # Display the prediction result
                elif y_pred == 1:
                    messagebox.showinfo("OUTPUT", "Fraudulant Transaction")

                    load = Image.open("fraud_img.jpg")
                    load = load.resize((300,300))
                    photo = ImageTk.PhotoImage(load)
                    label = tk.Label(self, image=photo)
                    label.image = photo
                    label.place(x=1000, y=300)
                    self.after(3000, label.destroy)



                else:
                    messagebox.showinfo("OUTPUT", "Normal Transaction")
                    load = Image.open("safe.png")
                    load = load.resize((300, 300))
                    photo = ImageTk.PhotoImage(load)
                    label = tk.Label(self, image=photo)
                    label.image = photo
                    label.place(x=1000, y=300)
                    self.after(3000, label.destroy)



            except ValueError:
                messagebox.showinfo("Error", "Please provide correct Input!!")


        def clear_fields():
            amount_entry.delete(0, 'end')
            grade_combobox.delete(0, 'end')
            years_entry.delete(0, 'end')
            ownership_combobox.delete(0, 'end')
            income_entry.delete(0, 'end')
            age_entry.delete(0, 'end')
            grade_combobox.current(0)
            ownership_combobox.current(0)

        model = joblib.load('credit_history')
        B1 = tk.Button(self,bg="lavender", fg="blue", text="Submit", font=("Arial", 25), command=verify)
        B1.place(x=350, y=560)
        B2 = tk.Button(self,bg="lavender", fg="blue", text="Clear", font=("Arial", 25), command=clear_fields)
        B2.place(x=350, y=620)


        B3 = tk.Button(self,bg="lavender", fg="blue", text="NEXT", font=("Arial", 35), command=lambda: controller.show_frame(ThirdPage))
        B3.place(x=700, y=660)


class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        load = Image.open("second.png")
        load = load.resize((1500, 800))
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        title_label = tk.Label(self, text="CREDIT CARD FRAUD DETECTION", font=("Arial Bold", 55), bg='lavender')
        title_label.place(x=300, y=150)

        Button = tk.Button(self,highlightbackground="lavender", bg="red", fg="dim gray", bd=15, relief="sunken",text="Come on let's Detect fraud", font=("Arial", 45), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=500, y=500)




class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        self.configure(bg='Purple')
        load = Image.open("third.jpg")
        load = load.resize((1500, 800))
        photo = ImageTk.PhotoImage(load)
        label = tk.Label(self, image=photo)
        label.image = photo
        label.place(x=0, y=0)

        title_label = tk.Label(self, text="KNOW MORE ABOUT CREDIT CARD FRAUDS", font=("Arial Bold", 40), bg='lavender')
        title_label.place(x=90, y=50)

        title_label = tk.Label(self, text="What is fraud ???   -- ", font=("Arial Bold", 25),bg='lavender')
        title_label.place(x=100, y=400)

        title_label = tk.Label(self, text="https://en.wikipedia.org/wiki/Credit_card_fraud", font=("Arial Bold", 25),
                               bg='lavender')
        title_label.place(x=100, y=460)
        title_label.bind("<Button-1>", self.open_wikipedia)

        title_label = tk.Label(self, text="Types of fraud and how to prevent it ???   -- ", font=("Arial Bold", 25),
                               bg='lavender')
        title_label.place(x=100, y=540)

        title_label = tk.Label(self, text="https://www.bajajfinserv.in/insights/types-of-credit-card-fraud-and-how-you-can-avoid-them", font=("Arial Bold", 25),
                               bg='lavender')
        title_label.place(x=100, y=600)
        title_label.bind("<Button-1>", self.open_wikipedia)

        Button = tk.Button(self, text="Home", font=("Arial", 35), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=250, y=720)

        Button = tk.Button(self, text="Back", font=("Arial", 35), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=600, y=720)

    def open_wikipedia(self, event):
        webbrowser.open_new(event.widget.cget("text"))


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()
        window.grid_rowconfigure(0, minsize=2000)
        window.grid_columnconfigure(0, minsize=2000)

        self.frames = {}
        for F in (SecondPage,FirstPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(SecondPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Application")


app = Application()
app.maxsize(2000, 2000)
app.mainloop()









