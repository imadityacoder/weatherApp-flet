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
    Icon,
    icons,
    ThemeMode,
    Theme,
    LinearGradient,
    Row,
    Column,
    alignment,
    FontWeight,
    animation,
    IconButton,
    AppView,
    ImageFit,
    Divider


)
import time
# import requests

# _api = "https://api.openweathermap.org/data/2.5/weather?q=patna&appid=35d1f8809c55d6524936b21a958f9904"

# req  = requests.get(_api).json()
# print(req)

def main(page:Page):
    page.window.height = 700
    page.window.width = 340
    page.horizontal_alignment = "center"
    page.theme_mode = 'dark'
    page.bgcolor = 'black'


    def show_weather(e):
        if searchbox.data == "true":
            if weatherbox.height == 0 :
                weatherbox.height = 700 * 0.5
                page.update()

            else:
                weatherbox.height = 700 * 0.0
                page.update()
        
                time.sleep(0.8)
                weatherbox.height = 700 * 0.5
                page.update()

        else: 
            weatherbox.height = 0
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
        on_submit=show_weather,
        data="true",

        )


    weatherbox = Container(
        padding=Padding(top=5,left=10,right=10,bottom=20),
        margin=Margin(left=0,right=0,bottom=5,top=5),
        gradient=LinearGradient(colors=[colors.LIGHT_BLUE_400,colors.LIGHT_BLUE_600,colors.LIGHT_BLUE_800]),
        height= 700 * 0.0,
        border_radius=18,
        animate= animation.Animation(duration=500,curve='decelerate'),

    
        content=Column(
            [
                Text(
                    value="PATNA",
                    weight="w500",
                    color='white',
                    size = 24,
                    
                ),

                Container(
                    Row(
                        [
                            Image(src='cloudy.png',aspect_ratio=1),
                            Column(
                                [
                                Text(
                                    value="40'C",
                                    weight="w400",
                                    color='white',
                                    size = 50,
                        
                                ),
                                Text(
                                    value='clear sky',
                                    color='white70',
                                    weight='w400',
                                    size=16,
                                     )

                                ],
                                horizontal_alignment='center',
                                alignment='center'
                                
                            ),
                            
                        ],
                        alignment='center',
                    ),
                    
                    width=240,
                    height=120,
                   
                    margin=Margin(top=6,bottom=6,right=0,left=0)
                ),
                Divider(color='white',thickness=0.7)
                
            ],
            horizontal_alignment='center',

        ),
        


    )


    page.add(
        ResponsiveRow(
            [
                searchbox,
                weatherbox,
                
            ],
            alignment="center"

        )
        )
    page.update()
app(target=main,view=AppView.WEB_BROWSER,assets_dir='assets')