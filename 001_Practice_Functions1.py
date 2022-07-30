latter = '''Dear <|Name|>, you are selected!
Have a great day.
Date: <|Date|>
NS1
'''
name = input("Enter your name\n")
date = input("Enter date\n")
latter = latter.replace("<|Name|>", name)
latter = latter.replace("<|Date|>", date)
print(latter)
#character replaced




