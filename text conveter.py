def detect_language(n, lines):
    count_t=0
    count_s=0
    for line in lines:
        count_t += line.count('t')+line.count('T')
        count_s += line.coutn('s')+line.count('S')
    if count_t > count_s:
        return "English"
    else:
        return "French"
n = int(input().strip())
lines = [input().strip() for _ in range(n)]

print(detect_language(n, lines))
