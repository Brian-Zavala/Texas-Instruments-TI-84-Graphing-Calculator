import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

class TI84Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("TI-84 Plus Calculator")
        self.root.geometry("400x600")  # Adjust size as needed
        self.root.configure(bg="#D0D0D0")  # Light gray background like the calculator
        
        # Set up the display
        self.setup_display()
        
        # Set up the keypad
        self.setup_keypad()
        
        # Initialize calculator state
        self.current_input = ""
        self.display_text.set("")
        
    def setup_display(self):
        # Create a frame for the display
        display_frame = tk.Frame(self.root, bg="#9AAC67", bd=2, relief=tk.SUNKEN)  # Greenish LCD color
        display_frame.pack(padx=20, pady=20, fill=tk.X)
        
        # Display text variable
        self.display_text = tk.StringVar()
        
        # Create the display label
        self.display = tk.Label(
            display_frame, 
            textvariable=self.display_text,
            font=("Courier", 14),
            anchor=tk.E,  # Right-aligned text
            bg="#9AAC67",  # Greenish LCD color
            fg="black",
            height=5,
            width=20
        )
        self.display.pack(padx=5, pady=5, fill=tk.BOTH, expand=True)
        
    def setup_keypad(self):
        # Create a frame for the keypad
        keypad_frame = tk.Frame(self.root, bg="#D0D0D0")
        keypad_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)
        
        # Define button styles
        number_btn_style = {
            "font": ("Arial", 12, "bold"),
            "bg": "#FFFFFF",
            "fg": "black",
            "width": 4,
            "height": 2,
            "relief": tk.RAISED
        }
        
        op_btn_style = {
            "font": ("Arial", 12),
            "bg": "#E0E0E0",
            "fg": "black",
            "width": 4,
            "height": 2,
            "relief": tk.RAISED
        }
        
        function_btn_style = {
            "font": ("Arial", 10),
            "bg": "#CCCCCC",
            "fg": "black",
            "width": 4,
            "height": 2,
            "relief": tk.RAISED
        }
        
        special_btn_style = {
            "font": ("Arial", 10),
            "bg": "#A0A0A0",
            "fg": "white",
            "width": 4,
            "height": 2,
            "relief": tk.RAISED
        }
        
        # Define button layout (simplified)
        # Row 0: Special buttons
        buttons = [
            {"text": "Y=", "row": 0, "col": 0, "style": special_btn_style},
            {"text": "WINDOW", "row": 0, "col": 1, "style": special_btn_style},
            {"text": "ZOOM", "row": 0, "col": 2, "style": special_btn_style},
            {"text": "TRACE", "row": 0, "col": 3, "style": special_btn_style},
            {"text": "GRAPH", "row": 0, "col": 4, "style": special_btn_style},
            
            # Row 1: Function buttons
            {"text": "2nd", "row": 1, "col": 0, "style": function_btn_style},
            {"text": "MODE", "row": 1, "col": 1, "style": function_btn_style},
            {"text": "DEL", "row": 1, "col": 2, "style": function_btn_style},
            {"text": "ALPHA", "row": 1, "col": 3, "style": function_btn_style},
            {"text": "STAT", "row": 1, "col": 4, "style": function_btn_style},
            
            # Row 2: More function buttons
            {"text": "MATH", "row": 2, "col": 0, "style": function_btn_style},
            {"text": "APPS", "row": 2, "col": 1, "style": function_btn_style},
            {"text": "PRGM", "row": 2, "col": 2, "style": function_btn_style},
            {"text": "VARS", "row": 2, "col": 3, "style": function_btn_style},
            {"text": "CLEAR", "row": 2, "col": 4, "style": function_btn_style},
            
            # Row 3: Math operations and parentheses
            {"text": "X", "row": 3, "col": 0, "style": function_btn_style},
            {"text": "(", "row": 3, "col": 1, "style": op_btn_style},
            {"text": ")", "row": 3, "col": 2, "style": op_btn_style},
            {"text": "÷", "row": 3, "col": 3, "style": op_btn_style},
            {"text": "ON", "row": 3, "col": 4, "style": special_btn_style},
            
            # Row 4-6: Numbers and operations
            {"text": "7", "row": 4, "col": 0, "style": number_btn_style},
            {"text": "8", "row": 4, "col": 1, "style": number_btn_style},
            {"text": "9", "row": 4, "col": 2, "style": number_btn_style},
            {"text": "×", "row": 4, "col": 3, "style": op_btn_style},
            {"text": "SIN", "row": 4, "col": 4, "style": function_btn_style},
            
            {"text": "4", "row": 5, "col": 0, "style": number_btn_style},
            {"text": "5", "row": 5, "col": 1, "style": number_btn_style},
            {"text": "6", "row": 5, "col": 2, "style": number_btn_style},
            {"text": "-", "row": 5, "col": 3, "style": op_btn_style},
            {"text": "COS", "row": 5, "col": 4, "style": function_btn_style},
            
            {"text": "1", "row": 6, "col": 0, "style": number_btn_style},
            {"text": "2", "row": 6, "col": 1, "style": number_btn_style},
            {"text": "3", "row": 6, "col": 2, "style": number_btn_style},
            {"text": "+", "row": 6, "col": 3, "style": op_btn_style},
            {"text": "TAN", "row": 6, "col": 4, "style": function_btn_style},
            
            # Row 7: Zero, decimal, and equals
            {"text": "0", "row": 7, "col": 0, "style": number_btn_style},
            {"text": ".", "row": 7, "col": 1, "style": number_btn_style},
            {"text": "(−)", "row": 7, "col": 2, "style": number_btn_style},
            {"text": "ENTER", "row": 7, "col": 3, "colspan": 2, "style": special_btn_style},
        ]
        
        # Create all buttons
        for btn in buttons:
            style = btn["style"].copy()  # Copy the style dict to avoid modifying the original
            
            # Handle buttons that span multiple columns
            colspan = btn.get("colspan", 1)
            if colspan > 1:
                style["width"] = style["width"] * colspan
            
            # Create the button
            button = tk.Button(
                keypad_frame, 
                text=btn["text"],
                command=lambda text=btn["text"]: self.button_click(text),
                **style
            )
            
            # Place the button in the grid
            button.grid(
                row=btn["row"], 
                column=btn["col"], 
                columnspan=btn.get("colspan", 1),
                padx=2, 
                pady=2, 
                sticky="nsew"
            )
        
        # Configure the grid to expand properly
        for i in range(8):  # 8 rows
            keypad_frame.grid_rowconfigure(i, weight=1)
        for i in range(5):  # 5 columns
            keypad_frame.grid_columnconfigure(i, weight=1)
    
    def button_click(self, value):
        if value == "CLEAR":
            self.current_input = ""
        elif value == "ENTER":
            try:
                # Replace the calculator symbols with Python operators
                expression = self.current_input.replace('×', '*').replace('÷', '/')
                result = eval(expression)
                self.current_input = str(result)
            except Exception as e:
                self.current_input = "Error"
        elif value == "DEL":
            self.current_input = self.current_input[:-1]
        elif value == "GRAPH":
            self.show_graph()
        elif value in ["Y=", "WINDOW", "ZOOM", "TRACE", "2nd", "MODE", "ALPHA", "STAT", 
                       "MATH", "APPS", "PRGM", "VARS", "ON", "SIN", "COS", "TAN"]:
            # For demonstration, just show these function names
            self.current_input += f" {value} "
        else:
            # For other buttons (numbers, operators), just append to input
            self.current_input += value
            
        # Update display
        self.display_text.set(self.current_input)
    
    def show_graph(self):
        # Simple demonstration of graphing capability
        try:
            # Create a new toplevel window for the graph
            graph_window = tk.Toplevel(self.root)
            graph_window.title("TI-84 Graph")
            graph_window.geometry("400x300")
            
            # Create a simple plot (y = x^2 as an example)
            fig, ax = plt.subplots(figsize=(5, 4))
            x = np.linspace(-10, 10, 1000)
            y = x**2  # Example function y = x^2
            ax.plot(x, y)
            ax.set_xlabel('x')
            ax.set_ylabel('y')
            ax.set_title('y = x^2')
            ax.grid(True)
            
            # Set a black background and green lines to mimic TI-84
            ax.set_facecolor('black')
            ax.spines['bottom'].set_color('green')
            ax.spines['top'].set_color('green')
            ax.spines['left'].set_color('green')
            ax.spines['right'].set_color('green')
            ax.tick_params(axis='x', colors='green')
            ax.tick_params(axis='y', colors='green')
            ax.yaxis.label.set_color('green')
            ax.xaxis.label.set_color('green')
            ax.title.set_color('green')
            fig.patch.set_facecolor('black')
            
            # Embed the plot in the tkinter window
            canvas = FigureCanvasTkAgg(fig, master=graph_window)
            canvas.draw()
            canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)
            
        except Exception as e:
            print(f"Error displaying graph: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TI84Calculator(root)
    root.mainloop()