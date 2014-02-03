#!/usr/bin/env python

# This file is part of PlasmaTransfusion.
#
# PlasmaTransfusion is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PlasmaTransfusion is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with PlasmaTransfusion.  If not, see <http://www.gnu.org/licenses/>.

"""transfusion.py

    A Utility for converting Plasma Ages
    by Joseph Davies (deledrius@gmail.com)

  * Requires libHSPlasma and PyHSPlasma (https://github.com/H-uru/libhsplasma)

  Usage:
    ./transfusion.py ... [TODO]
"""

import os
import sys
import argparse
import logging

try:
    import PyHSPlasma
except ImportError as e:
    logging.critical("Required module PyHSPlasma cannot be found.")
    sys.exit(1)

versionNames = {
    PyHSPlasma.pvEoa: "EoA",
    PyHSPlasma.pvHex: "HexIsle",
    PyHSPlasma.pvMoul: "MOUL",
    PyHSPlasma.pvPots: "PoTS",
    PyHSPlasma.pvPrime: "Prime",
    PyHSPlasma.pvUniversal: "Universal",
    PyHSPlasma.pvUnknown: "Unknown",
    }

unsupportedTypeList = {}

def updateLocation(pageLoc, newSequencePrefix):    
    newPageLoc = PyHSPlasma.plLocation(pageLoc.version)
    newPageLoc.version = pageLoc.version
    newPageLoc.prefix = newSequencePrefix
    newPageLoc.page = pageLoc.page
    newPageLoc.flags = pageLoc.flags

    return newPageLoc

def removeUnsupportedObjects(plResMgr, objectType, pageLocation):
    for key in plResMgr.getKeys(pageLocation, objectType):
        plResMgr.DelObject(key)

def doConvert(ageName, inpath, newAgeName, outpath, newSeqPrefix, newPlasmaVersion):
    ## Create our Resource Manager
    plResMgr = PyHSPlasma.plResManager()

    ageFile  = os.path.join(inpath, ageName)
    fullpath = os.path.abspath(ageFile)

    try:
        logging.info("Loading '{0}'...".format(ageFile))
        age = plResMgr.ReadAge(fullpath, True)
        logging.info("Age version: {0}".format(versionNames[plResMgr.getVer()]))
    except IOError as e:
        logging.critical("Unable to read Age: {0}".format(ageFile))
        return False
    except KeyboardInterrupt:
        logging.critical("Interrupt detected. Aborting.")
        return False
    else:
        try:
            logging.info("Processing {0}".format(age.name))

            ## Flip through pages and update to new location, if needed
            if newSeqPrefix != None:
                locs = plResMgr.getLocations()
                for pageLoc in locs:
                    logging.info("Changing page prefix for {0} (SeqPrefix: {1} --> {2})".format(pageLoc.page, age.seqPrefix, newSeqPrefix))
                    newPageLoc = updateLocation(pageLoc, newSeqPrefix)
                    plResMgr.ChangeLocation(pageLoc, newPageLoc)
            else:
                newSeqPrefix = age.seqPrefix

            ## Filter unsupported objects or objects which require conversion
            plResMgr.setVer(newPlasmaVersion, True)
            logging.info("Converting to version: {0}".format(versionNames[plResMgr.getVer()]))
            locs = plResMgr.getLocations()
            for pageLoc in locs:
                pageInfo = plResMgr.FindPage(pageLoc)
                plResMgr.setVer(newPlasmaVersion, True)
                logging.info("Processing page {0}: {1}".format(pageLoc.page, pageInfo.page))

                if plResMgr.getVer() in unsupportedTypeList:
                    for objectType in unsupportedTypeList[plResMgr.getVer()]:
                        logging.info("Removing unsupported objects (type: {0})".format(PyHSPlasma.plFactory.ClassName(objectType)))
                        removeUnsupportedObjects(plResMgr, objectType, pageLoc)
                pageInfo.age = newAgeName

                ## Write page
                pageOut = os.path.abspath(os.path.join(outpath, pageInfo.getFilename(newPlasmaVersion)))
                plResMgr.WritePage(pageOut, pageInfo)

            ## Write final Age
            age.seqPrefix = newSeqPrefix
            age.name = newAgeName
            ageOut = os.path.abspath(os.path.join(outpath, age.name + ".age"))
            age.writeToFile(ageOut, newPlasmaVersion)

        except MemoryError as e:
            logging.critical("Unable to process Age ({0}) - {1}".format(age.name, e))
            return False
        except KeyboardInterrupt:
            logging.critical("Interrupt detected. Aborting.")
            return False
        except Exception as e:
            logging.critical("Unhandled exception: {0}".format(e))
            return False

        plResMgr.UnloadAge(age.name)

