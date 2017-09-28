def add_small (x,y):
    if x > 10 or y > 10:
        return 0

        return x + y

        print(add_small(100,10))
        print(add_small(2,3))
        
#task2: create max function - two args, return the bigger, call it my_max

def some_fun(firstarg, some_arg=100):
    print('I am such a nice function, I got these args:', firstarg, some_arg)

some_fun(100,300)
some_fun(100)


def add(n1, n2):
    return n1 + n2

num = add(2,2)

# The fibonacci sequence is as such: 1 1 2 3 5 8 13 21 34
# f(0)
# f(n) = f(n-1) + f(n-2)
def fibonacci(n):
    # Your code here.
    if (n == 0 or n == 1):
        return 1
    return fibonacci(n-1) + fibonacci(n-2) 


print(fibonacci(5))
