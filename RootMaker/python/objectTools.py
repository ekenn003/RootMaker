import FWCore.ParameterSet.Config as cms

# Hopefully it is obvious what these functions do.
def getLowercaseSingular(name):
    return name.rstrip('s').downcase()
def getUppercaseSingular(name):
    if "ak4pfchsjets" in name:
        return "Jet"
    elif "puppi" in name:
        return name.replace("puppi","").rstrip('s').capitalize()
    else:
        return name.rstrip('s').capitalize()

# Filters an object collection based on a cut string from test/RootTree.py
def collectionFilter(process,obj,objSrc,selection):
    module = cms.EDFilter(
        "PAT{0}Selector".format(getUppercaseSingular(obj)),
        src = cms.InputTag(objSrc),
        cut = cms.string(selection),
    )
    modName = '{0}Selection'.format(obj)
    setattr(process,modName,module)
    pathName = '{0}SlectionPath'.format(obj)
    path = cms.Path(getattr(process,modName))
    setattr(process,pathName,path)
    process.schedule.append(getattr(process,pathName))
    return modName

# Cleans a PAT object collection. 
def objectCleaner(process,obj,objSrc,objectCollections,cleaning):
    cleanParams = cms.PSet()
    for cleanObj in cleaning:
        cleanSrc = objectCollections[cleanObj]
        cut = cleaning[cleanObj]['cut']
        dr  = cleaning[cleanObj]['dr']
        particleParams = cms.PSet(
            src=cms.InputTag(cleanSrc),
            algorithm=cms.string("byDeltaR"),
            preselection=cms.string(cut),
            deltaR=cms.double(dr),
            checkRecoComponents=cms.bool(False),
            pairCut=cms.string(''),
            requireNoOverlaps=cms.bool(True),
        )
        setattr(cleanParams,cleanObj,particleParams)
    module = cms.EDProducer(
        "PAT{0}Cleaner".format(getUppercaseSingular(obj)),
        src = cms.InputTag(objSrc),
        preselection = cms.string(''),
        checkOverlaps = cleanParams,
        finalCut = cms.string(''),
    )
    modName = '{0}Cleaning'.format(obj)
    setattr(process,modName,module)
    pathName = '{0}CleaningPath'.format(obj)
    path = cms.Path(getattr(process,modName))
    setattr(process,pathName,path)
    process.schedule.append(getattr(process,pathName))
    return modName
