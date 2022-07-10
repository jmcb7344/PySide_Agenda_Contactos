from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QHeaderView,
    QLabel, QLayout, QLineEdit, QPushButton,
    QSizePolicy, QTableWidget, QTableWidgetItem, QWidget)

class Agenda(object):
    def setupUi(self, Agenda_personal):
        if not Agenda_personal.objectName():
            Agenda_personal.setObjectName(u"Agenda_personal")
        Agenda_personal.resize(440, 400)
        self.formulario = QFrame(Agenda_personal)
        self.formulario.setObjectName(u"formulario")
        self.formulario.setGeometry(QRect(10, 10, 421, 131))
        self.formulario.setBaseSize(QSize(0, 0))
        self.formulario.setAcceptDrops(False)
        self.formulario.setAutoFillBackground(False)
        self.formulario.setFrameShape(QFrame.StyledPanel)
        self.formulario.setFrameShadow(QFrame.Plain)
        self.formLayoutWidget_2 = QWidget(self.formulario)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 0, 361, 104))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.formLayout_2.setFieldGrowthPolicy(QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout_2.setRowWrapPolicy(QFormLayout.DontWrapRows)
        self.formLayout_2.setContentsMargins(35, 10, 10, 10)
        self.nombreLabel_2 = QLabel(self.formLayoutWidget_2)
        self.nombreLabel_2.setObjectName(u"nombreLabel_2")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.nombreLabel_2)

        self.nombre_txt = QLineEdit(self.formLayoutWidget_2)
        self.nombre_txt.setObjectName(u"nombreLineEdit_2")

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.nombre_txt)

        self.emailLabel_2 = QLabel(self.formLayoutWidget_2)
        self.emailLabel_2.setObjectName(u"emailLabel_2")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.emailLabel_2)

        self.emai_txt = QLineEdit(self.formLayoutWidget_2)
        self.emai_txt.setObjectName(u"emailLineEdit_2")

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.emai_txt)

        self.telfLabel_2 = QLabel(self.formLayoutWidget_2)
        self.telfLabel_2.setObjectName(u"telfLabel_2")

        self.formLayout_2.setWidget(2, QFormLayout.LabelRole, self.telfLabel_2)

        self.telf_txt = QLineEdit(self.formLayoutWidget_2)
        self.telf_txt.setObjectName(u"telfLineEdit_2")

        self.formLayout_2.setWidget(2, QFormLayout.FieldRole, self.telf_txt)

        self.btn_Nuevo = QPushButton(self.formulario)
        self.btn_Nuevo.setObjectName(u"pushButton")
        self.btn_Nuevo.setGeometry(QRect(70, 100, 91, 24))
        self.btn_Editar = QPushButton(self.formulario)
        self.btn_Editar.setObjectName(u"pushButton_2")
        self.btn_Editar.setGeometry(QRect(170, 100, 91, 24))
        self.btn_Eliminar = QPushButton(self.formulario)
        self.btn_Eliminar.setObjectName(u"pushButton_3")
        self.btn_Eliminar.setGeometry(QRect(270, 100, 91, 24))
        self.table = QTableWidget(0,4,Agenda_personal)
        self.table.setHorizontalHeaderLabels(['ID', 'NOMBRE', 'EMAIL', 'TELF'])
        self.table.setGeometry(QRect(10, 150, 421, 241))
        self.table.setAlternatingRowColors(True)
        self.table.setEditTriggers(QTableWidget.NoEditTriggers)
        self.table.setSelectionBehavior(QTableWidget.SelectRows)
        self.table.setSelectionMode(QTableWidget.SingleSelection)
        self.table.setColumnWidth(0, 10)
        self.table.setColumnWidth(1, 120)
        self.table.setColumnWidth(2, 150)
        self.table.setColumnWidth(3, 90)

        self.retranslateUi(Agenda_personal)

        QMetaObject.connectSlotsByName(Agenda_personal)
    # setupUi

    def retranslateUi(self, Agenda_personal):
        Agenda_personal.setWindowTitle(QCoreApplication.translate("Agenda_personal", u"Agenda_personal", None))
#if QT_CONFIG(accessibility)
        self.formulario.setAccessibleName("")
#endif // QT_CONFIG(accessibility)
#if QT_CONFIG(accessibility)
        self.formulario.setAccessibleDescription("")
#endif // QT_CONFIG(accessibility)
        self.nombreLabel_2.setText(QCoreApplication.translate("Agenda_personal", u"Nombre", None))
        self.emailLabel_2.setText(QCoreApplication.translate("Agenda_personal", u"Email", None))
        self.telfLabel_2.setText(QCoreApplication.translate("Agenda_personal", u"Telf", None))
        self.btn_Nuevo.setText(QCoreApplication.translate("Agenda_personal", u"Nuevo", None))
        self.btn_Editar.setText(QCoreApplication.translate("Agenda_personal", u"Modificar", None))
        self.btn_Eliminar.setText(QCoreApplication.translate("Agenda_personal", u"Elinimar", None))
       
    # retranslateUi

