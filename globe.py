import random
from random import randrange
import matplotlib.pyplot as plt

subarray_size = 5

def swap(arr, idx1, idx2):
	temp = arr[idx1]
	arr[idx1] = arr[idx2]
	arr[idx2] = temp
	return arr

def measure(arr):
	submission_count = len(arr)

def select_idx(arr):
	idxs = []
	top = int(len(arr) / subarray_size)

	for i in range(subarray_size):
		sort = sorted(range(top * i, top * (i + 1)), key=lambda k: arr[k].picks)
		idxs.append(sort[0])

	return idxs

def sort_w_error(arr, err):
	sort = sorted(arr, key=lambda x: x.num)
	rand = random.uniform(0, 1)
	if err: 
		if rand < 0.75:
			sort = swap(sort, randrange(len(arr)), randrange(len(arr)))
			if rand < 0.5:
				sort = swap(sort, randrange(len(arr)), randrange(len(arr)))
				if rand < 0.25:
					sort = swap(sort, randrange(len(arr)), randrange(len(arr)))
					if rand < 0.12:
						sort = swap(sort, randrange(len(arr)), randrange(len(arr)))
	
	return sort
