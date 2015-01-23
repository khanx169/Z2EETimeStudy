import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
#'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/548BD0EF-5F67-E211-AB31-00261894393F.root'
'file:/hdfs/cms/phedex/store/data/Run2012C/SinglePhoton/RECO/EXODisplacedPhoton-PromptSkim-v3/000/198/941/00000/0EA7C91A-B8CF-E111-9766-002481E150EA.root'
#'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/507233A4-57AC-E211-9EA6-0026189438F7.root',
#'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/502CC367-5EAC-E211-A498-00261894385A.root'
])

# Output - dummy
process.out = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    fileName = cms.untracked.string('file:EcalTiming_RUn2012C.root'),
    )


# gfworks: to get clustering 

# Geometry
process.load("Configuration.Geometry.GeometryIdeal_cff")
process.load('Configuration/StandardSequences/GeometryExtended_cff')
process.load("Geometry.CaloEventSetup.CaloTopology_cfi")
process.load("Geometry.CaloEventSetup.CaloGeometry_cff")
process.load("Geometry.CaloEventSetup.CaloGeometry_cfi")
process.load("Geometry.EcalMapping.EcalMapping_cfi")
process.load("Geometry.EcalMapping.EcalMappingRecord_cfi")
process.load("Geometry.MuonNumbering.muonNumberingInitialization_cfi") # gfwork: need this?
process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder")

################# Recovering Unclean Supercluster of gsf/gedgsf electons##################
##########################################################################################


#---Needed to Reconsctruct on the fly from uncleaned SCs without timing cut for slpikes
process.load('Configuration.StandardSequences.Services_cff')
process.load('Configuration.StandardSequences.MagneticField_38T_cff')
process.load("Configuration.StandardSequences.Reconstruction_cff")
process.load("Configuration.StandardSequences.MagneticField_cff")
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
process.load("RecoEcal.Configuration.RecoEcal_cff")

## to get Hit Reco #############################################################
process.load("RecoLocalTracker.SiPixelRecHits.SiPixelRecHits_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitConverter_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.SiStripRecHitMatcher_cfi")
process.load("RecoLocalTracker.SiStripRecHitConverter.StripCPEfromTrackAngle_cfi")
process.load("RecoLocalTracker.SiStripZeroSuppression.SiStripZeroSuppression_cfi")
process.load("RecoLocalTracker.SiStripClusterizer.SiStripClusterizer_cfi")
process.load("RecoLocalTracker.SiPixelClusterizer.SiPixelClusterizer_cfi")
process.load("RecoLocalTracker.SiPixelRecHits.PixelCPEESProducers_cff")
process.load("RecoTracker.TransientTrackingRecHit.TTRHBuilders_cff")
process.load("Configuration.StandardSequences.RawToDigi_cff")
process.load("Configuration.EventContent.EventContent_cff")
process.load("RecoEgamma.EgammaElectronProducers.siStripSeeds_cff")


#from Configuration.StandardSequences.Reconstruction_cff import *
from RecoEcal.Configuration.RecoEcal_cff import *
from RecoEcal.EgammaClusterProducers.hybridSuperClusters_cfi import *
process.load("RecoEcal.EgammaClusterProducers.hybridClusteringSequence_cff")
process.load("RecoEcal.EgammaClusterProducers.unifiedSCCollection_cfi")


process.load("FWCore.MessageLogger.MessageLogger_cfi")
### First Recover the superclusters #######################################################
process.load("RecoEcal.EgammaClusterProducers.uncleanSCRecovery_cfi")
process.uncleanSCRecovered.cleanScCollection=cms.InputTag ("correctedHybridSuperClusters")

#### Egamma Clusters to GsfElectrons 
process.load('RecoEgamma.EgammaPhotonProducers.conversionTracks_cff')
process.load("RecoEgamma.EgammaElectronProducers.gsfElectronSequence_cff")

