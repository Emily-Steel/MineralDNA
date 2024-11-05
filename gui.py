import tkinter as tk
from mineral_DNA import calculate_mineral_DNA, positions

def is_valid_date(d: str) -> bool:
    if len(d) == 0:
        return False
    parts = d.split("/")
    if len(parts) != 3:
        return False
    day, month, year = parts
    return len(day) in [1, 2] and len(month) in [1, 2] and len(year) == 4

def update_outputs(*args):
    name = name_var.get().split(" ")
    surname = surname_var.get().split(" ")
    dob = dob_var.get()

    results = [""] * 13
    if len(name) >= 1 and len(surname) >= 1 and is_valid_date(dob):
        # Call the calculation function with the current inputs
        dna = calculate_mineral_DNA(name, surname, dob)
        results = [stone for _, stone in dna]

    # Update the output fields
    for i in range(13):
        output_vars[i].set(results[i])

# Create the main window
root = tk.Tk()
root.title("Mineral DNA Calculator")

# Input fields
name_var = tk.StringVar()
surname_var = tk.StringVar()
dob_var = tk.StringVar()

tk.Label(root, text="Name:").grid(row=0, column=0)
name_entry = tk.Entry(root, textvariable=name_var)
name_entry.grid(row=0, column=1)

tk.Label(root, text="Surname:").grid(row=1, column=0)
surname_entry = tk.Entry(root, textvariable=surname_var)
surname_entry.grid(row=1, column=1)

tk.Label(root, text="Date of Birth:").grid(row=2, column=0)
dob_entry = tk.Entry(root, textvariable=dob_var)
dob_entry.grid(row=2, column=1)

# Output fields (non-editable)
output_vars = [tk.StringVar() for _ in positions]
for i in range(13):
    position_name = positions[i].get_name_en()
    tk.Label(root, text=f"Pierre {position_name}:").grid(row=3 + i, column=0)
    output_entry = tk.Entry(root, textvariable=output_vars[i], state='readonly')
    output_entry.grid(row=3 + i, column=1)

# Bind the input fields to the update function
name_var.trace("w", update_outputs)
surname_var.trace("w", update_outputs)
dob_var.trace("w", update_outputs)

# Run the application
root.mainloop()