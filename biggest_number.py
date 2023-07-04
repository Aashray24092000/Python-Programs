def bigger(a,b):
  if a>b:
    return a
  else:
    return b

def biggest(a,b,c):
   return bigger(a,bigger(b,c))
   
print biggest(3,7,1)

# another way of finding big number by function 

def big(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c
big(1000,200,300)

#efficient code