#### Now do Electron reco sequence ######################################################
#### OR Import both as this
from RecoEgamma.EgammaElectronProducers.gsfElectronModules_cff  import * 
#### EcalDrivenseedElectrn Modules #######################################################
from RecoEgamma.EgammaElectronProducers.ecalDrivenElectronSeedsModules_cff  import*

#### Clone Electron/ElectronCores Dependency Modules
#process.mygsfElectronCores=RecoEgamma.EgammaElectronProducers.gsfElectronCores_cfi.gsfElectronCores.clone()
###################################################################################
#### 							  ##########################
####	CLONING  & CHANGING PROCESSES			  ##########################
####							  ##########################	
####################################################################################

from RecoEgamma.EgammaElectronProducers.ecalDrivenElectronSeedsParameters_cff import *
from RecoEgamma.EgammaElectronProducers.ecalDrivenElectronSeeds_cfi import *
process.uncleanedOnlyElectronSeeds = ecalDrivenElectronSeeds.clone()
process.uncleanedOnlyElectronSeeds.arrelSuperClusters = cms.InputTag("uncleanedOnlyCorrectedHybridSuperClusters")
process.uncleanedOnlyElectronSeeds.endcapSuperClusters = cms.InputTag("uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower")
#process.uncleanedOnlyElectronSeeds.barrelSuperClusters = cms.InputTag("CorrectedHybridSuperClusters")
#process.uncleanedOnlyElectronSeeds.endcapSuperClusters = cms.InputTag("CorrectedMulti5x5SuperClustersWithPreshower")
#process.uncleanedOnlyElectronSeeds.barrelSuperClusters = cms.InputTag("uncleanSCRecovered:uncleanHybridSuperClusters")
#process.uncleanedOnlyElectronSeeds.barrelSuperClusters = cms.InputTag("uncleanHybridSuperClusters")
#process.uncleanedOnlyElectronSeeds.endcapSuperClusters = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower")      ## As with Photons
    

#### make gsfElectrons from rechits ################
#electronSeeds = cms.Sequence(ecalDrivenElectronSeeds)
#electronSeeds = cms.Sequence(uncleanedOnlyElectronSeeds)
#electronCkfTrackCandidates.src = cms.InputTag('electronSeeds')
#from TrackingTools.GsfTracking.CkfElectronCandidateMaker_cff import *
#electronCkfTrackCandidates = electronCkfTrackCandidates.clone(
#    src = cms.InputTag("electronSeeds")
#    ) 
#process.p = cms.Path(process.siPixelRecHits*process.siStripMatchedRecHits*process.iterTracking*process.newSeedFromPairs*process.newSeedFromTriplets*process.newCombinedSeeds*process.ecalClusters*process.gsfElectronSequence)


### Tracks Making ####
from TrackingTools.GsfTracking.CkfElectronCandidateMaker_cff import *
process.uncleanedOnlyElectronCkfTrackCandidates = electronCkfTrackCandidates.clone()
process.uncleanedOnlyElectronCkfTrackCandidates.src = cms.InputTag("uncleanedOnlyElectronSeeds")

### Track Fitting ####
from TrackingTools.GsfTracking.GsfElectronGsfFit_cff import *
process.uncleanedOnlyElectronGsfTracks = electronGsfTracks.clone()
process.uncleanedOnlyElectronGsfTracks.src = cms.InputTag('uncleanedOnlyElectronCkfTrackCandidates')

###
### Building Unclean tracks from seeds ###
###
process.uncleanedOnlyTracking=cms.Sequence(process.uncleanedOnlyElectronSeeds*process.uncleanedOnlyElectronCkfTrackCandidates*process.uncleanedOnlyElectronGsfTracks)

#
# Conversions
#

