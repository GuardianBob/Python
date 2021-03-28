import os, time, sys

slp = input("Enter minutes for sleep: ")
# print(slp)
if slp != "":
    tm = float(slp)
    # print("Printed immediately.")
    n = tm * 60
    # time.sleep(n)
    print('Press "Ctrl+C to stop')
    t = round(n)
    for i in range(t,0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        time.sleep(1)
    # print(f"Printed after {tm} minutes.")
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")