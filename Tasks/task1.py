def Sort(list):
  for _ in range(len(list)):
    for j in range(len(list)-1):
      if list[j] > list[j+1]:
        list[j], list[j+1] = list[j+1], list[j]
        
  return list


if __name__ == '__main__':  
  list = [14,2,1,5,2,5,6,9]
  print(Sort(list))