import matplotlib.pyplot as plt
from globe import sort_w_error, select_idx, subarray_size
from random import randrange
from submission import Submission
import random

n = 400

submissions_entries = random.sample(range(n), n)
submissions = []
for submission in submissions_entries:
	submissions.insert(randrange(len(submissions) + 1), Submission(submission))
	if len(submissions) > subarray_size:
		random_idxs = select_idx(submissions)
		random_arr = []
		for idx in random_idxs:
			random_arr.append(submissions[idx])
		sort_arr = sort_w_error(random_arr, False)
		sorted_idxs = sorted(random_idxs, key=lambda x: x)
		for i, idx in enumerate(sorted_idxs):
			submissions[idx] = sort_arr[i]
			submissions[idx].picks = submissions[idx].picks + 1

print(submissions)

total = 0
for idx, sub in enumerate(submissions):
	total = total + abs(idx - sub.num)
print(total / 80000)

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