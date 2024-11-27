from tkinter import *
import requests
import json

df =  Tk()
df.title("Whether Status")
# df.maxsize(width=800,height=400)
# df.minsize(width=400,height=200)
lv1 = Label(df,text="***Whether Forcasting App***",bg="black",fg="white")
lv1.place(x=550,y=230)
photo = PhotoImage(file="logo.png")
lv2 = Label(df,image=photo)
lv2.pack()


v = StringVar()
def find():
    city = v.get()
    url = "https://api.weatherapi.com/v1/current.json?key=f7c52c5b9cf34b1eb7173703241311&q="+city

    df  = requests.get(url)
    data = json.loads(df.content)
    lv31.config(text=str(data["current"]["temp_c"]))
    
    lv41.config(text=str(data["current"]["temp_f"]))
 
    lv51.config(text=str(data["current"]["humidity"]))
    

entr = Entry(df,font=("calibary",30),bg="black",fg="white",textvariable=v)
entr.place(x=430,y=260)

btn = Button(text="Submit",bg="black",fg="white",command=find)
btn.place(x=600,y=320)

lv3= Label(text="Temprature in Celicus :-",fg="black")
lv3.place(x=450,y=350)

lv31= Label(text="Get Value",fg="black")
lv31.place(x=600,y=350)

lv4= Label(text="Temprature in Feranite :-",fg="black")
lv4.place(x=450,y=370)

lv41= Label(text="Get Value",fg="black")
lv41.place(x=600,y=370)

lv5= Label(text="Humidity :-",fg="black")
lv5.place(x=450,y=390)

lv51= Label(text="Get Value",fg="black")
lv51.place(x=600,y=390)
df.mainloop()