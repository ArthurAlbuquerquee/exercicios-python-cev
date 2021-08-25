from time import sleep
print('Os fogos vão estourar em:')
for c in range(10, -1, -1):
    sleep(1)
    print(c)
sleep(0.6)
print('BOOM! POOOW! POW!')
