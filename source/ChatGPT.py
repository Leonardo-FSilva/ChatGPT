# imports
import PySimpleGUI as sg
import openai
from pyperclip import copy

# type your openai api key bellow
openai.api_key = 'TYPE_YOUR_API_KEY_HERE'  # How to creat an api key in the README...

# theme of the window
sg.theme('DarkPurple1')

# the structure of window
layout = [
    [sg.Text('Ask something...')],
    [sg.InputText(key='-INPUT-', size=165)],
    [sg.Button('ask'), sg.Button('Close app'), sg.Button('Copy text')],
    [sg.Text('Answer:', size=(150, 35), key='-OUTPUT-')]
]

# create a window with name "Desktop GPT Chat"
window = sg.Window('Desktop GPT Chat', layout)

# function that receive a question and return GPT answer
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

# inside an infinite loop otherwise any interaction with the window will close it
while True:
    event, values = window.read()  # events is mouse clicks and values is what is typed in filds
    if event == sg.WINDOW_CLOSED or event == 'Close app':
        break  # close window
    elif event == 'ask':
        try:  # try connect with GPT Chat server
            question = values['-INPUT-']
            answer = ask_question(question)
            window['-OUTPUT-'].update(answer)
        except:  # if the software can't connect to server will return the message bellow
            window['-OUTPUT-'].update('ATENTION...\nERROR: Check if you put your api key correctly')
    elif event == 'Copy text':
        var_to_copy = answer
        copy(var_to_copy)

window.close()
