from functools import reduce
# from copy import deepcopy

def main():
    input_ = [1, 2, 3, 4, 5]
    length = len(input_)
    product = reduce((lambda x, y: x * y), input_)
    output = []
    
    # without using division
    for i in range (0, length):
        count = 0
        product1 = product
        while product1:
            count += 1
            product1 -= input_[i]
        output.append(count)

    """
    for i in range (0, length):
        input_1 = deepcopy(input_)
        input_1.pop(i)
        output.append(reduce((lambda x, y: x * y), input_1)) 
    """

    """
    for i in range (0, length):
        output.append(product // input_[i]) 
    """
    print(output)

if __name__ == "__main__":
    main()