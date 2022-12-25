temp_f = 40

while temp_f > 32:
    print(f'The water is {temp_f} degrees')
    temp_f -= 1
    if temp_f == 33:
        break

for number in range(1,11):
    if number == 7:
        print("We're skipping number 7")
        continue
    print(f'This is number {number}')

for number in range(1,11):
    if number == 3:
        pass
    else:
        print(f'This is the number {number}')