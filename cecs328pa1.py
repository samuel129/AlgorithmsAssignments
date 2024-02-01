# Samuel Kim - 027845491

import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]
    
def sumDigits(digits):
    return sum(int(digit) for digit in digits)
    
file_name = sys.argv[1]
numbers = read_file(file_name)

foundNums = set()
left = 0
currMax = 0
currSum = 0

for num in range(len(numbers)):
    total = sumDigits(numbers[num])
    
    while total in foundNums:
        foundNums.remove(sumDigits(numbers[left]))
        left += 1
        currMax = max(currMax, (num - left + 1))
        foundNums.add(total)

print(currMax)
