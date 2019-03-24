"""冒泡算法"""
# def maopao_sorted(A):
#     n = len(A)
#     for i in range(n-1):
#         for j in range(n-i-1):
#             if A[j] > A[j+1]:
#                 A[j],A[j+1] = A[j+1],A[j]
#     return A
# m = [3,4,2,1,7,5,6]
# print (maopao_sorted(m))
#
# """选择排序"""
# def xuanze_sorted(A):
#     n =len(A)
#     for i in range(n-1):
#         min_index = i
#         for j in range(i+1,n):
#             if A[min_index] > A[j]:
#                 min_index = j
#         A[min_index],A[i] = A[i],A[min_index]
#     return A
# m1 = [3,4,2,1,7,5,6]
# print(xuanze_sorted(m1))
#
# """插入排序"""
# def charu_sorted(A):
#     n = len(A)
#     for i in range(1,n):
#         j = i
#         while j > 0:
#             if A[j] < A[j-1]:
#                 A[j],A[j-1] = A[j-1],A[j]
#             j -= 1
#     return  A
# m2 = [3,4,2,1,7,5,6]
# print(charu_sorted(m2))
#
# """快速排序"""
# def kuaisu_sorted(A,first,last):
#     mid_value = A[first]
#     low = first
#     high = last
#     while low < high:
#         while low <high and A[high] > mid_value:
#             high -= 1
#         A[low] = A[high]
#         while low < high and A[low] < mid_value:
#             low += 1
#         A[high] = A[low]
#     A[low] = mid_value
#     kuaisu_sorted(A,first,low-1)
#     kuaisu_sorted(A,low +1,last)
#     return A
# m3 = [3,4,2,1,7,5,6]
# print(charu_sorted(m3))
#
# """希尔排序"""
# def xier_sorted(A):
#     n = len(A)
#     gap = n //2
#     while gap > 0:
#         for i in range(gap,n):
#             j = i
#             while j > 0:
#                 if A[j] < A[j-gap]:
#                     A[j] ,A[j-gap] = A[j-gap] ,A[j]
#                 j -= gap
#         gap //= 2
#     return  A
# m4 = [3,4,2,1,7,5,6]
# print(charu_sorted(m4))
# """归并算法"""
# def guibing_sorted(A):
#     n = len(A)
#     if n <= 1:
#         return
#     mid = n // 2
#     left_li = guibing_sorted(A[:mid])
#     right_li =guibing_sorted(A[mid:])
#     right_pointer,left_pointer = 0,0
#     result = []
#     while right_pointer < len(right_li) and left_pointer < len(left_li):
#         if right_li[right_pointer] < left_li[left_pointer]:
#             result.append(right_li[right_pointer])
#             right_pointer += 1
#         else:
#             result.append(left_li[left_pointer])
#             left_pointer += 1
#     result += left_li[left_pointer:]
#     result += right_li[right_pointer]
#     return  result
# m5 = [3,4,2,1,7,5,6]
# print(charu_sorted(m5))

# m = [4,-1,0,1,2,-1]
# def threeSum(nums):
#     n =len(nums)
#     res = []
#     if n < 3:
#         return []
#     for i in range(n-2):
#         for j in range(i+1,n-1):
#             if 0 - nums[i] - nums[j] in nums[max(i,j)+1:]:
#                 m = [nums[i],nums[j],-nums[i]-nums[j]]
#                 m.sort()
#                 if m not in res:
#                     res.append(m)
#     return res
# print(threeSum(m))
# def threeSumClosest(self, nums, target):
#     nums.sort()
#     res = sum(nums[:3])
#     for i in xrange(len(nums)):
#         l, r = i+1, len(nums)-1
#         while l < r:
#             s = sum((nums[i], nums[l], nums[r]))
#             if abs(s-target) < abs(res-target):
#                 res = s
#             if s < target:
#                 l += 1
#             elif s > target:
#                 r -= 1
#             else: # break early
#                 return res
#     return res

def sorted(n):
    m = [1 for i in range(n)]
    res = []
    res.append(m)
    while n >= 2:
        for i in range(n-2):
            d = [m[i]+m[i+1]]
            s = m[:i]+d+m[i+2:]
            res.append(s)
        n -= 1
    return res
print(sorted(6))

array = []
if not array:
    print("hello")
