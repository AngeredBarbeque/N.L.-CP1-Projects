list = [["A", "B", "C", "D", "E"], ["B", "C", "E", "A", "D"], ["C", "D", "A", "B", "B"], ["A", "A", "A", "A", "E"], ["B", "D", "C", "C", "A"]]
a = 0
b = 0
c = 0
d = 0
e = 0
for item in list:
    for i in item:
        if i == "A":
            a += 1
        if i == "B":
            b += 1
        if i == "C":
            c += 1
        if i == "D":
            d += 1
        if i == "E":
            e += 1
print("A:", a)
print("B:", b)
print("C:", c)
print("D:", d)
print("E:", e)