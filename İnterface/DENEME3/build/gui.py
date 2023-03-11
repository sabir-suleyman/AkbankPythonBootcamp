# PyPizza User Interface 
"""
from Sabir Süleymanlı 
Github: https://github.com/sabir-suleyman    
LinkedIn: https://www.linkedin.com/in/sabirs/

"""


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage


OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Beyza\OneDrive\Masaüstü\DENEME3\build\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("1368x768")
window.configure(bg = "#FFFFFF")


canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 768,
    width = 1368,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    684.0,
    384.0,
    image=image_image_1
)

canvas.create_rectangle(
    939.0,
    146.0,
    1317.0,
    679.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    490.0,
    147.0,
    868.0,
    680.0,
    fill="#FFFFFF",
    outline="")

canvas.create_rectangle(
    41.0,
    146.0,
    419.0,
    679.0,
    fill="#FFFFFF",
    outline="")

canvas.create_text(
    1079.0,
    639.0,
    anchor="nw",
    text="Afiyet olsun :)",
    fill="#403A4B",
    font=("Sansation BoldItalic", 15 * -1)
)

canvas.create_text(
    995.0,
    611.0,
    anchor="nw",
    text="Bizi tercih ettiğiniz için teşekkür ederiz !",
    fill="#403A4B",
    font=("Sansation BoldItalic", 15 * -1)
)

canvas.create_text(
    1024.0,
    583.0,
    anchor="nw",
    text="Ödeme işleminiz tamamlandı!",
    fill="#403A4B",
    font=("Sansation BoldItalic", 15 * -1)
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_1 clicked"),
    relief="flat"
)
button_1.place(
    x=985.0,
    y=522.0,
    width=273.0,
    height=40.0
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    1121.5,
    475.0,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#C4C4C4",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=993.0,
    y=455.0,
    width=257.0,
    height=38.0
)

canvas.create_text(
    1117.0,
    442.0,
    anchor="nw",
    text="*Lütfen Kredi Kartı şifresini giriniz.",
    fill="#F20D36",
    font=("Sansation Regular", 9 * -1)
)

