def rec(x):
    if x == 1:
        dms = "Turn off lights"
    if x == 2:
        dms = "Turn on lights"
    if x == 3:
        dms = "Turn on AC"
    if x == 4:
        dms = "Turn on Heat"
    if x == 5:
        dms = "Occupancy Limit Reached"
    return dms
