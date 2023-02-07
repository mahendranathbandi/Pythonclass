
# print first 100  prime number
# list1=[1,2,2,3,3,4,5,5] remove duplicate elements in given list
# input list1=[1,2,3,4,4,5] o/p=[1,4,9,16,16,25]
# "This is python" print reverse of the string.


#prime Numbers 1-100
#

flag = False
for i in range(1,100):

    for j in range(2,i):
        if(i%j)==0:
            flag=True
            break
    if flag==True:
        print(i,end=" ")
    else:
        print("This is prime number"+str(i))



def prime(n):
    if n>1:
        for j in range(2,n):
            if (n%j==0):
                return False
        return True
    else:
        return False

for i in range(1,100):
    if prime(i)==True:
        print(i,end=" ")


# list1=[1,2,2,3,3,4,5,5] remove duplicate elements in given list

# list1=[1,2,2,3,3,4,5,5]
# output=[]
# for i in list1:
#     if i not in output:
#         output.append(i)
#         print(output)

# input list1=[1,2,3,4,4,5] o/p=[1,4,9,16,16,25]

a=[1,2,3,4,4,5]
for i in a:
    j=i*i