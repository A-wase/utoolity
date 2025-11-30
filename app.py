import os
import importlib
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

TOOLS_FOLDER = "tools"

class UtilityApp(ttk.Window):
    def __init__(self):
        super().__init__(themename="cosmo")
        self.title("Utility App")
        self.geometry("800x500")

        # ----- Layout -----
        self.sidebar = ttk.Frame(self, padding=10)
        self.sidebar.pack(side=LEFT, fill=Y)

        self.main_area = ttk.Frame(self, padding=20)
        self.main_area.pack(side=RIGHT, fill=BOTH, expand=True)

        header = ttk.Label(
            self.main_area,
            text="Select a tool from the left",
            font="-size 18 -weight bold"
        )
        header.pack(pady=10)

        # Load tools
        self.tools = self.load_tools()
        self.build_sidebar()

    # --------------------------------------------------
    # Auto-discover tool modules
    # --------------------------------------------------
    def load_tools(self):
        tools = {}

        for filename in os.listdir(TOOLS_FOLDER):
            if filename.endswith(".py") and filename != "__init__.py":
                module_name = filename[:-3]
                module = importlib.import_module(f"{TOOLS_FOLDER}.{module_name}")

                # Tool must have a build(container) function
                if hasattr(module, "build"):
                    tools[module_name] = module.build

        return tools

    # --------------------------------------------------
    # Sidebar listing each tool
    # --------------------------------------------------
    def build_sidebar(self):
        title = ttk.Label(
            self.sidebar,
            text="Tools",
            font="-size 14 -weight bold",
            anchor="w"
        )
        title.pack(fill=X, pady=(0, 10))

        for tool_name, tool_func in self.tools.items():
            pretty = tool_name.replace("_", " ").title()

            button = ttk.Button(
                self.sidebar,
                text=pretty,
                bootstyle=PRIMARY,
                command=lambda f=tool_func: self.open_tool(f)
            )
            button.pack(fill=X, pady=5)

    # --------------------------------------------------
    # Load & display tool in main area
    # --------------------------------------------------
    def open_tool(self, tool_func):
        for widget in self.main_area.winfo_children():
            widget.destroy()

        tool_func(self.main_area)


if __name__ == "__main__":
    app = UtilityApp()
    app.mainloop()
