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

aca = os.path.dirname(os.path.realpath(__file__))
carpeta_principal = os.path.dirname(os.path.dirname(aca))

ruta_iconos = os.path.join(aca, 'recursos', 'iconos')

ruta_imagenes = os.path.join(aca, 'recursos', 'imagenes')

ruta_licencia = os.path.join(carpeta_principal, 'LICENSE.txt')