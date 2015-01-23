import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7402C6C0-58AC-E211-91AC-002618FDA250.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/740A50B7-57AC-E211-9BC6-002618FDA263.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/747E423C-58AC-E211-9F76-00261894395F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/747F3F2E-77AC-E211-8A50-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/74A9ED1C-56AC-E211-BF3A-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/74BAF9BA-5EAC-E211-A049-002618943948.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/74C5BB57-5EAC-E211-B0E9-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76170884-73AC-E211-9F7A-002618943932.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7639A42A-55AC-E211-B653-003048678E24.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/765310D6-55AC-E211-994B-002618943958.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76A6B052-5EAC-E211-A09D-0026189438EF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76B7B7F6-8DAC-E211-ADA3-0026189438FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76BB5805-58AC-E211-82A6-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76CC8222-5FAC-E211-B151-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76DF54E0-6BAC-E211-8284-002618943983.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/76EC17DC-6DAC-E211-822A-00248C0BE014.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7814B110-58AC-E211-8F76-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/783CA5AD-58AC-E211-B202-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/78A65F2C-56AC-E211-8A40-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7A45CE86-55AC-E211-AC89-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7A5D75F9-7DAC-E211-BAEC-002618943826.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7A91D0EB-56AC-E211-B143-002618943939.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7A9859BB-6AAC-E211-AF8B-00261894392B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7AA8D581-5EAC-E211-81D1-0026189437FC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7ACD1EA8-56AC-E211-8674-0026189437ED.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7AFCCF59-6FAC-E211-AC7C-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7C10A5F2-54AC-E211-B700-0025905938AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7C12AF6E-5EAC-E211-997F-002618943831.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7C7B813D-5EAC-E211-9AFD-002354EF3BCE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7CFCE85D-55AC-E211-AD18-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E40ABBD-6AAC-E211-A667-002618943910.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E4AEC52-71AC-E211-A837-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E4D2A7B-58AC-E211-8DB0-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E68D2B6-8BAC-E211-8F12-0026189438EB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E855906-6BAC-E211-9A20-002618943920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E884FDA-57AC-E211-BC41-002618943949.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/7E894157-6AAC-E211-AFF9-003048FFD730.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/80053C82-58AC-E211-9D60-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8009062A-6AAC-E211-BA92-00261894388F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/808626E6-56AC-E211-AFC4-003048678B36.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/80C0BE6C-58AC-E211-A3A7-00261894397D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/80C11479-5EAC-E211-8736-00261894398B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/80E28C6D-58AC-E211-B15D-0026189438FF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/80E6344E-58AC-E211-8BCB-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/82680526-8BAC-E211-9C79-002618943966.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/82785AED-5EAC-E211-9718-0026189438F4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/829402FC-54AC-E211-A6B5-002618943932.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/84647648-5EAC-E211-89D0-00261894387A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/84FA8ECF-73AC-E211-8FE1-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/86311C5B-54AC-E211-A3E4-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/863E6F1F-58AC-E211-A9D2-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/86E1B4E2-56AC-E211-A6C0-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/88255924-58AC-E211-8A9F-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/88517C8B-97AC-E211-A2FF-003048678B86.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/886D91F2-72AC-E211-B6A1-002354EF3BDA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8890316C-5EAC-E211-B3A4-003048679296.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/88D1A525-59AC-E211-928E-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/88ED77E0-55AC-E211-8BA7-002618943957.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8A203C30-58AC-E211-BCFC-00261894389C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8A6F6C06-71AC-E211-AE13-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8A88EB95-58AC-E211-B1A9-0026189437FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8C2897BF-5EAC-E211-A618-002618943860.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8C4E2B0F-55AC-E211-81D3-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8C5C2B73-6AAC-E211-A5FF-002354EF3BE0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8C5EC249-78AC-E211-B65A-002354EF3BD2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8EBFB661-5EAC-E211-AD5A-002618943919.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8EC2AC72-5EAC-E211-8383-00261894394A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/8EC4F67A-55AC-E211-A9CE-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/904EB1AB-56AC-E211-82E4-0026189438D9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/90D1C2CA-57AC-E211-9E7E-002618943821.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/90F88DD1-5EAC-E211-AA70-003048678CA2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/920EA7DF-56AC-E211-8ED7-00261894394F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/92348A92-5EAC-E211-8861-002618943980.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/924D5006-6BAC-E211-A0B9-0026189438F2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/92FEB048-9EAC-E211-8F44-002354EF3BDB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/94216379-6EAC-E211-ACA9-002618943896.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/94602321-5EAC-E211-A640-0030486790A0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/946701F6-5DAC-E211-B940-0026189438A7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/94AECF85-5EAC-E211-8476-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/94E9CC48-54AC-E211-B103-003048B835A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/960C337C-63AC-E211-8C17-002618943826.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9650E57F-55AC-E211-BFBB-00261894387E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/96A04851-58AC-E211-B03B-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/96D6FAD6-71AC-E211-B709-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/96F5FA86-57AC-E211-8EAE-003048678E24.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9A68EF00-54AC-E211-A695-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9A812EE8-69AC-E211-8061-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9C34C278-5EAC-E211-959A-00261894385D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9C3AE450-5EAC-E211-A1A3-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9C3B6093-58AC-E211-BA6A-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9C8C79BB-57AC-E211-9C66-00261894387C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9C8CEA33-55AC-E211-BD9E-00261894387B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9C8F04B5-70AC-E211-BEFE-003048FF9AC6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9CF1CBC7-57AC-E211-95C7-00304867D446.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9CFAC3BE-55AC-E211-8C9E-002618943986.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9E038FAB-56AC-E211-88C2-0026189438F7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9E2E1397-6BAC-E211-A877-00261894395C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9E52EC5F-55AC-E211-B90E-00261894386A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9EADAC7B-55AC-E211-B883-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9ECA22E0-8AAC-E211-9614-0026189438DD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9EE58340-54AC-E211-A36B-0026189438F6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/9EEC658A-71AC-E211-88E5-002618943932.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A0163C29-6CAC-E211-A080-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A045F397-8AAC-E211-856B-002618943944.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A0E6EFBA-6AAC-E211-AADB-002618943933.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A4B0206F-58AC-E211-AB77-0025905938A8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A650D6F3-53AC-E211-A924-002618943856.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A69A3EAA-54AC-E211-87C1-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A6B54BAE-55AC-E211-964F-002618943914.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A6B69713-8FAC-E211-AFE7-0026189438C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A6F69ABD-56AC-E211-B628-00304867903E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A88F0DE6-57AC-E211-AB19-00261894387B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/A8A9B2AE-70AC-E211-BFDD-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AA091700-54AC-E211-9BD3-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AA362F33-54AC-E211-81AD-00248C55CC9D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AA5F63AE-58AC-E211-B588-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AA9F22D4-56AC-E211-9A5E-0026189438AE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AAABBFF6-53AC-E211-809E-002618943885.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AAFE346E-55AC-E211-ADAC-002618943886.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AC26ADA9-5EAC-E211-ADCE-00304867902E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AC71AB1E-55AC-E211-842D-00261894380B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AC8DDAA6-5EAC-E211-92BA-00304867920C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AE2C9DF2-72AC-E211-AABC-002618943932.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AE66041A-55AC-E211-AD9E-002618943933.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AE691FCC-57AC-E211-A8F4-002618943957.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AE8A740B-6BAC-E211-AEE7-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AE8B1161-54AC-E211-B8EF-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AEC404EB-6BAC-E211-9222-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/AEE875C2-5EAC-E211-A99C-00261894383E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B03D94B3-57AC-E211-9D0F-002618943959.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B0906F52-58AC-E211-938C-0026189438AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B0972B28-6AAC-E211-BAA7-002618943932.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B098BAD7-57AC-E211-BBAC-00261894397E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B0BA755C-55AC-E211-94A4-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B23A1820-9FAC-E211-9CC1-002354EF3BDB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B29D33D3-54AC-E211-AF91-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B2FE0004-5FAC-E211-A004-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B4126590-58AC-E211-910C-0026189438FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B45BFE20-54AC-E211-B66B-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B4BFAEDA-53AC-E211-8142-00261894383F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B4E6E4BD-77AC-E211-9B94-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B6109705-6BAC-E211-998A-003048678B30.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B69DB188-54AC-E211-9D9A-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B6AFE7F7-56AC-E211-93E0-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B83A5EE3-53AC-E211-806B-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B88A8304-54AC-E211-94F1-002618FDA207.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/B8EFDB2E-58AC-E211-A718-002354EF3BE1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BA354F12-5FAC-E211-8CDF-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BAB7AD6F-58AC-E211-9EFD-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BC8FBEB0-54AC-E211-ADC5-003048FF9AA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BCE8440C-56AC-E211-BE34-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BE110CD7-57AC-E211-AD73-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BE64A244-56AC-E211-9C7E-003048678FF6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BEB082B3-56AC-E211-A569-0026189438E1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/BEECDB48-5EAC-E211-8155-003048FFD736.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C0D1A05B-5EAC-E211-B4FC-002618FDA248.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C20B458F-5EAC-E211-96A2-002618943857.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C2423D21-57AC-E211-ABF8-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C4316C74-70AC-E211-B7B3-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C46ADEC3-57AC-E211-BAF9-00261894393B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C4717530-75AC-E211-B5C6-00304867918A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C4BF42F2-56AC-E211-A5DE-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C4D51B83-5EAC-E211-A8C3-003048678B92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C652A572-57AC-E211-874C-0026189438B5.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C6929FBD-54AC-E211-9B6A-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C6B06C1D-55AC-E211-B64C-003048678C9A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C6CD7497-6FAC-E211-9305-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C6E6BD41-54AC-E211-91BC-0025905938A4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C813DD47-55AC-E211-994D-003048678FF6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C8666450-54AC-E211-8916-003048678C62.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/C87240AA-76AC-E211-AFB6-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CA67BA6F-5EAC-E211-BC9B-00248C0BE013.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CA770255-8AAC-E211-8FC3-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CAC08606-6BAC-E211-8A8C-00261894398D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CAC58474-54AC-E211-91B6-002618943976.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CAC9D082-55AC-E211-B471-0026189438AB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CAD53B4F-8AAC-E211-B7CA-002618943966.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CC80F5EE-74AC-E211-968C-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CCB17285-58AC-E211-ACA1-003048FFD752.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CCDDA4A6-56AC-E211-A22F-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CE16E0E0-69AC-E211-B0CC-00248C0BE014.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CE21607F-5EAC-E211-92B4-00261894398C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CE4725BE-57AC-E211-9393-002618943906.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CECC38C1-57AC-E211-82AB-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CED31DDD-54AC-E211-9C55-003048FFCC1E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/CEEF3AFC-56AC-E211-844D-002618943970.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D089D57B-55AC-E211-98D2-0026189438D2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D09D8AAB-57AC-E211-81F0-002618943880.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D0A70250-54AC-E211-B502-003048FFD756.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D0E8329F-57AC-E211-952A-002618943836.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2598F6B-57AC-E211-B6E2-002618943858.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2732C63-58AC-E211-BB41-003048678B86.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D27B48FB-55AC-E211-BA75-00261894388A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2A6AA1A-72AC-E211-AD8C-0026189438A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2E5DAAF-5EAC-E211-BB2B-002618943963.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2EC4B8B-6FAC-E211-A1A0-002618943933.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2EDDD63-5EAC-E211-BD0C-003048678E6E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2F64700-54AC-E211-8872-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D2F72B3D-55AC-E211-89E5-002618943911.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D41AE36B-54AC-E211-806D-003048678B38.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D42C5182-5EAC-E211-833F-002618FDA237.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D47F5E73-58AC-E211-BDA7-003048FFD76E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D4B5F832-55AC-E211-B6EF-002618943875.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D4D8BE63-72AC-E211-B6B0-00304867918A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D4DD32C7-5EAC-E211-BCE2-003048678EE2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6347196-6BAC-E211-99FC-0026189438F4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6362A98-5EAC-E211-8AFF-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D63642B3-58AC-E211-8C4B-003048679080.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D65AE618-58AC-E211-BB79-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D65C49B7-5EAC-E211-AE44-002618FDA207.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6670DC0-54AC-E211-87ED-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D67CC677-6AAC-E211-80F8-003048678F84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D68BD8BC-54AC-E211-8BB5-0026189438D3.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6A064BC-54AC-E211-8586-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6A92AD2-56AC-E211-B955-00261894388B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6CDBF75-54AC-E211-985E-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D6CE913A-6CAC-E211-AA69-003048678E52.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D821C04D-58AC-E211-8F19-00261894393E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D835DD75-54AC-E211-A2B7-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D851FB3B-54AC-E211-B1D5-0026189438D8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D853BAFE-57AC-E211-B07E-003048FF9AA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D871F0F1-56AC-E211-9AA8-003048FFCB9E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D87E9AE0-56AC-E211-A74E-0026189438CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/D8A460C1-57AC-E211-B311-002618943809.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DA467D4A-5EAC-E211-9027-00261894396E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DA811911-6BAC-E211-A1C9-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DAA6182D-58AC-E211-8583-0026189438FD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DC3488C4-57AC-E211-B64B-002354EF3BDB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DC4DD647-5EAC-E211-B56B-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DCD6FA94-54AC-E211-9C00-003048FFD7C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DCE20112-83AC-E211-96DA-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DEB212BA-57AC-E211-A314-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/DEC69024-56AC-E211-8D81-003048FFD796.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E028795C-59AC-E211-AF90-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E02B0C23-70AC-E211-BF8D-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E03B919A-5EAC-E211-9262-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E0C78520-58AC-E211-B202-003048FFD720.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E0F452D5-58AC-E211-86CE-002618943950.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E21BE9A1-5EAC-E211-B734-003048FFCB8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E22B1E03-6DAC-E211-B02A-002618943896.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E2A5F349-5EAC-E211-B7C2-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E46C3F8F-5EAC-E211-832A-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E491EA7D-54AC-E211-8251-003048FF9AA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E4F3FA58-19AE-E211-87DD-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E6223711-55AC-E211-907F-0026189437FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E65DCA25-5EAC-E211-B6C6-003048FFCC1E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E66FFCE9-55AC-E211-B60E-0030486792B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E6867AA3-57AC-E211-AAC5-002618943958.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E6C1C10D-6BAC-E211-B75E-00261894398D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/SingleElectron/RECO/22Jan2013-v1/10000/E819019E-55AC-E211-8561-003048FFD770.root'

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
process.ecalTimeEleTree.runNum = 99999910
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

