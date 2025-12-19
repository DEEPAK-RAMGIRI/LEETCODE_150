#  27 Remove Element
index = 0
for i in nums:
    if i == val:
        continue
    nums[index] = i
    index+=1
print(index)
