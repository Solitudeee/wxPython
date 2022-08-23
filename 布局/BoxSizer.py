import wx
class BoxSizerFrame(wx.Frame):
    def __init__(self,parent,title):
        wx.Frame.__init__(self,parent,title=title,size=(600,200))
        panel=wx.Panel(self)
        hbox=wx.BoxSizer(wx.HORIZONTAL)
        vbox=wx.BoxSizer(wx.VERTICAL)
        st1=wx.StaticText(panel,-1,'电影名称：',style=wx.CENTER)
        st2=wx.StaticText(panel,-1,'选择片源：')
        tc=wx.TextCtrl(panel,-1,size=(200,20))
        list=['电影天堂','卧龙影视','七彩云','蒙面大侠','爱奇艺','优酷','腾讯']
        c=wx.Choice(panel,-1,choices=list)
        button=wx.Button(panel,-1,'查询')
        # hbox.Add(st1,0,wx.EXPAND)
        # hbox.Add(tc,0,wx.EXPAND)
        # hbox.Add(st2,0,wx.EXPAND)
        # hbox.Add(c,0,wx.EXPAND)
        a=((st1,0,wx.EXPAND|wx.ALL,5),(tc,0,wx.EXPAND|wx.ALL,5),(st2,0,wx.EXPAND|wx.ALL,5),(c,0,wx.EXPAND|wx.ALL,5),(button,0,wx.EXPAND|wx.ALL,5))
        hbox.AddMany(a)

        vbox.Add(hbox,0,wx.EXPAND)

        st3=wx.StaticText(panel,-1,'查询结果：')

        vbox.Add(st3,0,wx.EXPAND|wx.ALL,5)

        tc=wx.TextCtrl(panel,-1,size=(200,200),style=wx.TE_MULTILINE)
        vbox.Add(tc,0,wx.EXPAND|wx.ALL,5)

        panel.SetSizer(vbox)
        # panel.Fit()
        vbox.Fit(panel)

if __name__ == '__main__':
    app=wx.PySimpleApp()
    bsf=BoxSizerFrame(None,'BoxSizer布局')
    bsf.Show()
    app.MainLoop()