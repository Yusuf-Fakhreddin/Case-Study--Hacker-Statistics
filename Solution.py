import numpy as np
import matplotlib as plt

np.random.seed(123)

# Simulate random walk 250 times
all_walks = []
for i in range(500) :
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)
        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)

        # Implement clumsiness
        if np.random.rand() <=.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
#transpose to make it 100 rows and 500 colums 
# number of rows represented on x-axis and value of column represented on y-axis
#each graph  representing the values of 1 random walk
#final steps for each walk represented in last row and on 1 x-axis point (the final point) on plot
np_aw_t = np.transpose(np.array(all_walks))
plt.plot(np_aw_t)
plt.show()
plt.clf()

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
#last row values ranges on x-axis and their number of occurrences on y-axis
plt.hist(ends)
plt.show()


