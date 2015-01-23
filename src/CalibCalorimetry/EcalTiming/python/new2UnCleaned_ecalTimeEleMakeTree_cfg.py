import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/ECB75850-5EAC-E211-8889-002618943947.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/ECB88B49-5EAC-E211-B040-003048FFCB74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/ECFA862B-6CAC-E211-958F-002618943896.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE051963-5EAC-E211-9476-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE0B6399-69AC-E211-AE66-002354EF3BDA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE0B8887-56AC-E211-B99D-00261894384A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE31014A-6DAC-E211-AC9C-002618943964.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE70E22C-56AC-E211-AFBC-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE790D00-54AC-E211-B7AC-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE85573A-55AC-E211-9386-002618943866.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EE9CB004-6BAC-E211-BDFC-00261894392B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EEC4AC21-70AC-E211-AC73-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/EEDFC641-7AAC-E211-AAED-002618943916.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F00BB474-54AC-E211-8F6B-003048FFCBFC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F05BCADA-78AC-E211-8AEC-002354EF3BD2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F07BF77A-5EAC-E211-A2A2-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F09C7E73-5EAC-E211-A6D3-0026189438AF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F0C6142C-5EAC-E211-AA1E-00304867BED8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F0D3B28F-54AC-E211-B0EC-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F202C0F7-53AC-E211-8125-002618943975.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F2392169-5EAC-E211-A949-0026189438DD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F2A99960-74AC-E211-AA8F-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F42F09BB-5EAC-E211-B69E-0026189437F5.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F43B3BB7-56AC-E211-A0EE-002618943978.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F44E182D-55AC-E211-88E5-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F462D00D-58AC-E211-9976-002618943916.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F4AB7A22-5FAC-E211-B3E7-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F4D67E3F-5EAC-E211-89A0-003048678F62.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F64DD501-6DAC-E211-936F-003048679228.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F652C192-5EAC-E211-95A4-00248C55CC3C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F659B7CA-56AC-E211-95A6-0026189437FC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F679BCDC-56AC-E211-95DA-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F6BCCE48-5EAC-E211-A9FB-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F6F49940-5EAC-E211-8215-002618FDA204.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F8484A94-5EAC-E211-917D-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F85E84F5-57AC-E211-AA14-002354EF3BCE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F88FA805-57AC-E211-B255-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F8A06D4A-55AC-E211-BAAA-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/F8C35ABB-56AC-E211-93EA-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/FA4E13CA-57AC-E211-9487-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/FAA5D49A-69AC-E211-B60B-003048678B1A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/FAB8997E-6CAC-E211-BA2D-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/FC18E63C-55AC-E211-AF79-002618943981.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/FE95692A-6AAC-E211-B152-002618943983.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/FEB6E0E2-69AC-E211-82B3-0026189438F3.root',
#### DoubleEle Here!
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10000/142D7143-D88E-E211-8202-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10001/0041A9F0-D98E-E211-A07F-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10001/3680E9BA-DC8E-E211-910C-0026189438E6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10001/EACD3211-DC8E-E211-9A3D-002618943923.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10002/625E5A41-E08E-E211-8407-0030486791DC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10004/9C930C0E-ED8E-E211-8BE6-002618943810.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10004/C0E5958B-F28E-E211-BAC1-003048FFCC18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10006/02AC9186-438F-E211-8B2E-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10006/50EB78C2-FC8E-E211-B6FB-00261894393F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10006/DE8D61ED-F98E-E211-B8F3-00261894394B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10007/2EEF3DF3-428F-E211-AE68-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10007/4C5D032D-498F-E211-BDC4-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10008/1096B6BA-4C8F-E211-90CC-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10010/C2D1A350-548F-E211-8CCB-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10011/48F4B50D-5A8F-E211-A428-002618943940.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10011/70A6BE6E-5C8F-E211-BDA6-0026189438CB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10012/248D2644-618F-E211-B435-003048678AC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10014/3684DF31-B68F-E211-B686-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10014/EE6E9EEA-AF8F-E211-A6DC-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10015/8A4B2D2D-B68F-E211-BA3F-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10016/AA63BC96-BC8F-E211-BE96-002618943939.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10017/A6AD276D-BC8F-E211-AB45-002618943901.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10019/CC1F265B-C48F-E211-8BEF-00261894389C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10021/96AD8B02-D88F-E211-BDDA-002618943980.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10023/566E13C9-EA8F-E211-A062-00248C65A3EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10023/E870595D-E58F-E211-A154-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10025/4890740A-F88F-E211-8174-0026189438D3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10025/527D1CA4-F18F-E211-862D-00261894395A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10026/0EFCE1BE-FE8F-E211-8B6A-002618943986.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10027/D2800FCD-0B90-E211-9FE3-00261894393E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/22Jan2013-v1/10028/7027D147-1290-E211-917A-0026189437F9.root',

