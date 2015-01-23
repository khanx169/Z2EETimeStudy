import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC20B4D3-3E75-E211-B460-0026189437FC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC35C3CE-E167-E211-9EAC-00261894394D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC3D3759-1970-E211-BBCB-002618FDA277.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC5AA558-DD67-E211-A93A-0026189438A5.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC7DA96F-E567-E211-A157-003048FFD744.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC8384DF-DF67-E211-A2B0-002618943951.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC861C80-E067-E211-89BC-003048678A78.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EC99D9F5-1970-E211-BFF2-003048678AFA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/ECB3FA3B-DD67-E211-A515-0030486792B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/ECBB50A7-E667-E211-B42A-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/ECCBD794-1870-E211-863B-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE0A3875-E567-E211-B759-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE4FEFDA-3E75-E211-8E2E-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE5A5B7B-E467-E211-B3DB-00261894382A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE689A42-DF67-E211-90D4-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE734317-DE67-E211-A4D4-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE7952CC-E167-E211-9AB3-003048678B04.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EE7E044C-1670-E211-B4E1-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EEB123D5-E367-E211-AD06-00261894394A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EEBE7189-E367-E211-8614-002354EF3BE6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EEBF85E3-1670-E211-860D-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EED5F5BB-3F75-E211-BCDF-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F003668B-E267-E211-81F3-0026189438E4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F015FF9A-E667-E211-9945-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F0253580-E367-E211-8D76-003048678FB4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F028AE83-E167-E211-91B9-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F02AB6C1-DF67-E211-86C5-002618943885.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F02DBE35-3F75-E211-9CAA-0026189438F6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F05DB419-1770-E211-9027-0026189438D2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F0876241-E367-E211-9191-003048FFCB74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F08BAF3F-DF67-E211-9F91-002618943963.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F0988D35-E567-E211-B3D1-002618FDA28E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F0DCCE47-E467-E211-BA02-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F0F6E081-E267-E211-AE7C-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F2039F08-4075-E211-96F6-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F2130C00-DE67-E211-BD18-002618943963.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F2232CC7-E167-E211-9923-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F23617B7-E467-E211-97E0-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F28091F9-3E75-E211-BEB3-00261894394A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F28A4A67-E467-E211-8469-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F28E6A72-E767-E211-B905-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F29169CE-E367-E211-A12C-0030486790C0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F2924D77-3E75-E211-8254-0026189438E2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F2C265E3-3E75-E211-A61A-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F2E0E2DF-E667-E211-8291-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F405381E-E167-E211-B271-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F4104253-E767-E211-9131-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F419186E-3F75-E211-89B1-0026189438E2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F41D9F5E-E567-E211-9BDF-00248C0BE01E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F43961DC-E367-E211-A6DD-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F47F5010-DF67-E211-A573-002618943971.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F4865DE5-E667-E211-BE9E-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F49F5A8C-1770-E211-9BC8-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F4A34B32-DF67-E211-A688-00304867BFC6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6202C11-E267-E211-91C3-002618943940.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F62E0D0A-E667-E211-8AE3-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F658644B-3E75-E211-8EA0-00261894396A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F68B9793-DE67-E211-9B58-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F690F263-E567-E211-8BD7-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6A4CCC2-E367-E211-9DBB-0026189438A7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6B16658-3F75-E211-BD7F-003048FF9AA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6CE4F86-AA67-E211-ADAA-002618943947.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6CF42D1-B167-E211-B8C8-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6CFB77D-1970-E211-85F8-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6F37119-1870-E211-ABE5-0026189437FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F6F4EEE0-DF67-E211-B6E9-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8118835-E267-E211-A58D-00261894386E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F860AE85-E567-E211-82B5-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8869E99-B167-E211-8851-00304866C398.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F88CD90E-E267-E211-81C8-003048679012.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8992893-DE67-E211-942C-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8A05696-3970-E211-AA0D-002354EF3BDC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8A32768-E767-E211-AE68-003048D15E24.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8B01E39-E567-E211-BBB8-003048678ADA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/F8D9432F-DD67-E211-929B-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FA2E14C7-E667-E211-B7D3-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FA3B704E-DD67-E211-8F59-003048678E8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FA3F4B96-E367-E211-9BA3-00304867924E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FA7380BE-DE67-E211-9907-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FA762532-E167-E211-8C80-00261894380B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FA76B429-E267-E211-9986-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FAC67CE8-E767-E211-B88A-003048678BAC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC067CF6-E367-E211-942B-003048679228.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC07AECF-E167-E211-B9F2-0026189438BD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC1F0485-E167-E211-8F1B-003048678B00.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC32B2DB-DD67-E211-A809-002618943810.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC4298E6-E167-E211-A704-003048678B38.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC5984BB-E667-E211-90E4-003048FFD736.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FC9109AB-E467-E211-9E57-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FCB37412-E667-E211-9219-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FCBFA8D4-E367-E211-A8D0-002618943939.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FCDA167B-DC67-E211-B0BF-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FCDCEDE7-1570-E211-8C94-0026189437FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FCFD4DA1-3F70-E211-9298-003048679182.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE0BCC66-E067-E211-8FD7-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE180666-E567-E211-8A43-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE57DACD-E267-E211-BF01-00261894398C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE5C526E-E367-E211-B81D-002618943960.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE6EC6AD-E667-E211-B3F2-0026189438DF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE7DE3D6-E167-E211-B758-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FE9D7536-DF67-E211-9F7A-003048FFD76E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FEA7562B-E667-E211-9E8A-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FEADD361-1570-E211-B6B0-003048FFD728.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FEAF3171-E567-E211-9B54-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/FEB0AD23-E367-E211-93E5-0025905938A8.root',

])

