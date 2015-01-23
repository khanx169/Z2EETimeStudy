import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([

'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A03FDFC-1770-E211-B3E6-00248C55CC9D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A1F6C37-E267-E211-99EA-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A2B62B2-E267-E211-B5CB-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A552090-E067-E211-BB2C-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A5C0A0F-B267-E211-8A4A-002618943800.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A615995-DC67-E211-95C2-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A732F9C-3F75-E211-B60E-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A89CCA6-E467-E211-B350-003048FFD796.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A8C5392-1670-E211-BEA8-0026189437FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5A94870B-E267-E211-A3DA-003048678BF4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5AB06F11-1670-E211-9BD8-002618943946.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5AD20AAC-E467-E211-BE9B-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5AE0DE1B-E367-E211-BCB1-00261894386F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C05657A-1570-E211-864E-0030486790BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C08432D-DF67-E211-B11E-002618943807.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C1DD93D-DD67-E211-8BE2-003048678BAE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C2D708A-1870-E211-9DC3-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C2EEB18-DF67-E211-B29C-0026189438BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C47F622-E367-E211-9D06-002618943849.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C90A898-E067-E211-843A-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5C9BD8EB-E367-E211-99C7-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5CB6EECA-E267-E211-961D-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5CCD7EB9-E367-E211-80E7-003048678B12.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5CDAA748-E267-E211-8115-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5CE2C78C-1870-E211-B138-0026189437FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5CE4E676-DE67-E211-9B9A-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5CF2372D-3E75-E211-9859-00248C0BE014.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E1011A7-E767-E211-BB6E-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E11611B-1A70-E211-89BE-003048FFD76E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E2AD6CD-E667-E211-B200-0026189438DD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E3A1E72-E067-E211-9FCE-003048678AC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E455C98-E467-E211-97D0-00304867C034.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E636D9E-DC67-E211-9822-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E7480E7-E767-E211-9BE3-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E8406C9-4970-E211-9A78-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E94D23C-E467-E211-A73A-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E97120E-E467-E211-A44F-003048FFD744.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5E9D901C-E367-E211-B872-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5EB8FB88-E167-E211-9502-002618943976.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5EC7A522-DF67-E211-AECD-002618943885.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5ED70F7A-E067-E211-A9BD-003048678F8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5ED87481-4770-E211-A3B9-002618943902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5EF74AA5-E167-E211-A984-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/5EFFD7B0-E167-E211-B838-003048FFD728.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/60041425-DF67-E211-BB7A-00261894386E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/60164980-E767-E211-8DA4-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6031FE82-3E75-E211-AC6B-0026189438ED.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/60607E0E-E467-E211-878F-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/608F0D36-1268-E211-A139-003048D3FC94.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/60A79C65-DC67-E211-9FD4-00261894386E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/60C2DDE4-3E75-E211-85A8-0026189438DD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/60D2A29E-E067-E211-87E4-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62121D59-E767-E211-B0D7-00261894397E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6224560E-E267-E211-A517-003048678B14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/624CC78A-E067-E211-B677-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62819046-E567-E211-9D1A-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62871077-3F75-E211-AB86-00261894397A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62B360CC-DF67-E211-B72E-0026189438AC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62B66C9C-3E75-E211-BE37-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62C0095D-E467-E211-BD16-0026189438FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62C512F0-E367-E211-B41A-002618943921.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62C7A493-E367-E211-8370-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62DCD37D-E267-E211-A87C-003048678B06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/62E023CB-E667-E211-A8EC-003048FFCC18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/641393A1-E467-E211-BD93-002354EF3BE2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6414FF2B-3F75-E211-8FD4-003048678E8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/642577B5-DF67-E211-8D82-00261894390B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/643764B4-E167-E211-8940-003048679294.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6482F649-DD67-E211-8D07-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64991AC1-4570-E211-BB00-002618943843.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64A21802-E367-E211-94FC-003048678B12.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64A64876-E567-E211-B438-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64B1F816-DF67-E211-95E7-002618943898.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64C1B194-3F75-E211-A235-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64CACCEE-3E75-E211-95F7-003048678B7C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64CF10D1-DF67-E211-A488-003048678F84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/64F19B40-E167-E211-A309-0026189438DB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/660D18A1-E667-E211-AAE6-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/66109BDA-E567-E211-8089-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/663608BF-E667-E211-83C0-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/664EFAF5-E667-E211-9337-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/666A266C-E767-E211-B17C-002618943870.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/666B02E5-E667-E211-B0DC-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/66720833-E167-E211-8DC7-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6674BF62-B267-E211-A148-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/66ADDA37-E367-E211-A605-0026189438A7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/66FD2588-DE67-E211-AF25-002354EF3BDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/68174F67-E267-E211-A614-0030486790A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/68524B15-4075-E211-8140-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6856CAF3-E667-E211-9AAB-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6866F749-E567-E211-8E21-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/68762A6D-1770-E211-A895-003048679182.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/689433A1-1670-E211-96EB-0030486791DC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/68D05828-E167-E211-94FC-0026189438F2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6A0591DA-3E75-E211-9B71-002618943939.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6A0BB527-E467-E211-9B26-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6A4FE788-AD67-E211-A098-0026189437F9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6A5BC4C4-3E75-E211-9A66-00261894385A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6A828436-DF67-E211-95D3-00261894388A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6A97D382-E367-E211-88EF-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6AA253A3-E767-E211-9AF3-002618943800.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6AAAA15D-AA67-E211-AFE6-003048678AC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6AAF0E9F-3E75-E211-9BD6-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6AC0BE91-B167-E211-A2AA-003048679266.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6AE50091-E167-E211-9877-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6C1F1E11-E067-E211-91A8-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6C363ADC-E667-E211-A990-0026189438D2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6CA969CF-E267-E211-A5F3-002618943960.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6CC2E2CC-DF67-E211-BF7B-002618943930.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6CC8709C-AE67-E211-ADCA-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6CF36864-DC67-E211-8EB2-003048678FAE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6E29E8D4-E167-E211-8825-002354EF3BE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6E4DEF33-E467-E211-9DBE-00304867924E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6E606534-E267-E211-891A-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6E608EBE-E367-E211-95F3-003048F9EB46.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6E7A4D09-DE67-E211-B908-00248C55CC9D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6E9548BC-E267-E211-A382-003048678C62.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EAD0169-E767-E211-9B0F-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EAFF530-3F75-E211-BAE3-00261894395C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EBB4098-E367-E211-8B33-003048FFD730.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EC4C85D-E767-E211-879A-002618943874.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6ECF7F49-DF67-E211-98AD-003048678B70.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EDBBB6C-E267-E211-83A8-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EEEA8BA-DF67-E211-A87B-003048FF9AC6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/6EFA338E-DE67-E211-8B94-0026189438DE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/70140208-DF67-E211-902D-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/702B35C3-E367-E211-8940-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/703C914B-DF67-E211-8B4D-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/706D5C7A-DC67-E211-AD26-002618943950.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/70836ED5-AE67-E211-8238-0025905938A4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7084C383-E167-E211-9A46-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/708CC0BD-DE67-E211-8538-003048679084.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/709D8235-1870-E211-8AB1-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/70E05A9C-E467-E211-8739-003048678BC6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/70ECA57C-E467-E211-B78E-003048678B12.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/70ED42B7-3F75-E211-86E6-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/70ED7148-DD67-E211-81D6-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7213948F-3E75-E211-8AD0-002618FDA250.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7234EBF0-1768-E211-B9ED-003048678AFA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7238E4F3-E567-E211-A51D-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/72486703-4075-E211-9E92-0026189438F4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7255C569-E067-E211-A148-00304867929E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/728DECE5-E167-E211-AD12-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/729AA50E-4868-E211-BBFB-00261894398C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/72C8EFBA-3E75-E211-AC6D-0026189438E0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/72F6B892-E167-E211-9191-00248C0BE018.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/74033375-1870-E211-94A5-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7409984B-AD67-E211-82C6-002354EF3BDF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/740E7BFF-DE67-E211-997A-003048D15E2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/74344A2F-3E75-E211-A42A-002618943939.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/744F52E6-1870-E211-919F-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7477F126-E267-E211-80A0-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/74901182-1870-E211-A23B-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/74A9CEA5-E067-E211-8AB3-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/74B925DD-E767-E211-928F-002618943807.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/74C57ADC-E667-E211-845A-00261894397E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7612283E-E367-E211-8250-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/762CD1FB-1870-E211-A6DC-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/763A7771-1770-E211-B39F-00248C55CC9D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/768F6E0B-DF67-E211-A14C-003048D42D92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/76D43ED2-DF67-E211-8344-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/76DAD7A2-E367-E211-94F8-003048FFCB74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/780A935A-E467-E211-8F15-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/780B5297-E267-E211-ABE6-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/784408D5-E267-E211-A85A-00261894391F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78463A71-E567-E211-B619-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78839575-E467-E211-A4CF-00261894393E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78A84CD1-1770-E211-BBF6-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78B3B4C7-B167-E211-A754-00304867BF9A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78C75C7C-1570-E211-AF25-0030486790A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78D7F804-DF67-E211-8170-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78DC4032-E267-E211-937C-003048678F84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78F892AA-E267-E211-BB15-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/78FC8FAC-E467-E211-BB0C-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A118080-AA67-E211-9B28-0026189438DA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A1934DB-E367-E211-BA38-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A23542F-E367-E211-91C9-002618943981.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A300B52-E367-E211-B21C-00261894396B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A3A33E4-DD67-E211-97A2-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A5FFD74-E567-E211-B327-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A78D48D-E167-E211-8567-00261894394A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7A9A8AF5-3E75-E211-9F39-00261894385A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7AA5AD85-E367-E211-A70B-00261894393B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7AB1CB90-AE67-E211-A6D2-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C05A2A9-4270-E211-AE06-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C0A250C-DE67-E211-ACC0-0026189438E4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C2BFB52-E167-E211-BC0D-003048678FF6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C310D4C-E467-E211-B9E6-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C515D5C-DC67-E211-A995-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C6AC45D-4870-E211-A14C-002618943914.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7C81E63E-AA67-E211-B4DB-003048679010.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7CAF83D6-3E75-E211-B2B4-002618943974.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7CBDD9F9-3E75-E211-B53A-00261894393B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7CC11D5C-E367-E211-88D2-00261894397D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7CFDEBCF-3E75-E211-90A7-003048679084.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E1956D5-E167-E211-AC77-0026189438D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E3B2017-E667-E211-AA52-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E493B56-E267-E211-AD17-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E65BEA6-DE67-E211-B44A-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E808B11-1A70-E211-B3C0-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E838E9F-3F75-E211-82CE-002618943901.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7E934F49-E167-E211-BA91-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7EAEFBDF-E267-E211-BC9C-002618FDA263.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7EBC7329-E167-E211-8FFC-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/7ED215CA-E267-E211-92DA-003048FFD76E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8022B38A-E767-E211-A155-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8032AEC9-E367-E211-8EC6-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/80442179-DC67-E211-ABB8-00261894398D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/804448EC-3E75-E211-833C-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/805B57E7-DF67-E211-B617-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8066A36A-DD67-E211-BA06-002618943926.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/807B0C65-DD67-E211-9407-0030486792B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/80977A7E-E467-E211-9886-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/80AB2D3A-E467-E211-A70F-00248C0BE005.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/820441D6-B167-E211-B722-002618943953.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/821BAB54-1870-E211-B17C-002618943832.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8228D154-E367-E211-9AD6-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/824EBD23-1870-E211-BD67-002618943946.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8287D0A0-3F75-E211-A2F7-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/82A58646-E267-E211-B129-003048679236.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/82B43D09-1A70-E211-B486-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/82D246D3-E567-E211-A2A3-002618943807.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/82D560F5-E267-E211-AFB3-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/82D5F7AC-DF67-E211-AA27-0030486791F2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8422B14F-E467-E211-97B4-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8425FA7C-B167-E211-B7C2-00261894383B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8430DC9E-3F75-E211-B872-002618943979.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/845B1898-E267-E211-BB22-002618943930.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/846C3BB9-E267-E211-9B83-00304867924E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/849721C7-E167-E211-A720-002618FDA204.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/84A60052-E167-E211-BDAB-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/84B1B382-E367-E211-9F97-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/84C9D272-E467-E211-AC6D-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/84E778E4-E567-E211-98D4-003048D3FC94.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/84FF0156-1670-E211-84CB-0025905938AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/861B2ABE-B167-E211-B1ED-002618943860.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/86492F7B-B267-E211-AD18-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8675BF75-E767-E211-B3C4-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8676A25B-AA67-E211-8FCB-003048678DA2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/86880D63-E467-E211-816E-003048678B94.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/86BABBDD-3F75-E211-A9D0-002618FDA216.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/86C4A0E4-DE67-E211-8036-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/881727BB-E167-E211-AA80-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8830B794-E167-E211-90D7-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/88460850-E767-E211-BA6D-0026189438DD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/886F1C4F-E267-E211-9E10-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/887FE583-DE67-E211-8017-002618943898.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/88836F5D-E567-E211-B91F-003048679010.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8892DE09-DE67-E211-A35B-00261894393A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/88A8FA06-E667-E211-A26F-002354EF3BE3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/88B21829-E267-E211-92FB-003048FFCB74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/88D4340D-DE67-E211-BCFE-00304867924A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8A2B6B00-DE67-E211-8050-0026189438CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8A481D03-DF67-E211-92BA-002354EF3BE3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/8A5E2306-DE67-E211-B419-003048FFCBA4.root'

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
process.PhotonIDProd.DoEcalRecHitIsolationCut = cms.bool(False)
process.PhotonIDProd.doCutBased = cms.bool(False)
process.myPhotonSequence = cms.Sequence(process.myphotonCores+
                                         process.myphotons)
# photonID sequence
from RecoEgamma.PhotonIdentification.photonId_cfi import *
process.myPhotonIDSequence = cms.Sequence(PhotonIDProd)
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
process.ecalTimeEleTree.runNum = 99999917
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

