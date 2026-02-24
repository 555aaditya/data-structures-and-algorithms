# 1752. Check if Array Is Sorted and Rotated

def checker(nums: list[int]) -> bool:
    n = len(nums)
    count = 1

    for i in range(1,n*2):
        if nums[(i-1)%n] <= nums[i%n]:
            count += 1
        else: 
            count = 1
        if count == n:
            return True
    return n == 1
            
    
if __name__ == "__main__":
    nums = [4,5,5,6,7,1,2,3,3,4]
    print(checker(nums))