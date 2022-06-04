with open('task_files_4_text.txt', 'r') as file:
    arr = []
    for i in file:
        arr.append(int(i))
    arr.sort()
    print(arr)
file.close()

with open('names_1.txt', 'a') as file:
    for i in arr:
        file.write('\n'+str(i))

