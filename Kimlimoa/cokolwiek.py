import multiprocessing as mp
pool = mp.Pool(mp.cpu_count())

results = []

# Step 1: Redefine, to accept i, the iteration number
def howmany_within_range2(i, row, minimum, maximum):
    """Returns how many numbers lie within maximum and minimum in a given row"""
    count = 0
    for n in row:
        if minimum <= n <= maximum:
            count = count + 1
    return (i, count)


# Step 2: Define callback function to collect the output in results
def collect_result(result):
    global results
    results.append(result)


# Step 3: Use loop to parallelize
for i, row in enumerate(data):
    pool.apply_async(howmany_within_range2, args=(i, row, 4, 8), callback=collect_result)

# Step 4: Close Pool and let all the processes complete
pool.close()
pool.join()  # postpones the execution of next line of code until all processes in the queue are done.
