#!/usr/bin/env python

from __future__ import print_function

import os
import sys


try:
    import PyHSPlasma
except ImportError as e:
    libPlasma = False
else:
    libPlasma = True

versionNames = {
    PyHSPlasma.pvEoa: "pvEoa",
    PyHSPlasma.pvHex: "pvHex",
    PyHSPlasma.pvMoul: "pvMoul",
    PyHSPlasma.pvPots: "pvPots",
    PyHSPlasma.pvPrime: "pvPrime",
    PyHSPlasma.pvUniversal: "pvUniversal",
    PyHSPlasma.pvUnknown: "pvUnknown",
    }
    
unsupportedTypeList = {
    PyHSPlasma.pvMoul: [
        #PyHSPlasma.plFactory.kGenericPhysical,
        PyHSPlasma.plFactory.kPythonFileMod,
        ]
}
    
def hsKeyedObject_Create(hsKeyedObject_type):
    if hsKeyedObject_type == PyHSPlasma.plFactory.kMipmap:
        return PyHSPlasma.plMipmap()
    elif hsKeyedObject_type == PyHSPlasma.plFactory.kCubicEnvironmap:
        return PyHSPlasma.plCreatableStub(hsKeyedObject_type, 0)
        #return PyHSPlasma.plCubicEnvironmap()
    else:
        return PyHSPlasma.plCreatableStub(hsKeyedObject_type, 0)

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
        
def doConvert(ageName):
    if not libPlasma:
        print("\nFatal Error: PyHSPlasma module not loaded.  Reading of Age files unavailable.")
        return False
        
    ## Only display Errors
    PyHSPlasma.plDebug.Init(PyHSPlasma.plDebug.kDLError)

    ## Create our Resource Manager
    plResMgr = PyHSPlasma.plResManager()
    
    indir = "indat"
    outdir = "outdat"
    ageFile  = os.path.join(indir, ageName)
    fullpath = os.path.abspath(ageFile)
    
    try:
        print("Loading {0}".format(ageFile))
        age = plResMgr.ReadAge(fullpath, True)
        print("Age version: {0}".format(versionNames[plResMgr.getVer()]))
    except IOError as e:
        print("Warning - Unable to read Age: {0}".format(ageFile))
    except KeyboardInterrupt:
        print("\nInterrupt detected. Aborting.")
        return False
    else:
        try:
            newSeqPrefix = age.seqPrefix + 100
            oldSeqPrefix = age.seqPrefix
            print("Processing {0}".format(age.name))
                
            locs = plResMgr.getLocations()
            for pageLoc in locs:
                print("Changing page prefix for {0} (SeqPrefix: {1} --> {2})".format(pageLoc.page, oldSeqPrefix, newSeqPrefix))
                newPageLoc = updateLocation(pageLoc, newSeqPrefix)
                plResMgr.ChangeLocation(pageLoc, newPageLoc)            

            plResMgr.setVer(PyHSPlasma.pvMoul, True)
            print("Converting to version: {0}".format(versionNames[plResMgr.getVer()]))
            locs = plResMgr.getLocations()
            for pageLoc in locs:
                plResMgr.setVer(PyHSPlasma.pvMoul, True)
                print("Processing page {0}".format(pageLoc.page))
                for objectType in unsupportedTypeList[plResMgr.getVer()]:
                    print(" - Removing unsupported objects (type: {0})".format(PyHSPlasma.plFactory.ClassName(objectType)))
                    removeUnsupportedObjects(plResMgr, objectType, pageLoc)
                pageInfo = plResMgr.FindPage(pageLoc)
                pageInfo.age = "Tiwah"
                pageOut = os.path.abspath(os.path.join(outdir, pageInfo.getFilename(PyHSPlasma.pvMoul)))
                plResMgr.WritePage(pageOut, pageInfo)

            age.seqPrefix = newSeqPrefix
            age.name = "Tiwah"
            ageOut = os.path.abspath(os.path.join(outdir, age.name + ".age"))
            age.writeToFile(ageOut, PyHSPlasma.pvMoul)
                    
        except MemoryError as e:
            print("\nFatal Error - Unable to process Age ({0}) - {1}".format(age.name, e))
            return False
        except KeyboardInterrupt:
            print("\nInterrupt detected. Aborting.")
            return False
        except Exception as e:
            print("** Unhandled exception: {0}".format(e))
            return False
        
        plResMgr.UnloadAge(age.name)
        
if __name__ == '__main__':
    ageList = [
        #"Direbo.age", 
        "Descent.age",
        ]
    for ageName in ageList:
        doConvert(ageName)