# The Code displayed in the values within the dictionary is the hex code for the colour in the key:
colour_to_code = {"Absolute Zero": "#0048ba", "Acid Green": "#b0bf1a", "AliceBlue": "#f0f8ff",
                  "Alizarin crimson": "#e32636", "Amaranth": "#e52b50", "Amber": "#ffbf00",
                  "Amethyst": "#9966cc", "AntiqueWhite": "#faebd7", "Apricot": "#fbceb1", "Aqua": "#00ffff"}
print(colour_to_code)
colour_to_code = {colour.lower(): code for colour, code in colour_to_code.items()}  # convert keys to lowercase
colour = input("Enter a colour (key) from the dictionary: ").lower()  # convert input to lowercase
while colour != "":
    if colour in colour_to_code:
        code = colour_to_code.get(colour)
        print(f"The code for {colour} is {code}")
    else:
        print("Invalid colour")
    colour = input("Enter a colour (key) from the dictionary: ").lower()  # convert input to lowercase
