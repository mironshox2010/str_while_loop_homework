def main(s):
    """
    A variable of type str is given. Find how many punctuations it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    t = 0
    for m in s:
        if m.isdigit() or m.isalpha():
            t +=1
    return len(s)-t
print(main(s = "#has23h\ t ag@$"))
    