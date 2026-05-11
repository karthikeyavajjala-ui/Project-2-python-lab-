text=input("Enter a string:")
print("\n------------String Conversions---------")
print("Lowercase:",text.lower())
print("Uppercase:",text.upper())
print("Titlecase:",text.title())
print("Swapcase:",text.swapcase())
print("Captalize:",text.capitalize())
print("Casefold:",text.casefold())
#center
print("\n------Center-------")
print("centered(width 30):",text.center(30,'*'))
#count
print("\n------Count-------")
ch=input("Enter character to count:")
print(f"count of'{ch}':",text.count(ch))
#find
print("\n-----Find------")
sub=input("Enter Substring to find:")
pos=text.find(sub)
if pos!=-1:
    print(f"'{sub}'Found at the position:",pos)
else:
    print(f"'{sub}' not found")