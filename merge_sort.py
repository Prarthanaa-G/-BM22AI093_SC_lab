def mergesort(arr,low,high):
  if low<high:
    mid=(low+high)//2
    mergesort(arr,low,mid)
    mergesort(arr,mid+1,high)
    merge(arr,low,mid,high)
  return arr

def merge(arr,low,mid,high):
  i=low
  j=mid+1
  b=[]
  while i<=mid and j<=high:
    if arr[i]<arr[j]:
      b.append(arr[i])
      i+=1
    elif arr[j]<arr[i]:
      b.append(arr[j])
      j+=1
  while i<=mid:
    b.append(arr[i])
    i+=1
  while j<=high:
    b.append(arr[j])
    j+=1

  for k in range(low,high+1):
    arr[k]=b[k-low]

arr=[5,4,3,2,1]
mergesort(arr,0,len(arr)-1)
print(arr)
