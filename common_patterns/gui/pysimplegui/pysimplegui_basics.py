import PySimpleGUI as sg

layout = [[sg.Text("Hello to the sarcastic fish")], [sg.Button("OK")]]

# Create the window
window = sg.Window("Lets 'ave a look then", layout)

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # pressed the OK button
    if event == "OK":
        window.set_title("OK was pressed")
    elif event == sg.WIN_CLOSED:
        break

window.ding()