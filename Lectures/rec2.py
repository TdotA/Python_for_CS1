memory = {}

# memory = {(20, 10): 184756, (30, 15): 155117520, ...}


def binomial(n, k):
	if k > n:
		return 0
	if k == 0 or n == k:
		return 1
	if not (n, k) in memory:
		memory[(n, k)] = binomial(n - 1, k - 1) + binomial(n -  1, k)
	return memory[(n, k)]

memory_f = {}

def f(n, k):
	if n == 0:
		return (0, None)
	if k == 0:
		return (float('inf'), None)
	if not (n, k) in memory_f:
		best = float('inf')
		best_i = None
		for i in range(1, n + 1):
			a, ai = f(i - 1, k - 1)
			b, bi = f(n - i, k)
			moves = 1 + max(a, b)
			if moves < best:
				best = moves
				best_i = i
		memory_f[(n, k)] = (best, best_i)
	return memory_f[(n, k)]

