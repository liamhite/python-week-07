def addList(inviteList):
  name = input("Enter name: ")
  if name not in inviteList:
   inviteList.append(name)
  else:
     print("Name already in list.")

def removeList(inviteList):
  name = input("Enter name: ")
  if name  in inviteList:
    inviteList.remove(name)
  else:
      print("Name is not in list.")

### MAIN CODE ###

inviteList = []

while True:
    try:
        print("*INVITE LIST MENU*")
        print(  "1  Add to list")
        print(  "2  Remove from list")
        print(  "3  Clear list")
        print(  "4  Print list")
        print(  "5  Exit")
        value = int(input())

        if value == 1:
           addList(inviteList)

        elif value == 2:
           removeList(inviteList)

        elif value == 3:
           inviteList.clear()

        elif value == 4:
           print(inviteList)

        elif value == 5:
           break

        else:
            print("Please enter a number from the menu.")

        print()
    except ValueError:
       print("Please enter a number from the menu.")
       print()





