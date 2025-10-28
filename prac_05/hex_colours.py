color_dict = {"ABSOLUTE ZERO": "#0048ba", "BURNT ORANGE": "#cc5500", "DARK ORCHID": "#9932cc", "EMERALD": "#50c878",
              "FERRARI RED": "#ff2800", "FLAMINGO PINK": "#fc8eac", "FROSTBITE": "#e936a7", "LEMON": "#fff700",
              "MAGENTA": "#ff00ff", "OLIVE": "#808000", "ROSE": "#ff007f"}

color = input("Please Enter Colour:").upper()

while color != "":
    if color in color_dict:
        print(color_dict[color])
    else:
        print("Invalid Input")
    color = input("Please Enter Colour:").upper()
