"""
Chris Reppel
Prac 5
2/4/19
"""

Colours = {"aquamarine1": "#7fffd4", "BlueViolet": "#8a2be2",
           "chartreuse1": "#7fff00", "cyan1": "#00ffff",
           "DarkOrchid": "#9932cc", "DeepPink1": "#ff1493",
           "DodgerBlue1": "#1e90ff", "FloralWhite": "#fffaf0",
           "LawnGreen": "#7cfc00", "MediumVioletRed": "#c71585"}

colour = input("Enter a colour name: ")
while colour != " ":
    print("The HEX Code for {} is {}".format(colour, Colours.get(colour)))
    colour = input("Enter another colour name: ")
