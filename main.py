data = [['*******'],['*******'],['***x***'],['**xxx**'],['***x***'],['***x***'],['***x***'],['*******']]

def findX(input):  
  for y in range(0, len(input)):    
    for x in range(0, len(input[y])):
      text = input[y][x]
      for t in range(0,len(text)):
        if text[t] == 'x':          
          return True


data_find = findX(data)
print(data_find)