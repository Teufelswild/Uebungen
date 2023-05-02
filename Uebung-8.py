from PyQt5.QtWidgets import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import matplotlib.pyplot as plt
import numpy as np




class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.layout=QVBoxLayout()

        self.figure=plt.figure(figsize=(16,9))
        self.canvas=FigureCanvas(self.figure)

        self.beschreibung=QLabel("Koeffizeinten der Polynomfunktion kommagetrennt eingeben")
        self.polynom=QLineEdit()
        self.label_wertebereich_von=QLabel("Untere Grenze Wertebereich")
        self.Wertebereich_von=QLineEdit()
        self.label_wertebereich_bis=QLabel("Obere Grenze Wertebereich")
        self.Wertebereich_bis=QLineEdit()
        self.label_AnzPunkte=QLabel("Gewünschte Anzahl Punkte")
        self.AnzPunkte=QLineEdit()
        self.QComboBox_farbe=QComboBox()
        self.QComboBox_farbe.addItems(["red","blue","green"])
        self.plot_button=QPushButton("Funktion Plotten")
        self.plot_button.clicked.connect(self.plot)


        self.layout.addWidget(self.beschreibung)
        self.layout.addWidget(self.polynom)
        self.layout.addWidget(self.label_wertebereich_von)
        self.layout.addWidget(self.Wertebereich_von)
        self.layout.addWidget(self.label_wertebereich_bis)
        self.layout.addWidget(self.Wertebereich_bis)
        self.layout.addWidget(self.label_AnzPunkte)
        self.layout.addWidget(self.AnzPunkte)
        self.layout.addWidget(self.QComboBox_farbe)
        self.layout.addWidget(self.plot_button)
        self.layout.addWidget(self.canvas)

        center=QWidget()
        center.setLayout(self.layout)
        self.setCentralWidget(center)
        self.show()



    def plot(self):
        plt.clf()

        koeff_string=self.polynom.text()
        koeff_string_list=koeff_string.split(",")
        try:
            koeff_int_list=list(map(int,koeff_string_list))
            f=np.poly1d(koeff_int_list)
            x=np.linspace(int(self.Wertebereich_von.text()),int(self.Wertebereich_bis.text()),int(self.AnzPunkte.text()))
            y=f(x)
            farbe=self.QComboBox_farbe.currentText()
            plt.plot(x,y,color=farbe)
            plt.xlabel("x-Achse")
            plt.ylabel("y-Achse")
            plt.title("Polynomfunktion")
            self.canvas.draw()


        except ValueError:
            print("Eingabe ungültig")
            QMessageBox.warning(self,"Nur ganze Zahlen komma-getrennt eingeben")




app=QApplication([])
window=Window()
app.exec()

