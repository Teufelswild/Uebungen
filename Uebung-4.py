from sys import argv
from PyQt5.QtWidgets import *
import os


class MyWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Gui-Programmierung")



        #Erstllen des Menüs
        menubar = self.menuBar()
        file_menu = menubar.addMenu("Datei")
        save_menu = file_menu.addMenu("Speichern")
        quit_menu = file_menu.addMenu("Beenden")

        #Erstellen der Aktionen
        save_action = QAction("Speichern", self)
        quit_action = QAction("Beenden", self)

        #Verknüpfen der Aktionen mit den Methoden
        save_menu.addAction(save_action)
        quit_menu.addAction(quit_action)
        save_action.triggered.connect(self.save_push_button_clicked)
        quit_action.triggered.connect(self.menu_quit)


        #Erstellen der Widgets
        self.vorname_line_edit = QLineEdit()
        self.nachname_line_edit = QLineEdit()
        self.geburtsdatum_date_edit = QDateEdit()
        self.adresse_line_edit = QLineEdit()
        self.postleitzahl_line_edit = QLineEdit()
        self.ort_line_edit = QLineEdit()
        self.land_combo_box = QComboBox()
        self.land_combo_box.addItems(["Schweiz","Deutscheland","Frankreich"])
        save_push_button = QPushButton("Speichern")

        
        #Erstellen des Layouts
        layout = QFormLayout()
        layout.setMenuBar(menubar)
        layout.addRow("Vorname:", self.vorname_line_edit)
        layout.addRow("Nachname:", self.nachname_line_edit)
        layout.addRow("Geburtsdatum:", self.geburtsdatum_date_edit)
        layout.addRow("Adresse:", self.adresse_line_edit)
        layout.addRow("Postleitzahl:", self.postleitzahl_line_edit)
        layout.addRow("Ort:", self.ort_line_edit)
        layout.addRow("Land:", self.land_combo_box)
        layout.addWidget(save_push_button)

        center_widget = QWidget()
        center_widget.setLayout(layout)
        self.setCentralWidget(center_widget)


        #Verknüpfen der Methode mit dem Button Click-Event
        save_push_button.clicked.connect(self.save_push_button_clicked)


    
    
    
    def save_push_button_clicked(self):
        
        path="/Users/gianschneider/temp_Macintosh_HD_gianschneider"
        os.chdir(path)
        
        file=open("ausgabe.txt","w", encoding="utf-8")
        vorname=self.vorname_line_edit.text()
        nachname=self.nachname_line_edit.text()
        geburtsdatum=self.geburtsdatum_date_edit.date()
        geburtsdatum=str(geburtsdatum)
        adresse=self.adresse_line_edit.text()
        postleitzahl=self.postleitzahl_line_edit.text()
        ort=self.ort_line_edit.text()
        land=self.land_combo_box.currentText()
       
        file.write("{},{},{},{},{},{},{}".format(vorname,nachname,geburtsdatum,adresse,postleitzahl,ort,land))

        file.close()
    

    def menu_quit(self):

        self.close()    

def main():
    app = QApplication(argv)
    main_window = MyWindow()
    main_window.show()
    app.exec_()


if __name__ == "__main__":
    main()