### Conversion Track Candidates ####
from RecoEgamma.EgammaPhotonProducers.conversionTrackCandidates_cfi import *
process.uncleanedOnlyConversionTrackCandidates = conversionTrackCandidates.clone()
#process.uncleanedOnlyConversionTrackCandidates.scHybridBarrelProducer = cms.InputTag("uncleanSCRecovered:uncleanHybridSuperClusters")   ## same as photons#
process.uncleanedOnlyConversionTrackCandidates.scHybridBarrelProducer = cms.InputTag("uncleanedOnlyCorrectedHybridSuperClusters")
process.uncleanedOnlyConversionTrackCandidates.bcBarrelCollection  = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridSuperClusters")
process.uncleanedOnlyConversionTrackCandidates.scIslandEndcapProducer  = cms.InputTag("uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower")
process.uncleanedOnlyConversionTrackCandidates.bcEndcapCollection  = cms.InputTag("multi5x5SuperClusters","uncleanOnlyMulti5x5EndcapBasicClusters")
 
### Tracks From Conversion ####
from RecoEgamma.EgammaPhotonProducers.ckfOutInTracksFromConversions_cfi import *
process.uncleanedOnlyCkfOutInTracksFromConversions = ckfOutInTracksFromConversions.clone()
process.uncleanedOnlyCkfOutInTracksFromConversions.src = cms.InputTag("uncleanedOnlyConversionTrackCandidates","outInTracksFromConversions")
process.uncleanedOnlyCkfOutInTracksFromConversions.producer = cms.string('uncleanedOnlyConversionTrackCandidates')
process.uncleanedOnlyCkfOutInTracksFromConversions.ComponentName = cms.string('uncleanedOnlyCkfOutInTracksFromConversions')

from RecoEgamma.EgammaPhotonProducers.ckfInOutTracksFromConversions_cfi import *
process.uncleanedOnlyCkfInOutTracksFromConversions = ckfInOutTracksFromConversions.clone()
process.uncleanedOnlyCkfInOutTracksFromConversions.src = cms.InputTag("uncleanedOnlyConversionTrackCandidates","inOutTracksFromConversions")
process.uncleanedOnlyCkfInOutTracksFromConversions.producer = cms.string('uncleanedOnlyConversionTrackCandidates')
process.uncleanedOnlyCkfInOutTracksFromConversions.ComponentName = cms.string('uncleanedOnlyCkfInOutTracksFromConversions')
    
###
### Process Reco Tracks From Conversion ##################################
###
process.uncleanedOnlyCkfTracksFromConversions = cms.Sequence(process.uncleanedOnlyConversionTrackCandidates*process.uncleanedOnlyCkfOutInTracksFromConversions*process.uncleanedOnlyCkfInOutTracksFromConversions)
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyGeneralConversionTrackProducer = generalConversionTrackProducer.clone()

from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyInOutConversionTrackProducer = inOutConversionTrackProducer.clone()
process.uncleanedOnlyInOutConversionTrackProducer.TrackProducer = cms.string('uncleanedOnlyCkfInOutTracksFromConversions')
    

from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyOutInConversionTrackProducer = outInConversionTrackProducer.clone()
process.uncleanedOnlyOutInConversionTrackProducer .TrackProducer = cms.string('uncleanedOnlyCkfOutInTracksFromConversions')

from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyGsfConversionTrackProducer = gsfConversionTrackProducer.clone()
process.uncleanedOnlyGsfConversionTrackProducer.TrackProducer = cms.string('uncleanedOnlyElectronGsfTracks')

###
### Process Unclean Conversion Tracks ####################################
###
process.uncleanedOnlyConversionTrackProducers  = cms.Sequence(process.uncleanedOnlyGeneralConversionTrackProducer*process.uncleanedOnlyInOutConversionTrackProducer*process.uncleanedOnlyOutInConversionTrackProducer*process.uncleanedOnlyGsfConversionTrackProducer)
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

