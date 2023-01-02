# https://www.hackerearth.com/practice/machine-learning/prerequisites-of-machine-learning/basic-probability-models-and-rules/tutorial/

m,a,r = float(input()),float(input()),float(input())
p = r *(a * (1 - m) + m * (1 - a))
print('%.6f' % p)
