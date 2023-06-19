import PySimpleGUI as sg
import openai
from pyperclip import copy

openai.api_key = 'TYPE_YOUR_API_KEY_HERE'  # How to creat an api key in the README...

sg.theme('DarkPurple1')

layout = [
    [sg.Text('Ask something...')],
    [sg.InputText(key='-INPUT-', size=165)],
    [sg.Button('ask'), sg.Button('Close app'), sg.Button('Copy text')],
    [sg.Text('Answer:', size=(150, 35), key='-OUTPUT-')]
]


window = sg.Window('Desktop ChatGPT', layout)

def ask_question(question):
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=question,
        max_tokens=3000,
        n=1,
        stop=None,
        temperature=0.7
    )
    answer = response.choices[0].text.strip()
    return answer

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == 'Close app':
        break
    elif event == 'ask':
        try:
            question = values['-INPUT-']
            answer = ask_question(question)
            window['-OUTPUT-'].update(answer)
        except:
            window['-OUTPUT-'].update('ATENTION...\nERROR: Check if you put your api key correctly')
    elif event == 'Copy text':
        var_to_copy = answer
        copy(var_to_copy)

window.close()
