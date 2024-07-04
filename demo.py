print("hello world")
# Q1
a=int(input("enter a number :"))
cube=a*a*a
print(cube)   

# Q2  
def convert(seconds) :
   seconds = seconds % (24 * 3600)
   seconds %= 3600
   minutes = seconds // 60
   seconds %= 60

   return "%02d:%02d" % (minutes,seconds)

n=int(input("enter number of secs :"))
print(convert(n))


# Q3
sum=0
while True :
   
    b=input("enter some no. :")
    if b.lower() == 'done':
       break

    try:
       number=float(b)
       sum+=number
    except ValueError:
       print("invalid input")
                                  
print("total sum is :",sum)   
     
# Q4

# Q5     
c=int(input("enter a number between 0-999 :"))
if (c>0) and (c<=9):
   print("1 digit number")
elif (c>=10) and (c<=99):
    print("2 digit number")
elif (c>=100) and (c<=999):
    print("3 digit number")
else:
   print("not valid")    
   

# Q6
d="hello Everyone,I Am Learning Python"
e=print(d[0].upper() + d[1:])

if(d>='A' and d<='Z'):
    print(True)
elif(d>='a' and d<='z'):
    print(True)
else:
    print(False)

if(d>='0' and d<='9'):
    print(True)
else:
    print(False)   


f=d.title()
if(f == d):
    print("yes,it is in title case")
else:
    d=f
    print(d)

g=d.swapcase()
print(g)

# Q7
l=['P','Y','T','H','O','N']
for h in l:
    print(h)

# Q8
list1=[1,2,3]
list2=[4,5,6]
list3=print(list1+list2)
list4=[1, 2, 3, 4, 5, 6]
print(list4 *3)

# Q9
list=[13,18,12,14,20,1,6]
print(list.index(1))
print(list.index(12))
list.append("PBX1")
print(list)
list.insert(3,"Red")
print(list)
list.pop(4)
print(list)
print(len(list))
list.reverse()
print(list)
print(list[1:4])
print(list[0::2])

# Q10
t1=(1,2,3,4,5)
t2=('a','b','c','d')
t3=print(t1+t2)
print(t3)
t4=(1, 2, 3, 4, 5, 'a', 'b', 'c', 'd')
print(len(t4))
print(max(t1))
print(min(t1))

# Q11
t5=tuple([5,4,9])
print(t5)

# Q12
t6=tuple({1:'A',2:'N'})
print(t6)

# Q13
winners={"kohli":76,"rohit":69,"sky":56}
print(winners["kohli"])