def is_triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a < b + c and b < a + c and c < a + b:
        return True
    else:
        return False

