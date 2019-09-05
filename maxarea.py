import time
def twoSum( nums, target):
   def maxArea(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        maxarea=0
        while r-l>=1:                       
            if height[l]>height[r]: 
                maxarea=max(maxarea,(r-l)*height[r])
                r=r-1
            else:
                maxarea=max(maxarea,(r-l)*height[l])
                l=l+1
        return maxarea