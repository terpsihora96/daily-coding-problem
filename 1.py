import sys

def main():
    numbers = [2, 15, 23, 3, 4]
    k = 17

    elements = dict()
    for number in numbers:
        y = k - number
        x = elements.get(y, False)
        if (x == False):
            elements[number] = k - number
        else:
            print(k - number, number)
            sys.exit(0) 

if __name__ == "__main__":
    main()