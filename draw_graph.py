import sys
import matplotlib
matplotlib.use('QtAgg')

from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QApplication

from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg, NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(MplCanvas, self).__init__(fig)


def plot_with_axes(axes, *data):
    axes.plot(*data)

def plot_dataframe(axes, df):
    pass

if __name__ == "__main__":

    class MainWindow(QMainWindow):

        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)

            sc = MplCanvas(self, width=5, height=4, dpi=100)
            plot_with_axes(sc.axes, [0,1,2,3,4], [10,1,20,3,40])

            # Create toolbar, passing canvas as first parament, parent (self, the MainWindow) as second.
            toolbar = NavigationToolbar(sc, self)

            layout = QVBoxLayout()
            layout.addWidget(toolbar)
            layout.addWidget(sc)

            # Create a placeholder widget to hold our toolbar and canvas.
            widget = QWidget()
            widget.setLayout(layout)
            self.setCentralWidget(widget)

            self.show()


    app = QApplication(sys.argv)
    w = MainWindow()
    app.exec()

