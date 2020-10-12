#import wx
import matplotlib

matplotlib.interactive(True)
matplotlib.use('WXAgg')

import wx
class Canvas(wx.Panel):
    def __init__(self, parent):
        self.parent = parent
        self.ax = None
        wx.Panel.__init__(self, parent)


    def ReadFromCSV(self, _csv, _delim = ",", _hasHeader = True):
        from ..util import dataManager
        manager = dataManager.DataManager()
        manager.Read(_csv, _delim, _header = 0 if _hasHeader is True else None)


    
        from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg
        from matplotlib.figure import Figure

    
        self.figure = Figure(None)
        self.figure.set_facecolor((0.7, 0.7, 1.0))
        #self.subplot = self.figure.add_subplot(111)

        self.canvas = FigureCanvasWxAgg(self, -1, self.figure)
        self.canvas.SetBackgroundColour(wx.Colour(100, 255, 255))
        self._SetSize()


        self._draw(manager.df())

    def _SetSize(self):
        size = tuple( self.parent.GetClientSize() )
        self.SetSize( size )
        self.canvas.SetSize( size )
        self.figure.set_size_inches( float( size[0] )/self.figure.get_dpi(),
                                     float( size[1] )/self.figure.get_dpi() )

    def onclick(self, event):
        print ('event.button=%d,  event.x=%d, event.y=%d, event.xdata=%f, event.ydata=%f' %(event.button, event.x, event.y, event.xdata, event.ydata))

    def _draw(self, _df):
        from mpl_toolkits.mplot3d import Axes3D
        import matplotlib.pyplot as plt
        import numpy as np

        if self.ax is not None:
            self.ax.remove()
        self.ax = self.figure.add_subplot(111)
        for column_name, item in _df.iteritems():
            self.ax.plot(_df.index.values, item.values)    


        

        cid = self.figure.canvas.mpl_connect('button_press_event', self.onclick)


