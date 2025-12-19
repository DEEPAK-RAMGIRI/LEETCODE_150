# 169. Majority Element

# Time Complexcity O(n)
# Space Complexcity O(1)
ans = freq = 0
for i in nums:
    if freq == 0:
        ans = i
        freq =1
    elif i == ans:
        freq+=1
    else:
        freq-=1
print(ans)

