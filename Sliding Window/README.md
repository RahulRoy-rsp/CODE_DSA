- [binarySubSumGoal.py](https://github.com/RahulRoy-rsp/CODE_DSA/blob/main/Sliding%20Window/binarySubSumGoal.py)
  - Given a array containing only binary nums and an integer goal, return the total number of non-empty contiguous subarrays with a sum goal.
  - Example:
    - Input: nums = [1, 0, 1, 1], sum = 2
    - Output: 3
      - because only 3 contiguous subarrays sum is equal to the goal(2), which are [**1**, 0, **1**, 1], [**1**, 0, 1, **1**], [1, 0, **1**, **1**],(take the bold ones in consideration)

- [longestSubstringWitoutoutRep.py](https://github.com/RahulRoy-rsp/CODE_DSA/blob/main/Sliding%20Window/longestSubstringWitoutoutRep.py)
  - find the length of the longest substring without repeating characters.
  - Example:
    - Input: s = "abca"
    - Output: 3
      - because **abc** is the longest substring without repeating characters
 
- [niceSubArrays.py](https://github.com/RahulRoy-rsp/CODE_DSA/blob/main/Sliding%20Window/niceSubArrays.py)
  - Given an array of integers nums and an integer k.
  - A continuous subarray is called nice if there are k odd numbers on it.
  - Return the number of nice sub-arrays.
  - Example:
    - Input: nums = [1,1,2,1,1], k = 3
    - Output: 2
      - because only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

- [substringWithABC.py](https://github.com/RahulRoy-rsp/CODE_DSA/blob/main/Sliding%20Window/substringWithABC.py)
  - Find the number of substrings containing a, b and c atleast once.
  - Example:
    - Input: s = "abca"
    - Output: 3
      - The substrings possible in above string is a, ab, **abc**, **abca**, bc, **bca**, ca, a
      - where the bold ones contains a, b, c atleast once. 
