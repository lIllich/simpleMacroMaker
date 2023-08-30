def inputInteger(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Error! Integers Only!")
            continue
        except Exception as e:
            print("Error! Invalid Input!")     
            continue