# Output - dummy
process.out = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    fileName = cms.untracked.string('file:EcalTiming_Run2012C.root'),
    )

import FWCore.PythonUtilities.LumiList as LumiList
import FWCore.ParameterSet.Types as CfgTypes
import FWCore.ParameterSet.Config as cms
# setup process
process = cms.Process("FWLitePlots")
process.inputs = cms.PSet (
    lumisToProcess = CfgTypes.untracked(CfgTypes.VLuminosityBlockRange())
)
# get JSON file correctly parced
JSONfile ='Cert_190456-208686_8TeV_22Jan2013ReReco_Collisions12_JSON.txt'
myList = LumiList.LumiList (filename = JSONfile).getCMSSWString().split(',')
process.inputs.lumisToProcess.extend(myList)

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

#process.load('Configuration.StandardSequences.MagneticField_38T_cff')
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


#####                       ########
#####  DO UNCLEANED PHOTONS ########
#####                       ########

# Specify IdealMagneticField ESSource
process.load("MagneticField.Engine.uniformMagneticField_cfi")
process.load("Geometry.CSCGeometryBuilder.cscGeometry_cfi")
process.CaloTowerConstituentsMapBuilder = cms.ESProducer("CaloTowerConstituentsMapBuilder")
process.load("RecoEcal.EgammaClusterProducers.uncleanSCRecovery_cfi")
process.uncleanSCRecovered.cleanScCollection=cms.InputTag ("correctedHybridSuperClusters")
# myPhoton sequence
process.load("RecoEgamma.PhotonIdentification.photonId_cff")
process.load("RecoLocalCalo.EcalRecAlgos.EcalSeverityLevelESProducer_cfi")
#process.ecalSeverityLevel.timeThresh = cms.double(2.0)
import RecoEgamma.EgammaPhotonProducers.photonCore_cfi
import RecoEgamma.EgammaPhotonProducers.photons_cfi
process.myphotonCores=RecoEgamma.EgammaPhotonProducers.photonCore_cfi.photonCore.clone()
process.myphotonCores.scHybridBarrelProducer=cms.InputTag ("uncleanSCRecovered:uncleanHybridSuperClusters")
from RecoEgamma.PhotonIdentification.isolationCalculator_cfi import*
newisolationSumsCalculator = isolationSumsCalculator.clone()
newisolationSumsCalculator.barrelEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEB')
newisolationSumsCalculator.endcapEcalRecHitCollection = cms.InputTag('reducedEcalRecHitsEE')
process.myphotons=RecoEgamma.EgammaPhotonProducers.photons_cfi.photons.clone()
process.myphotons.barrelEcalHits=cms.InputTag("reducedEcalRecHitsEB")
process.myphotons.endcapEcalHits=cms.InputTag("reducedEcalRecHitsEE")
process.myphotons.isolationSumsCalculatorSet=newisolationSumsCalculator
process.myphotons.runMIPTagger = cms.bool(False)
process.myphotons.photonCoreProducer=cms.InputTag("myphotonCores")
process.myPhotonSequence = cms.Sequence(process.myphotonCores+
                                         process.myphotons)
# photonID sequence
from RecoEgamma.PhotonIdentification.photonId_cfi import *
process.myPhotonIDSequence = cms.Sequence(PhotonIDProd)
process.PhotonIDProd.DoEcalRecHitIsolationCut = cms.bool(False)
process.PhotonIDProd.doCutBased = cms.bool(False)
process.PhotonIDProd.photonProducer=cms.string("myphotons")
process.uncleanPhotons = cms.Sequence(
                                       process.uncleanSCRecovered *process.myPhotonSequence *process.myPhotonIDSequence
	                             )


## Skip unfound Products!
process.options = cms.untracked.PSet(
SkipEvent = cms.untracked.vstring('ProductNotFound')	
)

# this is the ntuple producer
process.load("CalibCalorimetry.EcalTiming.ecalTimeEleTree_cfi")
process.ecalTimeEleTree.OutfileName = 'EcalTimeTree'
process.ecalTimeEleTree.muonCollection = cms.InputTag("muons")
process.ecalTimeEleTree.runNum = 999999110
process.ecalTimeEleTree.gsfElectrons = cms.InputTag("gsfElectrons","")
process.ecalTimeEleTree.photonSource = cms.InputTag("myphotons","")

#process.ecalTimeEleTree.gsfElectrons = cms.InputTag("uncleanedOnlyGsfElectrons","")
#process.ecalTimeTree.endcapSuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower","")
##vector<reco::SuperCluster>            "hybridSuperClusters"       "uncleanOnlyHybridSuperClusters"   "RECO")
#vector<reco::CaloCluster>             "hybridSuperClusters"       "uncleanOnlyHybridBarrelBasicClusters"   "RECO"

#process.ecalTimeEleTree.barrelSuperClusterCollection = cms.InputTag("correctedHybridSuperClusters","")

#process.ecalTimeEleTree.barrelSuperClusterCollection = cms.InputTag("hybridSuperClusters","uncleanOnlyHybridSuperClusters","")
#process.ecalTimeEleTree.endcapSuperClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower","")
#process.ecalTimeEleTree.barrelBasicClusterCollection = cms.InputTag('hybridSuperClusters','uncleanOnlyHybridBarrelBasicClusters')
#process.ecalTimeEleTree.endcapBasicClusterCollection = cms.InputTag("correctedMulti5x5SuperClustersWithPreshower","")

process.dumpEvContent = cms.EDAnalyzer("EventContentAnalyzer")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))


## Define Process path
process.p = cms.Path(
    #process.patMyDefaultSequence *
   # process.dumpEvContent  *
    process.uncleanPhotons*
    process.ecalTimeEleTree
    )
process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery =250

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

