def TotalTime(height,climb,slip):
    time_taken = 2 # 1 min for climb and 1 min for slip
    total_time = ((height-climb)//(climb-slip))*time_taken + 1 # 1 for the last min where the monkey climb 5 meter and reach the top
    print(total_time)
height,climb,slip = map( int,input().split())
TotalTime(height,climb,slip)
    
