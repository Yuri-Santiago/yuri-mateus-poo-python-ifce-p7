def verificar(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    else:
        if a < b + c and b < a + c and c < a + b:
            return True
        return False
