import random
from globe import swap, update_scores
from random import randrange
from submission import Submission
n = 5
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


g = random.sample(range(n), n)
submissions = [Submission(j) for j in g]

for i in range(n):
	f = sort_w_error(submissions, True)
	print('bf', f)
	update_scores(f)
	print('af', f)
	f = sorted(f, key=lambda x: x.score)

print(sorted(f, key=lambda x: x.score))

asd = [0, 1, 2, 3, 4]
print(asd[0:4 + 1])