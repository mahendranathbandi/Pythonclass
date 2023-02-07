###


#
# def functionaname():
#     print("I am mahaesh ")
#
# functionaname()

# def sunmof(a,b):
#     print(a+b)
#     return a+b
#
# print(sunmof(10,56))

#default arguments or non -positional arguments
# postional arggymnets
# *var
# **var
#
# def sum1(a,b):
#     print(a,b)
#
# sum1(5,6)

# def sum1(*var):
#     sum2=0
#     for i in var:
#         sum2=sum2+i
#     return sum2
#
# result=sum1(1,2,3,4,5,6,7,8,9)
# print(result)


def sum2(**var):
    return (var)

result=sum2(name="mahesh",age=25,place="narasarpet")
print(result)


# result=lambda x,y:x+y+1
# print(result(5,6))
#
# def fun(x):
#     print(x+1)
# fun(5)



# list1=[1,2,3,5,6,9]
# list1.sort(key=lambda x:(x%2,x))
# print(list1)



# dic1={"name":145,"name2":56,"name4":89,"name6":895}


result=[(lambda x: x*x)(x) for x in range(10)]



print(result)


call by value vs refrence

recursive function

global var local var






