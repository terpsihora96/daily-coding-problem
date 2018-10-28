import sys

def main():
    numbers = [-2, -15, 23, 3, 4]
    k = -17
    dict_numbers = dict()
    
    for number in numbers:
        v = k - number
        if dict_numbers.get(v, False):
            dict_numbers[number] = v
        else:
            print(f'({v}) + ({number}) = {k}')
            sys.exit(0) 

if __name__ == "__main__":
    main()