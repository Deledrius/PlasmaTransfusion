PlasmaTransfusion
=================

PlasmaTransfusion facilitates conversion of Ages between Plasma client versions

PlasmaTransfusion is a small, simple command-line script that relies on 
[libHSPlasma] [1] to assist in the conversion of fan-made worlds (Ages) made 
for Uru:Complete Chronicles into data compatible with the open-source 
[Plasma Engine] [2]. Conversion between other Plasma versions should be 
possible but is not as thoroughly tested and relies on the current level of
support provided by the libHSPlasma library.



## Installation

Very little is needed to run PlasmaTransfusion.  Follow the instructions to 
install [libHSPlasma] [1] for your platform, and be sure to build the Python 
bindings as well (by using `-DDISABLE_PYTHON=OFF` in your cmake command).  
Place **transfusion.py** in your path or cwd and you're ready to begin.  
Due to being a pre-requisite for libHSPlasma, this guide assumes you also 
have a working [Python interpreter] [3] installed.  
Python 3.x is recommended but Python 2.7 is currently supported.  The GUI
application requires PyQt5.

### Linux

No platform-specific instructions are currently needed.

### OSX

No platform-specific instructions are currently needed.

### Windows

After building libHSPlasma be sure to install the **HSPlasma.dll** and 
**PyHSPlasma.pyd** files into your Python's library path
(typically *C:\Python33\DLLs*) or the same directory as the one in which 
you'll be running **transfusion.py**.  If you don't have Python associated 
for executing Python scripts, you'll need to modify the example commands to 
invoke it directly, depending on the version and appropriate path for the 
version of Python you have installed: 

`py -3 transfusion.py -a MyAgeName` or 
`C:\Python33\python.exe transfusion.py -a MyAgeName`

As PlasmaTransfusion is currently a command-line script, you will need to
open the Windows Command Prompt in order to begin the conversion; if you
prefer to avoid that you can create a customized command script to 
automatically perform a specific conversion (an excellent idea for iterative 
testing of an in-development Age).  To do so, create a text file with the 
following contents, modified appropriately as mentioned above for your 
system's Python, the Age you wish to convert, and input/output locations as 
desired:

    py -3 transfusion.py -i indat -o outdat -a MyAgeName
    pause

Save the file with any valid name you choose and the **cmd** extension 
(e.g. **convert.cmd**) and you're all set!  Of course, you can make as many of 
these cmd scripts as you like for different projects to streamline your 
conversion process.



## Usage

For the simplest use-case:

`./transfusion.py -a MyAgeName`

I recommend using separate input and output directories to avoid name 
collisions:

`./transfusion.py -i ./indat -o ./outdat -a MyAgeName`

The input and output directory options accept both relative and absolute paths.

### Other Options

Note: Use `-h` or `--help` to get a complete list of the supported options.

If you find that you need to rename the Age, or change the Sequence Prefix, 
this can be done using either of the `-n` and `-s` options respectively.

`./transfusion.py -i ./indat -o ./outdat -a MyAgeName -n MyNewAgeName -s 313`

The `-q` option is available to silence the script's textual output should you 
desire quiet operations as part of an automated process.

By default the script will convert to the MOUL-compatible [Plasma Engine] [2] 
format.  To specify another version supported by libHSPlasma for output, use 
the `-v` option.  Notable supported values are `EoA`, `HexIsle`, `MOUL`, 
`PoTS`, and `Prime`.  The library should automatically detect the input 
version and does not need to be specified.  Version names are not 
case-sensitive (e.g. `-v EoA` and `-v eoa` are equivalently acceptable).

`./transfusion.py -a MyHexIsleLevelName -v HexIsle`



## License

PlasmaTransfusion was created by Joseph Davies and released under the
GPLv3 license.  See LICENSE.txt for more information.




[1]: https://github.com/H-uru/libhsplasma
[2]: https://github.com/H-uru/Plasma
[3]: http://www.python.org/
