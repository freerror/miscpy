import re
import tkinter as tk


# Make fstr a Thing(tm)
def fstr(template, email_body, email_subject):
    return eval(f"f'{template}'")


# Create input window
window = tk.Tk()
label_in = tk.Label(text="f-string:")
label_out = tk.Label(text="Output:")
text_box = tk.Text(
    width=100,
    height=2,
)
check_button = tk.Button(
    text="Evaluate",
    width=10,
    height=2,
)
out_box = tk.Text(
    width=100,
    height=20,
)

# Event Manager for Window
def handle_click(event):
    # Get entered fstring
    input_fstring = text_box.get("1.0", "end-1c")

    # Get the sample email
    with open(
        "common_patterns/gui/sample_email.txt", "r", encoding="utf-8"
    ) as f:
        sample_email = f.read()
        email_subject = sample_email.split("===subject:===\n")[1].split(
            "\n===body:==="
        )[0]
        email_body = sample_email.split("===body:===\n")[1]

    # Print the resulting string
    out_box.delete("1.0", "end")
    for line in input_fstring.split("\n"):
        out_box.insert("end", fstr(line, email_body, email_subject))


check_button.bind("<Button-1>", handle_click)

label_in.pack()
text_box.pack()
check_button.pack()
label_out.pack()
out_box.pack()
window.mainloop()
