from tkinter import *

def click(event):
    global scvalue
    if scvalue.get() == "Error":
        scvalue.set("")
        screen.update()

    text = event.widget.cget("text") #get text of a button
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(scvalue.get())
            except Exception as e:
                print(e)
                value = "Error"
        
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get()+ text)
        screen.update()
    

root = Tk()
root.geometry("400x700")
root.title("Calculator")

root.wm_iconbitmap("calc.ico")
root.configure(background="black")

scvalue = StringVar()
#scvalue.set("0")
screen = Entry(root, textvar= scvalue,font= "lucida 40 bold")
screen.pack(fill=X, ipadx=8, padx= 10, pady=5)

#make frames
f = Frame(root, bg="grey")
b = Button(f, text="7", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="8", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="9", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="4", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="5", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="6", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="1", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="2", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="3", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="0", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text=".", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="C", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="+", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 19, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="-", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 19, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="*", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 19, pady=12)
b.bind("<Button-1>",click)
f.pack()

f = Frame(root, bg="grey")
b = Button(f, text="/", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="%", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)

b = Button(f, text="=", font= "lucida 25 bold",padx=28, pady=5)
b.pack(side= LEFT, padx= 18, pady=12)
b.bind("<Button-1>",click)
f.pack()



root.mainloop()