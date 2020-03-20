def is_good_size(x,y,a,b,c):
    if (x>a) and (y>b) or (x>a) and (y>c) or (x>c) and (y>b):
        return True
    else:
        return False
print(is_good_size(60,70,20,30,40))