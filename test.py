import PySimpleGUI as sg

default_gray = "gray25"
second_gray = "gray30"
sg.theme("Dark")

def new_layout(name, i):
    return [
        [
            sg.Text(name, key=("modname", i), size=(40,1)),
            sg.Button("↑", key=("up", i)),
            sg.Button("↓", key=("down", i)),
            sg.Button("🗑", key=("delete", i))
        ]
    ]

plist = ["a", "b", "c"]

firstmodname = "placeholder"

column_layout = [
    [
        sg.Text(firstmodname, key=("modname", 0), size=(40,1)),
        sg.Button("↑", key=("up", 0)),
        sg.Button("↓", key=("down", 0)),
        sg.Button("🗑", key=("delete", 0))
    ]
]

editor_layouts = [
    [sg.text("Profiles editor", background_color=default_gray)],
    [
        sg.Text("Select Profile", background_color=default_gray),
        sg.Combo(
            [],
            size=(40, 1),
            background_color=second_gray,
            text_color="White",
            key="profileselector",
            expand_x=True,
        ),
    ],
    [
        sg.Column(column_layout, size=(50, 10), scrollable=True, vertical_scroll_only=True, visible=False)
    ]
    [sg.Button("Start editing", key="starteditor")]
]

ewindow = sg.Window("Profiles Editor", editor_layouts, return_keyboard_events=True, resizable=True)

while True:
    event, values = ewindow.read()
    if event == sg.WIN_CLOSED:
        #check for attemp to close
        break
    elif event == "starteditor":
        #get mods list in profile
        
        pass