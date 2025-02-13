
print("please answer by (y) for yes and (n) for no or (e) for exit ")
while True:
    try:
        user_input=input("Do you want to add a new To-Do item?\n")
        if user_input=="y":
            file=open("To_Do","+a", encoding="utf-8")
            contant=input("type in his new To-Do item \n")
            file.write(contant+"\n")
            file.close()  
        elif user_input=="n":
            Ask_user=input("Do you want to list your To-Do items?\n")
            if Ask_user=="y":
                file1=open("To_do","r",encoding="utf-8")
                contant1=file1.read()
                print(contant1)
                file1.close()
            elif Ask_user=="n":
                pass  
            else:
                print("please answer by (y) for yes and (n) for no")
        elif user_input=="e":
            break
        else:
            print("please answer by (y) for yes and (n) for no")
              

    except Exception as e:
        print(e)