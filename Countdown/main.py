import time
while True:
    timerLength = input("How long should the timer run?")
    try:
        timerLength = int(timerLength)
        break
    except:
        print("Please try again.")
        continue
t = timerLength
for i in range(timerLength):
    print(t)
    t -= 1
    time.sleep(1)
    if t == 0:
        print("BEEP, BEEP, BEEP!\nTIMES UP!")
        break