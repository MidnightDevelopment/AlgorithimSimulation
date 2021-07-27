num = 1
length = 5

left = num - 2
right = num + 2

if length - right < 2:
	left = left + (length - right)
	right = length

if left < 0:
	right = right - left
	left = 0

print(left)
print(right)