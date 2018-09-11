import sys
import os
from cx_Freeze import setup, Executable
from gui import __about__, ruta_iconos, ruta_licencia


build_exe_opciones = dict(
    packages=[
        'numpy.core._methods', 'numpy.lib.format', 'asyncio', 'jinja2'
    ],
    excludes=[
        'tkinter', 'PyQt5.QtBluetooth', 'PyQt5.QtNetwork', 'PyQt5.QtNfc',
        'PyQt5.QtWebChannel', 'PyQt5.QtWebSockets', 'PyQt5.QtWebEngineCore'
        'PyQt5.QtSql', 'PyQt5.QtNetwork', 'PyQt5.QtScript'
    ],
    include_files=[ruta_licencia],
    optimize=2,
)

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

target = Executable(
    script='main.py',
    base=base,
    targetName='Zonda.exe',
    icon=os.path.join(ruta_iconos, 'zonda.ico'),
    copyright=__about__.__autor__
)

setup(
    name='Zonda',
    version=__about__.__version__,
    author=__about__.__autor__,
    description='Cálculo de carga de viento de acuerdo a CIRSOC 102-2005',
    options={'build_exe': build_exe_opciones},
    executables=[target]
)