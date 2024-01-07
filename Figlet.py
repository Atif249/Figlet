'''import pyfiglet'''
'''import os'''

os.system("clear")

a=("""
    _      _____   ___   _____
   / \    |_   _| |_ _| |  ___|
  / _ \     | |    | |  | |_
 / ___ \    | |    | |  |  _|
/_/   \_\   |_|   |___| |_|
""")
print(a)
print("---------------------------")
print()
def start():
     Name = input ("ENTER YOUR NAME : ")
     print()
     print("banner")
     print("doom")
     print("digital")
     print("diamond")
     print("epic")
     print()
     
     font_style=input("SELLECT FONT TO APPLY : ")
     print("---------------------------")
     a=pyfiglet.figlet_format(Name,font_style)
     print(a)
     print("---------------------------")
     print()
     
     res = input("RESTART Y or EXIT X :")
     print()
     
     if res=='y':
          start()
     else:
      print("THANKS FOR USE MY PROGRAM")
      print()
      
     
start()
