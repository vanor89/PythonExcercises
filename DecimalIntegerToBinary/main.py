from ..common/stack import Stack 

def convert_int_to_bin(dec_num):
    if dec_num == 0:
        return 0
    s = Stack()
    res = ""
    while dec_num > 0:
        s.push(dec_num % 2)
        dec_num = dec_num // 2

    while not s.is_empty():
        res += str(s.pop())
    return res


