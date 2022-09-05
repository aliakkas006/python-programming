def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed -= 5

    if speed <= 60:
        return 0
    if speed <= 80:
        return 1
    return 2


print(caught_speeding(65, True))


def has22(nums):
    for i in range(1, len(nums)):
        if nums[i] == 2 and nums[i-1] == 2:
            return True
    return False


print(has22([1,2,2]))
print(has22([1, 2, 1, 2]))
