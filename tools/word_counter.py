import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def build(container):
    title = ttk.Label(
        container,
        text="Word Counter",
        font="-size 18 -weight bold"
    )
    title.pack(pady=(0, 15))

    text_box = ttk.Text(container, height=12)
    text_box.pack(fill=BOTH, expand=True, pady=5)

    result_label = ttk.Label(container, text="", font="-size 12")
    result_label.pack(pady=10)

    def count_words():
        text = text_box.get("1.0", "end").strip()
        words = len(text.split())
        chars = len(text)
        result_label.config(text=f"Words: {words}   Characters: {chars}")

    count_btn = ttk.Button(
        container,
        text="Count",
        bootstyle=SUCCESS,
        command=count_words
    )
    count_btn.pack(pady=5)
