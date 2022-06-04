with open('task_files_3_text.txt', 'r') as file:
    arr = []
    count = 0
    a = 0
    for i in file:
        arr.append(int(i))
    for i in range(len(arr)):
        if i == len(arr) - 2:
            break
        if arr[i] == arr[i+1]:
            count+=1
        elif arr[i] != arr[i+1] and count > a:
            a = count
            count = 0
        else:
            count = 0
    a = a+1
    print(a)
file.close()

with open('names_1.txt', 'a') as file:
    file.write('\nLenth of longest chain of identical numbers = ' + str(a))