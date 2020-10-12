#include "mainWindow.h"
#include <iostream>

namespace CPlot {
namespace GUI {
MainWindow::MainWindow() {
  set_border_width(10);
  set_default_size(800, 500);
  set_title("CPlot");

  show_all_children();
}
} // namespace GUI
} // namespace DiskInfo
