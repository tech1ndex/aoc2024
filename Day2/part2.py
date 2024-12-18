def check_safety(a):
  diffs = [a[i + 1] - a[i] for i in range(len(a) - 1)]    # build list of differences between consecutive pairs
  if (all(x < 0 and x in range(-3, 0) for x in diffs) or  # all differences are negative and between -3 and -1
      all(x > 0 and x in range(1, 4) for x in diffs)):    # all differences are positive and between 1 and 3
    return True
  else:
    return False


# read input_data from file
with open("input.txt", "r") as file:
  input_data = file.readlines()

total = 0
for line in input_data:
  nums = [int(num.strip()) for num in line.split()]
  if check_safety(nums):
    total += 1
  else:
      i = 0
      abs_len = len(nums) - 1
      while i < len(nums):
        value = nums[i]
        nums.pop(i)
        if len(nums) >= abs_len:
          if check_safety(nums):
            total += 1
          else:
            nums.insert(i, value)
            i += 1

print(total)