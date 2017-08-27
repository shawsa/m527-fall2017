
def power_series(coef, x):
	ret = 0
	for c in reversed(coef):
		ret = ret * x + c
	return ret

a = [1,2]

def gen_a(a0, a1, num):
	a = [0] * num
	a[0] = a0
	a[1] = a1
	a[2] = a[1]/2
	a[3] = (a[1] - a[0]) / 6
	a[4] = (0 - a[0] - a[1]) / 24
	for i in range(3, num-2):
		a[i+2] =  ((i+1)*a[i+1] - a[i-1]) / (i*i + 3*i + 2)
	
	return a


