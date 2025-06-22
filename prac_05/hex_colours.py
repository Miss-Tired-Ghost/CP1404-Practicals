"""
Convert colour names into hexadecimal colour
Code by: Miss Ghost/April First
"""
COLOUR_TO_HEX = {"AMARANTH": "#e52b50",
                 "AMBER": "#ffbf00",
                 "AMETHYST": "#9966cc",
                 "CERULEAN": "#007ba7",
                 "CHARCOAL": "#36454f",
                 "GINGER": "#b06500",
                 "ICEBERG": "#71a6d2",
                 "JADE": "#00a86b",
                 "LEMON": "#fff700",
                 "LINEN": "#faf0e6"}


def main():
    colour = input("Enter a colour: ").upper()
    while colour != "":
        try:
            hex_code = COLOUR_TO_HEX[colour]
            print(f"{colour:8} : {hex_code}")
        except KeyError:
            print("Unknown colour")
        colour = input("Enter a colour: ").upper()


if __name__ == "__main__":
    main()
