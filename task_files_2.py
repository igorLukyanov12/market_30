with open('task_files_2_text.txt', 'r') as file:
    arr = []
    max = -1
    min = 100
    for i in file:
        arr.append(int(i))
        if int(i) > max and int(i) >= 0 and int(i)%2 == 0:
            max = int(i)
        if int(i) < min and int(i) >=0 and int(i)%2 == 0:
            min = int(i)
    print(arr)
    print(max, 'max')
    print(min, 'min')
file.close()
with open('names_1.txt', 'a') as file:
    if max == -1:
        file.write('\nNo needed max value')
    else:
        file.write('\nmax = '+ str(max))
    if min == 100:
        file.write('\nNo needed min value')
    else:
        file.write('\nmin = ' + str(min))

