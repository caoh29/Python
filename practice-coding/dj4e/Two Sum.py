nums = [2,7,11,15]
target = 9
numbers = []

#nums.index[number]

for number in nums:
    if (target - number) >= 0:
        numbers.append(nums.index(number))
        

sum = 0
print(numbers)
for i in numbers:
    sum += i

if sum == target:
    answer = True
else:
    answer = False

print(answer)
