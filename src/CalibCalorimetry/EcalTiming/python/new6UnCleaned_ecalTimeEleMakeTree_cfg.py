import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([

'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E60CEE4-DD67-E211-A403-003048FF9AA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E64B2FB-E367-E211-887A-0026189438E9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E7CDB43-DD67-E211-BDF2-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0EB539D7-DF67-E211-8998-003048678BAC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0EC0EFE8-DF67-E211-A3DB-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0EC1542B-3E75-E211-8796-002618943901.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0ECA27A5-1570-E211-A3A4-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0EE597EC-E167-E211-9E12-0026189438DB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0EF73A6A-E167-E211-A162-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10398C16-E167-E211-91BB-003048679236.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1045B379-DC67-E211-B879-00304867D446.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/104AE736-E167-E211-BCA3-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10555B24-3F75-E211-8B2C-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10706DB8-E067-E211-A03C-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1072B0DC-E567-E211-9C4B-002618943966.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/108D582F-DF67-E211-9C32-002618943860.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10D0BD0F-DE67-E211-94FB-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10D6506F-E567-E211-8CEF-00261894389D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10E61380-E367-E211-AD54-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/10E9BBBD-E667-E211-A42A-002618943946.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12096E39-1670-E211-AE98-00248C55CC97.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/120E9B0B-E867-E211-8226-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1239241F-E467-E211-8238-00261894396A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/123B2969-3F75-E211-B0AE-002618943964.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12412145-E167-E211-9057-003048678BF4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1249067A-E767-E211-AF60-003048679244.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/126A7B48-3E75-E211-9E29-003048679236.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1295207D-DD67-E211-96D6-00261894398D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12AEDC0F-1870-E211-ABC7-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12B5DC1C-E467-E211-B870-002618943910.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12C2574C-1570-E211-9D90-00248C55CC9D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12D342B6-DF67-E211-A941-0026189438E7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12EBFB04-DE67-E211-8635-002618943948.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/12F7CA7E-E367-E211-AE9E-002618943882.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/143602B1-B167-E211-B99F-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1442F5DE-B167-E211-83EB-00304867D836.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/145BD54F-E367-E211-AFEA-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/14751F05-3F75-E211-912E-003048678E8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/149DD51B-E467-E211-9ACB-003048678F84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/149E0AF1-E267-E211-98CD-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/14B55D5E-3F75-E211-BF02-002618943979.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/14C87986-E167-E211-9EC5-003048FFD730.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/14D4DC33-3F75-E211-9EA9-00248C0BE014.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/14DE5573-1870-E211-BB9E-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/14F33E99-E367-E211-8EF1-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16096B75-E167-E211-A53B-00261894394B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/160F2EC2-DF67-E211-ADA3-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16121363-1770-E211-A3FD-003048FFD76E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/161AEA61-DD67-E211-8B4C-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16215A4E-E367-E211-B370-0026189438DF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/163F7588-B167-E211-930C-003048678AE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1648227A-E167-E211-9844-00261894386E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1691E617-E667-E211-AAB2-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16CC3F49-E467-E211-873F-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16CCAD3D-1A70-E211-997B-003048FFCC18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16E3262D-1870-E211-99E3-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16E94BDC-E667-E211-9504-002618943800.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/16F93ADC-E767-E211-AEB8-00304867904E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/182E3DF5-E567-E211-B659-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/183CE1EB-DD67-E211-BA79-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/185984B6-E467-E211-A25A-003048FFCC18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1878A6E5-E267-E211-AF73-002618943976.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/18DEE2F7-DD67-E211-9582-002618943926.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/18E5E6DA-E567-E211-BB16-003048679244.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/18EA0ED8-E367-E211-B445-003048679006.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A0575C9-E267-E211-8399-003048FFD736.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A18202A-E267-E211-A7F9-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A3A3A26-1570-E211-9788-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A41BDFD-E367-E211-91DF-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A42C010-E167-E211-9A33-0026189438B8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A8F9F4B-E367-E211-A6C0-0025905964C0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A93C6D4-3F75-E211-90DF-0026189438C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1A94A0E1-3E75-E211-AB83-002618943981.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1AA30F3A-1870-E211-A41F-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C0A2A01-E067-E211-984B-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C1082DC-E767-E211-A801-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C152362-E467-E211-B05A-00261894384A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C2D8950-1570-E211-A167-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C2E745B-E067-E211-ADE4-002618943860.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C3C7A9E-B167-E211-A40C-0026189437FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C459D5A-E267-E211-87B0-0026189438F3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C64618F-DE67-E211-9786-002618943807.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C847039-1670-E211-876B-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1C8E1146-DF67-E211-B411-002618943951.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1CC295A7-B167-E211-ABB4-003048678B92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1CD39A97-5C70-E211-9B3D-003048679296.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1CF88352-3E75-E211-97F5-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E0E9AC0-E167-E211-A5F2-00304867903E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E19CAD3-DE67-E211-B064-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E2E3F01-E667-E211-825D-00248C0BE01E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E4D563B-DF67-E211-B03B-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E811164-E067-E211-9AD6-0026189438D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E8312DF-DF67-E211-ADF3-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E8D2677-3F75-E211-9EE0-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E911838-E167-E211-A529-003048678F84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E979DBE-3F75-E211-98B7-00304867C1B0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1E982BE9-E367-E211-A000-003048678FF6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1EB43FCC-DF67-E211-9590-003048679236.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1EC4FD1F-E167-E211-8D43-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1EDB6F90-E267-E211-9433-002618943849.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1EE0C6C8-DF67-E211-8165-002354EF3BDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1EED19F8-E167-E211-BB85-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/1EF586B0-E167-E211-9BA7-00261894397D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/200409FA-E167-E211-B58C-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/203A8682-E767-E211-B301-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/203D6C98-1770-E211-8786-0026189438AC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2048FF56-DC67-E211-AB2D-00261894386F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2056BA22-E367-E211-B538-00304867916E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/20A3E142-E567-E211-B5E4-00261894394B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/20B2E0B7-DF67-E211-9736-003048678F8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/20B765D5-E267-E211-A044-003048678B14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/20D20992-4075-E211-B6E4-0026189438F4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/20F47E83-DE67-E211-A5F5-002618943948.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/22130B30-E467-E211-ACB7-00304867903E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/221A7BF6-1670-E211-BFC7-003048678F9C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/223419AC-B167-E211-83C1-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2273485A-1970-E211-A7D0-0030486791DC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/22921C85-E067-E211-A94C-00261894386E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/22932C67-E367-E211-8DDB-00304867903E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/22ADB15F-1670-E211-B57E-0025905938AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/22C29D64-AA67-E211-B736-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/22F013E3-E167-E211-BAD9-002354EF3BE3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/24298809-E467-E211-A31D-003048678FDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2431BE49-E367-E211-B777-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2489E493-E367-E211-92B4-00304867C1BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/248C4683-E467-E211-ADC8-002618943946.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/24907B96-DE67-E211-93ED-0026189438D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/24AFA1FD-E667-E211-BD5E-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/24CE95E6-1970-E211-8C9B-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/24FFDE59-E467-E211-B553-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2600799C-E667-E211-B57E-003048679244.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2600F377-E167-E211-93F7-00304867906C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26035007-E367-E211-9936-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/260ACE45-E367-E211-BD58-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/263C9BC8-5370-E211-938F-003048678FD6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26590097-3F75-E211-A5A4-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2688B611-E367-E211-B203-003048678FF6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26913EB4-E167-E211-83C1-00248C55CC7F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/269ED3AC-3E75-E211-82F3-00261894395C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26B4BC5D-DD67-E211-82DB-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26C341CF-E667-E211-8C71-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26D0DC82-E567-E211-8854-003048D15E02.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26D373C4-E167-E211-AC2B-0026189438DA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26E6F64B-E767-E211-9DD9-0026189438E4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26E9E040-DD67-E211-BFCC-002618943948.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26F3B4C9-DF67-E211-BE7C-00261894390C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/26F7F564-1570-E211-BFD7-002618943922.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2837D63A-1870-E211-913F-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/283992AE-DF67-E211-8819-002618943860.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/286D2D47-AA67-E211-B24F-0026189438AE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/287E7641-DD67-E211-B858-003048FFCBFC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2885318F-E167-E211-B16E-0026189438F5.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/28A91275-DD67-E211-8DA9-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/28B2DC79-3E75-E211-A4B1-003048679248.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/28FA9362-DC67-E211-B4E4-002618943829.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A01F37F-1770-E211-A133-0030486790A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A159317-1770-E211-882C-0026189438DB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A25137E-E767-E211-A49E-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A2914B1-E667-E211-B393-00248C0BE01E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A3A03F1-DD67-E211-BFC6-003048678F9C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A4D4BEC-E167-E211-B645-003048678BAA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A60608B-3F75-E211-A332-003048678B0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2A707C96-E367-E211-B7B6-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2ADDF973-E467-E211-A06A-002354EF3BE3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2AE5C88A-E267-E211-AB18-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2AFDCCFC-E567-E211-BDAF-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2C2CC37D-DE67-E211-8469-00261894392B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2C6998FA-E567-E211-9B08-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2C7D36C4-E267-E211-88C9-003048678CA2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2C803FF0-E167-E211-A90E-003048678C26.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CA723D5-3E75-E211-A3A4-002618943901.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CA92743-3E75-E211-9DEF-003048D15DDA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CB9A1FF-1570-E211-8DE2-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CBD0266-E467-E211-88CD-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CC74B09-DF67-E211-BDD3-0026189438CE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CD0FDF9-E767-E211-8E8A-00248C0BE01E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CD750FB-E167-E211-9FC1-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CDF9AAB-DF67-E211-8087-0026189438BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2CF9BF5B-DC67-E211-9511-002618943984.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2E126E32-DD67-E211-BC6C-002618943923.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2E15FD6F-E567-E211-A744-0026189438EB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2E1826F1-DD67-E211-A389-0026189438D9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2E668323-E267-E211-8C54-00304867924E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2E770897-E767-E211-966C-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2E7AD82F-1970-E211-AF65-003048678AFA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EA04D51-DD67-E211-BBEB-003048678F9C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EA52907-1670-E211-AD84-003048FFCC18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EAD1B8E-DE67-E211-9B3C-0030486790B8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EAF9F49-E367-E211-A3C7-00261894388D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2ED66E08-DE67-E211-95BF-002618943882.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2ED72269-DC67-E211-AA87-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EE2FC8F-E467-E211-BB97-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EEBA501-DF67-E211-AE1E-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/2EEC8990-B167-E211-8D63-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/300EC292-E467-E211-BC08-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30202669-3F75-E211-A512-00261894395C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30267A1F-1670-E211-BA34-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30357ADE-E167-E211-B9EE-00261894395F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30367E2D-E367-E211-9ED3-003048679228.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3037A091-DE67-E211-B509-002618943885.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3044A652-E767-E211-A690-0026189438D2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30685BB2-E067-E211-BA25-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/307F4456-1670-E211-B3FE-003048679182.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30B86C94-1770-E211-A13F-002618943982.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30C13C1A-E467-E211-A5FC-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/30F19168-E367-E211-9676-0030486792B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3207E41B-E467-E211-BDD0-003048FFD736.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3249FF8B-E467-E211-9CC7-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/325C489F-DE67-E211-91CE-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3260F2D5-E567-E211-9DDA-002618943899.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3273957A-E567-E211-A261-0026189438DF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/328B29E9-E367-E211-9BF4-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/32B2B52E-E167-E211-912E-00261894389F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/32BB1EFA-0C68-E211-ADE2-0030486792BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/32C2D5F1-E367-E211-B32C-002618943939.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/32C6E1AF-3F75-E211-9765-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/32CD865F-E267-E211-B47E-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/34046663-AD67-E211-8FEE-0026189438A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3411CDCE-E667-E211-8F27-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/34459653-1670-E211-87F8-0026189437EB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/345CD46D-1570-E211-98CE-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/34D50B07-1770-E211-9D81-0030486791DC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/34DD6064-E767-E211-868A-00261894389D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/34F2795F-DC67-E211-8D9B-003048678B34.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/34F2B5BB-DF67-E211-AFB1-003048678E2A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/361098CD-1870-E211-B2A3-0025905938A4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3626A9AC-B167-E211-B5E4-003048679182.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/363CBAC5-DF67-E211-85DF-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/363FDFB4-E667-E211-9DF2-00261894391B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/364D8A2D-E267-E211-AFF7-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/364EFB32-3F75-E211-9EC0-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36589865-AA67-E211-BB62-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3679A9D2-E267-E211-ADA3-003048678B00.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/367EAAA6-E067-E211-BEB7-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3699DD27-DF67-E211-BFC7-002354EF3BDB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36A3E151-E367-E211-8E3D-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36B73805-1770-E211-B09B-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36BA86DD-1570-E211-843B-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36CCE0C5-E267-E211-955A-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36CFC520-E667-E211-BB73-00261894389A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36D0A69B-3F75-E211-A3D4-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36D57D63-E067-E211-BE46-003048678BAC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36E6EEF7-3E75-E211-B5D1-00304867924A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/36FA9C19-E667-E211-8FDF-003048D15E24.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/380A38FC-1670-E211-93D5-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/380C2EFB-E167-E211-BE55-003048678BAA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/38116474-E267-E211-A715-00261894394A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/384C0B0A-E367-E211-96F0-003048678FDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3865D59E-B167-E211-86CD-002618943967.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/387FF8F0-E567-E211-ABCB-0026189438EB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/3883FF2B-E167-E211-9602-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/38BB6D0A-DF67-E211-B348-003048678BAA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/38CFB021-E467-E211-A59F-00261894397D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/38D26843-DF67-E211-A645-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/38F05765-E767-E211-8705-002618943970.root'

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
process.PhotonIDProd.photonProducer=cms.string("myphotons")
process.PhotonIDProd.DoEcalRecHitIsolationCut = cms.bool(False)
process.PhotonIDProd.doCutBased = cms.bool(False)
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
process.ecalTimeEleTree.runNum = 99999915
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