### Merge Uncleaned Conversion Tracks ############################
from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyInOutOutInConversionTrackMerger = inOutOutInConversionTrackMerger.clone()
process.uncleanedOnlyInOutOutInConversionTrackMerger.TrackProducer2 = cms.string('uncleanedOnlyOutInConversionTrackProducer')
process.uncleanedOnlyInOutOutInConversionTrackMerger.TrackProducer1 = cms.string('uncleanedOnlyInOutConversionTrackProducer')


from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyGeneralInOutOutInConversionTrackMerger = generalInOutOutInConversionTrackMerger.clone()
process.uncleanedOnlyGeneralInOutOutInConversionTrackMerger.TrackProducer2 = cms.string('uncleanedOnlyGeneralConversionTrackProducer')
process.uncleanedOnlyGeneralInOutOutInConversionTrackMerger.TrackProducer1 = cms.string('uncleanedOnlyInOutOutInConversionTrackMerger')


from RecoEgamma.EgammaPhotonProducers.conversionTrackSequence_cff import *
process.uncleanedOnlyGsfGeneralInOutOutInConversionTrackMerger = gsfGeneralInOutOutInConversionTrackMerger.clone()
process.uncleanedOnlyGsfGeneralInOutOutInConversionTrackMerger.TrackProducer2 = cms.string('uncleanedOnlyGsfConversionTrackProducer')
process.uncleanedOnlyGsfGeneralInOutOutInConversionTrackMerger.TrackProducer1 = cms.string('uncleanedOnlyGeneralInOutOutInConversionTrackMerger')
 
####
#### Process Merging of conversion Tracks #################################
####
process.uncleanedOnlyConversionTrackMergers = cms.Sequence(process.uncleanedOnlyInOutOutInConversionTrackMerger*process.uncleanedOnlyGeneralInOutOutInConversionTrackMerger*process.uncleanedOnlyGsfGeneralInOutOutInConversionTrackMerger)
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

### All Uncleaned Conversions #############################################
from RecoEgamma.EgammaPhotonProducers.allConversions_cfi import *
process.uncleanedOnlyAllConversions = allConversions.clone()
process.uncleanedOnlyAllConversions.scBarrelProducer = cms.InputTag("uncleanedOnlyCorrectedHybridSuperClusters")
#process.uncleanedOnlyAllConversions.scBarrelProducer = cms.InputTag("uncleanSCRecovered:uncleanHybridSuperClusters")
process.uncleanedOnlyAllConversions.bcBarrelCollection  = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridSuperClusters")
process.uncleanedOnlyAllConversions.scEndcapProducer = cms.InputTag("uncleanedOnlyCorrectedMulti5x5SuperClustersWithPreshower")
process.uncleanedOnlyAllConversions.bcEndcapCollection = cms.InputTag("multi5x5SuperClusters","uncleanOnlyMulti5x5EndcapBasicClusters")
process.uncleanedOnlyAllConversions.src = cms.InputTag("uncleanedOnlyGsfGeneralInOutOutInConversionTrackMerger")
    
###
###  Process Recover All Conversions #########################################################
###
process.uncleanedOnlyConversions = cms.Sequence(process.uncleanedOnlyCkfTracksFromConversions*process.uncleanedOnlyConversionTrackProducers*process.uncleanedOnlyConversionTrackMergers*process.uncleanedOnlyAllConversions)
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

##
## Particle Flow Tracking
##
from RecoParticleFlow.PFTracking.pfTrack_cfi import *
process.uncleanedOnlyPfTrack = pfTrack.clone()
process.uncleanedOnlyPfTrack.GsfTrackModuleLabel = cms.InputTag("uncleanedOnlyElectronGsfTracks")

from RecoParticleFlow.PFTracking.pfConversions_cfi import *
process.uncleanedOnlyPfConversions = pfConversions.clone()
process.uncleanedOnlyPfConversions .conversionCollection = cms.InputTag("allConversions")

