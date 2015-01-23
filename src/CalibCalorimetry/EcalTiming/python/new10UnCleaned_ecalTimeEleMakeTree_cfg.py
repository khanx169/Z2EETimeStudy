import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BA0A981B-E667-E211-AB92-0026189438DF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BA157C34-3F75-E211-B17D-0026189438F4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BA470287-3E75-E211-A53E-00261894390B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BA67D136-E467-E211-9173-00304867918A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BA7D8C16-E367-E211-9D56-003048679168.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BA83BA83-DD67-E211-881C-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BAB3CE5D-E267-E211-9BE4-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BAB90188-DE67-E211-96A8-003048678B70.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BABAE6D3-E367-E211-9CF5-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BADC8876-E167-E211-A0C2-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BAFE3C7B-E367-E211-86F0-002618943910.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC004E5C-E367-E211-BC21-00261894383B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC069366-E367-E211-830C-003048678B38.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC082BFF-E267-E211-92FF-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC087155-DD67-E211-849E-00261894397B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC12A276-E067-E211-96DB-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC216327-DD67-E211-AC96-00261894387B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC2412C0-E267-E211-8D3E-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC267980-E167-E211-9587-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC29B4DF-DF67-E211-AAF8-0030486790B8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC36A2DE-E567-E211-A7DD-00304867C034.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC43AD5C-DC67-E211-9177-003048678BAE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC534B83-1870-E211-BA15-003048678AFA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC546870-1770-E211-BE43-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC810838-E567-E211-8F2A-00261894388D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC8134A9-B167-E211-AFBB-0026189438BF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC896A11-E367-E211-BD1F-002618943838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC8B3784-3E75-E211-930A-0026189438F6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC94774B-E167-E211-8E2C-002354EF3BDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BC97C540-E167-E211-957D-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BCAF2833-DD67-E211-8B37-003048678B34.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BCB2D4A5-DE67-E211-BBF2-002618FDA279.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BCEE22A7-E467-E211-A67A-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BCF2FF68-E767-E211-B578-002618943978.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BCF5CE36-E367-E211-9AC2-0026189438E4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BCFE4C51-DD67-E211-B50B-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BE2E19D4-B167-E211-BD9A-002618FDA208.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BE4FAF0E-E367-E211-AF49-00261894380B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BE8FDB8B-E067-E211-92F0-00261894389F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BEB9F734-E267-E211-A0AF-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BEBC337E-1570-E211-89BC-002354EF3BDB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BECBA7AF-E667-E211-9C2D-003048D15E24.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BED3D760-AD67-E211-B6E3-00304867C1BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/BEF3780E-DF67-E211-B54C-002618943923.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C00BBE6E-3F75-E211-B1BC-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C015D4D7-E667-E211-AF34-00304867904E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C0431982-E267-E211-BEBF-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C07944C1-E267-E211-A597-003048678FF6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C0B48FCA-DF67-E211-9FA1-003048D15E2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C0B87E97-3F75-E211-A090-0026189438ED.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C0C2C307-E867-E211-91AD-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C0D7EAA2-DE67-E211-9B10-00261894397B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C0E05333-E167-E211-9603-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C20A036D-E067-E211-BDDE-003048D15E2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C21149E7-E167-E211-9E0D-0026189438F9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C2119DE3-E667-E211-A685-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C24F28A0-B167-E211-9F6B-0026189438D7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C25107E2-E367-E211-A81D-0026189438E9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C28A173F-E367-E211-B922-003048D15D22.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C29A9563-5570-E211-8426-00304867C1B0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C2A1B40B-4B70-E211-B032-0026189438D2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C2ABB6D5-E667-E211-89A4-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C40FB0E7-1C70-E211-B0E4-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C418A991-E767-E211-80AC-00261894396F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C419E2CE-E367-E211-A96F-002618943915.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C41FA0C1-1570-E211-8397-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C42CFB7F-DE67-E211-8064-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C48D89E0-E367-E211-854B-00304867901A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C4E9B926-E467-E211-9DA1-002618943960.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6009A1C-E667-E211-9C71-003048FFD796.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C60D03DC-E267-E211-8F7C-002618943885.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6182168-1670-E211-A1B9-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6226F99-E567-E211-967E-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C638B0EE-1770-E211-8981-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6565FFE-DE67-E211-A4DE-0026189438A9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C656D488-4075-E211-8FC5-00261894396D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C671606A-E367-E211-A296-002618943925.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C672EB8B-E067-E211-AAB3-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6761C73-E767-E211-8F60-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C67BAC98-E167-E211-B8AF-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C67E323D-AA67-E211-9E53-003048679084.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C69EE58B-E267-E211-8D14-003048679168.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6C95D48-E767-E211-A200-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C6D54752-E267-E211-8E26-00261894394B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C821880B-E167-E211-891E-002618943926.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C84086EB-1770-E211-BCD4-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C8411BC3-DF67-E211-8938-002618943984.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C84D0247-E167-E211-BDAC-003048678F8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C8515EA8-DE67-E211-92E1-002618FDA28E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C85EDB5B-DD67-E211-9751-002618943947.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C865AF72-1570-E211-85D6-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C8BB7013-DE67-E211-91E1-00304867D446.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C8C3ACA1-DE67-E211-A857-003048678F9C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/C8D56F99-E467-E211-AAF7-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA0058F4-E267-E211-B084-00261894394D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA1FB7E8-3F75-E211-B4D0-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA32D818-DF67-E211-8696-0030486790B0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA39D591-AD67-E211-BACA-0026189438DD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA5583E8-E167-E211-908A-003048FFD7D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA8118D6-E267-E211-8916-002618943921.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CA8DBA03-1870-E211-AB60-003048678AFA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CACFA16B-AD67-E211-9FD5-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CAD658C9-E667-E211-B75B-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CC3D3497-E367-E211-9EBE-003048FFCC18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CC4AA8AE-1570-E211-9AE4-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CC4E2A45-E367-E211-A957-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CC60F11A-E467-E211-9DA1-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CC62207E-1570-E211-9F6A-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CC9DFFF5-1970-E211-880F-003048678AFA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CCFC3F46-E267-E211-857E-002618943838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CE2BA0BD-E367-E211-AAF0-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CE56DD4C-DD67-E211-9AD0-002618943882.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CE6F8D9C-E267-E211-AAD3-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CE7E308A-DE67-E211-94A9-0026189437ED.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CE7F0F94-E067-E211-AA5E-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CE9D0C40-E267-E211-A8BB-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CEB08388-E767-E211-927C-00261894393E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CEDFA357-E767-E211-BB01-003048678E2A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CEE2DA59-E267-E211-A961-00261894380B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CEF2DE7A-E467-E211-BEAF-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/CEFB3F95-3E75-E211-BD81-0026189438D7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D039464A-E267-E211-BC31-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D0706386-B167-E211-90C9-00261894397F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D077A4B6-B167-E211-BA20-003048678F26.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D0AD87CE-DF67-E211-8FC3-003048FFD76E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D0B2E649-DD67-E211-8BDF-002354EF3BE1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D0BAFE6B-DC67-E211-97C3-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D0E0F561-E767-E211-B7B5-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D0F94651-3F75-E211-9B6A-003048679084.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2054FAB-1570-E211-A238-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2070688-1670-E211-B27F-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2156673-E367-E211-AA47-00248C0BE005.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D225EF6B-E367-E211-8E18-003048678C62.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2618495-DE67-E211-AAEA-0030486792BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D275633F-DD67-E211-A213-00304867D446.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D279B23B-E367-E211-84B7-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2C3DC31-1670-E211-863D-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2C77F82-E567-E211-975E-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2DD5ECA-DF67-E211-8515-00261894388A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2E06AA4-E267-E211-91A6-00261894383B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D2E74693-3F75-E211-AC48-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D40CA3ED-DD67-E211-852C-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D421A57F-E467-E211-A122-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D4441AEF-E667-E211-BC6D-003048FFD796.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D44A10CB-E167-E211-BC7C-003048678C62.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D44C4DC8-E167-E211-9B5E-002618943849.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D477E7A5-E467-E211-B201-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D48B428F-E167-E211-A629-00261894396A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D4CD7C4A-E167-E211-A92A-003048678B70.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D4ECFAEC-3E75-E211-B0D5-003048679164.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D60F393A-E267-E211-896F-0026189438B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D613F99C-3F75-E211-BDE0-002618943877.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D6273C32-E367-E211-A28F-003048678B70.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D653E052-E367-E211-A36F-003048FFD7D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D6AC98C5-E667-E211-93A4-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D6B6F962-3F75-E211-AC3E-00261894396B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D6D0078C-E767-E211-85C3-002618943923.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D6FE886F-DC67-E211-A09F-0026189438A5.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D84E3AB2-E167-E211-8A6B-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D87C6EAA-E167-E211-8A44-0030486790A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D895ED6B-DD67-E211-B549-00304867C1BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D89CD36A-E767-E211-8C9C-0026189438DE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D8C5B573-DD67-E211-8D22-003048678B26.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D8CB6EAE-E367-E211-A564-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D8E17852-3F75-E211-9764-0026189438F2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D8F022C5-DF67-E211-BFF3-00261894380B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D8F8E73F-1770-E211-A0A9-0026189437FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/D8FA26A7-AE67-E211-9DFD-0026189438F5.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA38ED30-E267-E211-989C-003048679006.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA4551C0-E167-E211-8DF8-00261894380B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA74D4C4-DF67-E211-8C03-0026189437EB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA776AD4-E667-E211-83AE-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA896902-4075-E211-8797-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA946F03-E667-E211-82FD-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DA9C5D12-E667-E211-A73B-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DABE5458-AA67-E211-A2E3-00248C0BE01E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DAE57685-DE67-E211-B4E8-00261894388A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DAF212B4-B167-E211-AE87-002618943810.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DAF4A09C-3F75-E211-9C7D-00261894393B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DC01C938-3F75-E211-A543-00248C0BE005.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DC1B026D-3F75-E211-973F-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DC1C8C92-E267-E211-A615-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DC6C0FE6-E367-E211-827E-002618FDA250.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DC7853A0-DE67-E211-AB9E-003048678E52.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DC7B350C-DE67-E211-9450-0030486792B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DCA5EB2B-E367-E211-9657-002618943980.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DCB2651A-E667-E211-8B97-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DCBCDC79-E767-E211-A8A6-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DCCAB7C2-E267-E211-812C-003048678B38.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DCE97817-1970-E211-8690-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DCEA47FE-E767-E211-8F2E-0026189438F7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE1265BA-AD67-E211-A90B-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE18C5F7-E167-E211-9997-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE5B0D7D-AE67-E211-85C4-003048FFD7D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE6A94EA-E667-E211-8B5A-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE74ECD3-E167-E211-9F3D-003048679168.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE8F7B81-E467-E211-ACCC-0026189438DF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DE97477D-E767-E211-8C84-002618943974.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DEDFDE88-B167-E211-9724-00261894387C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/DEE074A9-E067-E211-A19C-002618943930.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E0104E19-E367-E211-8DA2-00261894398B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E01418E7-3E75-E211-96F8-00261894393E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E03C5B03-1770-E211-9E7B-0026189438AC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E09F783D-E267-E211-8585-003048678B94.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E269E0EA-E267-E211-97BA-002618943963.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E271950C-E167-E211-A03B-0026189438F9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E29D860F-E467-E211-8785-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E2A8E2F9-3E75-E211-B97A-003048678B0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E2AADC9C-AD67-E211-AB79-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E2B7379B-6670-E211-9DBB-0026189438FC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E2CC59D4-E567-E211-BB38-002618FDA28E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E401D854-DD67-E211-ADAE-003048679266.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4138144-1670-E211-90E2-0030486792A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E417C185-1870-E211-AED6-003048678BB2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E446A94C-3F75-E211-8985-00304867C026.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E44930CD-1670-E211-AD4E-002618943982.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E44EB530-E167-E211-91BA-003048679294.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4512540-3870-E211-B853-00304867915A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E47F5B4A-E167-E211-B240-002618943951.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E49D3E49-AA67-E211-820D-0026189438E2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4B42C88-1770-E211-AE63-003048FFD7D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4B6DE56-3F75-E211-9D10-003048679166.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4D7DFED-DE67-E211-81C4-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4DD17A8-E667-E211-9348-00261894393C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4E1F7A4-E267-E211-B369-00261894384A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E4E64594-E167-E211-B152-003048678B00.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E65326EA-E167-E211-9B9D-0026189438E4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E65A825F-AA67-E211-AB26-003048D3C010.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E66F9EAD-DF67-E211-8337-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E67A0871-E367-E211-9F09-00304867D446.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E6928677-E267-E211-8E5F-003048FFD730.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E6C80944-DF67-E211-AE5F-00261894388F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E6DFD84D-E567-E211-8B8F-00304867929E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E6E5B8DA-1970-E211-8DA0-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E6F23D14-3F75-E211-BEFC-00261894396F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E8125F68-1670-E211-B328-003048678B8E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E8202025-1770-E211-B193-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E835AE40-3F75-E211-86B9-00304867BF9A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E852F312-E667-E211-BBD6-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E895E5D1-1670-E211-B69F-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E8978A69-E067-E211-88DC-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E89F89EB-E367-E211-891C-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E8B47D17-E167-E211-B99E-00248C55CC7F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E8BA085D-DD67-E211-8178-003048678BAA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/E8FF0713-E867-E211-B28A-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EA244B6A-AE67-E211-8CA0-00261894389A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EA2EE693-E467-E211-AEC5-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EA39CA67-E067-E211-A1C7-002618943984.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EA46542C-E467-E211-8EB3-00304867D446.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EA531A73-3F75-E211-B283-0026189438C9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EA60E488-3E75-E211-8635-00304867C026.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EAA9AC8C-E167-E211-BE46-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EADC4150-DD67-E211-BDC4-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EAEE7A42-E167-E211-B534-0030486790B8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/EAEFE92F-1770-E211-83CF-002618943922.root'

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
process.myphotons.photonCoreProducer=cms.InputTag("myphotonCores")
process.myphotons.runMIPTagger = cms.bool(False)
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
process.ecalTimeEleTree.runNum = 99999919
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

