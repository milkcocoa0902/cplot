from cplot.gui import canvas
import wx

if __name__ == "__main__":
    app = wx.App()
    frame = wx.Frame(None, -1, 'CPlot', size = (1200, 800))
    panel = canvas.Canvas(frame)
    panel.ReadFromCSV("aaa.csv")
    frame.Show()
    app.MainLoop()