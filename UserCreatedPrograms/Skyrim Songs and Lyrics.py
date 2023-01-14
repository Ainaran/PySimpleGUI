import PySimpleGUI as sg
from tkhtmlview import html_parser

def set_html(widget, html, strip=True):
    prev_state = widget.cget('state')
    widget.config(state=sg.tk.NORMAL)
    widget.delete('1.0', sg.tk.END)
    widget.tag_delete(widget.tag_names)
    html_parser.w_set_html(widget, html, strip=strip)
    widget.config(state=prev_state)

sg.theme('DarkTeal9')

Songnames = ['Dragonborn Comes', 'Ragnar the Red', 'Tale of Tongues', 'Age of Aggression', 'Bonus: Skyrim (Main Title)']
Leftcolumn = [[sg.Listbox(Songnames, size=(60,10), enable_events= True, key='-Song List-')]]
Rightcolumn = [[sg.Text("", key='-Song Lyrics-')]]
#copy-paste layout
layout_SkyrimVideo = [
    [sg.Multiline(
        size=(1,25),
        border_width=2,
        text_color='white',
        background_color='black',
        disabled=True,
        no_scrollbar=True,
        expand_x=True,
        expand_y=True,
        justification='center',
        key='SkyrimVideo')],]
#copy-paste layout

Skyrim_layout = [
    [sg.Text('Elder Scrolls V Skyrim Music and Lyrics', size=(40,1), font='Helvetica', background_color='black', text_color='red', justification='center')],
    [sg.Column(Leftcolumn),sg.VSeperator(),
     sg.Frame("Video",  layout_SkyrimVideo, expand_x=True, expand_y=False)],
    [sg.Column(Rightcolumn, element_justification ='center' , size=(350,750), scrollable =True, vertical_scroll_only =True)],
]

"""while True:
    event, values = Songlistbox.read()
    if event == "Dragonborn Comes" :
        sg.Window
"""
Skyrim_window = sg.Window('My Skrim Music Library', Skyrim_layout, finalize =True, use_default_focus =False, size=(1000,850), element_justification='center', resizable =True)
SongListbox = Skyrim_window['-Song List-']

html_default = """
    <div class="infobox-caption" style="text-align:center;color:white">Please select a song from the list to listen it and read its lyrics</div></td>
"""

html_dragonborncomes = """
     <p style="text-align:center;"><td colspan="2"><a href="https://www.youtube.com/embed/4z9TdDCWN7g?autohide=1&autoplay=1">
<img src="https://i.ytimg.com/vi/4z9TdDCWN7g/hqdefault.jpg"></a>
<div class="infobox-caption" style="text-align:center;color:white">Click on image to listen the song from Youtube</div></td></p>
"""

DCLyrics = """Our hero, our hero, claims a warriors heart
I tell you, I tell you, the Dragonborn comes
With a voice wielding power of the ancient nord arts
Believe, believe, the Dragonborn comes

It's an end to the evil of all Skyrim's foes
Beware, beware, the Dragonborn comes
For the darkness has passed, and the legend yet grows
You'll know, you'll know, the Dragonborns come

Dovahkiin, Dovahkiin
Naal ok zin los vahriin
Wah dein vokul mahfaeraak ahst vaal
Ahrk fin norok paal graan
Fod nust hon zindro zaan
Dovahkiin, fah hin kogaan mu draal"""

html_ragnarthered = """
    <p style="text-align:center;"><td colspan="2"><a href="https://www.youtube.com/embed/eBo9IrJxQzw?autohide=1&autoplay=1">
    <img src="https://i.ytimg.com/vi/eBo9IrJxQzw/hqdefault.jpg" class="center"></a>
<div class="infobox-caption" style="text-align:center;color:white">Click on image to listen the song from Youtube</div></td></p>
"""

RTRLyrics = """Oh, there once was a hero named Ragnar the Red
Who came riding to Whiterun from ole Rorikstead
And the braggart did swagger and brandish his blade
As he told of bold battles and gold he had made

But then he went quiet, did Ragnar the Red
When he met the shieldmaiden Matilda who said
Oh, you talk and you lie and you drink all our mead
Now I think it's high time that you lie down and bleed

And so then came clashing and slashing of steel
As the brave lass Matilda charged in full of zeal
And the braggart named Ragnar was boastful no more
When his ugly red head rolled around on the floor

And the braggart named Ragnar was boastful no more
When his ugly red head rolled around on the floor"""



html_taleoftongues = """
     <p style="text-align:center;"><td colspan="2"><a href="https://www.youtube.com/embed/UjEpw4O-WNI?autohide=1&autoplay=1">
<img src="https://i.ytimg.com/vi/UjEpw4O-WNI/hqdefault.jpg"></a>
<div class="infobox-caption" style="text-align:center;color:white">Click on image to listen the song from Youtube</div></td></p>
"""

ToTLyrics = """Alduin's wings, they did darken the sky
His roar fury's fire and his scales sharpened scythes
Men ran and they cowered and they fought and they died
They burned and they bled as they issued their cries

Dovahkiin Dovahkiin naal ok zin los vahriin
Wah dein vokul mahfaeraak ahst vaal
Ahrk fin norok paal graan fod nust hon zindro zaan
Dovahkiin fah hin kogaan mu draal

We need saviors to free us from Alduin's rage
Heroes on the field of this new war to wage
And if Alduin wins man is gone from this world
Lost in the shadow of the black wings unfurled
But then came the Tongues on that terrible day
Steadfast as winter, they entered the fray
And all heard the music of Alduin's doom
The sweet song of Skyrim, sky-shattering Thu'um

And so the Tongues freed us from Alduin's rage
Gave the gift of the Voice, ushered in a new Age
If Alduin is eternal, then eternity's done
For his story is over and the dragons... are gone"""


