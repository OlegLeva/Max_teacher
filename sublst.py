def check(lst, sublst):
   for i in range(0, len(lst)):
       if lst[i:i+len(sublst)] == sublst:
           return True
   return False
print(check([1,2,3,4,5,6,7,8],[2,3,4]))