import timeit

# to compare we use memory and time
## O(n) n is the factor
code = '''
def sum1(n):
    total = 0
    for x in range(n+1):
        total += x
    return total
'''

print(timeit.timeit(setup="", stmt=code))


# compare the effciency can come by compairing the number of assignments
# in example it will assign x to zero then to one ....etc
# Big ) how quickly run time increases if data increase
# asymptotic analysis what is the limiting factor
###### example 
def bigO(n):
    return 45 * n ** 3 + 20 * n ** 2 + 19


print(bigO(1))
print(bigO(2))


# we can see the 19 is not the factor
# we can ignore the constants
# we have to look at n**2 and n**3
# the final result is heavily dependant on the n**3 so it is the big O
# and it will require the most time so the order is n^3


# o(1)
def func_constant(values):
    print(values[0])


func_constant([1, 2, 3, 4, 5])


# O(n)
def func_lin(lst):
    for val in lst:
        print(val)


func_lin([1, 2, 3, 4, 5, 6])


# O(n^2)
def func_quad(lst):
    for item_1 in lst:
        for item_2 in lst:
            print(item_1, item_2)


func_quad([1, 2, 3, 4, 5, 6])


# it will be n*n because each for is dependant on n and
# we know that it is nested so it is n*n


# for example
def print_3(lst):
    for i in lst:
        print(i)
    for i in lst:
        print(i)
    for i in lst:
        print(i)


print_3([1, 2, 3, 4])

# this is not bigO(n^3) but bigO(n*3) so linear or bigO(n)
# we ignore the constant

print('comp')


def comp(lst):
    print(lst[0])  # O(1)
    midpoint = len(lst) // 2

    # O(n/2)
    for val in lst[:midpoint]:  # :midpoint means from the beginning to the mid
        print(val)

    # O(10)
    for x in range(10):
        print('number')


comp([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# we end up with O(n)


################ Worst Case v Best Case #################
def mathcer(lst, match):
    for item in lst:
        if item == match:
            return True
        return False


mathcer([1, 2, 3, 4, 5, 6], 1)  # best case because it is index 0
mathcer([1, 2, 3, 4, 5, 6],
        20)  # worst case it will go through all elements so
# it is worst case
print('---------- space---------')


################ Space Complexity #################
def memory(n):
    for x in range(n):  # time O(n)
        print('Memory')  # space complexity O(1) it will not change
# it is not storing 10 versions if n = 10