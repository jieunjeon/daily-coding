
"""
https://leetcode.com/problems/trapping-rain-water/
42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

"""
def maxWaterBruteForce(arr, n) :
    """
    Time Complexity: O(n^2): two nested loops.
    Space Complexity: O(1)

    The idea is to traverse every array element and find the highest bars on the left and right sides. Take the smaller of two heights. The difference between the smaller height and height of the current element is the amount of water that can be stored in this array element.

    1. Traverse the array from start to end.
    2. For every element, traverse the array from start to that index and find the maximum height (a) and traverse the array from the current index to end, and find the maximum height (b).
    3. The amount of water that will be stored in this column is min(a,b) – array[i], add this value to the total amount of water stored
    4. Print the total amount of water stored.
    """
    res = 0
    # For every element of the array
    for i in range(1, n - 1) :
        # Find the maximum element on its left
        left = arr[i]
        for j in range(i) :
            left = max(left, arr[j])
         
        # Find the maximum element on its right
        right = arr[i]
        for j in range(i + 1 , n) :
            right = max(right, arr[j])
             
        # Update the maximum water
        res = res + (min(left, right) - arr[i])
    return res

def maxWaterStack(height):
    """
    Time Complexity: O(n): Traverse the arr 1 time and put heights into a stack
    Space Complexity: O(n): use a stack to keep track of the height of each sides bar.
    
    We can use a Stack to track the bars that are bounded by the longer left and right bars. This can be done using only one iteration using Stacks.

    1. Loop through the indices of the bar array.
    2. For each bar, we can do the following:
    - While the Stack is not empty and the current bar has a height greater than the top bar of the stack,
    - Store the index of the top bar in pop_height and pop it from the Stack.
    - Find the distance between the left bar(current top) of the popped bar and the current bar.
    - Find the minimum height between the top bar and the current bar.
    - The maximum water that can be trapped in distance * min_height.
    - The water trapped including the popped bar is (distance * min_height) – height[pop_height].
    - Add that to the fans.
    """
    # Stores the indices of the bars
    stack = []
     
    # size of the array
    n = len(height)
     
    # Stores the final result
    ans = 0
     
    # Loop through the each bar
    for i in range(n):
         
        # Remove bars from the stack
        # until the condition holds
        while(len(stack) != 0 and (height[stack[-1]] < height[i]) ):
             
            # store the height of the top
            # and pop it.
            pop_height = height[stack[-1]]
            stack.pop()
             
            # If the stack does not have any
            # bars or the the popped bar
            # has no left boundary
            if(len(stack) == 0):
                break
             
            # Get the distance between the
            # left and right boundary of
            # popped bar
            distance = i - stack[-1] - 1
             
            # Calculate the min. height
            min_height = min(height[stack[-1]],height[i])-pop_height
             
            ans += distance * min_height
         
        # If the stack is either empty or
        # height of the current bar is less than
        # or equal to the top bar of stack
        stack.append(i)
     
    return ans
 
if __name__ == "__main__" :
 
    arr = [0, 1, 0, 2, 1, 0,
           1, 3, 2, 1, 2, 1]
    n = len(arr)
    
    print(maxWaterBruteForce(arr, n))
    print(maxWaterStack(arr, n))