# This Python file uses the following encoding: utf-8
import sys
from db_Agenda import Conexion
from gui_Pyside import Agenda
from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem


class Agenda_personal(QWidget, Agenda):
    iten = []

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Agenda Personal')

        self.table.itemClicked.connect(self.seleccionar)
        self.btn_Eliminar.clicked.connect(self.delete)
        self.btn_Nuevo.clicked.connect(self.nuevo)
        self.btn_Editar.clicked.connect(self.modificar)

        self.mostrar()

    def mostrar(self):
        index = 0
        _seleccionar = "SELECT * FROM contactos"
        cursor = Conexion.cursor()
        cursor.execute(_seleccionar)
        datos = cursor.fetchall()

        for dato in datos:
            ids = dato[0]
            nombre = dato[1]
            email = dato[2]
            telf = dato[3]
            self.table.setRowCount(index + 1)
            self.table.setItem(index, 0, QTableWidgetItem(str(ids)))
            self.table.setItem(index, 1, QTableWidgetItem(nombre))
            self.table.setItem(index, 2, QTableWidgetItem(email))
            self.table.setItem(index, 3, QTableWidgetItem(telf))
            index += 1

    def seleccionar(self):
        self.iten = self.table.selectedItems()
        self.nombre_txt.setText(self.iten[1].text())
        self.emai_txt.setText(self.iten[2].text())
        self.telf_txt.setText(self.iten[3].text())

    def limpiar(self):
        self.nombre_txt.clear()
        self.emai_txt.clear()
        self.telf_txt.clear()
        
    def delete(self):
        with Conexion.conexion() as conexion:
            _eliminar = "DELETE FROM contactos WHERE id=?"
            cursor = conexion.cursor()
            num = self.table.selectedItems()[0]
            cursor.execute(_eliminar, (num.text(),))
            self.limpiar()
            self.mostrar()
            self.iten = []
        

    def nuevo(self):
        if self.nombre_txt == None:
            print('Campos vacios')
        else:
            with Conexion.conexion() as conexion:
                _agregar = "INSERT INTO contactos (id, nombre, email, telf) VALUES (null,?,?,?)"
                persona = [(self.nombre_txt.text(), self.emai_txt.text(), self.telf_txt.text())]
                cursor = conexion.cursor()
                cursor.executemany(_agregar, persona)
                self.limpiar()
                self.mostrar()


    def modificar(self):
        with Conexion.conexion() as conexion:
            _actualizar = "UPDATE contactos set nombre=?, email=?, telf=? WHERE id=?"
            cursor = conexion.cursor()
            persona = (self.nombre_txt.text(), self.emai_txt.text(), self.telf_txt.text(), self.iten[0].text())
            cursor.execute(_actualizar, persona)
            self.limpiar()
            self.iten = []
            self.mostrar()

if __name__ == "__main__":
    app = QApplication([])
    widget = Agenda_personal()
    widget.show()
    sys.exit(app.exec())