html_ageofaggression = """
     <p style="text-align:center;"><td colspan="2"><a href="https://www.youtube.com/embed/KNDT7EInclo?autohide=1&autoplay=1">
<img src="https://i.ytimg.com/vi/KNDT7EInclo/hqdefault.jpg"></a>
<div class="infobox-caption" style="text-align:center;color:white">Click on image to listen the song from Youtube</div></td></p>
"""

AOALyrics = """We drink to our youth, for the days come and gone
For the age of aggression is just about done
We'll drive out the Stormcloaks and restore what we own
With our blood and our steel we will take back our home

Down with Ulfric, the killer of kings
On the day of your death we will drink and we'll sing
We're the children of Skyrim, and we fight all our lives
And when Sovngarde beckons everyone of us dies
But this land is ours and we'll see it whiped clean
Of the scourge that has sullied our hopes and our dreams

Down with Ulfric, the killer of kings
On the day of your death we will drink and we'll sing
We're the children of Skyrim, and we fight all our lives
And when Sovngarde beckons everyone of us dies

We drink to our youth, for the days come and gone
For the Age of Aggression is just about done"""




html_skyrimmaintitles = """
     <p style="text-align:center;"><td colspan="2"><a href="https://www.youtube.com/embed/BSLPH9d-jsI?autohide=1&autoplay=1">
<img src="https://i.ytimg.com/vi/BSLPH9d-jsI/hqdefault.jpg"></a>
<div class="infobox-caption" style="text-align:center;color:white">Click on image to listen the song from Youtube</div></td></p>
"""

SMTLyrics = """Dovahkiin, Dovahkiin
Naal ok zin los vahriin
Wah dein vokul mahfaeraak ahst vaal!
Ahrk fin norok paal graan
Fod nust hon zindro zaan
Dovahkiin, fah hin kogaan mu draal!

Huzrah nu, kul do od, wah aan bok lingrah vod
Ahrk fin tey, boziik fun, do fin gein!
Wo lost fron wah ney dov
Ahrk fin reyliik do jul
Voth aan suleyk wah ronit faal krein
Ahrk fin kel lost prodah
Do ved viing ko fin krah
Tol fod zeymah win kein meyz fundein!
Alduin, feyn do jun
Kruziik vokun staadnau
Voth aan bahlok wah diivon fin lein!

Nuz aan sul, fent alok
Fod fin vul dovah nok
Fen kos nahlot mahfaeraak ahrk ruz!
Paaz Keizaal fen kos stin nol bein Alduin jot!"""


#html element settings
for element in Skyrim_window.key_dict.values():
    element.block_focus()
VideoPlayer = Skyrim_window['SkyrimVideo'].Widget
html_parser = html_parser.HTMLTextParser()
set_html(VideoPlayer, html_default)
width, height = VideoPlayer.winfo_width(), VideoPlayer.winfo_height()
#html element settings

Skyrim_window.read()

while True:
    event, values = Skyrim_window.read()
    if SongListbox.get() == ['Dragonborn Comes'] :
        Skyrim_window['-Song Lyrics-'].update(value = DCLyrics)
        for element in Skyrim_window.key_dict.values():
            element.block_focus()
        VideoPlayer = Skyrim_window['SkyrimVideo'].Widget
        set_html(VideoPlayer, html_dragonborncomes)
        width, height = VideoPlayer.winfo_width(), VideoPlayer.winfo_height()
    elif SongListbox.get() == ['Ragnar the Red'] :
        Skyrim_window['-Song Lyrics-'].update(value=RTRLyrics)
        for element in Skyrim_window.key_dict.values():
            element.block_focus()
        VideoPlayer = Skyrim_window['SkyrimVideo'].Widget
        set_html(VideoPlayer, html_ragnarthered)
        width, height = VideoPlayer.winfo_width(), VideoPlayer.winfo_height()
    elif SongListbox.get() == ['Tale of Tongues']:
        Skyrim_window['-Song Lyrics-'].update(value=ToTLyrics)
        for element in Skyrim_window.key_dict.values():
            element.block_focus()
        VideoPlayer = Skyrim_window['SkyrimVideo'].Widget
        set_html(VideoPlayer, html_taleoftongues)
        width, height = VideoPlayer.winfo_width(), VideoPlayer.winfo_height()
    elif SongListbox.get() == ['Age of Aggression']:
        Skyrim_window['-Song Lyrics-'].update(value=AOALyrics)
        for element in Skyrim_window.key_dict.values():
            element.block_focus()
        VideoPlayer = Skyrim_window['SkyrimVideo'].Widget
        set_html(VideoPlayer, html_ageofaggression)
        width, height = VideoPlayer.winfo_width(), VideoPlayer.winfo_height()
    elif SongListbox.get() == ['Bonus: Skyrim (Main Title)']:
        Skyrim_window['-Song Lyrics-'].update(value=SMTLyrics)
        for element in Skyrim_window.key_dict.values():
            element.block_focus()
        VideoPlayer = Skyrim_window['SkyrimVideo'].Widget
        set_html(VideoPlayer, html_skyrimmaintitles)
        width, height = VideoPlayer.winfo_width(), VideoPlayer.winfo_height()
    elif event == (sg.WIN_CLOSED):
        break
Skyrim_window.close()
