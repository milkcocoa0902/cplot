import wx
from . import canvas
import os

class CPlot(wx.App):
    def OnInit(self):
        self.initFrame()
        self.createMenu()
        return True

    def initFrame(self):
        self.frm_main = wx.Frame(None)
        self.frm_main.SetTitle("CPlot")
        self.frm_main.SetSize((800, 500))

        self.sizer = wx.BoxSizer()
        self.frm_main.SetSizer(self.sizer)

        self.canvas = canvas.Canvas(self.frm_main)

        self.canvas.ReadFromCSV("aaa.csv")
        self.sizer.Add(self.canvas, 0, wx.ALIGN_CENTER_VERTICAL)


        self.frm_main.Show()

    def createMenu(self):
        
        
        fileMenu = wx.Menu()
        open = fileMenu.Append(-1, "&Open")
        save = fileMenu.Append(-1, "&Save")
        exit = fileMenu.Append(-1, "&Exit")

        self.Bind(wx.EVT_MENU, self.OnOpen, open)
        self.Bind(wx.EVT_MENU, self.OnSave, save)
        self.Bind(wx.EVT_MENU, self.OnExit, exit)

        menuBar = wx.MenuBar()
        menuBar.Append(fileMenu, "&File")
        self.frm_main.SetMenuBar(menuBar)

    def OnOpen(self, evvent):
        filter = "csv file(*.csv)|*.csv|All file(*.*)|*.*"
        path = os.path.dirname(__file__)
        dialog = wx.FileDialog(self.frm_main, u'ファイルを選択してください', path, '', filter, wx.FD_OPEN)

        if dialog.ShowModal() == wx.ID_OK:
            dir = dialog.GetDirectory()
            file = dialog.GetFilename()
        dialog.Destroy()

        print(os.path.join(dir, file))

        self.canvas.ReadFromCSV(os.path.join(dir, file))

    def OnSave(self, event):
        pass

    def OnExit(self, event):
        self.frm_main.Close()