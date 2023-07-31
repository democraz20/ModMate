import PySimpleGUI as sg

default_gray = "gray25"
second_gray = "gray30"
sg.theme("Dark")

plist = ["a", "b", "c"]

column_lay

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
    [sg.Button("Start editing", key="starteditor")]
]