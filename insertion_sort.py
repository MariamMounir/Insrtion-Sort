def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[i]
        j=i-1

        while j>=0 and key <arr[j]:
            arr[j+1],arr[j]=arr[j],arr[j+1]
            j=j-1
    return arr       

  

rar=[]
n=int(input("Enter the number of element: "))
for i in range (0,n):
    element=int(input("Enter the element: "))
    rar.append(element)
    
print(insertion_sort(rar))
