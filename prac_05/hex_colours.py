
#Dictionary of basic color and their corresponding hex codes
COLOUR_CODES = {"BLACK": "#000000", "WHITE": "#ffffff", "RED": "#ff0000", "GREEN": "#008000",
"BLUE": "#0000ff", "YELLOW": "#ffff00", "CYAN": "#00ffff", "MAGENTA": "#ff00ff", "GRAY": "#808080",
"ORANGE": "#ffa500"}

colour = input("Enter a basic colour:").upper()
while colour != "":
    if colour in COLOUR_CODES:
        print(f"{colour} code is {COLOUR_CODES[colour]}")
    else:
        print("Invalid colour name. Try again.")
    colour = input("Enter a basic colour:").upper()

