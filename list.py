nums=list(map(int,input("Enter integers seperated by space:").split()))
for i in range(len(nums)):
  if nums[i]>100:
     nums[i]="over"
print("Modified List:",nums)
