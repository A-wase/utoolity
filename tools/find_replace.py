import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter as tk


def build(container):
    # --------------------------------------------------
    # Header
    # --------------------------------------------------
    header = ttk.Label(
        container,
        text="Find & Replace",
        font="-size 18 -weight bold"
    )
    header.pack(anchor="w", pady=(0, 15))

    subtitle = ttk.Label(
        container,
        text="Replace words or characters and highlight matches",
        foreground="#6c757d"
    )
    subtitle.pack(anchor="w", pady=(0, 20))

    # --------------------------------------------------
    # Text input
    # --------------------------------------------------
    ttk.Label(container, text="Text").pack(anchor="w")

    text_input = tk.Text(
        container,
        height=8,
        wrap="word",
        relief="solid",
        borderwidth=1
    )
    text_input.pack(fill=X, pady=(5, 15))

    # Highlight style
    text_input.tag_configure(
        "highlight",
        background="#fff3cd"
    )

    # --------------------------------------------------
    # Find / Replace fields
    # --------------------------------------------------
    fields = ttk.Frame(container)
    fields.pack(fill=X, pady=10)

    # Find
    find_frame = ttk.Frame(fields)
    find_frame.pack(side=LEFT, fill=X, expand=True, padx=(0, 10))

    ttk.Label(find_frame, text="Find").pack(anchor="w")
    find_entry = ttk.Entry(find_frame)
    find_entry.pack(fill=X, pady=5)

    # Replace
    replace_frame = ttk.Frame(fields)
    replace_frame.pack(side=LEFT, fill=X, expand=True)

    ttk.Label(replace_frame, text="Replace with").pack(anchor="w")
    replace_entry = ttk.Entry(replace_frame)
    replace_entry.pack(fill=X, pady=5)

    # --------------------------------------------------
    # Highlight logic
    # --------------------------------------------------
    def highlight_matches(*_):
        text_input.tag_remove("highlight", "1.0", END)

        query = find_entry.get()
        if not query:
            return

        start = "1.0"
        while True:
            pos = text_input.search(query, start, stopindex=END)
            if not pos:
                break

            end = f"{pos}+{len(query)}c"
            text_input.tag_add("highlight", pos, end)
            start = end

    find_entry.bind("<KeyRelease>", highlight_matches)
    text_input.bind("<KeyRelease>", highlight_matches)

    # --------------------------------------------------
    # Actions
    # --------------------------------------------------
    def replace_text():
        content = text_input.get("1.0", END)
        find_value = find_entry.get()
        replace_value = replace_entry.get()

        if not find_value:
            return

        updated = content.replace(find_value, replace_value)

        text_input.delete("1.0", END)
        text_input.insert("1.0", updated)
        highlight_matches()

    def copy_text():
        container.clipboard_clear()
        container.clipboard_append(text_input.get("1.0", END).strip())

    action_bar = ttk.Frame(container)
    action_bar.pack(fill=X, pady=(15, 0))

    copy_btn = ttk.Button(
        action_bar,
        text="Copy Text",
        bootstyle=SECONDARY,
        command=copy_text
    )
    copy_btn.pack(side=LEFT)

    replace_btn = ttk.Button(
        action_bar,
        text="Replace All",
        bootstyle=SUCCESS,
        command=replace_text
    )
    replace_btn.pack(side=RIGHT)
