import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime

def build(container):

    # Title
    ttk.Label(
        container,
        text="Clock",
        font="-size 18 -weight bold"
    ).pack(pady=(0, 20))

    # Time Label
    time_label = ttk.Label(
        container,
        text="--:--:--",
        font="-size 36 -weight bold"
    )
    time_label.pack(pady=10)

    # Date Label
    date_label = ttk.Label(
        container,
        text="",
        font="-size 14"
    )
    date_label.pack(pady=5)

    # 12h / 24h mode toggle
    format_var = ttk.StringVar(value="24")

    toggle_frame = ttk.Frame(container)
    toggle_frame.pack(pady=10)

    ttk.Radiobutton(
        toggle_frame,
        text="24-Hour",
        variable=format_var,
        value="24"
    ).grid(row=0, column=0, padx=10)

    ttk.Radiobutton(
        toggle_frame,
        text="12-Hour",
        variable=format_var,
        value="12"
    ).grid(row=0, column=1, padx=10)

    # Update Clock
    def update_clock():
        now = datetime.now()

        if format_var.get() == "12":
            time_str = now.strftime("%I:%M:%S %p")
        else:
            time_str = now.strftime("%H:%M:%S")

        date_str = now.strftime("%A, %B %d, %Y")

        time_label.config(text=time_str)
        date_label.config(text=date_str)

        container.after(1000, update_clock)

    update_clock()

    # Optional: Copy current time button
    def copy_time():
        container.clipboard_clear()
        container.clipboard_append(time_label.cget("text"))

    ttk.Button(
        container,
        text="Copy Time",
        bootstyle=INFO,
        command=copy_time
    ).pack(pady=10)
