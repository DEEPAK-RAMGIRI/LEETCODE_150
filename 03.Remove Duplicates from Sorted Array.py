# 26.Remove Duplicates from Sorted Array

index = 0
seen = set()
for i in nums:
    if i in seen:
        continue
    seen.add(i)
    nums[index] = i
    index+=1
print(index)
