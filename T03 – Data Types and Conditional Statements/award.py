swim_time=input('Swimming (mins): ')
cyc_time=input('Cycling (mins): ')
run_time=input('Running (mins): ')
record=[int(swim_time),int(cyc_time),int(run_time)]

total_time=sum(record)
# if swim_time==0 or cyc_time==0 or run_time==0:
#     print('Disqualified')
# break

if 0 <= total_time <= 100 : print('The Honorary Colours Award is being presented.')
elif 101 <= total_time <= 105 : print('The Honorary Half Colours Award is being presented.')
elif 106 <= total_time <= 110 : print('The Honorary Scroll Award is being presented.')
elif total_time >= 111 : print('No award is being presented.')
