def main(s):
    """
    A variable of type str is given. Find how many letters it contains and return.
    Args:
        s: str
    Returns:
        int: return answer
    """
    t = 0
    for m in s:
        if m.isalpha():
            t +=1
    return t
print(main(s ="python 2022"))