from RecoParticleFlow.PFTracking.pfTrackElec_cfi import *
process.uncleanedOnlyPfTrackElec = pfTrackElec.clone()
process.uncleanedOnlyPfTrackElec .PFConversions = cms.InputTag("uncleanedOnlyPfConversions")
process.uncleanedOnlyPfTrackElec .GsfTrackModuleLabel = cms.InputTag("uncleanedOnlyElectronGsfTracks")
process.uncleanedOnlyPfTrackElec .PFRecTrackLabel = cms.InputTag("uncleanedOnlyPfTrack")

####
#### Recovering Uncleaned PF track ############################################################
process.uncleanedOnlyPfTracking = cms.Sequence(process.uncleanedOnlyPfTrack*process.uncleanedOnlyPfConversions*process.uncleanedOnlyPfTrackElec)
####@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

##
## Electrons
##
##
## Electrons from GsfElectronCore && GsfElectron #########
##

###### New GsfElectronCore to be used by GsfElectrons
from RecoEgamma.EgammaElectronProducers.gsfElectronCores_cfi import *
process.uncleanedOnlyGsfElectronCores=RecoEgamma.EgammaElectronProducers.gsfElectronCores_cfi.ecalDrivenGsfElectronCores.clone()
process.uncleanedOnlyGsfElectronCores.gsfTracks = cms.InputTag("uncleanedOnlyElectronGsfTracks")
process.uncleanedOnlyGsfElectronCores.gsfPfRecTracks = cms.InputTag("uncleanedOnlyPfTrackElec")

#### clone ecaldrivenGsfelectrons b/c gsfElecrton uses it! 
from RecoEgamma.EgammaElectronProducers.gsfElectrons_cfi import *
process.uncleanedOnlyGsfElectrons=RecoEgamma.EgammaElectronProducers.gsfElectrons_cfi.ecalDrivenGsfElectrons.clone()
process.uncleanedOnlyGsfElectrons.gsfElectronCoresTag = cms.InputTag("uncleanedOnlyGsfElectronCores")
#process.uncleanedOnlyGsfElectrons.barrelRecHitCollectionTag = cms.InputTag("reducedEcalRecHitsEB")
#process.uncleanedOnlyGsfElectrons.endcapRecHitCollectionTag = cms.InputTag("reducedEcalRecHitsEE")
process.uncleanedOnlyGsfElectrons.barrelRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEB")
process.uncleanedOnlyGsfElectrons.endcapRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEE")
process.uncleanedOnlyGsfElectrons.seedsTag = cms.InputTag("uncleanedOnlyElectronSeeds")
process.uncleanedOnlyGsfElectrons.gsfPfRecTracksTag = cms.InputTag("uncleanedOnlyPfTrackElec")
process.uncleanedOnlyGsfElectrons.ctfTracksTag = cms.InputTag("generalTracks")

#### Now do My own GsfElectron
from RecoEgamma.EgammaElectronProducers.gsfElectrons_cfi import *
process.mygsfElectrons=RecoEgamma.EgammaElectronProducers.gsfElectrons_cfi.gsfElectrons.clone()
process.mygsfElectrons.previousGsfElectronsTag = cms.InputTag("uncleanedOnlyGsfElectrons")
process.mygsfElectrons.barrelRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEB")
process.mygsfElectrons.endcapRecHitCollectionTag = cms.InputTag("ecalRecHit","EcalRecHitsEE")
#process.mygsfElectrons.barrelRecHitCollectionTag = cms.InputTag("reducedEcalRecHitsEB")
#process.mygsfElectrons.endcapRecHitCollectionTag = cms.InputTag("reducedEcalRecHitsEE")
process.mygsfElectrons.seedsTag = cms.InputTag("uncleanedOnlyElectronSeeds")
process.mygsfElectrons.gsfPfRecTracksTag = cms.InputTag("uncleanedOnlyPfTrackElec")
process.mygsfElectrons.gsfElectronCoresTag = cms.InputTag("uncleanedOnlyGsfElectronCores")


