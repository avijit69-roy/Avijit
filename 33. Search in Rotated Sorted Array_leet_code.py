nums = [1,3,5]

target = 3

sta=0
end=len(nums)-1
c=0
if (len(nums) == 1 and nums[0] == target):
    print(0)
elif target not in nums:
    print(-1)
else:
    while (sta <= end):
        if (nums[sta] == target):
            print(sta)
            break
        if (nums[end] == target):
            print(end)
            break
        sta += 1
        end -= 1
