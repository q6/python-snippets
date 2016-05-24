import subprocess
import re
# 315360000 max secs
# max time is 10 years

# ask the user how long from now they want to shutdown
shutdown_countdown = input('''How long from now would you like to shutdown?
Enter in the following format: ##h##m##s

Examples of working entries:
12h30m00s
99s55h
31h2s
6m
10s

(Enter nothing to shutdown immediately)
''')

# convert the user input: '12h44m65s' --> ['12h', '44m', '65s']
list_shutdown_countdown = (re.findall('(\d+[hms])', shutdown_countdown))
shutdown_countdown_seconds = 0

# convert list_shutdown_countdown to total number of seconds of when to shutdown
for i in list_shutdown_countdown:
    # Ex. i = 12h
    key = i[-1]  # Ex. h
    value = int(i[:-1])  # Ex. 12
    # print(key, value)  # DEBUG

    if key == 'h':
        shutdown_countdown_seconds += 3600 * value  # 1 hour = 3600 seconds
    elif key == 'm':
        shutdown_countdown_seconds += 60 * value  # 1 minute = 60 seconds
    elif key == 's':
        shutdown_countdown_seconds += value  # 1 second = second

print(shutdown_countdown)
print(shutdown_countdown_seconds)

# run the shutdown command
subprocess.run(['shutdown', '/s', '/t', str(shutdown_countdown_seconds)])
print('Computer will shutdown in ' + str(shutdown_countdown_seconds) + ' seconds.')


input('Press Enter to exit.')