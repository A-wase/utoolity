# Utility Toolbox (Python + ttkbootstrap)

A modular desktop utility application built with **Python**, **Tkinter**, and **ttkbootstrap**.  
This app provides a clean main menu with multiple tools, and supports a **plugin-style system**:  
any Python script placed inside the `tools/` folder is automatically detected and added to the UI.

This allows you (and other users) to easily create new tools without modifying the core app.

---

## ✨ Features

- 🧩 **Plugin-based architecture**  
  Drop a Python file into the `tools/` folder and it becomes a selectable tool.

- 🎨 **Modern UI using ttkbootstrap**  
  Clean styling, theme support, responsive layouts.

- 📋 **Built-in tools included**
  - Word Counter  
  - Age Calculator  
  - Clock  
  - (More coming soon…)

- ⚙️ **Self-contained and extendable**  
  Tools can be shared as standalone `.py` files.


---

## 🚀 Running the App

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd project


2. **(Recommended) Create a virtual environment**

   **Windows**

   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```

   **macOS / Linux**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the app**

   ```bash
   python app.py
   ```

---

## 🧩 Creating Your Own Tools

To create a new tool:

1. Inside the `tools/` folder, create a Python file:

   ```
   tools/my_tool_name.py
   ```

2. Inside that file, **define a single function** with this signature:

   ```python
   def build(container):
       # Create your UI using ttk / ttkbootstrap widgets
       # Pack/place/grid them inside the provided container
       ...
   ```

3. The app will automatically:

   * Import the file
   * Add it to the main menu
   * Display your UI when selected

### Example Template

```python
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def build(container):
    label = ttk.Label(container, text="Hello from my tool!", font="-size 16")
    label.pack(pady=20)
```