numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0

for number in numbers:
    i = numbers.index(number)
    if number > 10:
        if number % 10 > 5:
            numbers[i] = number // 10 * 10 + 10
        else:
            numbers[i] = number // 10 * 10
    elif number >= 5:
        numbers[i] = 10
    else:
        numbers[i] = 0

numbers.sort()
numbers.pop(0)
numbers.pop(len(numbers) - 1)

mean_number = sum(numbers) / len(numbers)
print(numbers)
print(mean_number)
