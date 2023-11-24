import time
x = 0
while True:
    x += 1 
    try:
        print(x)
        time.sleep(1)
    except KeyboardInterrupt:
        exit()
    