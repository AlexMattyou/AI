m = float(input()) #probability of Mike in bus
a = float(input()) #probability of Alice in bus
r = float(input()) #probability of rain

p1 = a * (1 - m) # probability of Alice in bus but not Mike
p2 = m * (1 - a) # probability of Mike in bus but not Alice

p = r *(p1 + p2) # probability it'll rain when both won't meet in bus

print('%.6f' % p) #rounded up to six decimal places
