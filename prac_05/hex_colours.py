COLOUR_NAME_TO_HEX_CODE = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                           "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                           "Amethyst": "#9966cc",
                           "AntiqueWhite": "#faebd7", "Aqua": "#00ffff", "Cadmium Orange": "#ed872d"}
print(COLOUR_NAME_TO_HEX_CODE)

color_name = input("Enter color name: ").title()
while color_name != "":
    try:
        print(color_name, "is", COLOUR_NAME_TO_HEX_CODE[color_name])
    except KeyError:
        print("Invalid color name")
    color_name = input("Enter color name: ").title()
