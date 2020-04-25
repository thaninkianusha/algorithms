'''
A sequence of integers is said to be beautiful if the bitwise AND, OR, and XOR of its elements are pairwise equal to each other.

You are given a sequence  of size . Find the number of non-empty subsequences of  that are beautiful. Print the answer modulo 10**9 + 7.

Input format

The first line contains an integer  representing the number of elements in the sequence.
The second line contains  space-separated integers  representing the sequence. 
Output format

In a single line, print the number of non-empty subsequences of  that are beautiful.
'''

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

inp = input()
li_ = input().split(" ")
dic = {}
result = 0
for i in li_:
    if i in dic:
        dic[i] = dic[i]+1
    else:
        dic[i] = 1
lop = []
maxi = 0
result = 0
for i in dic:
    if i == '0':
        result = result + 2**dic[i] -1
    else:
        result  = result + (2**(dic[i]-1))
    

print(int(result%(7+(10**9))))

