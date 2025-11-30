import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from datetime import datetime
import calendar

def build(container):

    # Title
    ttk.Label(
        container,
        text="Age Calculator",
        font="-size 18 -weight bold"
    ).pack(pady=(0, 20))

    # ============================================================
    # BIRTH DATE SELECTORS
    # ============================================================

    ttk.Label(container, text="Date of Birth:", font="-weight bold").pack(anchor="w")

    dob_frame = ttk.Frame(container)
    dob_frame.pack(pady=10)

    # Year
    ttk.Label(dob_frame, text="Year:").grid(row=0, column=0, padx=5, pady=5)
    current_year = datetime.now().year

    dob_year_var = ttk.IntVar(value=current_year)
    dob_year_box = ttk.Spinbox(
        dob_frame,
        from_=1900,
        to=current_year,
        width=6,
        textvariable=dob_year_var
    )
    dob_year_box.grid(row=0, column=1, padx=5)

    # Month
    months = list(calendar.month_name)[1:]
    ttk.Label(dob_frame, text="Month:").grid(row=0, column=2, padx=5)

    dob_month_var = ttk.StringVar(value=months[0])
    dob_month_box = ttk.Combobox(
        dob_frame,
        values=months,
        width=10,
        state="readonly",
        textvariable=dob_month_var
    )
    dob_month_box.grid(row=0, column=3, padx=5)

    # Day
    ttk.Label(dob_frame, text="Day:").grid(row=0, column=4, padx=5)

    dob_day_var = ttk.IntVar(value=1)
    dob_day_box = ttk.Combobox(
        dob_frame,
        width=5,
        state="readonly",
        textvariable=dob_day_var
    )
    dob_day_box.grid(row=0, column=5, padx=5)

    # Update DOB days list
    def update_dob_days():
        year = int(dob_year_var.get())
        month = months.index(dob_month_var.get()) + 1
        _, num_days = calendar.monthrange(year, month)
        dob_day_box["values"] = list(range(1, num_days + 1))

        if dob_day_var.get() > num_days:
            dob_day_var.set(num_days)

    dob_month_box.bind("<<ComboboxSelected>>", lambda e: update_dob_days())
    dob_year_box.bind("<KeyRelease>", lambda e: update_dob_days())
    dob_year_box.bind("<<Increment>>", lambda e: update_dob_days())
    dob_year_box.bind("<<Decrement>>", lambda e: update_dob_days())

    update_dob_days()

    # ============================================================
    # TODAY OR CUSTOM DATE OPTION
    # ============================================================

    ttk.Label(container, text="Calculate age as of:", font="-weight bold").pack(anchor="w", pady=(20, 0))

    mode_var = ttk.StringVar(value="today")

    mode_frame = ttk.Frame(container)
    mode_frame.pack(pady=5)

    ttk.Radiobutton(
        mode_frame,
        text="Today",
        variable=mode_var,
        value="today"
    ).grid(row=0, column=0, padx=10)

    ttk.Radiobutton(
        mode_frame,
        text="Choose Date",
        variable=mode_var,
        value="custom"
    ).grid(row=0, column=1, padx=10)

    # Frame for custom date
    custom_frame = ttk.Frame(container)
    custom_frame.pack(pady=10)

    # Year
    ttk.Label(custom_frame, text="Year:").grid(row=0, column=0, padx=5)
    custom_year_var = ttk.IntVar(value=current_year)
    custom_year_box = ttk.Spinbox(
        custom_frame,
        from_=1900,
        to=3000,
        width=6,
        textvariable=custom_year_var
    )
    custom_year_box.grid(row=0, column=1, padx=5)

    # Month
    ttk.Label(custom_frame, text="Month:").grid(row=0, column=2, padx=5)
    custom_month_var = ttk.StringVar(value=months[0])
    custom_month_box = ttk.Combobox(
        custom_frame,
        values=months,
        width=10,
        state="readonly",
        textvariable=custom_month_var
    )
    custom_month_box.grid(row=0, column=3, padx=5)

    # Day
    ttk.Label(custom_frame, text="Day:").grid(row=0, column=4, padx=5)
    custom_day_var = ttk.IntVar(value=1)
    custom_day_box = ttk.Combobox(
        custom_frame,
        width=5,
        state="readonly",
        textvariable=custom_day_var
    )
    custom_day_box.grid(row=0, column=5, padx=5)

    # Update custom days list
    def update_custom_days():
        year = int(custom_year_var.get())
        month = months.index(custom_month_var.get()) + 1
        _, num_days = calendar.monthrange(year, month)
        custom_day_box["values"] = list(range(1, num_days + 1))

        if custom_day_var.get() > num_days:
            custom_day_var.set(num_days)

    custom_month_box.bind("<<ComboboxSelected>>", lambda e: update_custom_days())
    custom_year_box.bind("<KeyRelease>", lambda e: update_custom_days())
    custom_year_box.bind("<<Increment>>", lambda e: update_custom_days())
    custom_year_box.bind("<<Decrement>>", lambda e: update_custom_days())

    update_custom_days()

    # Hide/show custom date selectors
    def update_visibility(*args):
        if mode_var.get() == "today":
            custom_frame.pack_forget()
        else:
            custom_frame.pack(pady=10)

    mode_var.trace_add("write", update_visibility)
    update_visibility()

    # ============================================================
    # RESULT + CALCULATE BUTTON
    # ============================================================

    result = ttk.Label(container, text="", font="-size 12")
    result.pack(pady=20)

    def calculate():

        # Birth date
        year = int(dob_year_var.get())
        month = months.index(dob_month_var.get()) + 1
        day = int(dob_day_var.get())
        birth_date = datetime(year, month, day)

        # Today or custom
        if mode_var.get() == "today":
            today = datetime.today()
        else:
            cyear = int(custom_year_var.get())
            cmonth = months.index(custom_month_var.get()) + 1
            cday = int(custom_day_var.get())
            today = datetime(cyear, cmonth, cday)

        if today < birth_date:
            result.config(text="The selected date is before the date of birth.")
            return

        # Age calculation
        years = today.year - birth_date.year
        months_diff = today.month - birth_date.month
        days_diff = today.day - birth_date.day

        if days_diff < 0:
            months_diff -= 1
            prev_month = (today.month - 1) or 12
            prev_year = today.year if today.month > 1 else today.year - 1
            days_diff += calendar.monthrange(prev_year, prev_month)[1]

        if months_diff < 0:
            years -= 1
            months_diff += 12

        result.config(
            text=f"Age: {years} years, {months_diff} months, {days_diff} days"
        )

    ttk.Button(
        container,
        text="Calculate Age",
        bootstyle=SUCCESS,
        command=calculate
    ).pack(pady=5)
