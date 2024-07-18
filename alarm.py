from tkinter import *
from tkinter import messagebox
import time
import threading

# Function to set the alarm
def set_alarm():
    alarm_time = f"{hour.get()}:{minute.get()}:{second.get()}"
    alarm_label.config(text=f"Alarm set for {alarm_time}")
    threading.Thread(target=alarm_trigger, args=(alarm_time,), daemon=True).start()

# Function to trigger the alarm
def alarm_trigger(alarm_time):
    while True:
        current_time = time.strftime("%H:%M:%S")
        if current_time == alarm_time:
            messagebox.showinfo("Alarm", "Time's up!")
            break
        time.sleep(1)

# Main window setup
background = "#ffffff"

window = Tk()
window.title("Alarm Clock")
window.geometry("300x150")
window.configure(bg=background)

frame_line = Frame(window)
frame_line.pack()

# Time selection
Label(frame_line, text="Set Time", font=("Helvetica", 16)).grid(row=0, columnspan=3, pady=10)

hour = StringVar(window)
hours = [f"{i:02d}" for i in range(24)]
hour.set(hours[0])  # default value

minute = StringVar(window)
minutes = [f"{i:02d}" for i in range(60)]
minute.set(minutes[0])  # default value

second = StringVar(window)
seconds = [f"{i:02d}" for i in range(60)]
second.set(seconds[0])  # default value

# Dropdowns for hour, minute, second
hour_menu = OptionMenu(frame_line, hour, *hours)
minute_menu = OptionMenu(frame_line, minute, *minutes)
second_menu = OptionMenu(frame_line, second, *seconds)

hour_menu.grid(row=1, column=0, padx=5)
minute_menu.grid(row=1, column=1, padx=5)
second_menu.grid(row=1, column=2, padx=5)

# Set Alarm Button
set_button = Button(frame_line, text="Set Alarm", command=set_alarm)
set_button.grid(row=2, columnspan=3, pady=10)

# Alarm status label using tkinter's Label
alarm_label = Label(window, text="", bg=background, font=("Helvetica", 12))
alarm_label.pack(pady=10)

window.mainloop()
