import tkinter as tk

#Function to add numbers/operators to thw display

def click_button(value):
    display.insert(tk.END, value)

 #Function to clear the display   

def clear_display():
    display.delete(0, tk.END) 

#Function to calculate the result    

def calculate():
    try:
        expression = display.get()
        result = eval(expression)

        display.delete(0, tk.END)
        display.insert(0, str(result))

    except ZeroDivisionError:
        display.delete(0, tk.END)
        display.insert(0, "Cannot divide by zero")

    except Exception:
        display.delete(0, tk.END)
        display.insert(0, "Invalid input")

# Create main window        
root = tk.Tk()
root.title("Python Calculator")
root.geometry("350x500")
root.resizable(False, False)

#Display
display = tk.Entry(
    root,
    font=("Arial", 24),
    justify="right",
    bd=10
)
display.pack(
    padx=10,
    pady=20,
    fill="x"
)

buttons = [
    ['7',"8","9","/"],
    ["4","5","6","*"],
    ["1","2","3","-"],
    ["0",".","=","+"]

]

#Create calculator buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")

    for button_text in row:

        if button_text == "=":
            button = tk.Button(
                frame,
                text=button_text,
                font=("Arial",18),
                command=calculate
            )

        else:
            button = tk.Button(
                frame,
                text=button_text,
                command=lambda value=button_text: click_button(value)
            )
        button.pack(
            side="left",
            expand="True",
            fill="both",
            padx=2,
            pady=2
        ) 
# Clear button
clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial",18),
    command=clear_display
)
clear_button.pack(
    padx=10,
    pady=10,
    fill="both"
) 

# Start the application
root.mainloop()