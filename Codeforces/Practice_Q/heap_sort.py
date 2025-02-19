#User function Template for python3

class Solution:
    def heapify(self,arr, n, i):
        largest = i
        left = 2*i+1
        right = 2*i+2
        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest!=i:
            arr[i],arr[largest]=arr[largest],arr[i]
            self.heapify(arr,n,largest)
    
    
    #Function to build a Heap from array.
    def buildHeap(self,arr,n):
        for i in range(n//2-1,-1,-1):
            self.heapify(arr,n,i)
    
    #Function to sort an array using Heap Sort.    
    def HeapSort(self, arr, n):
        self.buildHeap(arr,n)
        for i in range(n-1,0,-1):
            arr[0],arr[i]=arr[i],arr[0]
            self.heapify(arr,i,0)
        return arr
        
arr = [4,1,3,9,7,6,5,8,2]
n = len(arr)
ob = Solution()
print(ob.HeapSort(arr,n))