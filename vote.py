import matplotlib.pyplot as plt
from globe import sort_w_error, select_idx, subarray_size, measure, vis, wrap, update_scores
from random import randrange
from submission import Submission
import random

n = 400

submissions_entries = random.sample(range(n), n)
submissions = []
for idx, submission in enumerate(submissions_entries):
	submissions.append(Submission(submission))
	if len(submissions) > subarray_size:
		random_idxs = select_idx(submissions)
		random_arr = []
		for idx in random_idxs:
			random_arr.append(submissions[idx])
		tournament_results = sort_w_error(random_arr, False)
		update_scores(tournament_results)
		for j, idx in enumerate(random_idxs):
			submissions[idx] = tournament_results[j] 
		submissions = sorted(submissions, key = lambda k: k.score)
print(submissions)
print(measure(submissions))
vis(submissions)