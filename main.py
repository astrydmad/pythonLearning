# This is a sample Python script.

from statistics import mean

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
   # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

print("Hi!")

a = [100, 100, 99, 100, 88, 85, 95, 95, 100, 100, 100]
avg = mean(a)
print(avg)

b = [5, 5, 4, 5, 5, 4.5, 4.5]
avg2 = mean(b)
print(avg2)

def numbers(n, k):
    if n > 20:
        print(n)
    else:
        sum5 = 0
        for i in range(1, n):
            q = 0
            q = i ** k
            sum5 = sum5 + q
        print(sum5)

a = numbers(2, 2)