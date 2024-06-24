# first try 
# x=int(input())
# y=int(input())
# ans=0
# if x*y<=1000:
#     ans=x*y
# else:
#     ans=x+y
# print("The result is {}".format(int(ans)))

# secound try 
def product_or_sum(x, y):
    product = x * y
    if product <= 1000:
        return product
    else:
        return x + y
x=int(input())
y=int(input())
result = product_or_sum(x, x)
print("The result is {}".format(result))