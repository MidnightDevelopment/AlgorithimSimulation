import random
from random import randrange
import matplotlib.pyplot as plt

subarray_size = 5

def wrap(num, length):
	left = num - 2
	right = num + 2

	if length - right < 2:
		left = left + (length - right)
		right = length

	if left < 0:
		right = right - left
		left = 0
	return (left, right)

def swap(arr, idx1, idx2):
	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp
	return arr

def measure(arr):
	total = 0
	for idx, sub in enumerate(arr):
		total = total + abs(idx - sub.num)
	return total / 80000

def vis(submissions):
	for idx, submission in enumerate(submissions):
		if submission.picks <= 1:
			plt.plot(idx, submission.num, 'b.')
		elif submission.picks <= 3:
			plt.plot(idx, submission.num, 'c.')
		elif submission.picks <= 5:
			plt.plot(idx, submission.num, 'g.')
		elif submission.picks <= 7:
			plt.plot(idx, submission.num, 'r.')
		else:
			plt.plot(idx, submission.num, 'k.')

	plt.show()

def select_idx(arr):
	idxs = []
	top = int(len(arr) / subarray_size)
	sort = sorted(range(len(arr)), key = lambda k: arr[k].score)
	for i in range(subarray_size):
		pick_sorted = sorted(range(top * i, top * (i + 1)), key=lambda k: arr[k].picks)
		idxs.append(pick_sorted[0])
	return idxs
def update_scores(arr):
	for i in range(len(arr)):
		opp_score = 0
		for j in range(len(arr)):
			if i != j:
				opp_score = opp_score + arr[j].score
		arr[i].losses = arr[i].losses + (len(arr) - i - 1)
		arr[i].wins = arr[i].wins + i
		arr[i].picks = arr[i].picks + (len(arr) - 1)
		arr[i].score = (opp_score + (400 * (arr[i].wins - arr[i].losses))) / arr[i].picks

def choose_one_close(num):
	if num - 1 < 0:
		return num + 1
	else:
		return num - 1

def sort_w_error(arr, err):
	sort = sorted(arr, key=lambda x: x.num)
	rand = random.uniform(0, 1)
	if err: 
		if rand < 0.75:
			num = randrange(len(arr))
			sort = swap(sort, num, choose_one_close(num))
			if rand < 0.50:
				num = randrange(len(arr))
				sort = swap(sort, num, choose_one_close(num))
				if rand < 0.25:
					num = randrange(len(arr))
					sort = swap(sort, num, choose_one_close(num))
					if rand < 0.125:
						num = randrange(len(arr))
						sort = swap(sort, num, choose_one_close(num))
	return sort
