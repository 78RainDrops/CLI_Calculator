equation = [5, "-", 2, "+", 2, "*", 2, "%", 2]

nums = []
operations = []
result = None

for ops in equation:
    if isinstance(ops, int):
        nums.append(ops)
    else:
        operations.append(ops)

result = nums[0]

for i in range(1,len(nums)):
    op = operations[i-1]
    num = nums[i]
    
    match op:
        case "+":
            result += nums[i]
        case "-":
            result -= nums[i]
        case "*":
            result *= nums[i]
        case "/":
            result /= nums[i]
        case "%":
            result %= nums[i]
        case _:
            print("Something is wrong")

print(f"Final Result: {result}")
         