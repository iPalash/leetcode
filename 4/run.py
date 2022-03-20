class Solution:
    def findMediaSortedArrays(self, nums1: list[int], nums2: list[int]) -> int:
        print(nums1,nums2)

        def find(s1, e1, s2, e2, k):
            if s1>e1:
                return nums2[k-s1]
            if s2>e2:
                return nums1[k-s2]

            m1 = (s1+e1)//2
            m2 = (s2+e2)//2
            med1 = nums1[m1]
            med2 = nums2[m2]

            if m1+m2<k:
                # Right half of one array 
                if med1>med2:
                    # All of 2nd arr first half comes before med1
                    return find(s1,e1,m2+1,e2,k)
                else:
                    return find(m1+1,e1,s2,e2,k)
            else:
                if med1>med2:
                    # All of 1st arr right half can be removed
                    return find(s1,m1-1,s2,e2,k)
                else:
                    return find(s1,e1,s2, m2-1,k)

        m = len(nums1)
        n = len(nums2)

        if (l:=m+n)%2==1:
            return find(0,m-1,0,n-1,l//2)
        else:
            return (find(0,m-1,0,n-1,l//2) + find(0,m-1,0,n-1,l//2-1))/2

nums1 = [int(el) for el in input()[1:-1].split(',')]
nums2 = [int(el) for el in input()[1:-1].split(',')]

print(Solution().findMediaSortedArrays(nums1,nums2))
