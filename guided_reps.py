from time import sleep

def do_reps(rep_count, rep_time, rep_pause=1):
  """
  Guides the user through specified number of reps that last for a specified amount of time in seconds.
  
  rep_count: int, how many reps do you want to do?
  rep_time: int, how long should each rep be in seconds?
  rep_pause: int, how long to wait between reps? default is 1 second
  """
  rep_current = 1  # used to tell user what rep they are on
  print('Doing {} reps at {} seconds each.'.format(rep_count, rep_time))  # let the uder know how many reps they are doing and for how long
  
  # start the loop that guides user through all the reps
  for rep in range(rep_count):
    print('Starting rep number: {}.'.format(rep_current))
    sleep(int(rep_time))  # wait required time for rep to be complete
    print('End of rep number: {}.\n'.format(rep_current))
    rep_current += 1
    sleep(float(rep_pause))  # wait time between reps

print('Starting Set #1\n\n')
do_reps(60, 1, 0.1)
print('Starting Set #2\n\n')
do_reps(6, 10, 2)
print('Starting Set #3\n\n')
do_reps(3, 20, 2)
print('Starting Set #4\n\n')
do_reps(1, 60, 2)