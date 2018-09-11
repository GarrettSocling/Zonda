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
from PyQt5 import QtWidgets, QtGui, QtCore
from gui import ruta_iconos
from . import widgets, dialogos, __about__


class VentanaPrincipal(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.resize(1366, 768)
        self.setWindowTitle(f'Zonda {__about__.__version__}')
        self._menu = self.menuBar()
        self.label_calculos = QtWidgets.QLabel('Sin resultados')
        self.label_calculos.setAlignment(QtCore.Qt.AlignVCenter)
        # self.label_calculos.setContentsMargins(10, 0, 0, 0)

        barra_estado = self.statusBar()
        barra_estado.setSizeGripEnabled(False)
        barra_estado.addWidget(self.label_calculos, 1)

        self.setWindowIcon(QtGui.QIcon(os.path.join(ruta_iconos, 'zonda.svg')))
        self._widget_central = widgets.WidgetPrincipal(self)
        self.setCentralWidget(self._widget_central)
        self._menu_archivo()
        self._calcular()
        self._acerca_de()

    def _menu_archivo(self):
        menu_archivo = self._menu.addMenu('&Archivo')

        salir_act = QtWidgets.QAction('&Salir', self)
        salir_act.setShortcut('Ctrl+Q')
        salir_act.triggered.connect(QtWidgets.qApp.quit)

        menu_archivo.addAction(salir_act)

    def _calcular(self):
        calcular_act = QtWidgets.QAction('&Calcular', self)
        calcular_act.setShortcut('Alt+C')
        calcular_act.triggered.connect(self._widget_central.calcular)
        self._menu.addAction(calcular_act)

    def _acerca_de(self):
        acerca_de_act = QtWidgets.QAction('&Acerca', self)
        acerca_de_act.triggered.connect(dialogos.AcercaDe)
        self._menu.addAction(acerca_de_act)

