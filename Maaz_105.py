def menu():
    print()
    print("This Program is made By-")
    print()
    print("               Maaz Mohammed")
    print("               BT18GCS105")
    print("               Section 3")
    print()
    print()
    print()
    print("Welcome to IT solutions")
    print()
    print()
    print("1)  To extract I.P Address from a file")
    print("2)  To extract Email Addreess from a file")
    print("3)  To extract values in front of Call ID, To, From")
    print("4)  Contact us")
    print("5)  Exit")
    print()
    print()
    print("Please choose any one of the options")
    op=int(input())
    if op==1:
        find_IP()
    elif op==2:
        find_ID()
    elif op==3:
        find_various()
    elif op==5:
        exit(0)
    elif op==4:
        print()
        print("IT Solutions by-")
        print("Maaz Mohammed")
        print("Room no.- 3113")
        print("UG-1")
        print("NIIT University, Neemrana")
        print("Mob- 9811259816")
        print("Email ID- maaz.mohammed18@st.niituniversity.in")
    else:
        print("Wrong key pressed")
        exit(0)
def find_IP():
    import re
    pattern=re.compile(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b")
    fol=open('RegularExpression.txt','r+',encoding='utf-8',errors='ignore')
    text_to_search=fol.read()
    matches=pattern.findall(text_to_search)
    abc=open('Extract_IP.txt', 'w+',encoding='utf-8',errors='ignore')
    abc.write("\n Following I.P Address is found \n")
    for i in matches:
        abc.write(i)
        abc.write("\n")
    abc.close()
    fol.close()
    print("Task completed Successfully")
    print("1) Main Manu")
    print("Or any key to exit")
    print()
    print("Enter your choice")
    a=int(input())
    if a==1:
        menu()
    else:
        exit()
def find_ID():
    import re
    pattern2=re.compile(r'[a-zA-Z0-9._]+@[a-zA-z-.]+\.[a-zA-Z]+')
    fol=open('RegularExpression.txt','r+',encoding='utf-8',errors='ignore')
    text_to_search=fol.read()
    matches=pattern2.findall(text_to_search)
    abc=open('Extract_ID.txt', 'w+',encoding='utf-8',errors='ignore')
    abc.write("\n Following email ID is found \n")
    for i in matches:
        abc.write(i)
        abc.write("\n")
    abc.close()
    fol.close()
    print("Task completed Successfully")
    print("1) Main Manu")
    print("Or any key to exit")
    print()
    print("Enter your choice")
    a=int(input())
    if a==1:
        menu()
    else:
        exit()
def find_various():
    import re
    print("Please choose any one of the following : ")
    print('1)Extract values in front of Call ID only')
    print('2)Extract values in front of From only')
    print('3)Extract values in front of To only')
    print('4)Ectract values in front of Call ID,From,to')
    print()
    print("Please choose any one of the options")
    num=int(input())
    if num==1:
        pattern3=re.compile(r'Call-ID: \S*')
        fol=open('RegularExpression.txt','r+',encoding='utf-8',errors='ignore')
        text_to_search=fol.read()
        matches1=pattern3.findall(text_to_search)
        abc=open('Extract_CallID.txt', 'w+',encoding='utf-8',errors='ignore')
        abc.write("\n Following Call-ID is found \n")
        for i in matches1:
            abc.write(i)
            abc.write("\n")
        abc.close()
        fol.close()
        print("Task completed Successfully")
        print("1) Main Manu")
        print("Or any key to exit")
        print()
        print("Enter your choice")
        a=int(input())
        if a==1:
            menu()
        else:
            exit()
    elif num==2:
        pattern4=re.compile(r'From: \S*')
        fol=open('RegularExpression.txt','r+',encoding='utf-8',errors='ignore')
        text_to_search=fol.read()
        matches2=pattern4.findall(text_to_search)
        abc=open('Extract_From.txt', 'w+',encoding='utf-8',errors='ignore')
        abc.write("\n Following From statement is found \n")
        for i in matches2:
            abc.write(i)
            abc.write("\n")
        abc.close()
        fol.close()
        print("Task completed Successfully")
        print("1) Main Manu")
        print("Or any key to exit")
        print()
        print("Enter your choice")
        a=int(input())
        if a==1:
            menu()
        else:
            exit()
    elif num==3:
        pattern5=re.compile(r'To: \S*')
        fol=open('RegularExpression.txt','r+',encoding='utf-8',errors='ignore')
        text_to_search=fol.read()
        matches3=pattern5.findall(text_to_search)
        abc=open('Extract_To.txt', 'w+',encoding='utf-8',errors='ignore')
        abc.write("\n Following To Statement is found \n")
        for i in matches3:
            abc.write(i)
            abc.write("/n")
        abc.close()
        fol.close()
        print("Task completed Successfully")
        print("1) Main Manu")
        print("Or any key to exit")
        print()
        print("Enter your choice")
        a=int(input())
        if a==1:
            menu()
        else:
            exit()
    elif num==4:
        pattern3=re.compile(r'Call-ID: \S* From: \S* To: \S*')
        pattern4=re.compile(r'From: \S*')
        pattern5=re.compile(r'To: \S*')
        fol=open('RegularExpression.txt','r+',encoding='utf-8',errors='ignore')
        text_to_search=fol.read()
        matches1=pattern3.findall(text_to_search)
        matches2=pattern4.findall(text_to_search)
        matches3=pattern5.findall(text_to_search)
        abc=open('Extract_CallID_From_To.txt','w+',encoding='utf-8',errors='ignore')
        abc.write("\n Following Data is found ")
        abc.write("\n")
        abc.write("\n")
        abc.write("\n Following Call-ID is found \n")
        for i in matches1:
            abc.write(i)
            abc.write("\n")
        abc.write("\n")
        abc.write("\n Following From statement is found \n")
        for i in matches2:
            abc.write(i)
            abc.write("\n")
        abc.write("\n")
        abc.write("\n Following To Statement is found \n")
        for i in matches3:
            abc.write(i)
            abc.write("/n")
        print("Task completed Successfully")
        print("1) Main Manu")
        print("Or any key to exit")
        print()
        print("Enter your choice")
        a=int(input())
        if a==1:
            menu()
        else:
            exit()
print()
print("This Program is made By-")
print()
print("               Maaz Mohammed")
print("               BT18GCS105")
print("               Section 3")
print()
print()
print()
print("Welcome to IT solutions")
print()
print()
print("1)  To extract I.P Address from a file")
print("2)  To extract Email Addreess from a file")
print("3)  To extract values in front of Call ID, To, From")
print("4)  Contact US")
print("5)  Exit")
print()
print()
print("Please choose any one of the options")
op=int(input())
if op==1:
    find_IP()
elif op==2:
    find_ID()
elif op==3:
    find_various()
elif op==5:
    exit(0)
elif op==4:
    print()
    print("IT Solutions by-")
    print("Maaz Mohammed")
    print("Room no.- 3113")
    print("UG-1")
    print("NIIT University, Neemrana")
    print("Mob- 9811259816")
    print("Email ID- maaz.mohammed18@st.niituniversity.in")
else:
    print("Wrong key pressed")
    exit(0)
        
        
        
        
        
        
    
              
