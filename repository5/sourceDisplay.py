import wx

class DisplayFrame(wx.Dialog):
    def __init__(self,parent,id):
        wx.Dialog.__init__(self,parent,id,size=(400,400))
        panel=wx.Panel(self,-1)
        self.tx=wx.TextCtrl(panel,-1,size=(400,400),style=wx.TE_MULTILINE)
        with open('students.txt') as f:
            # for line in f:
            #     self.tx.AppendText(line)
            #     self.tx.AppendText('\n')
            # else:
            #     return None
            self.tx.AppendText(f.read())