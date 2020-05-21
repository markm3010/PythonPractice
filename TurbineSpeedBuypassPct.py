from signal import signal, SIGINT
import sys

print('\nPBI\'s ADV:369915 and CAD:330643 \nVerify percent calc is correct: ( (hivalue-lowvalue)/hivalue*100 )')
print()

def handler(signal_received, frame):
    print('\n')
    exit()

while True:
    signal(SIGINT, handler)

    loval = input("enter lo value: ")
    hival = input("enter hi value: ")

    if float(hival) == 0.0:
        print('Error: hi value cannot be zero, start over!\n')
        next
    else:
        perc = (float(hival) - float(loval)) / float(hival) * 100
        rounded_perc = round(perc, 3)
        print(f"TRPMPERCTX should be {rounded_perc}\n")

