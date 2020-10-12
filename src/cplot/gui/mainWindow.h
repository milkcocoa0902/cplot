#ifndef CPLOT_GUI_MAINWINDOW_H_
#define CPLOT_GUI_MAINWINDOW_H_

#include <gtkmm.h>
#include <vector>
#include <array>
#include <memory>

namespace CPlot {
namespace GUI {
class MainWindow : public Gtk::Window {
public:
  MainWindow();
  MainWindow(const MainWindow&) = default;

private:   
    Gtk::DrawingArea canvas_;

};
} // namespace GUI
} // namespace DiskInfo

#endif
