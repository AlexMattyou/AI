# https://www.hackerearth.com/practice/basic-programming/input-output/basics-of-input-output/practice-problems/algorithm/cartag-948c2b02/

i = input().strip()
a = 'invalid'
if i[2] not in ["A","E","I","O","U","Y"]:
    if (int(i[0])+int(i[1]))%2==0 and (int(i[3])+int(i[4]))%2==0 and (int(i[4])+int(i[5]))%2==0 and (int(i[7])+int(i[8]))%2==0:
        a = 'valid'
print(a)
