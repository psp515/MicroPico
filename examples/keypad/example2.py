from micropico import Keypad

print("Hello KeyPad!")

keypad = Keypad([0, 1, 2, 3], [4, 5, 6], [["1", "2", "3"],
                                       ["4", "5", "6"],
                                       ["7", "8", "9"],
                                       ["*", "0", "#"]] )
i = 0
while True:
    x = keypad.read()
    if x != "":
        i += 1
        print(i, "Pressed: ", x)

    if x == "*":
        break

print("Program finished")