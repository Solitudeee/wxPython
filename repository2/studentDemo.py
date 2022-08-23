# -*- coding: gbk -*-
import wx
import wx.grid
class Student:
    def __init__(self):
        self.name=''
        self.ID=''
        self.score1=0
        self.score2=0
        self.score3=0
        self.sum=0
    def __str__(self):
        return 'ID:'+self.ID+'\n姓名：'+self.name+'\n语文成绩：'+str(self.score1)+'\n数学成绩：'+str(self.score2)+'\n英语成绩：'+str(self.score3)+'\n总成绩：'+str(self.sum)
def Init_student(i):
    with open('students.txt') as f:
        for line in f:
            stu=Student()
            print(line)
            line=line.split()
            stu.ID=line[0]
            stu.name=line[1]
            stu.score1=line[2]
            stu.score2=line[3]
            stu.score3=line[4]
            stu.sum=line[5]
            stulist.append(stu)
        print('初始化成功！')



class MyFrame(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'文本',size=(900,600))
        self.panel=wx.Panel(self,size=(400,100),style=wx.BORDER_SIMPLE)
        self.sign=False
        #单选按钮
        wx.StaticText(self.panel, -1, '--------菜单---------', pos=(10,10))
        panel2=wx.Panel(self.panel,-1,pos=(10,35),size=(100,150))
        self.radio1 = wx.RadioButton(panel2, -1, '所有学生信息', pos=(0, 0), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel2, -1, '查找学生信息', pos=(0, 20))
        self.radio3 = wx.RadioButton(panel2, -1, '删除学生信息', pos=(0, 40))
        self.radio4 = wx.RadioButton(panel2, -1, '修改学生信息', pos=(0, 60))
        self.radio5 = wx.RadioButton(panel2, -1, '增加学生信息', pos=(0, 80))
        self.radio6 = wx.RadioButton(panel2, -1, '按照分数排序', pos=(0, 100))

        #文本框
        # self.tc=wx.TextCtrl(self.panel,-1,'',pos=(130,10),size=(300,400),style=wx.TE_MULTILINE)
        # self.tc.Enable(False)
        # self.display()


        # girder表格
        self.grid=wx.grid.Grid(self.panel,-1,size=(572,397),pos=(180,10))
        self.grid.CreateGrid(17,6)
        colLabels=['ID','姓名','语文','数学','英语','总分']
        for col in range(6):
            self.grid.SetColLabelValue(col,colLabels[col])
        # self.grid.Enable(False)
        self.display()


        #输入框
        panel3=wx.Panel(self.panel,-1,pos=(10,200),size=(110,120))
        wx.StaticText(panel3,-1,label='ID:',pos=(0,0))
        self.tc_id=wx.TextCtrl(panel3,-1,pos=(40,0),size=(70,20))
        self.tc_id.Enable(False)

        wx.StaticText(panel3, -1, label='姓名：', pos=(0, 25))
        self.tc_name = wx.TextCtrl(panel3, -1, pos=(40, 25), size=(70, 20))
        self.tc_name.Enable(False)

        wx.StaticText(panel3, -1, label='语文：', pos=(0, 50))
        self.tc_yw = wx.TextCtrl(panel3, -1, pos=(40, 50), size=(70, 20))
        self.tc_yw.Enable(False)

        wx.StaticText(panel3, -1, label='数学：', pos=(0, 75))
        self.tc_sx = wx.TextCtrl(panel3, -1, pos=(40, 75), size=(70, 20))
        self.tc_sx.Enable(False)

        wx.StaticText(panel3, -1, label='英语：', pos=(0, 100))
        self.tc_yy = wx.TextCtrl(panel3, -1, pos=(40, 100), size=(70, 20))
        self.tc_yy.Enable(False)

        self.bt=wx.Button(self.panel,-1,label='确定',pos=(10,340))
        self.bt.Enable(True)
        self.Bind(wx.EVT_BUTTON,self.onButtonClick,self.bt)


        for eachRadio in [self.radio1, self.radio2, self.radio3,self.radio4,self.radio5,self.radio6]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)

    def searchByID(self,ID):
        with open('students.txt') as f:
            for line in f:
                list = line.split()
                if list[0] == ID:
                    return True
            else:
                return False
    def searchByID2(self,ID):
        if (self.searchByID(ID)):
            with open('students.txt') as f:
                for line in f:
                    list = line.split()
                    if list[0] == ID:
                        stu = Student()
                        stu.ID = list[0]
                        stu.name = list[1]
                        stu.score1 = list[2]
                        stu.score2 = list[3]
                        stu.score3 = list[4]
                        stu.sum = list[5]
                        return stu
        else:
            print("ID不存在")

    def add_S(self):
        self.tc_id.Enable(True)
        self.tc_name.Enable(True)
        self.tc_yw.Enable(True)
        self.tc_sx.Enable(True)
        self.tc_yy.Enable(True)

    def delStuByID(self,ID):
        if (self.searchByID(ID)):
            f = open('students.txt', 'r')
            l = f.readlines()
            f.close()
            f = open('students.txt', 'w+')
            for line in l:
                list = line.split()
                if list[0] != ID:
                    f.write(line)
            f.close()
            self.display()
        else:
            dlg=wx.MessageDialog(self.panel, "ID不存在", '删除学生信息',wx.YES_NO|wx.ICON_QUESTION)
            dlg.ShowModal()
            dlg.Destroy()

    def modify(self):
        self.tc_id.Enable(True)
        self.tc_name.Enable(True)
        self.tc_yw.Enable(True)
        self.tc_sx.Enable(True)
        self.tc_yy.Enable(True)

    def display(self):
        self.grid.ClearGrid()
        f = open('students.txt', 'r')
        n=0
        while (True):
            l = list(f.readline().split())
            if l == []:
                break
            for i in range(len(l)):
                self.grid.SetCellValue(n,i,l[i])
            n+=1
        f.close()
        self.grid.SetSortingColumn(0)
    def sort_p(self,l):
        return l[-1]

    def sort(self):
        f = open('students.txt', 'r')
        line = []
        while (True):
            l = list(f.readline().split())
            if l == []:
                break
            line.append(l)
        c = sorted(line, key=self.sort_p)
        c=reversed(c)
        f.close()
        f = open('students.txt', 'w')
        for i in c:
            for j in i:
                f.write(j)
                f.write(' ')
            f.write('\n')
            # f.write(i[0],' ',i[1],' ',i[2],' ',i[3],' ',i[4],' ',i[5],'\n')
        f.close()

    def onButtonClick(self,evnet):

        if self.radio5.GetValue():
            stu = Student()
            stu.ID = self.tc_id.GetValue()
            if self.searchByID(stu.ID):
                dlg = wx.MessageDialog(self.panel, "ID已存在", '添加学生信息', wx.YES_NO | wx.ICON_QUESTION)
                dlg.ShowModal()
                dlg.Destroy()
            else:
                stu.name = self.tc_name.GetValue()
                stu.score1 = self.tc_yw.GetValue()
                stu.score2 = self.tc_sx.GetValue()
                stu.score3 = self.tc_yy.GetValue()
                stu.sum = int(stu.score1) + int(stu.score2) + int(stu.score3)
                f = open('students.txt', 'a')
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
                self.display()
        if self.radio4.GetValue():
            stu = Student()
            stu.ID = self.tc_id.GetValue()
            stu.name = self.tc_name.GetValue()
            stu.score1 = self.tc_yw.GetValue()
            stu.score2 = self.tc_sx.GetValue()
            stu.score3 = self.tc_yy.GetValue()
            stu.sum = int(stu.score1) + int(stu.score2) + int(stu.score3)
            if (self.searchByID(stu.ID)):
                f = open('students.txt', 'r')
                l = f.readlines()
                f.close()
                t = open('students.txt', 'w+')
                for line in l:
                    list = line.split()
                    if list[0]!= stu.ID:
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
                self.display()
            else:
                dlg = wx.MessageDialog(self.panel, "ID不存在", '修改学生信息', wx.YES_NO | wx.ICON_QUESTION)
                dlg.ShowModal()
                dlg.Destroy()

    def OnRadio(self,event):
        radioSelected = event.GetEventObject()
        label=radioSelected.GetLabel()
        print(label)
        if label=='所有学生信息':
            self.display()
        elif label=='查找学生信息':
            dlg1 = wx.TextEntryDialog(self.panel, "输入ID：", '查找信息', '')
            if dlg1.ShowModal() == wx.ID_OK:
                id = dlg1.GetValue()
            stu = self.searchByID2(id)
            # self.tc.Clear()
            # self.tc.AppendText(stu.__str__())
            i=0
            while True:
                if self.grid.GetCellValue(i,0)=='':
                    break
                elif self.grid.GetCellValue(i,0)==id:
                    self.grid.SelectRow(i,False)
                i+=1
        elif label=='删除学生信息':
            dlg1 = wx.TextEntryDialog(self.panel, "输入ID：", '删除信息', '')
            if dlg1.ShowModal() == wx.ID_OK:
                id = dlg1.GetValue()
            self.delStuByID(id)
        elif label=='修改学生信息':
            self.modify()
        elif label=='增加学生信息':
            self.add_S()
        elif label=='按照分数排序':
            # self.grid.SetSortingColumn(6)
            # print(self.grid.GetSortingColumn())
            # print(self.grid.IsSortOrderAscending())
            self.sort()
            self.display()






if __name__=='__main__':
    stulist = []
    # Init_student(stulist)
    app=wx.PySimpleApp()
    frame=MyFrame(None,wx.NewId())
    frame.Show()
    app.MainLoop()

