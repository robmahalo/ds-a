def add_two_numbers() -> int:
    two_nums = input()
    new_nums = two_nums.split(",")
    res = 0
    
    for num in new_nums:
        res += int(num)
    
    return res



# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
