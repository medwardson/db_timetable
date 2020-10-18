import tkinter as tk
from tkinter import font
import requests
HEIGHT = 700
WIDTH = 800

def test_function(entry):
    print("This is the entry: ",entry)
# 4118a636e49235b4ac502e8672ed87a3
# api.openweathermap.org/data/2.5/forecast?q={city name},{state code},{country code}&appid={API key}

"""
    def format_response(weather):
        try:
            name = weather['name']
            desc = weather['weather'][0]['description']
            temp = weather['main']['temp']

            final_str = 'City: %s \nConditions: %s \nTemperature (F): %s' % (name,desc,temp)
        except:
            final_str = 'There was a problem retrieving that information'

        return final_str

    def get_weather(city):
        weather_key = '4118a636e49235b4ac502e8672ed87a3'
        url = 'https://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': weather_key, 'q':city, 'units':'imperial' }
        response = requests.get(url, params=params)
        weather = response.json()
        label['text'] = format_response(weather)
"""


root = tk.Tk()

#enlarges the screen to the inputted size, when program is ran
canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()


background_image = tk.PhotoImage(file='notepadbackgroundpng.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)
#Creates the blue frame, centers it and sets it to the middle with a color of blue written in hexadecimal
frame = tk.Frame(root, bg='#80c1ff',bd = 5)
frame.place(relx = 0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')




#entry = tk.Entry(frame, font=('Courier',18))
#entry.place(relwidth=0.65, relheight=1)


#Creates the button
#button = tk.Button(frame, text="Get Weather", font=('Courier',18), command=lambda: get_weather(entry.get()))
#button.place(relx=0.7,relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.2, relwidth=0.75, relheight=0.7, anchor='n')


#creates a label
label = tk.Label(lower_frame, text=' Tracker Menu:',font=('Courier',30), anchor='nw', justify='left', bd=6)
label.place(relwidth=1, relheight=1)

button1 = tk.Button(lower_frame, text="1. Add student", font=('Courier',18))
button1.place(rely = 0.2, relwidth=0.4)

button2 = tk.Button(lower_frame, text="2. Get a students info", font=('Courier',18))
button2.place(rely = 0.35, relwidth=0.6)

button3 = tk.Button(lower_frame, text="3. Delete a student", font=('Courier',18))
button3.place(rely = 0.5, relwidth=0.6)

button4 = tk.Button(lower_frame, text="4. Edits student class", font=('Courier',18))
button4.place(rely = 0.65, relwidth=0.6)

button5 = tk.Button(lower_frame, text="5. Quit", font=('Courier',18))
button5.place(rely = 0.8, relwidth=0.4)


Upper_label = tk.Label(frame, text= 'Student Timetable Tracker', font=('Courier',18))
Upper_label.place(relwidth=1, relheight=1)


root.mainloop()
