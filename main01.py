#Print the list of integers from 1 through n as a string, 
#without spaces

#if __name__ == '__main__':
# n = int(input("Type an integer:"))
# print(*range(1,n+1), sep="")

# Print the three most common characters along with their occurrence count each on a separate line. 
# Sort output in descending order of occurrence count. 
# If the occurrence count is the same, sort the characters in alphabetical order.

# 1. sort the letters in a string alphabetically in Python
s = input("Type a string: ").lower()
#sorted_s = ''.join(sorted(s, key=str.lower))
# sorting secondary key first.
counted_s = sorted([(x, s.count(x)) for x in set(s)], key =lambda alpha:alpha[0])
print(counted_s)

sorted_s = sorted(counted_s, key = lambda alpha:alpha[1] , reverse=True)
print(sorted_s)

for x in sorted_s[0:3]:
    print(f"{x[0]} {x[1]}")

# counted_s = {}
# counted_s = dict((x,s.count(x)) for x in s)


#In order to write the sorted string without changing the case of letter. Use the code:
# >>> a = "Hello World!"
# >>> "".join(sorted(a,key=lambda x:x.lower()))
#' !deHllloorW'

#OR (Ref: https://docs.python.org/3/library/functions.html#sorted)

# >>> a = "Hello World!"
# >>> "".join(sorted(a,key=str.lower))
# ' !deHllloorW'

#If you want to remove all punctuation and numbers. Use the code:
#>>> a = "Hello World!"
#>>> "".join(filter(lambda x:x.isalpha(), sorted(a,key=lambda x:x.lower())))
# 'deHllloorW'