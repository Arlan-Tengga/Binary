consversion_table = {
    0: '0', 1: '1', 2: '2', 3: '3', 4: '4',
    5: '5', 6: '6', 7: '7',
    8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C',
    13: 'D', 14: 'E', 15: 'F'
}

def d_biner(x):
    res = ''
    while x > 0:
        res = str(x%2)+res
        x //= 2
    return res

def d_hexal(x):
    hexadecimal = ''
    while(x>0):
        r = x % 16
        hexadecimal = consversion_table[r] + hexadecimal
        x = x // 16
    return hexadecimal

def d_octav(x):
    octal = 0
    countval = 1
    dNo = x
    
    while(x != 0):

        r = x % 8
        octal += r * countval
        countval = countval * 10
        x //= 8

    return octal





        



        