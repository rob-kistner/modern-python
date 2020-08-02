
how_many_times = input('How many times do I have to tell you? ')
how_many_times = int(how_many_times)

# not having 2 params in range means "0 to <var>" times
for time in range(how_many_times):
    print(f'Time {time+1}: Clean your room !'.upper())