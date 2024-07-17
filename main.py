from flet import (
    app,
    Page,
    ResponsiveRow,
    Container,
    Text,
    TextField,
    colors,
    Padding,
    Margin,
    Image,
    LinearGradient,
    Row,
    Column,
    animation,
    Divider,
    padding,
    FloatingActionButton,
    SnackBar,
)
from time import sleep
import requests



def main(page:Page):
    page.window.height = 740
    page.window.width = 360
    page.horizontal_alignment = "center"
    page.theme_mode = 'dark'
    page.bgcolor = 'black'



    def show_weather(e):
        City = searchbox.value
        _api = f"https://api.openweathermap.org/data/2.5/weather?q={City}&appid=35d1f8809c55d6524936b21a958f9904"
        if searchbox.data == "true":
            if weatherbox.height == 0 :
                weatherbox.height = 700 * 0.6
                page.update()

            else:
                weatherbox.height = 700 * 0.0
                page.update()
                sleep(2)
                weatherbox.height = 700 * 0.6
                page.update()

        try:
            response = requests.get(_api)
            data = response.json()

            main = data['main']
            weather = data['weather'][0]
                    
            _temp = main['temp']
            _desc = weather['description']
            _icon = weather['icon']
            _icon_url = f"http://openweathermap.org/img/wn/{_icon}@4x.png"
            _windspeed = data['wind']['speed']
            _humidity = main['humidity']
            _pressure = main['pressure']

            
            city.value = str(City)
            temp.value = str((int(_temp)-273.15//1))+"°C"
            desc.value = _desc
            weather_icon.src = _icon_url
            wspeed.value = f"{_windspeed}km/h"
            humid.value = f"{_humidity}%"
            pres.value = f"{_pressure}hPa"
            page.update()

        except Exception as E:
            city.value = "Not Found!"
            print(E)
            page.update()

        page.update()



    searchbox = TextField(
        border_color=colors.LIGHT_BLUE_600,
        border_radius=18,
        color='white',
        border_width=2,
        text_align='center',
        suffix_icon='search',
        label="City",
        hint_text="e.g. New York",
        on_submit=lambda e:show_weather(e),
        data="true",

        )

    city = Text(
            value="---- ----",
            weight="w500",
            color='white',
            size = 24,
            )
    
    weather_icon = Image(src='cloudy.png',aspect_ratio=1)
    
    temp = Text(
            value="--°C",
            weight="w400",
            color='white',
            size = 50,
    )
    desc = Text(
            value='--- ---',
            color='white70',
            weight='w400',
            size=16,
        )
    
    wspeed = Text('-- km/h',size=20)

    humid = Text('-- %',size=20)

    pres = Text('-- hPa',size=20)
            
    weather = Column(
            [
                city,
                Container(
                    Row(
                        [
                            weather_icon,
                            Column(
                                [
                                Text(
                                    value="Today",
                                    weight="w300",
                                    color='white',
                                    size = 20,
                        
                                ),
                                temp,
                                desc,

                                ],
                                horizontal_alignment='center',
                                alignment='center',
                                spacing=1,
                                
                            ),
                            
                        ],
                        alignment='center',
                    ),
                    
                    width=240,
                    height=120,
                   
                    margin=Margin(top=6,bottom=6,right=0,left=0)
                ),
                Divider(color='white',thickness=0.7,height=2),

                Container(
                    
                    height=100,
                    width=340,
                    content=Row(
                        vertical_alignment="center",
                        alignment="center",
                        spacing=32,
                        controls=[
                            Column(
                                [
                                    Image(src='wind.png',height=38,width=38),
                                    wspeed,
                                    Text('wind',size=10),
                                ],
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=1,
                            
                                
                            ),
                            Column(
                                [
                                    Image(src='humidity.png',height=38,width=38),
                                    humid,
                                    Text('humidity',size=10),
                                ],
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=1,
                            ),
                            Column(
                                [
                                    Image(src='pressure.png',height=38,width=38),
                                    pres,
                                    Text('pressure',size=10),
                                ],
                                alignment='center',
                                horizontal_alignment='center',
                                spacing=1,
                            ),
                            
                        ]
                    )

                ),
                Container(
                    Text("Powered by OpenWeatherMap",opacity=0.25),
                    
                    
                ),
                Container(
                    Text("Created by Aditya",weight="w500",italic=True,color="black"),
                    padding=padding.only(top=17),
                    
                ),
                        
            ],
            horizontal_alignment='center',

        )
        


    weatherbox = Container(
        padding=Padding(top=5,left=10,right=10,bottom=20),
        margin=Margin(left=0,right=0,bottom=5,top=5),
        gradient=LinearGradient(colors=[colors.LIGHT_BLUE_400,colors.LIGHT_BLUE_600,colors.LIGHT_BLUE_800]),
        height= 700 * 0.6,
        border_radius=18,
        animate= animation.Animation(duration=500,curve='decelerate'),
        content=weather,
        


    )
    def fab_pressed(e):
        page.open(
            SnackBar(Text("This a project of Aditya ",color='white'), open=True ,duration=3000,bgcolor=colors.LIGHT_BLUE_600)
        )

    page.floating_action_button = FloatingActionButton(
        icon='info', on_click=fab_pressed, bgcolor=colors.LIGHT_BLUE_900,mini=True,
    )

    page.add(
        ResponsiveRow(
            [
                searchbox,
                weatherbox,
                
            ],
            alignment="center"

        ),

    )

    page.update()

app(target=main,assets_dir='assets')