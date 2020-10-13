# -------------- PROBLEM 3 -----------------
#solution1
sequence=[10, 39, 47, 1, 49,100]
max=-999
min=999
for s in range(len(sequence)):
    if sequence[s]>max:
        max=sequence[s]
    if sequence[s]<min:
        min=sequence[s]
print("Maximum number is: " + str(max) + " and the Minimal number is: " + str(min))

#solution2
sequence=[10, 39, 47, 1, 49,100]
max=-999
min=999
for x in sequence:
    if x>max:
        max=x
    if x<min:
        min=x
print("Maximum number is: " + str(max) + " and the Minimal number is: " + str(min))

# ----------- PROBLEM 4 -----------

# Function for Finding Minimal number
def findMinAndMax(n, left, right, min, max):
	# if sequence contains only one element
	if left == right:
		if min > n[right]:
			min = n[right]
		if max < n[left]:
			max = n[left]
		return min, max
	# if sequence contains only two elements
	if right - left == 1:
		if n[left] < n[right]:
			if min > n[left]:
				min = n[left]

			if max < n[right]:  # comparison 3
				max = n[right]
		else:
			if min > n[right]:  # comparison 2
				min = n[right]

			if max < n[left]:   # comparison 3
				max = n[left]
		return min, max
if __name__ == '__main__':
	A = [10, 39, 47, 1, 49,100]
	print("The minimal number: ", min)
	print("The maximal number: ", max)



        #  ------------- PROBLEM 5 ----------------
def reverse(r):
        if len(r) == 0:
            return r
        else:
            return reverse(r[1:]) + r[0]
r = "SDSU@San"
print ("The original string  is : ", r)
print ("The reversed string(using recursion) is : ", reverse(r))

# The string is passed as an argument to a recursive function which reverses
# the string. Must pass condition to verify length isn't equal to zero.
# If not equal to 0, the reverse function is called to slice the string except the
# first character and concatenate the first character to the back of the string.
