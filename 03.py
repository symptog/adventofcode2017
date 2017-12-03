puzzle = 347991

rings = 0
count = 1
step = 2

while puzzle > count**2:
    count += step
    rings += 1

print("result = ", rings-((count**2 - puzzle)%rings+1)+rings+1)


