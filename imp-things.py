arr = list(map(int, input().split()))  #helps to input an array  of inputs from a single line

a, b = map(int, input().split()) #input 2 or more inputs from a single line
 
 
 #map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

#eg:

def addition(n):
    return n + n
  
# We double all numbers using map()

numbers = (1, 2, 3, 4)
result = map(addition, numbers)
print(list(result))



 arr = list(filter(lambda x: x != 0, arr)) #to remove all occurences of zero

#python method to create a alphabet list lowercase

alphabets = list(map(chr, range(97, 123)))

#python method to create a alphabet list uppercase

alphabets = list(map(chr, range(65, 91)))

# string operations /list operations
# a="hello"
# b="world"
#c="helloworld"
# print(a,b,c)
# a,b=b,a
# print(a,b,c)
# print(c[:5]) #from 0  till 4
# print(c[5:]) #from 5 till end of string
# print(c[3:8]) # starting from 3(inclusive) till 8(exclusive)
# print(c[:-5])  #first 5 words
# print(c[-5:]) # last five words

# print(c[-5]) # 5th word from last
# print(c[4]) # 4th word from first
# print(c[:]) #makes a copy of the string
# print(c[::-1]) # string reversal





# s="aabbcbbaa"

# def palindrome(s,l,r):
#     if(l>=r):
#         return True
        
#     if(s[l]!=s[r]):
#         return False
    
#     return palindrome(s,l+1,r-1)
    
# print(palindrome(s,0,(len(s)-1)))






# s="aabcda"

# def reverse(s,l):
#     if(l==len(s)):
#         return
#     reverse(s,l+1)
#     print(s[l],end=" ")

# reverse(s,0)




# s="abcd"

# def substring(s,i,c):
#     if(i==len(s)):
#         print(c,end =" ")
#         return
#     substring(s,i+1,c+s[i])
#     substring(s,i+1,c)
    
# substring(s,0,'')


#Majority element Moores algo

# s=[2,1,1,2,2]
# c=0
# majorityElement=0

# for i in s:
#     if(c==0):
#         majorityElement=i
#     if(i==majorityElement):
#         c=c+1
#     else:
#         c=c-1

# print(majorityElement)

#kadens alog max contiguous subarray

l=[-2, -3, -4, -1, -2, -1, -5, -3]
# maxel=l[0]
# for i in range(len(l)):
#     s=0
#     for j in range(i,len(l)):
#         s=s+l[j]
#         if(s>maxel):
#             maxel=s
# print(maxel)

maxSum=l[0]
currSum=0
for i in range(len(l)):
    currSum=currSum+l[i]
    if(currSum > maxSum):
        maxSum=currSum
    if(currSum < 0 ):
        currSum=0
print(maxSum)




import copy

old_list = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
new_list = copy.deepcopy(old_list) #deepcopy
new_slist=copy.copy(old_list) #Shallow copy
old_list[1][0] = 'BB'

print("Old list:", old_list)
print("New list:", new_list)
print("Shallow List",new_slist)






Generally you have an input in CodeChef like this:
1 2 3 4 5 6 7
To get them as a list of numbers simply _list = map(int, raw_input().split())
Always use the raw_input() function irrespective of the type of input and then convert it using the map function. map functions are one of the most beautiful in python. Worth knowing.

swapping :
a, b = b, a

Be fluent with slicing operations.

X[:N] - all elements below index N.
X[N:] - all elements above index N.
X[a:b] - all elements between a, b.
And remember python lists are circular
X[-k] gives k'th element from the last. Quite usefull to use in slicing also
X[-k:] - gives last k elements.
X[:-k] - gives first n-k elements where n is the lenght of the list.
There are many more: Neat Features in Python: Slicing and Sliding (Stepping) and Slicing, Dicing and Splicing

While iterating always use xrange() and never range().
This is a common mistake most beginners do. range() gives a list which is a kind of overkill. xrange() is a generator, produces elements one by one and only once. Though if you are using Python3 then it is safe to use range. Thanks to Tarun Kumar for pointing it out in the comments :) .

sort() function.

Collections module. Very often you need to remove duplicates. While in languages like java you have to use HashMap and all that shit, in python it's simply  _list = list(set(_list)).

Difference between extend() and append() in lists.
merge a=[1, 2, 3] and b=[4, 5, 6] should be
 a.extend(b)
which gives

[1, 2, 3, 4, 5, 6]

 a.append(b)
gives

[1, 2, 3, [4, 5, 6]]

String concatenations:
strings = ['I', 'am', 'the', 'laziest', 'person', 'in', 'the', 'world' ]
To concatenate the above strings we would be tempted to do:

s = '' 
for string in strings: 
    s = s+string 
print s 
It gives the right answer but it's the worst way to do it and has a huge time overhead. The correct way is to use join() function.

s = '' 
s.join(strings) 

Stop using reduce functions in python if you are. They are not well supported and will be deprecated soon. The fate of reduce() in Python 3000 from the inventor of python himself. Start using lambda extensively. See this post Python Lambda - why? - Stack Overflow.

And list goes on and on.
check out this book Writing Idiomatic Python Book
I am sure you can get a pdf somewhere.

Finally, practice !!. HackerRank is best for beginners and especially if you are a python lover, you'll find it really comfortable.