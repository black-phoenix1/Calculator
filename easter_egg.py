


def first():
    while True:
        try:
            print("What is your name?")
            name = input("")
            if name != "hahahahaha":
                print("wrong answer man")

        except SyntaxError:
            print("")