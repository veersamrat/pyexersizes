# import pandas

# dtWords=pandas.read_csv('D:\\SystemFiles(DontDelete)\\Downloads\\4000-most-common-english-words-csv.csv')

# print(dtWords);

# pie = "Apple Pie"
# print(pie.split(' '))

'''
x = 11
# x is the variable to match
match x:
    
    # if x is 0
    case 0:
        print("x is zero")
    # case with if-condition
    case 4 if x % 2 == 0:
        print("x % 2 == 0 and case is 4")
    # Empty case with if-condition
    case _ if x < 10:
        print("x is < 10")
    # default case(will only be matched if the above cases were not matched)
    # so it is basically just an else:
    case _:
        print(x)
        '''
# viresh={'sdfsdf':56,56:'dfsdf'}
# print(viresh[56])

# add=lambda x,y:x+y

# print(add(5,6))

a=(1,2,3)
b=(1,2,3)

print(a is b)
print(a==b)