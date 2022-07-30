a = ("Raja's")      # we can use single double or triple quote , but opening & closing wll be same.
print (a)           # triple quote also used for new line
print(type(a))      # type

greeting = "Good Evening,"  #str1
name = " Manish"            #str2    
print(type(name))           #type
print(greeting + name)      #we can also create c = (greeting + name) & print(c)
#This process of adding 2 strings is called concatination
name = "Singh"
print(name[0])              #use of [] is as indexing, as String "Singh"
#                                                                "01234" is indexing
#String Slicing
print(name[0:4])            # slicing counts till 3 index excluding 4th as shown
#                            [:4] is same as name [0:4] or [0:] is also as [1:5]
print(name[-4:-1])          # This is a negative index which is same as [1:4] 
#Skip Value
name = "Shankaranpellai"    # not clear
d = name[1::2]
print(d)        


