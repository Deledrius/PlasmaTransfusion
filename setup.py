from distutils.core import setup
import py2exe


setup(name='PlasmaTransfusion',
      version = '1.0',
      description = 'Converts Ages between Plasma versions',
      windows = [{"script":'gui.py',"dest_base":"PlasmaTransfusion"}],
      options={"py2exe":{"includes":["sip"],"dll_excludes":
      ["w9xpopen.exe"],}},
      dest_base="PlasmaTransfusion")