def main():
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    ## Only display Errors
    PyHSPlasma.plDebug.Init(PyHSPlasma.plDebug.kDLError)

    ## Default Paths
    DefaultPath = "."

    ## Define Options
    userVersionNames = versionNames.values()
    userVersionNames.remove("Unknown")

    parser = argparse.ArgumentParser(description='A Utility for converting Plasma Ages.')
    parser.add_argument("-q", "--quiet", dest="verbose", default=True, action="store_false", help="Don't print status messages")
    parser.add_argument("-i", "--indir", dest="indir", default=DefaultPath, help="Sets input path for Ages.")
    parser.add_argument("-o", "--outdir", dest="outdir", default=DefaultPath, help="Sets output path for Ages.")
    parser.add_argument("-a", "--agename", dest="ageName", help="Sets input Age name. (Direbo, Neighborhood01, etc.)")
    parser.add_argument("-n", "--newagename", dest="newAgeName", help="Sets output name for converted Age.")
    parser.add_argument("-s", "--seqprefix", dest="newSeqPrefix", type=int, help="Sets new SequencePrefix for converted Age.")
    parser.add_argument("-v", "--version", dest="newPlasmaVersion", default="MOUL", choices=userVersionNames, help="Sets new Plasma version for converted Age.")

    args = parser.parse_args()

    ## Send output to OS's null if unwanted
    if not args.verbose:
        sys.stdout = open(os.devnull,"w")
        sys.stderr = open(os.devnull,"w")

    ## Compute Paths
    indir = os.path.expanduser(args.indir)
    outdir = os.path.expanduser(args.outdir)

    if args.ageName:
        ageName = args.ageName
    else:
        logging.error("Transfusion requires an input file for conversion!")
        return False

    if args.newAgeName:
        newAgeName = args.newAgeName
    else:
        logging.warning("No output name specified.  Using {} for converted Age.".format(ageName))
        newAgeName = ageName

    ## Other Options
    newSeqPrefix = args.newSeqPrefix

    if args.newPlasmaVersion.lower() in [name.lower() for name in versionNames.values()]:
        newPlasmaVersion = [k for k, v in versionNames.items() if args.newPlasmaVersion.lower() == v.lower()][0]
    else:
        logging.warning("Requested Plasma Version '{}' not recognized.  Defaulting to 'MOUL' for output.".format(newPlasmaVersion))
        newPlasmaVersion = versionNames[PyHSPlasma.pvMoul]

    ## Sanitize Agenames
    if ageName.endswith(".age"):
        ageName = ageName[:-4]
    if newAgeName.endswith(".age"):
        newAgeName = newAgeName[:-4]

    ## Check for existing files
    if not os.path.exists(os.path.join(indir, "{}.age".format(ageName))):
        logging.error("Input Age '{}' cannot be found.".format(os.path.join(indir, "{}.age".format(ageName))))
        return False

    if os.path.exists(os.path.join(outdir, "{}.age".format(newAgeName))):
        logging.warning("Output Age '{}' already exists.  It will be overwritten.".format(os.path.join(outdir, "{}.age".format(newAgeName))))

    ## Do the work!
    doConvert(ageName + ".age", indir, newAgeName, outdir, newSeqPrefix, newPlasmaVersion)

if __name__ == '__main__':
    main()