#DoubleEle_Run2012D-16Janv1
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/002FAA3A-B660-E211-BCF0-0025905938A4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0082B638-9F60-E211-B7B5-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0093AB27-E660-E211-B438-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/00A7B9D4-A360-E211-ADD3-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/00DDAE88-A160-E211-A4BB-003048679006.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/00E7E7FE-AB60-E211-9B8A-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/022A884A-CB60-E211-9277-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/02489CA7-B960-E211-9AF2-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0297FB81-9F60-E211-91B6-003048678B38.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/02A0A6F9-C860-E211-8C1F-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/02B53312-A060-E211-8738-003048678FA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/02C3909A-C560-E211-9126-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/02C8C2D1-9D60-E211-B629-003048678DD6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/040F0DEE-B160-E211-B9C8-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/041751F5-A460-E211-86A1-002618943975.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/042BD2F4-B560-E211-A3E8-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0459B31C-A260-E211-B2D9-00304867924A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/04740236-B060-E211-A4DB-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/04B9B096-B660-E211-AEAF-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/04BE3B87-9560-E211-9202-002618943925.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0620BECD-B860-E211-96CE-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/06223992-A960-E211-8788-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0645A1B7-A860-E211-9599-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0672215D-9260-E211-AF52-00248C0BE012.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0687DB9A-AD60-E211-9037-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0815C275-AC60-E211-BB15-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/083F38C6-A760-E211-8997-003048678BEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/08739789-C960-E211-A5F9-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/08E87B12-B560-E211-AE55-003048678ED2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0A117DAB-A460-E211-9326-002618943898.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0A391B59-9A60-E211-9D49-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0A3AD7AE-C860-E211-9FFA-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0AAF46C6-9F60-E211-9EC9-00304867901A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0AD157E6-AB60-E211-B27D-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0AEBE8EF-9C60-E211-8930-002618943821.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0AF62DC5-B860-E211-A781-00248C0BE005.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0C47845F-B160-E211-AE8A-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0C85375E-9E60-E211-99E2-00261894398A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0C9AAB2F-B260-E211-8BF9-003048679076.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0CBDF05A-CE60-E211-BE2B-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0E0AF9AC-CA60-E211-BCA7-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0E411BA8-B760-E211-BDC7-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0E4B5DB6-A860-E211-A82F-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0E6202CF-BA60-E211-8463-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0E679D14-B760-E211-9821-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/0EAA64D9-8D60-E211-9A74-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/10512337-9B60-E211-95A8-003048678FA0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/108ADA49-D460-E211-A802-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/10992218-9660-E211-92BB-003048678F78.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/10B9EF1C-A460-E211-813B-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/10BD8C45-A360-E211-A947-003048D15E02.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12149B84-9D60-E211-BB2A-00261894389D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1217F55C-B360-E211-844B-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1249593C-A760-E211-99A7-0026189438FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/125C1E16-B960-E211-805D-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12659D58-C160-E211-895B-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/129239CD-B060-E211-8CBB-002618943884.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12A145F5-A460-E211-A4EA-002618943924.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12A64E31-B060-E211-A99A-002618943870.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12C0AF87-9D60-E211-9D0A-003048678A7E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12DBDCC9-C260-E211-9E40-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/12E65B5C-9C60-E211-BE46-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1457EF88-B460-E211-8650-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1458EEAE-8E60-E211-91FB-003048678B84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1461E3FE-CC60-E211-BB85-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/146736AE-9C60-E211-970F-003048678FAE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/148C955E-A460-E211-9914-00248C0BE018.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/14A50CAD-CA60-E211-85DA-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/14CF42D3-A360-E211-ACF7-003048678B1A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/14D06DEB-A060-E211-92AF-003048678FA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/14DE648A-9D60-E211-9960-003048678F74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/14E34385-9B60-E211-9D52-003048678FA0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/16622B0D-BF60-E211-AD21-003048678F02.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/16A5453B-A760-E211-B174-002618943972.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/16EC44A6-B960-E211-87AF-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/16ED8E5F-9C60-E211-B4F7-002354EF3BDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/18246486-B260-E211-8A21-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/18631FFD-AA60-E211-B5D6-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1867D856-7660-E211-B60F-0026189438D8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/18A09EF3-BB60-E211-8753-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/18BF4E97-AD60-E211-B35F-00261894389E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/18DAB43D-A960-E211-96B9-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/18F70FC6-9960-E211-AAF0-0026189438CB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1A8009D2-C760-E211-BF26-002618FDA259.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1A85D0CC-A160-E211-B4AE-00261894398A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1AAF03AC-9C60-E211-9859-00304867926C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1ABE48FE-9660-E211-93D9-00304867904E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1ACBDFA6-A960-E211-BFD3-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C1044F2-9E60-E211-BABA-002354EF3BD2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C1B2762-A060-E211-96E0-0026189438DC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C465D56-AF60-E211-9BA8-003048678FF8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C4CCBDA-D460-E211-86CB-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C4D7122-AA60-E211-B20D-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C7D8E92-AB60-E211-8D97-003048678F02.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C957DF2-A860-E211-9E71-00261894384A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1C9FE616-A860-E211-9E8D-00261894386E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1CBBB1F2-B760-E211-801C-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1CE809AE-9A60-E211-BB6B-003048678F92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1E0C764F-9960-E211-BE8E-00304867902E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1E10710D-AF60-E211-AE69-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1E4943B8-B760-E211-B33B-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1E59747E-B060-E211-9952-0026189438CB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1E7C1160-AF60-E211-A2FF-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/1E8DBBBA-A860-E211-8B92-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/204E2119-B360-E211-97D6-00304867901A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/207FF6CE-9760-E211-8AA0-00304867904E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/20AA7850-8760-E211-8A46-003048678A6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/20E2636C-9860-E211-8133-003048678F92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/221F311F-CA60-E211-A93C-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2247014E-AD60-E211-AC79-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22808DD9-9D60-E211-81E1-00304867903E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22965BE7-AB60-E211-A940-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22A57F5F-8860-E211-903A-00304867C0EA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22BE4CF2-AF60-E211-AD1E-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22EBAC36-C060-E211-8A41-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22F76F3F-B660-E211-AB05-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22F8C03A-B460-E211-87F3-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/22FD47AA-B360-E211-8B8A-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/24614480-B260-E211-88CF-003048679168.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/24D794DE-BA60-E211-9FF1-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/24D81513-A060-E211-8A3C-003048678FEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/24E43498-D160-E211-BE03-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/24F2545E-BF60-E211-B826-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/26267AD7-9560-E211-93A6-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/262ADBF2-9C60-E211-AF8B-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/26431423-CA60-E211-9796-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/264D0441-BC60-E211-9D57-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/26FCE680-B860-E211-9E1E-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/26FFED41-9D60-E211-A623-003048678E52.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/28978A3B-9560-E211-95A8-002618FDA248.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/28A00B72-AC60-E211-BB18-002618943868.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/28AFF848-C560-E211-8433-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/28EADDD1-7660-E211-AB1A-00304867BFB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2A78D8B2-A660-E211-B082-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2AE2A305-BA60-E211-944D-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2AF63964-A260-E211-BF85-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2C24A6CA-9F60-E211-ACD4-003048678F92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2C510460-BB60-E211-A7BB-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2C520C1E-A460-E211-8B24-00304867C1B0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2C735FEE-A060-E211-815A-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2CD9D33C-CD60-E211-9F7E-003048FFD728.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2E2CA63E-B860-E211-AA26-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2E446D64-A460-E211-A4AA-00304867C034.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2E7D488D-A360-E211-8336-00304867C1B0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2EEA78AA-9860-E211-B980-003048678F78.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/2EF5AE6D-B760-E211-B772-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/30562C6E-A460-E211-9ED7-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/30893097-CB60-E211-A53B-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/308A93CB-B060-E211-8BC7-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/3093625D-9C60-E211-8500-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/322E183E-CD60-E211-B53A-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/32313EC5-9F60-E211-ADF5-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/323D32C3-9C60-E211-8A91-003048678B18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/324A312A-A260-E211-AE9B-002354EF3BE3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/32D03E83-9760-E211-AABE-003048678E6E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/34044F3E-DC60-E211-A2B8-003048FFD796.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/3415BB15-9C60-E211-AC4B-003048678E80.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/3426EDF5-9660-E211-888E-00304867901A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/342A6213-BF60-E211-8130-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/3451251E-8460-E211-9A88-00304867C1B0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/34658348-B060-E211-89DA-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/347A1282-9B60-E211-9860-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/347A3CA6-9860-E211-B9E2-003048678E6E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/348D7382-B860-E211-BC31-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/36014419-9060-E211-8C47-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/36368480-B860-E211-8360-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/364D65D9-BC60-E211-AF91-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/3678DED2-9760-E211-85E8-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/36ACB0F5-C860-E211-B6EF-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/36B124EB-AF60-E211-9508-003048679168.root'
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
process.ecalTimeEleTree.runNum = 99999911
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

