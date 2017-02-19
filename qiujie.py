def map(a):
    a -= 97
    for i in range(0, 26):
        if (i * 5 + 11) % 26 == a:
            return i + 97
    return -1

if __name__ == '__main__':
    s = 'xztiofwhf'
    ans = []
    for val in s:
        ans.append(chr(map(ord(val))))
    print ans
