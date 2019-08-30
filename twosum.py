import time
def twoSum( nums, target):
    """
    nums是包含负数，正数，零，所以target可以与元素相等，也可以大于或小于元素
    :param nums:
    :param target:
    :return:
    """
    numlen = len(nums)
    for i in range(numlen - 1):
        for n in range(i + 1, numlen):
            if (nums[i] + nums[n] == target):
                return [i, n]

def twosumhash(nums,target):
    dic={}
    for i in range(len(nums)):
        com=target-nums[i]
        if com in dic:
            return [dic.get(com),i]
        dic[nums[i]]=i

if __name__=='__main__':
    start=time.time()
    nums=[0,4,3,0]
    target=0
    result=twosumhash(nums,target)
    print(result)
    end=time.time()
    print(end-start)