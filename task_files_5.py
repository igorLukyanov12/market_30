with open('task_files_5_text.txt', 'r') as file:
    arr = []
    arr_write = []
    for i in file:
        arr.append(i)
    print(arr)
file.close()
for i in arr:
    age = 0
    for index, item in enumerate(i):
        if index == len(i) - 1:
            break
        if item.isdigit():
            if i[index+1].isdigit():
                break
            else:
                if int(item) < 5:
                    arr_write.append(i)
print(arr_write)

with open('names_1.txt', 'a') as file:
    for i in arr_write:
        file.write(i)
file.close()