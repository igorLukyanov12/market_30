with open('tasks_files_text.txt', 'r') as file:
    arr = []
    for i in file:
        arr.append(int(i))
file.close()

sum = 0
for i in arr:
    sum+=i
print(sum)
avrg = sum/len(arr)
print(avrg)
with open('names_1.txt', 'a') as file:
    file.write('\n'+str(avrg))
