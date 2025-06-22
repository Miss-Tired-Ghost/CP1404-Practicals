"""
CP1404/CP5632 Practical
State names in a dictionary
"""

# DONE?: Reformat this file so the dictionary code follows PEP 8 convention
# I think pycharm did this automatically when I cloned the file.
# I made the formatting incorrect, then used reformating to fix it, but this won't be detected in commits unfortunately
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania", "SA": "South Australia"}
print(CODE_TO_NAME)
for code, state in CODE_TO_NAME.items():
    print(f"{code:3} is {state}")


state_code = input("Enter short state: ").upper()
while state_code != "":
    # LLBY
    # if state_code in CODE_TO_NAME:
    #     print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    # else:
    #     print("Invalid short state")

    # EAFP
    try:
        print(f"{state_code:3} is {CODE_TO_NAME[state_code]}")
    except KeyError:
        print("Invalid short state")

    state_code = input("Enter short state: ").upper()
