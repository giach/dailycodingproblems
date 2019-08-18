# We say a number is sparse if there are no adjacent ones in its binary
#representation. For example, 21 (10101) is sparse, but 22 (10110) is not.
# For a given input N, find the smallest sparse number greater than or equal to N.

# Do this in faster than O(N log N) time.

def main(n):
	n1 = 0
	n2 = 1
	i = 1
	while True:
		p = pow(2,i)
		if i % 2 == 1:
			if (n1 + p) > n:
				break
			n1 += p
		else:
			if (n2 + p) > n:
				break
			n2 += p

		i += 1

	# print(max(n1,n2), bin(max(n1,n2)))
	return max(n1,n2)

n = int('1001001',2)
print(n, bin(n))
main(n)


n = int('1001001000',2)
print(n, bin(n))
main(n)