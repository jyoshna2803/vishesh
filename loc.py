from tkinter import *
import time
import sys
a=Tk()
a.title("LOCATION DETECTOR")
a.configure(bg="black")
a.geometry("750x1200")
l1=Label(a,text="Location Tracker",font=("times new roman",30),bg="black",fg="white")
l1.pack()
l2=Label(a,text="Enter Phone Number :",font=("times new roman",20),bg="black",fg="white")
l2.place(x=250,y=80)
e1=Entry(a,width=40)
e1.place(x=250,y=120)
a.resizable(False,False)
def call():

    import phonenumbers
    import folium
    from geopy import Nominatim

    from phonenumbers import geocoder, timezone
    key = "7f7e22d3a52f4f4aa06ae46543ef5b07"
    number = e1.get()

    samnumber = phonenumbers.parse(number)

    yourlocation = geocoder.description_for_number(samnumber, "en")
    timezone = timezone.time_zones_for_number(samnumber)
    l3=Label(a,text=" ",bg="black",fg="white",font=("times new roman",18))
    l3.place(x=230,y=220)
    l3.configure(text=yourlocation)
    l8 = Label(a, text=" ", bg="black")
    l8.place(x=230, y=300)
    from phonenumbers import carrier
    service_provider = phonenumbers.parse(number, "RO")
    sp=carrier.name_for_number(service_provider, "en")
    l4 = Label(a, text=" ",bg="black",fg="white",font=("times new roman",18))
    l4.place(x=230, y=250)
    l4.configure(text=sp)
    l5 = Label(a, text=" ", bg="black",fg="white",font=("times new roman",18))
    l5.place(x=230, y=280)
    l5.configure(text=timezone)
    from opencage.geocoder import OpenCageGeocode
    geocoder = OpenCageGeocode(key)

    query = str(yourlocation)
    results = geocoder.geocode(query)
    lat=results[0]['geometry']['lat']

    lng=results[0]['geometry']['lng']
    l9=Label(a,text="Country:",bg="black",fg="white",font=("times new roman",18))
    l9.place(x=0,y=220)
    l10= Label(a, text="Service Provider:", bg="black", fg="white", font=("times new roman", 18))
    l10.place(x=0, y=250)
    l11= Label(a, text="Time Zone:", bg="black", fg="white", font=("times new roman", 18))
    l11.place(x=0, y=280)
    if yourlocation=="India":
    #print("latitude:",lat)
        # print("longitude:",lng)
        # coord=(lat,lng)

        geolocator = Nominatim(user_agent="geoapiexercises")
        location = geolocator.reverse((17.5585, 78.4513))
        location2 = geolocator.geocode(yourlocation)
        lkg = location2.latitude
        ukg = location2.longitude
        addr = location.address
        l6 = Label(a, text=" ", bg="black",fg="white",font=("times new roman",18))
        l6.place(x=230, y=310)
        text2="latitude:17.5585,longitude:78.4513"
        l6.configure(text=text2)

        l7 = Label(a,text=" ",bg="black",fg="white",font=("times new roman",18))
        l7.place(x=230, y=340)
        l7.configure(text="Hyderabad")
        myMap = folium.Map(location=[17.5585, 78.4513], zoom_start=9)
        folium.Marker([17.5585, 78.4513], popup=addr[5]).add_to((myMap), "en")
    # save in html

        myMap.save("mylocation.html")

    else:

        geolocator = Nominatim(user_agent="geoapiexercises")
        location = geolocator.reverse((lat,lng))
        location2 = geolocator.geocode(yourlocation)
        lkg = location2.latitude
        ukg = location2.longitude
        addr = location.address
        l6 = Label(a, text=" ", bg="black",fg="white", font=("times new roman", 18))
        l6.place(x=230, y=310)
        l6.configure(text=(lat,lng))
        l7 = Label(a, text=" ", bg="black",fg="white", font=("times new roman", 18))
        l7.place(x=0, y=340)
        l7.configure(text=addr)
        myMap = folium.Map(location=[lat,lng], zoom_start=9)
        folium.Marker([lat,lng], popup=addr[5]).add_to((myMap), "en")
        myMap.save("mylocation.html")

btn= Button(a, text="Trace", command=call, bg="black", fg="white", font=("times new roman", 18),
                 activebackground="white", activeforeground="black")
btn.place(x=320, y=170)
a.mainloop()