with open('names_1.txt', 'r') as file:
    arr = []
    for i in file:
        arr.append(i)
    for index, item in enumerate(arr):
        if item == 'Johan\n':
            arr[index] = 'Alex\n'
        if item == 'Johan':
            arr[index] = 'Alex'

file.close()
print(arr)

with open('names_1.txt', 'w') as file:
    file.write(arr[0])
file.close()

a = len(arr)
with open('names_1.txt', 'a') as file:
    for i in range(1, len(arr)):
        file.write(arr[i])


