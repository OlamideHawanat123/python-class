import statistics
numbers = [9, 11, 22, 34, 17, 22, 34, 22, 40, 34]

sorted_number = sorted(numbers)
the_mean = statistics.mean(sorted_number)
the_median = statistics.median(sorted_number)

the_mode = statistics.mode(sorted_number)

print(f'Mean: {the_mean:.3f}, Median:{the_median}, Mode:{the_mode}')