####The unleaned Electron process ###############

#uncleanedOnlyElectrons = cms.Sequence( process.uncleanSCRecovered*uncleanedOnlyGsfElectronCores*mygsfElectrons)
process.uncleanedOnlyElectrons = cms.Sequence(process.uncleanedOnlyGsfElectronCores*process.uncleanedOnlyGsfElectrons)
#uncleanedOnlyElectrons = cms.Sequence(uncleanedOnlyGsfElectronCores*mygsfElectrons
#uncleanedOnlyElectrons = cms.Sequence(gsfElectronCores*gsfElectrons)
#uncleangsfElectronSequence = cms.Sequence(uncleanedOnlyGsfElectronCores*mygsfElectrons)


#########################################################################################
#######										#########
####### 			Whole Sequence         				#########
#######										#########
#########################################################################################
from RecoEgamma.EgammaElectronProducers.uncleanedOnlyElectronSequence_cff import *

process.uncleanedOnlyElectronSequence = cms.Sequence(process.uncleanedOnlyTracking*process.uncleanedOnlyConversions*process.uncleanedOnlyPfTracking*process.uncleanedOnlyElectrons)



######
######	PatElectron Begins!!
######
# pat needed to work out electron id/iso
from PhysicsTools.PatAlgos.tools.metTools import *
from PhysicsTools.PatAlgos.tools.tauTools import *
from PhysicsTools.PatAlgos.tools.jetTools import *
from PhysicsTools.PatAlgos.tools.coreTools import *
from PhysicsTools.PatAlgos.tools.pfTools import *
from PhysicsTools.PatAlgos.selectionLayer1.leptonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.photonCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.electronCountFilter_cfi import *
from PhysicsTools.PatAlgos.selectionLayer1.jetCountFilter_cfi import *

# Global Tag
process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_cff")
#process.load("Configuration.StandardSequences.FrontierConditions_GlobalTag_noesprefer_cff")

from Configuration.AlCa.GlobalTag import GlobalTag
#process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V18::All' )
process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V20::All' )
# tag below tested in CMSSW_4_3_0_pre3
#process.GlobalTag.globaltag = 'GR_R_42_V14::All'

# this is for jan16 reprocessing - tested in CMSSW_4_3_0_pre3
#process.GlobalTag.globaltag = 'FT_R_42_V24::All'

process.load('Configuration.StandardSequences.MagneticField_38T_cff')


# Trigger
process.load("L1TriggerConfig.L1ScalesProducers.L1MuTriggerScalesConfig_cff")
process.load("L1TriggerConfig.L1ScalesProducers.L1MuTriggerPtScaleConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtBoardMapsConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.L1GtConfig_cff")
process.load("L1TriggerConfig.L1GtConfigProducers.Luminosity.startup.L1Menu_startup2_v2_Unprescaled_cff")
import FWCore.Modules.printContent_cfi
process.dumpEv = FWCore.Modules.printContent_cfi.printContent.clone()

import EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi
process.gtDigis = EventFilter.L1GlobalTriggerRawToDigi.l1GtUnpack_cfi.l1GtUnpack.clone()


process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')	
)

