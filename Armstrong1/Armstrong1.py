def is_armstrong(num):
    """Check whether a number is an Armstrong number"""
    n=len(str(num))
    total=sum(int(digit)**n for digit in str(num))
    return total==num

