nums = [2, 14, 18, 22, 22]
# return true if any value appears twice

dict = {}

for i in range(len(nums)):
    j = 1
    if nums[i] not in dict:
        dict[nums[i]] = j
    elif nums[i] in dict:
        dict[nums[i]] = j + 1

print(dict)
for i in dict.values():
    if i == 2:
        print("true")
        break
    else:
        continue
