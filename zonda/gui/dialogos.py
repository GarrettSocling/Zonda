# Copyright (c) 2018, Eduardo Di Loreto <efdiloreto@gmail.com>

# This file is part of Zonda.

# Zonda is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# Zonda is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with Zonda.  If not, see <https://www.gnu.org/licenses/>.

import os
import webbrowser
from PyQt5 import QtWidgets, QtCore, QtGui
from gui import ruta_imagenes, ruta_licencia
from . import widgets, excepciones
from . import __about__


def hyperlink(link, texto):
    return f'<a href={link}>{texto}</a>'


class AcercaDe(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()

        imagen_zonda = QtWidgets.QLabel()
        imagen_zonda.setAlignment(QtCore.Qt.AlignHCenter)
        ruta_zonda = os.path.join(ruta_imagenes, 'zonda.png')
        pixmap_zonda = QtGui.QPixmap(ruta_zonda)
        imagen_zonda.setPixmap(pixmap_zonda)

        linea = QtWidgets.QFrame()
        linea.setFrameShape(QtWidgets.QFrame.HLine)
        linea.setFrameShadow(QtWidgets.QFrame.Sunken)

        imagen_gnu = QtWidgets.QLabel()
        ruta_gnu = os.path.join(ruta_imagenes, 'gplv3-with-text-84x42.png')
        pixmap_gnu = QtGui.QPixmap(ruta_gnu)
        imagen_gnu.setPixmap(pixmap_gnu)

        mensaje_que_es = 'Zonda es un software gratis y de código abierto' \
            ' destinado a calcular las cargas de viento sobre las estructuras de' \
            ' acuerdo al Reglamento Argentino CIRSOC 102-2005.\n\n'\
            'Si el software te es de utilidad, podes apoyarnos' \
            ' colaborando en el proyecto o mediante donaciones que ayudarán a' \
            ' mantener vivo el mismo.'
        label_que_es = QtWidgets.QLabel(mensaje_que_es)
        label_que_es.setWordWrap(True)

        informacion_req = (
            'Versión', 'Licencia', 'Autor', 'E-Mail', 'Source', 'Colaboradores'
        )

        label_licencia = QtWidgets.QLabel(__about__.__licencia__)
        label_autor = QtWidgets.QLabel(
            hyperlink(__about__.__autor_link__, __about__.__autor__)
        )
        label_mail = QtWidgets.QLabel(__about__.__autor_email__)
        label_proyecto = QtWidgets.QLabel(
            hyperlink(__about__.__url__, __about__.__url__)
        )
        label_colaboradores = QtWidgets.QLabel(
            hyperlink(__about__.__colaboradores__, __about__.__colaboradores__)
        )
        for label in (label_autor, label_mail, label_proyecto, label_colaboradores):
            label.setTextFormat(QtCore.Qt.RichText)
            label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
            label.setOpenExternalLinks(True)

        boton_licencia = QtWidgets.QPushButton('Licencia')
        boton_licencia.clicked.connect(self._abrir_licencia)

        boton_donar = QtWidgets.QPushButton('Donar')
        boton_donar.clicked.connect(
            lambda: webbrowser.open(__about__.__url__ + '/DONATE.md')
        )

        layout_info = QtWidgets.QGridLayout()

        for i, info_req in enumerate(informacion_req):
            layout_info.addWidget(QtWidgets.QLabel(info_req + ':'), i, 0)

        layout_info.addWidget(QtWidgets.QLabel(__about__.__version__), 0, 1)
        layout_info.addWidget(label_licencia, 1, 1)
        layout_info.addWidget(label_autor, 2, 1)
        layout_info.addWidget(label_mail, 3, 1)
        layout_info.addWidget(label_proyecto, 4, 1)
        layout_info.addWidget(label_colaboradores, 5, 1)
        layout_info.addWidget(imagen_gnu, 0, 3, 3, 1)
        layout_info.setColumnStretch(2, 1)

        layout_botones = QtWidgets.QHBoxLayout()
        layout_botones.addWidget(boton_licencia)
        layout_botones.addStretch()
        layout_botones.addWidget(boton_donar)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(imagen_zonda)
        layout.addSpacing(25)
        layout.addWidget(label_que_es)
        layout.addWidget(linea)
        layout.addLayout(layout_info)
        layout.addWidget(linea)
        layout.addSpacing(15)
        layout.addLayout(layout_botones)
        layout.addStretch()

        self.setLayout(layout)

        self.setWindowTitle('Acerca de Zonda')
        self.setLayout(layout)
        self.exec_()

    def _abrir_licencia(self):
        try:
            os.startfile(ruta_licencia)
        except FileNotFoundError:
            QtWidgets.QMessageBox.warning(
                self, 'Error', 'Archivo no encontrado.'
            )


class DialogoComponentes(QtWidgets.QDialog):
    def __init__(self, datos):
        super().__init__()
        self._datos = datos

        self._componentes_paredes = widgets.WidgetComponentes(
            datos['componentes_paredes']
        )
        self._componentes_cubierta = widgets.WidgetComponentes(
            datos['componentes_cubierta']
        )

        layout_componentes = QtWidgets.QGridLayout()
        layout_componentes.addWidget(
            QtWidgets.QLabel('<b>PAREDES</b>'), 0, 0, QtCore.Qt.AlignCenter
        )
        layout_componentes.addWidget(
            QtWidgets.QLabel('<b>CUBIERTA</b>'), 0, 2, QtCore.Qt.AlignCenter
        )
        layout_componentes.addItem(QtWidgets.QSpacerItem(20, 0), 0, 1, 3, 1)
        layout_componentes.addWidget(self._componentes_paredes, 2, 0)
        layout_componentes.addWidget(self._componentes_cubierta, 2, 2)
        layout_componentes.setVerticalSpacing(2)

        botones = QtWidgets.QDialogButtonBox(
            QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel
        )
        botones.accepted.connect(self.accept)
        botones.rejected.connect(self.reject)

        layout_principal = QtWidgets.QVBoxLayout()
        layout_principal.addLayout(layout_componentes)
        layout_principal.addWidget(botones)

        self.setLayout(layout_principal)
        self.setWindowTitle('Componentes y Revestimientos - Edificio')
        self.resize(self.width(), self.height())

    def accept(self):
        try:
            self._datos = {
                'componentes_paredes': self._componentes_paredes(),
                'componentes_cubierta': self._componentes_cubierta()
            }
            super().accept()
        except excepciones.ErrorComponentes as error:
            QtWidgets.QMessageBox.warning(self, 'Error de Datos de Entrada', str(error))

    def __call__(self):
        return self._datos
