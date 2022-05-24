print("Do you have a problem?")
accept=input("Give response in only Yes or No")
if accept=='Yes' or accept=='YES' or accept=='yes' :
    print("Then why worry?")
elif accept=='No' or accept=='no' or accept=='NO' :
    print("Can you do something about it")
    accept1=input("Give response in only Yes or No")
    if accept1=='Yes' or accept1=='YES' or accept1=='yes' :
        print("Then why worry?")
    elif accept1=='No' or accept1=='no' or accept1=='NO' :
        print("Then why worry?")
    else:
        print('You have responded wrong')
else:
    print('You have responded wrong')