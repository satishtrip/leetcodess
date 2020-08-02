
#nums = [1,1,1,2,2,3,4,4,5,5]

#j = 0
#for i in range(len(nums) - 1):
 #   if nums[i] != nums[i + 1]:
  #      nums[j] = nums[i + 1]
   #     j += 1

#print(j)


#for x in range(len(nums)):


 #   if nums[x]==nums[x+1]:
  #      nums.pop(x)


#print(len(nums))
#print(nums)
        #and diff in dd:
                 #return [dd[diff],i]
#i=0

#while i+1<len(nums):
 #   if nums[i]==nums[i+1]:
  #      nums.pop(i)
   # else:
    #    i=i+1
    #rint(len(nums))
    #print(nums)


#w = input()
#li = list(map(len, w.split()))
#print(li[-1])

#x = [8,8,1,1,2,2,2,2,3,3,3,3,3,3,3,77,77,77,77,77,77,77,77,77,77]
#x.sort()
#print(x)
#print(x[(len(x)//2)])
#s = "satish is blue waala ladka"
#rev = s.split()
#print(rev)
#print(' '.join(rev[::-1]))
#print(r.reverse())
#s = ''
#s = ' '.join(r)
#print(s)
#l = s.split()
#return ' '.join(l[::-1])
#x = [100, 4, 200, 1, 3, 2]
#for i in x:
 #   if x[i] >10 :
  #      x[i] // 10

 # Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
  # Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
import random
#k = int(input())
#nums = [1,2,3,4,5,6,7]
#print(nums[:])
#print(len(nums))
#if k > len(nums):
#    k = k - len(nums)
 #   nums = nums[-k:] + nums[:-k]
#else:
 #   nums = nums[-k:] + nums[:-k]
#print(nums)

#An array is monotonic if it is either monotone increasing or monotone decreasing.
#
#An array A is monotone increasing if for all i <= j, A[i] <= A[j].  An array A is monotone decreasing if for all i <= j, A[i] >= A[j].

#Return true if and only if the given array A is monotonic.



#Example 1:

#Input: [1,2,2,3]
#Output: true
#Example 2:

#Input: [6,5,4,4]
#Output: true

#A = [1,2,2,4,6,6]
#for x in A:
 #   if A[x] <= A[x+1] and A[x] >= A[x+1] :
  #  return True
   #     else:
    #            return False
#            #
#def isMonotonic(self, A) -> bool:
   # A = [6,5,4,4]
    #increase = 0
    #decrease = 0
    #for i in range(len(A) - 1):
     #   if A[i] == A[i + 1]: continue
#
 #       if A[i + 1] > A[i]:
  #          increase += 1
   #     else:
    #        decrease += 1
     #   if increase > 0 and decrease > 0:
      #      return False
    #return True

#A= [-4,-1,0,3,10]
#A = ([i**2 for i in A])
#A.sort()
#print(A)
#class Solution:
 #   def sortedSquares(self, A: List[int]) -> List[int]:
  #      A=[i**2 for i in A]
   #     A.sort()
    #    return A
# Given an array of integers where 1 ≤ a[i] ≤ n (n = size of array), some elements appear twice and others appear once.
#
# Find all the elements of [1, n] inclusive that do not appear in this array.
#
# Could you do it without extra space and in O(n) runtime? You may assume the returned list does not count as extra space.
# Input:
# [4,3,2,7,8,2,3,1]
#
# Output:
# [5,6]
# A= [4,3,2,7,8,2,3,1]
#
# D=[]
# A.sort(reverse=True)
# print(A)
# x = 0
# for x in range(len(A) - 1):
#     s = A[x]-A[x+1]
#     if s != A[x]:
#         D.append(s)
#
# print(D)

# getMissingNo takes list as argument
#def find_missing(lst):
 #   return [x for x in range(lst[0], lst[-1] + 1)
  #          if x not in lst]


#lst = [4,3,2,7,8,2,3,1]
#print((set([i for i in range(1, len(lst)+1)])))
#print(set(lst))
#lst.sort(reverse=True)
#print(find_missing(lst))



# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.
#
# You may return any answer array that satisfies this condition.
#
#
#
# Example 1:
#
# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

#A=[2,4,3,1]
#odd = []
#even = []
#for i in A:
 #   if i % 2==0:
  #      even.append(i)
   # else:
    #    odd.append(i)

#print(even+odd)
#arr = [2,2,3,4,4,4]
#count = 0

#out = []
#for i in range(len(arr)):
 #   if arr.count(arr[i]) == arr[i]:
  #      out.append(arr[i])
#return max(out) if out != [] else -1
#for i in range(len(arr)):
 #   if arr.count(arr[i]) == arr[i]:
  #      count = count+1
   #     if count == arr[i]:
    #        print(arr[i])
     #   else:
      #      count = count
    #else:
     #   print("No lucky")
# def findLucky(self, arr):
#     arr = [1,2,2,3,3,3]
#     c = []
#     for i in range(len(arr)):
#         if arr[i] == arr.count(arr[i]):
#             c.append(arr[i])
#         if c == None or len(c) == 0:
#             return -1
#
#         else:
#             return (max(c))




# lucky numbers
# from  collections import Counter
# arr = [2,2,2,3,3,]
# c = Counter(arr)
# m = -1
# print(c)
# for i in c:
#     if c[i] == i:
#         m = max(m, i)
# print(m)

#nums1 = [4,9,5]
#nums2 = [9,4,9,8,4]

#print(set(nums1))
#print(set(nums2))
#nums1=set(nums1)
#nums2=set(nums2)
#print(nums1 & nums2)

#print((set(nums1).intersection(set(nums2))))

# 1365. How Many Numbers Are Smaller Than the Current Number
# Input: nums = [6,5,4,8]
# Output: [2,1,0,3]
# a=[]
# for i in range(0,len(nums)):
#     count=0
#     for j in range(0, len(nums)):
#         if j!=i and nums[j] < nums[i]:
#             count = count+1
#     a.append(count)
# return a
# nums = [8,1,2,2,3]
#                                                   #
#
# j=0
# s=[]
# for i in range(0,len(nums)):
#     count = 0
#     for j in range(0,len(nums)):
#         if j!=i and nums[j]< nums[i]:
#             count = count+1
#     s.append(count)
#
#
# print(s)

#  Replace Elements with Greatest Element on Right Side

# Given an array arr, replace every element in that array with the greatest element among the elements to its right, and replace the last element with -1.
#
# After doing so, return the array.
#
#
#
# Example 1:
#
# Input: arr = [17,18,5,4,6,1]
# Output: [18,6,6,6,1,-1]
#

# arr = [17,18,5,4,6,1]
# i=0
# rep = []
# #print(arr[0])
# #print(max(arr[:]))
# for i in range(len(arr)):
#     if i == len(arr)-1:
#         rep.append(-1)
#     else:
#         rep.append(max(arr[i+1:]))
#         print(rep)

   # v=arr[0]=max(arr[1:])
#print(v)
#i = len(arr)-1
#print(arr[i])
#print(answer.append(-1))
#for i in range(0,len(arr)):
 #   sub = arr[i] - arr[i+1]
  #  print(min(sub))


  