# -*- coding: gbk -*-
import wx
import wx.grid
from sourceDisplay import DisplayFrame


class Student:
    def __init__(self):
        self.name = ''
        self.ID = ''
        self.score1 = 0
        self.score2 = 0
        self.score3 = 0
        self.sum = 0

    def __str__(self):
        return 'ID:' + self.ID + '\n姓名：' + self.name + '\n语文成绩：' + str(self.score1) + '\n数学成绩：' + str(
            self.score2) + '\n英语成绩：' + str(self.score3) + '\n总成绩：' + str(self.sum)


class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, '学生信息管理', size=(1200, 600))

        self.panel = wx.Panel(self, size=(400, 100), style=wx.BORDER_SIMPLE)
        self.sign = False
        # 单选按钮
        wx.StaticText(self.panel, -1, '--------菜单---------', pos=(10, 10))
        panel2 = wx.Panel(self.panel, -1, pos=(10, 35), size=(100, 150))
        self.radio1 = wx.RadioButton(panel2, -1, '所有学生信息', pos=(0, 0), style=wx.RB_GROUP)
        self.radio2 = wx.RadioButton(panel2, -1, '查找学生信息', pos=(0, 20))
        self.radio3 = wx.RadioButton(panel2, -1, '删除学生信息', pos=(0, 40))
        self.radio4 = wx.RadioButton(panel2, -1, '修改学生信息', pos=(0, 60))
        self.radio5 = wx.RadioButton(panel2, -1, '增加学生信息', pos=(0, 80))
        self.radio6 = wx.RadioButton(panel2, -1, '按照分数排序', pos=(0, 100))

        # girder表格
        self.grid = wx.grid.Grid(self.panel, -1, size=(572, 397), pos=(180, 10))
        self.grid.CreateGrid(17, 6)
        colLabels = ['ID', '姓名', '语文', '数学', '英语', '总分']
        for col in range(6):
            self.grid.SetColLabelValue(col, colLabels[col])
        # self.grid.Enable(False)
        self.Bind(wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.grid_left_click, self.grid)
        self.display()

        # 输入框
        panel3 = wx.Panel(self.panel, -1, pos=(10, 200), size=(110, 120))
        wx.StaticText(panel3, -1, label='ID:', pos=(0, 0))
        self.tc_id = wx.TextCtrl(panel3, -1, pos=(40, 0), size=(70, 20))
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

        self.bt = wx.Button(self.panel, -1, label='确定', pos=(10, 340))
        self.bt.Enable(True)
        self.Bind(wx.EVT_BUTTON, self.onButtonClick, self.bt)

        for eachRadio in [self.radio1, self.radio2, self.radio3, self.radio4, self.radio5, self.radio6]:
            self.Bind(wx.EVT_RADIOBUTTON, self.OnRadio, eachRadio)

        # 菜单
        self.menuBar = wx.MenuBar()

        self.menu1 = wx.Menu()
        self.M_new = self.menu1.Append(-1, '新建(&N)')
        self.M_open = self.menu1.Append(-1, '打开(&O)')
        self.menu1.AppendSeparator()
        self.M_exit = self.menu1.Append(-1, '退出(&E)')
        self.menuBar.Append(self.menu1, '文件(&N)')

        self.menu2 = wx.Menu()
        self.M_display = self.menu2.Append(-1, '所有学生信息')
        self.M_search = self.menu2.Append(-1, '查找学生信息')
        self.M_delete = self.menu2.Append(-1, '删除学生信息')
        self.M_modify = self.menu2.Append(-1, '修改学生信息')
        self.M_add = self.menu2.Append(-1, '增加学生信息')
        self.M_sort = self.menu2.Append(-1, '按照分数排序')
        self.menuBar.Append(self.menu2, '操作(&P)')

        self.menu3 = wx.Menu()
        self.M_source = self.menu3.Append(-1, '显示源文件')
        self.menuBar.Append(self.menu3, '展示')

        self.menu4 = wx.Menu()
        self.menuBar.Append(self.menu4, '帮助(&H)')

        self.SetMenuBar(self.menuBar)

        # 菜单绑定事件
        self.Bind(wx.EVT_MENU_RANGE, self.onMenu, id=self.M_display.GetId(), id2=self.M_sort.GetId())
        self.Bind(wx.EVT_MENU, self.onExit, self.M_exit)
        self.Bind(wx.EVT_MENU, self.onDisplaySource, self.M_source)

        # 菜单绑定图标
        self.M_display.SetBitmap(wx.Bitmap(wx.Image('img/display.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_search.SetBitmap(wx.Bitmap(wx.Image('img/search.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_delete.SetBitmap(wx.Bitmap(wx.Image('img/delete.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_modify.SetBitmap(wx.Bitmap(wx.Image('img/modify.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_add.SetBitmap(wx.Bitmap(wx.Image('img/add.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_sort.SetBitmap(wx.Bitmap(wx.Image('img/sort.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_new.SetBitmap(wx.Bitmap(wx.Image('img/new.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))
        self.M_exit.SetBitmap(wx.Bitmap(wx.Image('img/exit.png', wx.BITMAP_TYPE_PNG).Rescale(15, 15)))

        # 状态栏
        self.statusBar = self.CreateStatusBar()

        # tree
        self.tree_refresh_bt = wx.Button(self.panel, -1, '刷新', pos=(900, 10), size=(40, 30))
        self.Bind(wx.EVT_BUTTON, self.treeRefresh, self.tree_refresh_bt)
        self.tree = wx.TreeCtrl(self.panel, -1, pos=(850, 50), size=(300, 400))
        self.root = self.tree.AddRoot('学生信息')
        self.AddTreeNodes(self.root, self.getData())
        self.Bind(wx.EVT_TREE_BEGIN_DRAG, self.treeBeginDrag, self.tree)
        self.Bind(wx.EVT_TREE_END_DRAG, self.treeEndDrag, self.tree)

    # 树的拖动
    def treeBeginDrag(self, event):
        print('正在拖动。。。。')

    def treeEndDrag(self, event):
        print('拖动结束')

    # 树的刷新
    def treeRefresh(self, event):
        self.tree.DeleteChildren(self.root)
        self.AddTreeNodes(self.root, self.getData())

    # 为树添加节点
    def AddTreeNodes(self, parentItem, items):
        for i in range(len(items)):
            if type(items[i]) == str:
                # print(items[i])
                self.tree.AppendItem(parentItem, text=items[i])
            else:
                newItem = self.tree.AppendItem(parentItem, text=items[i][0])
                self.AddTreeNodes(newItem, items[i][1])

    # 展示students.txt的信息弹窗
    def onDisplaySource(self, event):
        self.dialog = DisplayFrame(self.panel, -1)
        self.dialog.Show()

    # 网格内左键选择
    def grid_left_click(self, event):
        # 设置当前点击单元格被选中
        self.grid.SelectBlock(event.GetRow(), event.GetCol(), event.GetRow(), event.GetCol(), False)
        # 将光标放置在当前点击的单元格内
        self.grid.SetGridCursor(event.GetRow(), event.GetCol())
        # 设置状态栏的文字
        txt = '点击了' + str(event.GetRow()) + '行' + str(event.GetCol()) + '列，' + '值是' + str(
            self.grid.GetCellValue(event.GetRow(), event.GetCol()))
        self.SetStatusText(txt)

    # 退出
    def onExit(self, event):
        self.Close(True)

    # 操作按钮
    def onMenu(self, event):

        menu = event.GetEventObject()
        label = menu.GetLabel(event.GetId())
        print(label)
        if label == '所有学生信息':
            self.display()
        elif label == '查找学生信息':
            dlg1 = wx.TextEntryDialog(self.panel, "输入ID：", '查找信息', '')
            if dlg1.ShowModal() == wx.ID_OK:
                id = dlg1.GetValue()
            stu = self.searchByID2(id)
            # self.tc.Clear()
            # self.tc.AppendText(stu.__str__())
            i = 0
            while True:
                if self.grid.GetCellValue(i, 0) == '':
                    break
                elif self.grid.GetCellValue(i, 0) == id:
                    self.grid.SelectRow(i, False)
                i += 1
        elif label == '删除学生信息':
            dlg1 = wx.TextEntryDialog(self.panel, "输入ID：", '删除信息', '')
            if dlg1.ShowModal() == wx.ID_OK:
                id = dlg1.GetValue()
            self.delStuByID(id)
        elif label == '修改学生信息':
            self.modify()
        elif label == '增加学生信息':
            self.add_S()
        elif label == '按照分数排序':
            # self.grid.SetSortingColumn(6)
            # print(self.grid.GetSortingColumn())
            # print(self.grid.IsSortOrderAscending())
            self.sort()
            self.display()

    def onButtonClick(self, evnet):

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
                    if list[0] != stu.ID:
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

    def OnRadio(self, event):
        radioSelected = event.GetEventObject()
        label = radioSelected.GetLabel()
        print(label)
        if label == '所有学生信息':
            self.display()
        elif label == '查找学生信息':
            dlg1 = wx.TextEntryDialog(self.panel, "输入ID：", '查找信息', '')
            if dlg1.ShowModal() == wx.ID_OK:
                id = dlg1.GetValue()
            stu = self.searchByID2(id)
            # self.tc.Clear()
            # self.tc.AppendText(stu.__str__())
            i = 0
            while True:
                if self.grid.GetCellValue(i, 0) == '':
                    break
                elif self.grid.GetCellValue(i, 0) == id:
                    self.grid.SelectRow(i, False)
                i += 1
        elif label == '删除学生信息':
            dlg1 = wx.TextEntryDialog(self.panel, "输入ID：", '删除信息', '')
            if dlg1.ShowModal() == wx.ID_OK:
                id = dlg1.GetValue()
            self.delStuByID(id)
        elif label == '修改学生信息':
            self.modify()
        elif label == '增加学生信息':
            self.add_S()
        elif label == '按照分数排序':
            # self.grid.SetSortingColumn(6)
            # print(self.grid.GetSortingColumn())
            # print(self.grid.IsSortOrderAscending())
            self.sort()
            self.display()

    # 为树获取数据
    def getData(self):
        data = []
        with open('students.txt') as f:
            for line in f:
                line = line.split()
                stu = [line[1], ]
                stu_info = ['ID:' + line[0], '语文：' + line[2], '数学：' + line[3], '英语：' + line[4], '总分：' + line[5]]
                stu.append(stu_info)
                data.append(stu)
        return data

    # ---学生信息操作开始--------
    def searchByID(self, ID):
        with open('students.txt') as f:
            for line in f:
                list = line.split()
                if list[0] == ID:
                    return True
            else:
                return False

    def searchByID2(self, ID):
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

    def delStuByID(self, ID):
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
            dlg = wx.MessageDialog(self.panel, "ID不存在", '删除学生信息', wx.YES_NO | wx.ICON_QUESTION)
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
        n = 0
        while (True):
            l = list(f.readline().split())
            if l == []:
                break
            for i in range(len(l)):
                self.grid.SetCellValue(n, i, l[i])
            n += 1
        f.close()
        self.grid.SetSortingColumn(0)

    def sort_p(self, l):
        return l[-1]

    def sort(self):
        f = open('students.txt', 'r')
        line = []
        while (True):
            l = list(f.readline().split())
            if l == []:
                break
            line.append(l)
        print(line)
        c = sorted(line, key=self.sort_p)
        c = reversed(c)
        f.close()
        f = open('students.txt', 'w')
        for i in c:
            for j in i:
                f.write(j)
                f.write(' ')
            f.write('\n')
        f.close()
    # ---学生信息操作结束--------


if __name__ == '__main__':
    stulist = []
    # Init_student(stulist)
    app = wx.PySimpleApp()
    frame = MyFrame(None, wx.NewId())
    frame.Show()
    app.MainLoop()
