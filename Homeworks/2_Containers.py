h = [1, 8, 6, 2, 5, 4, 8, 3, 7]
p1, p2 = 0, len(h) - 1

max_c = min(h[p1], h[p2]) * (p2 - p1)

while p2 != p1:
    h1, h2 = h[p1], h[p2]
    cur = min(h1, h2) * (p2 - p1)
    max_c = max(cur, max_c)
    if h1 > h2: p2 -= 1
    else: p1 += 1

print('Max container is ', max_c)