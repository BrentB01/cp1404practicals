"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

# TODO: Reformat this file so the dictionary code follows PEP 8 convention
CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_code = input("Enter short state: ")
while state_code != "":
    state_code = state_code.upper()  # Convert input to uppercase
    try:
        state_name = CODE_TO_NAME[state_code]
        print(f"{state_code} is {state_name}")
    except KeyError:
        print("Invalid short state")
    state_code = input("Enter short state: ")

# Once loop finishes, eg "" is entered, states are printed with correct formatting:
for state_code, state_name in CODE_TO_NAME.items():
    print(f"{state_code} is {state_name}")