########## NOW  DO PAT ################################################
##########             ################################################
#########Load PAT sequences
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.load("PhysicsTools.PatAlgos.tools.pfTools")
## THis is NOT MC => remove matching
removeMCMatching(process, ['All'])
## bugfix for DATA Run2011 (begin)
removeSpecificPATObjects( process, ['Taus'] )
process.patDefaultSequence.remove( process.patTaus )
process.patElectrons.isoDeposits = cms.PSet()
process.patElectrons.addElectronID = cms.bool(True)
process.patElectrons.electronIDSources = cms.PSet(
            simpleEleId95relIso= cms.InputTag("simpleEleId95relIso"),
            simpleEleId90relIso= cms.InputTag("simpleEleId90relIso"),
            simpleEleId85relIso= cms.InputTag("simpleEleId85relIso"),
            simpleEleId80relIso= cms.InputTag("simpleEleId80relIso"),
            simpleEleId70relIso= cms.InputTag("simpleEleId70relIso"),
            simpleEleId60relIso= cms.InputTag("simpleEleId60relIso"),
            simpleEleId95cIso= cms.InputTag("simpleEleId95cIso"),
            simpleEleId90cIso= cms.InputTag("simpleEleId90cIso"),
            simpleEleId85cIso= cms.InputTag("simpleEleId85cIso"),
            simpleEleId80cIso= cms.InputTag("simpleEleId80cIso"),
            simpleEleId70cIso= cms.InputTag("simpleEleId70cIso"),
            simpleEleId60cIso= cms.InputTag("simpleEleId60cIso"),
            )
###
process.load("ElectroWeakAnalysis.WENu.simpleEleIdSequence_cff")

########## The Electron ID sequence #############################
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)

#### Make Pat Electrons Begining with Unlcean gsfCores #####################################
# Make my own patElectron ##################
#process.UncleanedpatElectrons=PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi.patElectrons.clone()
from PhysicsTools.PatAlgos.producersLayer1.electronProducer_cfi import *
process.UncleanedpatElectrons=patElectrons.clone()
#process.UncleanedpatElectrons.electronSource=cms.InputTag("gsfElectrons")
process.UncleanedpatElectrons.electronSource=cms.InputTag("uncleanedOnlyGsfElectrons")

process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.UncleanedpatElectrons)

#process.makePatElectrons = cms.Sequence(process.patElectronIDs*process.patElectrons)
process.makePatCandidates = cms.Sequence(process.makePatElectrons)
process.patMyDefaultSequence = cms.Sequence(process.makePatCandidates)



# this is the ntuple producer
process.load("CalibCalorimetry.EcalTiming.ecalTimeEleTree_cfi")
process.ecalTimeEleTree.OutfileName = 'EcalTimeTree'
process.ecalTimeEleTree.muonCollection = cms.InputTag("muons")
process.ecalTimeEleTree.runNum = 999999
#process.ecalTimeTree.endcapSuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower","")



process.dumpEvContent = cms.EDAnalyzer("EventContentAnalyzer")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.p = cms.Path(
    process.patMyDefaultSequence *
    # process.dumpEvContent  *
    process.ecalTimeEleTree
    )

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 250

# dbs search --query "find file where dataset=/ExpressPhysics/BeamCommissioning09-Express-v2/FEVT and run=124020" | grep store | awk '{printf "\"%s\",\n", $1}'
process.source = cms.Source("PoolSource",
    skipEvents = cms.untracked.uint32(0),
    fileNames = filelist,
    #fileNames = cms.untracked.vstring('file:input.root')
    #'/store/data/Commissioning10/MinimumBias/RAW-RECO/v9/000/135/494/A4C5C9FA-C462-DF11-BC35-003048D45F7A.root',
    #'/store/relval/CMSSW_4_2_0_pre8/EG/RECO/GR_R_42_V7_RelVal_wzEG2010A-v1/0043/069662C9-9A56-E011-9741-0018F3D096D2.root'
    #'/store/data/Run2010A/EG/RECO/v4/000/144/114/EEC21BFA-25B4-DF11-840A-001617DBD5AC.root'

   # 'file:/data/franzoni/data/Run2011A_DoubleElectron_AOD_PromptReco-v4_000_166_946_CE9FBCFF-4B98-E011-A6C3-003048F11C58.root'
   # 'file:/hdfs/cms/phedex/store/data/Run2012C/SinglePhoton/RECO/EXODisplacedPhoton-PromptSkim-v3/000/198/941/00000/0EA7C91A-B8CF-E111-9766-002481E150EA.root'

 #   )
    
 )

