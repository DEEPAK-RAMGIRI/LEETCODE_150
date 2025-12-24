80. Remove Duplicates from Sorted Array II
maps = dict()
  index = 0
  for i in nums:
      maps[i] = maps.get(i,0)+1
      if maps[i] > 2:
          continue
      nums[index] = i
      index+=1
  print(index)
