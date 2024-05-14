import random

def generate_code(code_len=6):
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_char = len(all_chars) - 1
    code = ''

    for _ in range(code_len):
        index = random.randint(0, last_char)
        code += all_chars[index]
    
    return code

