import requests as re 
from bs4 import BeautifulSoup

s=re.Session()
print("\n\n\n")
print("Holaaa... Welcome !\n")

try:
    id_num=input("Enter the ID: ")
    url="http://intranet.rguktn.ac.in/SMS/logic/login.php"
    header={"X-Requested-With": "XMLHttpRequest"}
    data={"user1": id_num,
    "passwd1": input("Enter the password: "),
    "uri":""}
    s=re.Session()
    output=s.post(url=url,headers=header,data=data)
    marks_url="http://intranet.rguktn.ac.in/SMS/results/mt.php"
    mid_marks=s.get(marks_url)
    soup=BeautifulSoup(mid_marks.content,"html.parser")
    total_marks=[]
    

    result=soup.find_all("td")
    for values in result:
        total_marks.append(values.text.strip())
    
        

    for i in total_marks:
        if i=='AB':
            total_marks[total_marks.index(i)]="0"
    #print(total_marks)
    name_url="http://intranet.rguktn.ac.in/SMS/dashboard.php"
    result_=s.get(name_url)
    soup2=BeautifulSoup(result_.content,"html.parser")
    details=[]
    name=soup2.find("h3",class_="widget-user-username")
    details.append(name.text)
    year=soup2.find("h5",class_="widget-user-desc")
    details.append(year.text)
    
    #slicing elements based on the 1st subject
    index_values=[]
    sub=total_marks[0]
    for i in range(len(total_marks)):
        if total_marks[i]==sub:
            index_values.append(i)
    #print(index_values)
    mid_1=total_marks[index_values[0]:index_values[1]]
    mid_2=total_marks[index_values[1]:index_values[2]]
    mid_3=total_marks[index_values[2]: ]
    """print(mid_1)
    print(mid_2)
    print(mid_3)"""
    sub=[]
    for j in range(len(mid_1)):
        if(j%3==1):
            sub.append(mid_1[j])
    marks=[]
    mid_1_marks=[]
    mid_2_marks=[]
    mid_3_marks=[]

    for mark in range(2,len(mid_1),3):
        mid_1_marks.append(mid_1[mark])
        mid_2_marks.append(mid_2[mark])
        mid_3_marks.append(mid_3[mark])

    def marks_int(a):
        marks=[]
        for i in a:
            i=int(i)
            marks.append(i)
        return (marks)
    m1=marks_int(mid_1_marks)
    m2=marks_int(mid_2_marks)
    m3=marks_int(mid_3_marks)
    final_marks=[]
    final_marks.append(m1)
    final_marks.append(m2)
    final_marks.append(m3)
    #print(final_marks)
    #printed thelist in a sequence
    temp=[]
    c=0
    while c<5:
        for i in range(len(final_marks)):
            #print(i,"-i")
            #print(c,"-j")
            temp.append(final_marks[i][c])           
        c=c+1
    #print(temp)
    #subject_wise mid marks
    subject_wise=[]
    for i in range(0,len(temp),3):
        subject_wise.append(temp[i:i+3])
    #print(subject_wise)
    best_sub_marks=[]
    #to get the best values
    for best in subject_wise:
        best.sort(reverse=True)
        best.remove(best[-1])
        best_sub_marks.append(sum(best))
    #print(sub)
    #adding the best values
    #print(best_sub_marks)
    #making a dictionary
    final_values=dict(zip(sub,best_sub_marks))
    #print(final_values)
    #DECORATION :)
    print("\n\n")
    print("\t\t\t\tWELCOME",details[0],"(",id_num,")..!")
    print("\t\t\t\t\t",details[1],"IIIT")
    #print("I am so happy that you are here......")
    print("\n\n\n\t\t\tTotal Mid marks of Each subject you have in the SEMESTER..")
    print("\n\n\tSubject\t\t\t\t\t-\t\t\t Average Mid Marks\n")
    for lo in final_values:
        if lo=="Design and Analysis of Algorithm":
            print(lo.rstrip(),"\t\t-\t\t\t",final_values[lo],"\n")
        elif lo=="Operating System":
            print(lo.rstrip(),"\t\t\t\t-\t\t\t",final_values[lo],"\n")
        else:
            print(lo.rstrip(),"\t\t\t-\t\t\t",final_values[lo],"\n")
except Exception:
    print("\n\nCouldn't fetch results . The reasons are listed below:")
    print("\n1.Check your Internet Connection....\n2.Couldn't connect this website at this moment\n3.Please check your Username and password are correct\n4.Your college administration haven't posted the results")
    print("\n\nPlease Try Again in a moment _/\_ \n\n")

 
