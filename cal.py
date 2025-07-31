def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("Enter choice (1/2/3/4): ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if choice == '1':
    print("Result:", add(num1, num2))
elif choice == '2':
    print("Result:", subtract(num1, num2))
elif choice == '3':
    print("Result:", multiply(num1, num2))
elif choice == '4':
    print("Result:", divide(num1, num2))
else:
    print("Invalid Input")
import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = str(eval(str(entry.get())))
            entry.set(result)
        except:
            entry.set("Error")
    elif text == "C":
        entry.set("")
    else:
        entry.set(entry.get() + text)

root = tk.Tk()
root.geometry("300x400")
root.title("Calculator")

entry = tk.StringVar()
entrybox = tk.Entry(root, textvar=entry, font="Arial 20")
entrybox.pack(fill=tk.BOTH, ipadx=8, pady=10, padx=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["C", "0", "=", "+"]
]

for row in buttons:
    frame = tk.Frame(btn_frame)
    frame.pack()
    for btn_text in row:
        button = tk.Button(frame, text=btn_text, font="Arial 15", width=5, height=2)
        button.pack(side=tk.LEFT, padx=5, pady=5)
        button.bind("<Button-1>", click)

root.mainloop()
