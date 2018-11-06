# Given a list of integers, 
# write a function that returns the largest sum of non-adjacent numbers. 
# Numbers can be 0 or negative.

def main():
    a = [2, 4, 6, 2, 5]
    n = len(a)
    sum0, sum1, sum2 = 0, 0, 0
    i1, i2 = 0, 1
    # a flag that indicates whether a list consists only of negative numbers
    p = 0

    # find a starting point - 1st non negative number
    # 0 is considered as 'a negative numbers'
    while i1 < n and a[i1] <= 0:
        i1 = i1 + 1
        i2 = i2 + 1

    if n % 2 == 0:
        begin = i1
        end = n - 1
        # find a starting point - 1st non negative number from end of a list
        while a[end] <= 0 and end >= 0:
            end = end - 1
        
        while end > begin:
            if end - begin == 1 and n > 4 and a[begin] > 0 and a[end] > 0:
                sum0 = sum0 + a[begin] if a[begin] > a[end] else sum0 + a[end]
                # because it's always the last possible choice
                break
            if a[begin] > 0:
                sum0 = sum0 + a[begin]
                begin = begin + 2
                p = 1
            else:
                begin = begin + 1
            if a[end] > 0:
                sum0 = sum0 + a[end]
                end = end - 2
                p = 1
            else:
                end = end - 1
  
    while i1 < n:
        if a[i1] > 0:
            sum1 = sum1 + a[i1]
            i1 = i1 + 2
            p = 1
        else:
            i1 = i1 + 1

    while i2 < n:
        if a[i2] > 0:
            sum2 = sum2 + a[i2]
            i2 = i2 + 2
            p = 1
        else:
            i2 = i2 + 1

    # final sum is
    # a maximum of sum0, sum1, sum2
    # or
    # a maximum element if a list consists only of negative numbers
    if p != 0:
        sum_ = max(sum0, sum1, sum2)
    else:
        sum_ = max(a)

    print(sum_)

if __name__ == "__main__":
    main()