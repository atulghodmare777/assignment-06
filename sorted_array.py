def intersection_sorted_arrays(array1,array2):
  i,j=0,0
  result=[]
  while i < len(array1) and j < len(array2);
    if array1[i] < array2[j];
      i+=1
elif array1[i] > array2[j];
      j+=1
else:
  if not result or result [-1]! = array1[i]:
    result.append(array1[i])
  i+=1
  j+=1
  return result
array1=[1,2,2,3,4,5]
array2=[2,2,5,6]
print (intersection_sorted_arrays(array1,array2))