canvas.create_text(
    985.0,
    430.0,
    anchor="nw",
    text="Kredi Kartı Şifresi",
    fill="#403A4B",
    font=("Lora Regular", 12 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    1121.5,
    394.0,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#C4C4C4",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=993.0,
    y=374.0,
    width=257.0,
    height=38.0
)

canvas.create_text(
    1102.0,
    361.0,
    anchor="nw",
    text="*Lütfen Kredi Kartı Numarasını giriniz.",
    fill="#F20D36",
    font=("Sansation Regular", 9 * -1)
)

canvas.create_text(
    985.0,
    349.0,
    anchor="nw",
    text="Kredi Kartı No\n",
    fill="#403A4B",
    font=("Lora Regular", 12 * -1)
)

entry_image_3 = PhotoImage(
    file=relative_to_assets("entry_3.png"))
entry_bg_3 = canvas.create_image(
    1121.5,
    315.0,
    image=entry_image_3
)
entry_3 = Entry(
    bd=0,
    bg="#C4C4C4",
    fg="#000716",
    highlightthickness=0
)
entry_3.place(
    x=993.0,
    y=295.0,
    width=257.0,
    height=38.0
)

canvas.create_text(
    1102.0,
    281.0,
    anchor="nw",
    text="*Lütfen T.C Kimlik Numarasını giriniz.",
    fill="#F20D36",
    font=("Sansation Regular", 9 * -1)
)

canvas.create_text(
    985.0,
    266.0,
    anchor="nw",
    text="T.C Kimlik No\n",
    fill="#403A4B",
    font=("Lora Regular", 12 * -1)
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    1122.0,
    243.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    1119.0,
    184.0,
    image=image_image_3
)

canvas.create_text(
    601.0,
    604.0,
    anchor="nw",
    text="Siparişiniz onaylandı!",
    fill="#403A4B",
    font=("Sansation BoldItalic", 15 * -1)
)

canvas.create_text(
    550.0,
    636.0,
    anchor="nw",
    text=" Lütfen bir sonraki aşamaya geçiniz →",
    fill="#403A4B",
    font=("Sansation BoldItalic", 15 * -1)
)

button_image_2 = PhotoImage(
    file=relative_to_assets("button_2.png"))
button_2 = Button(
    image=button_image_2,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_2 clicked"),
    relief="flat"
)
button_2.place(
    x=575.0,
    y=548.0,
    width=213.0,
    height=40.0
)

canvas.create_rectangle(
    528.0,
    522.0,
    829.0,
    523.0,
    fill="#000000",
    outline="")

entry_image_4 = PhotoImage(
    file=relative_to_assets("entry_4.png"))
entry_bg_4 = canvas.create_image(
    767.0,
    468.5,
    image=entry_image_4
)
entry_4 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_4.place(
    x=703.0,
    y=444.0,
    width=128.0,
    height=47.0
)

canvas.create_text(
    526.0,
    454.0,
    anchor="nw",
    text="Toplam Ücret",
    fill="#000000",
    font=("Sansation Regular", 25 * -1)
)

entry_image_5 = PhotoImage(
    file=relative_to_assets("entry_5.png"))
entry_bg_5 = canvas.create_image(
    682.0,
    381.5,
    image=entry_image_5
)
entry_5 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_5.place(
    x=533.0,
    y=354.0,
    width=298.0,
    height=53.0
)

canvas.create_text(
    526.0,
    302.0,
    anchor="nw",
    text="Sos Seçimi",
    fill="#000000",
    font=("Sansation Regular", 30 * -1)
)

entry_image_6 = PhotoImage(
    file=relative_to_assets("entry_6.png"))
entry_bg_6 = canvas.create_image(
    682.0,
    255.5,
    image=entry_image_6
)
entry_6 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_6.place(
    x=533.0,
    y=228.0,
    width=298.0,
    height=53.0
)

canvas.create_text(
    526.0,
    171.0,
    anchor="nw",
    text="Pizza Seçimi",
    fill="#000000",
    font=("Sansation Regular", 30 * -1)
)

canvas.create_text(
    59.0,
    638.0,
    anchor="nw",
    text="MISIR - - - - - - - - - - - - - - - -  4 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    60.0,
    603.0,
    anchor="nw",
    text="SOĞAN - - - - - - - - -- - - - - - 5 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    60.0,
    568.0,
    anchor="nw",
    text="ET - - - - - - - - - - - - - -  - -  -  10 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    60.0,
    533.0,
    anchor="nw",
    text="KEÇİ PEYNİRİ - - - - - -  - - - 8 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    54.0,
    498.0,
    anchor="nw",
    text=" MANTAR  - - - - - - - - - - - - - 5 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    58.0,
    463.0,
    anchor="nw",
    text="ZEYTİN - - - - - - - - - - - - - - - 4 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_rectangle(
    54.0,
    446.0000305175781,
    368.99993896484375,
    448.0228271484375,
    fill="#000000",
    outline="")

canvas.create_text(
    55.0,
    413.0,
    anchor="nw",
    text="Sos çeşitleri",
    fill="#000000",
    font=("Inter Regular", 23 * -1)
)

canvas.create_text(
    55.0,
    361.0,
    anchor="nw",
    text="PLAİN PİZZA  - - - - -  - - - -  - 40 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    54.0,
    326.0,
    anchor="nw",
    text="TÜRK PİZZA - - - - - -  - - - -  - 35 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    54.0,
    291.0,
    anchor="nw",
    text="MARGARİTA PİZZA - - - - -- 30 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_text(
    54.0,
    256.0,
    anchor="nw",
    text="KLASİK PİZZA - - - - - - - - - - 20 TL",
    fill="#000000",
    font=("Sansation Bold", 20 * -1)
)

canvas.create_rectangle(
    52.0,
    241.9771990776062,
    366.99993896484375,
    244.0,
    fill="#000000",
    outline="")

canvas.create_text(
    53.0,
    206.0,
    anchor="nw",
    text="Pizza çeşitleri",
    fill="#000000",
    font=("Inter Regular", 23 * -1)
)

canvas.create_text(
    185.0,
    158.0,
    anchor="nw",
    text="Menü",
    fill="#FFFFFF",
    font=("Inter ExtraBold", 30 * -1)
)

button_image_3 = PhotoImage(
    file=relative_to_assets("button_3.png"))
button_3 = Button(
    image=button_image_3,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_3 clicked"),
    relief="flat"
)
button_3.place(
    x=379.0,
    y=638.0,
    width=19.0,
    height=19.0
)

button_image_4 = PhotoImage(
    file=relative_to_assets("button_4.png"))
button_4 = Button(
    image=button_image_4,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_4 clicked"),
    relief="flat"
)
button_4.place(
    x=379.0,
    y=602.0,
    width=19.0,
    height=19.0
)

button_image_5 = PhotoImage(
    file=relative_to_assets("button_5.png"))
button_5 = Button(
    image=button_image_5,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_5 clicked"),
    relief="flat"
)
button_5.place(
    x=379.0,
    y=568.0,
    width=19.0,
    height=19.0
)

button_image_6 = PhotoImage(
    file=relative_to_assets("button_6.png"))
button_6 = Button(
    image=button_image_6,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_6 clicked"),
    relief="flat"
)
button_6.place(
    x=379.0,
    y=534.0,
    width=19.0,
    height=19.0
)

button_image_7 = PhotoImage(
    file=relative_to_assets("button_7.png"))
button_7 = Button(
    image=button_image_7,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_7 clicked"),
    relief="flat"
)
button_7.place(
    x=379.0,
    y=499.0,
    width=19.0,
    height=19.0
)

button_image_8 = PhotoImage(
    file=relative_to_assets("button_8.png"))
button_8 = Button(
    image=button_image_8,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_8 clicked"),
    relief="flat"
)
button_8.place(
    x=379.0,
    y=463.0,
    width=19.0,
    height=19.0
)

button_image_9 = PhotoImage(
    file=relative_to_assets("button_9.png"))
button_9 = Button(
    image=button_image_9,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_9 clicked"),
    relief="flat"
)
button_9.place(
    x=380.0,
    y=362.0,
    width=19.0,
    height=19.0
)

button_image_10 = PhotoImage(
    file=relative_to_assets("button_10.png"))
button_10 = Button(
    image=button_image_10,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_10 clicked"),
    relief="flat"
)
button_10.place(
    x=380.0,
    y=325.0,
    width=19.0,
    height=19.0
)

button_image_11 = PhotoImage(
    file=relative_to_assets("button_11.png"))
button_11 = Button(
    image=button_image_11,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_11 clicked"),
    relief="flat"
)
button_11.place(
    x=380.0,
    y=291.0,
    width=19.0,
    height=19.0
)

button_image_12 = PhotoImage(
    file=relative_to_assets("button_12.png"))
button_12 = Button(
    image=button_image_12,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_12 clicked"),
    relief="flat"
)
button_12.place(
    x=380.0,
    y=258.0,
    width=19.0,
    height=19.0
)

button_image_13 = PhotoImage(
    file=relative_to_assets("button_13.png"))
button_13 = Button(
    image=button_image_13,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: print("button_13 clicked"),
    relief="flat"
)
button_13.place(
    x=332.0,
    y=25.0,
    width=738.0,
    height=88.0
)
window.resizable(False, False)
window.mainloop()
