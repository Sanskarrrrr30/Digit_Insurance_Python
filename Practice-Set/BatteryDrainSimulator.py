drainperminute = int(input())

battery = 100
minutes = 0

while battery > 0:
    battery -= drainperminute
    minutes += 1

print(minutes)