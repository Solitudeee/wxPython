class Student:
    def __init__(self):
        self.name=''
        self.ID=''
        self.score1=0
        self.score2=0
        self.score3=0
        self.sum=0
    def __str__(self):
        return 'ID:'+self.ID+'姓名：'+self.name+'语文成绩：'+str(self.score1)+'数学成绩：'+str(self.score2)+'英语成绩：'+str(self.score3)+'总成绩：'+str(self.sum)
def Init_student(i):
    with open('students.txt') as f:
        for line in f:
            stu=Student()
            print(line)
            line=line.split(' ')
            print(line)
            stu.ID=line[0]
            stu.name=line[1]
            stu.score1=line[2]
            stu.score2=line[3]
            stu.score3=line[4]
            stu.sum=line[5]
            stulist.append(stu)
        print('初始化成功！')

def searchByID(ID):
    # for item in stulist:
    #     print(item.ID)
    #     if item.ID==ID:
    #         return True
    with open('students.txt') as f:
        for line in f:
            list=line.split()
            if list[0]==ID:
                return True
        else:
            return False

def searchByID2(ID):
    if(searchByID(ID)):
        with open('students.txt') as f:
            for line in f:
                list = line.split()
                if list[0] == ID:
                    stu=Student()
                    stu.ID=list[0]
                    stu.name=list[1]
                    stu.score1=list[2]
                    stu.score2=list[3]
                    stu.score3=list[4]
                    stu.sum=list[5]
                    return stu
    else:
        print("ID不存在")

def add_S():
    stu=Student()
    while True:
        stu.ID = input("输入ID：")
        if searchByID(stu.ID):
            print("ID已存在：")
        else:
            break

    stu.name=input("输入姓名：")
    stu.score1=int(input("输入语文成绩："))
    stu.score2=int(input("输入数学成绩："))
    stu.score3=int(input("输入英语成绩："))
    stu.sum=stu.score1+stu.score2+stu.score3
    f=open('students.txt','a')
    f.write(stu.ID)
    f.write(" ")
    f.write(stu.name)
    f.write(" ")
    f.write(str(stu.score1))
    f.write(" ")
    f.write(str(stu.score2))
    f.write(" ")
    f.write(str(stu.score3))
    f.write(" ")
    f.write(str(stu.sum))
    f.write('\n')
    f.close()
    print('保存成功')


def delStuByID(ID):
    if(searchByID(ID)):
       f=open('students.txt','r')
       l=f.readlines()
       f.close()
       f=open('students.txt','w+')
       for line in l:
        list = line.split()
        if list[0] != ID:
            f.write(line)
       f.close()
       print('删除成功！')
    else:
        print("ID不存在")

def modify(ID,stu):
    if(searchByID(ID)):
        f = open('students.txt', 'r')
        l = f.readlines()
        f.close()
        t = open('students.txt', 'w+')
        for line in l:
             list = line.split()
             if list[0] != ID:
                t.write(line)
             else:
                t.write(stu.ID)
                t.write(" ")
                t.write(stu.name)
                t.write(" ")
                t.write(str(stu.score1))
                t.write(" ")
                t.write(str(stu.score2))
                t.write(" ")
                t.write(str(stu.score3))
                t.write(" ")
                t.write(str(stu.sum))
                t.write('\n')
        t.close()
        print('修改成功')
    else:
        print("ID不存在")

def display():
    f=open('students.txt','r')
    print('ID    姓名  语文  数学  英语')
    while(True):
        l=list(f.readline().split())
        if l==[]:
            break
        for i in range(len(l)-1) :
            print(l[i],end='    ')
        print('\n')
    f.close()

def sort_p(l):
    return l[-1]

def sort():
    f = open('students.txt', 'r')
    line=[]
    while (True):
        l = list(f.readline().split())
        if l == []:
            break
        line.append(l)
    c=sorted(line,key=sort_p)
    f.close()
    f = open('students.txt', 'w')
    for i in c:
        for j in i:
            f.write(j)
            f.write(' ')
        f.write('\n')
        # f.write(i[0],' ',i[1],' ',i[2],' ',i[3],' ',i[4],' ',i[5],'\n')
    f.close()

def main():
    while True:
        print("*********************")
        print(u"--------菜单---------")
        print(u"增加学生信息--------1")
        print(u"查找学生信息--------2")
        print(u"删除学生信息--------3")
        print(u"修改学生信息--------4")
        print(u"所有学生信息--------5")
        print(u"按照分数排序--------6")
        print(u"退出程序------------0")
        print("*********************")

        nChoose=input('输入选择：')
        if nChoose=="1":
            add_S()
        elif nChoose=='2':
            id=input("请输入ID：")
            stu=searchByID2(id)
            print(stu)
        elif nChoose=='3':
            id=input("输入要删除的ID：")
            delStuByID(id)
        elif nChoose=='4':
            stu=Student()
            stu.ID=input("输入要修改的ID：")
            stu.name=input('输入姓名:')
            stu.score1 = int(input("输入语文成绩："))
            stu.score2 = int(input("输入数学成绩："))
            stu.score3 = int(input("输入英语成绩："))
            stu.sum = stu.score1 + stu.score2 + stu.score3
            modify(stu.ID,stu)
        elif nChoose=='5':
            display()
        elif nChoose=='6':
            sort()
        elif nChoose=='0':
            break


if __name__=='__main__':
    stulist=[]
    Init_student(stulist)
    main()