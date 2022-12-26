input_string = " ☐B - PURCHASE DEVICE: "
new_string = input_string.encode("ascii",errors="ignore").decode()
newer_string = new_string.strip()
print(new_string)