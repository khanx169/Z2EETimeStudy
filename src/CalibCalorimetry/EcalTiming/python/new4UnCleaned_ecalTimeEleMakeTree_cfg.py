import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/82A2C29B-BF60-E211-9AEA-0026189438FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/82D0C3A0-BD60-E211-BE7A-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/82D239BC-AC60-E211-B238-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/82E09A83-BC60-E211-A4AF-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8406445B-A060-E211-BACD-00304867C0EA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8409DBF1-9C60-E211-BFC9-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/841FFEA2-AD60-E211-BEDC-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/84230044-A760-E211-A2E3-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8461DF3B-9760-E211-83DA-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/84717C24-AC60-E211-88FB-003048679000.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/848792A5-A960-E211-A158-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8487E0B2-9E60-E211-88E3-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8492FE69-9660-E211-9AFB-00304867901A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/84AE5DFC-A660-E211-B5BC-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/84B506DD-9D60-E211-8A30-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/84CCDCFD-A860-E211-8A76-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/84E2CB60-B960-E211-8EA8-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/863800CF-9B60-E211-B11F-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/865C20F0-9A60-E211-8B08-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/86629FAA-9260-E211-B3BB-003048678F92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/86692231-AA60-E211-A1A5-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8693B86F-C460-E211-BA06-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/86B34FC7-B060-E211-87F1-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/86E27DB8-D060-E211-9ADE-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/88270037-A760-E211-9C0F-003048678A7E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/88644237-9B60-E211-8FEE-002618943947.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/88682CA4-A960-E211-861E-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/88A99A7D-BC60-E211-9BA4-002618943935.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/88F00F0D-AD60-E211-B83C-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8A01B4A3-A060-E211-8980-003048678FEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8A0E825A-B960-E211-9BFA-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8A67F4D6-A360-E211-87C3-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8A6DBAD5-B060-E211-8998-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8A8A349E-BF60-E211-ADA2-0026189438B1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8A8F5E2A-AA60-E211-AAD1-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8AABD162-AB60-E211-BE97-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8AAE99CD-A760-E211-BC98-0026189438E2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8AC8B9C1-A160-E211-A251-003048678FEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8ADCD236-B460-E211-9E63-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8C273D64-A260-E211-827A-002618943985.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8C2A0C69-A860-E211-9971-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8C395C86-D160-E211-A463-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8C3BFAC0-C460-E211-A66D-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8C738CB8-A860-E211-AAA3-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8E113965-A060-E211-94AC-003048678F92.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8E32D75A-B960-E211-8A8F-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8E32D889-A760-E211-BF52-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8E659565-A460-E211-902B-003048678B06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8E674D49-C560-E211-AF52-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8E8EF806-C760-E211-8083-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8EBDB8E2-AB60-E211-8843-002618943984.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8EBDECE1-CD60-E211-994D-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8EC32911-BB60-E211-8A72-003048678DA2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8ECC1E66-CC60-E211-9CCB-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/8ECEEF80-A760-E211-8916-003048D15E2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/902578E6-AB60-E211-A5A0-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/902D08DB-C960-E211-9A74-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/90369E05-AB60-E211-AACA-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/904672FD-A660-E211-94EE-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9079E6FF-A260-E211-9435-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/90FC6B4E-AB60-E211-8F8C-002618943867.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/920D58B2-D960-E211-A748-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/924A7BC8-D160-E211-AB8C-003048FFD770.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/924B2B8E-AB60-E211-985C-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/924F52DF-7F60-E211-A511-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/92EAE585-A560-E211-80A1-002618943975.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/94410141-9960-E211-B904-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/945AC03C-9D60-E211-9C36-003048678B12.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9460C5D3-A560-E211-9ECF-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/946EC5C8-A760-E211-833D-003048678A7E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9495E68A-9360-E211-870A-003048678B18.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/94C64482-9960-E211-99D4-002618943947.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9600489D-AD60-E211-B407-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9697BA6E-AA60-E211-98E1-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/96ABEC16-D060-E211-93D9-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/96EAC438-A160-E211-BC08-003048678FE0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/983274F1-9E60-E211-BE58-002618943935.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9834F265-A060-E211-AEAC-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/987557C5-9F60-E211-BADF-00261894398C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/98D293CC-AE60-E211-98AB-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/98F3A734-BC60-E211-A247-0025905938AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9A50FEA5-B360-E211-AC29-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9ABF1E3E-A560-E211-BC8A-003048679166.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9AE30F5D-9E60-E211-B1E9-002618943935.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9C48309E-AD60-E211-834A-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9CC68A40-9760-E211-AE5F-003048678FA0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9CC93B82-B060-E211-8378-0026189438C1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9CF645D3-A560-E211-8BAD-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9E074937-9F60-E211-8547-00261894388D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9E26AC2B-C460-E211-9E6E-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9E3BCCB0-C860-E211-BFA8-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9E4ADBF8-B760-E211-9A4A-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9E8B7119-9860-E211-BA3E-003048678E6E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9ED2E8FC-AA60-E211-ADCE-002354EF3BD2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9EF41C39-9B60-E211-8394-0026189438C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/9EF96E84-A360-E211-900B-003048678FEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A0130AAF-A860-E211-9A39-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A02F9C21-B560-E211-8B43-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A034265B-9C60-E211-AB30-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A06C3FB9-C460-E211-BB3B-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A0CAB6E3-AB60-E211-8F98-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A0E2FEAB-9C60-E211-AF13-003048678A7E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A219051B-A860-E211-8661-0026189438F9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A24CE7C0-A660-E211-80F1-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A26C3EB4-B960-E211-942A-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A28E909E-BF60-E211-B59C-003048678F02.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A2A82EA4-B160-E211-AEC5-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A2B9FBFC-A260-E211-BBB7-0030486792AC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A2D1CB94-CD60-E211-8731-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A2E1CFE3-AB60-E211-96C0-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A43A13D7-C960-E211-83CD-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A45E494F-B660-E211-A2C5-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A47A0D24-A260-E211-B0CA-003048678BAA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A63C1E0B-D260-E211-B63C-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A6546FA7-9A60-E211-A136-003048678FA0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A6E51604-B060-E211-AA37-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A6F78FEB-AB60-E211-8BD5-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A801E646-9960-E211-A419-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A80CABEC-B960-E211-B86C-002618B27F8A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A811045F-9E60-E211-8868-00261894389D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A86782F1-AF60-E211-AD02-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A87D5677-AE60-E211-A5F8-002590593872.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A8C1326E-C460-E211-A075-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/A8EDB29F-AF60-E211-878C-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AA243B34-AA60-E211-843D-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AA722EFA-7F6A-E211-AFB9-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AA9FD4C5-AE60-E211-AC4B-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AAB5D036-AE60-E211-93E7-003048FFD740.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AAC1A118-A460-E211-A4DD-0026189438E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AAC4815F-B160-E211-B2BE-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AACFD9AB-B160-E211-9C77-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AAD1AC3B-A760-E211-A147-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AC19A384-A560-E211-9337-003048678FA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AC4F3F43-C960-E211-8A8F-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AC821070-A260-E211-8320-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AC96D90E-BD60-E211-BA5C-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/ACA6F741-CF60-E211-8366-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/ACE8B017-D660-E211-B076-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AE5F9FCB-A160-E211-9414-003048678FE0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AE691CED-B760-E211-BEC3-00248C0BE005.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AE8EC9FD-A260-E211-8DEF-003048678FE0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AEA0E5B2-A660-E211-8832-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AEC181F0-9C60-E211-95EF-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/AED66130-C260-E211-A7CC-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B0055FF2-BD60-E211-B0DD-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B02AEEEE-9E60-E211-850B-00261894389D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B059C1CE-9960-E211-94C5-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B06AAE88-B460-E211-B49B-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B07B4D99-AD60-E211-8FB7-003048679000.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B0A7C380-B060-E211-A303-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B0B86B5D-A260-E211-8422-0026189438E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B0F5B085-9D60-E211-BE9E-003048678B34.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B2254CEC-A060-E211-BC97-002618943966.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B2C057CD-B460-E211-B1F9-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B4233646-A360-E211-AA79-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B435A15C-BF60-E211-9F80-0025905964B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B457CFC6-AA60-E211-88BA-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B48ACADE-C360-E211-8F36-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B4926BAD-9C60-E211-91E8-003048D15DCA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B499A036-9B60-E211-AC7D-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B499FD8F-CB60-E211-94A7-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B4FCABF1-9E60-E211-A80B-003048678FA0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B62494D3-A560-E211-A331-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B653269F-AF60-E211-A265-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B654C0D8-A360-E211-A5E5-002618943972.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B6C33FCB-9F60-E211-8E54-0026189437FA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B6C5ED94-AD60-E211-87C9-002618943971.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B6D23260-B360-E211-B0EA-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B6D99041-A960-E211-894F-003048678F74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B82CFA6F-C660-E211-A1C4-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B843EF5E-A860-E211-885C-003048678BEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B855222A-AC60-E211-98BB-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/B8787B87-B460-E211-922A-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BA162FB1-B960-E211-80E4-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BA58B214-9660-E211-8064-0030486792F0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BA610835-C660-E211-B346-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BA6B9A93-A360-E211-A603-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BA75F28B-8A6A-E211-864B-003048678B86.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BA875919-A260-E211-A385-003048678B3C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC00743A-AA60-E211-9378-0026189438FE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC2A4DC6-DE60-E211-8757-003048FFCBB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC46CC87-A560-E211-889D-00304867BFB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC70229B-AD60-E211-8192-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC7B7CA2-D260-E211-A21E-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC88BECE-AC60-E211-A9C9-003048679000.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC8F265F-B760-E211-9BEC-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BC919A7C-A160-E211-941C-002618943975.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BCAFAC54-AD60-E211-9B80-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BCB32B9E-A960-E211-B118-0025905964BC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BCDBA9F2-9060-E211-9725-00304867904E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BCF844C4-AC60-E211-8A2D-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BE2A4CFA-CC60-E211-9262-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BE9DA5CB-A760-E211-A5F5-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BEEA30E9-B160-E211-9C15-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BEECD6F8-A460-E211-BADA-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/BEFC7017-B960-E211-AD0D-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C02E1601-AB60-E211-B7E0-003048FFD736.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C03709F2-A460-E211-9297-002618943896.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C039248F-A960-E211-96D7-00304867924E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C04481D3-E360-E211-9D77-003048FFD754.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C06A2663-A260-E211-BFC4-003048678FC4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C0E56C12-A060-E211-85C4-002618943985.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C20F4817-B760-E211-9755-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C2702322-9860-E211-8CAD-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C2A3453E-9560-E211-B733-003048678FB8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C2D4E33E-9360-E211-8C81-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C419624F-7760-E211-A542-003048678B0C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C43E003A-BA60-E211-9B4B-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C45744A8-B760-E211-ADA1-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C45A14CA-9F60-E211-A105-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C48CD3F2-9E60-E211-A068-00261894398A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C4B43DF7-A860-E211-8606-003048678B34.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C4BF78F4-9260-E211-8BC4-003048678F8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C4D6165E-9C60-E211-A553-00261894387A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C4D63A60-A860-E211-AD7A-003048678FAE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C4D914FE-AA60-E211-BA10-0026189438F9.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C4E6B2FA-B760-E211-AC1D-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C64903B4-C660-E211-9DB6-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C64B5A3E-A760-E211-BD47-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C67320FF-A260-E211-A6A1-003048678FC4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C68CABA3-A060-E211-8F26-003048678B1A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C6C4C58A-BC60-E211-9C47-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C6FC543A-BE60-E211-8922-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C8065CAC-9860-E211-8258-003048679006.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C89D9B15-B360-E211-9F8F-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C8A483EE-CC60-E211-B614-002618FDA279.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/C8CBA945-AB60-E211-B6A4-00261894389E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CA58D7C6-9F60-E211-B21C-00261894389D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CA784935-9F60-E211-B6EA-0026189437E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CC0E6DC6-DE60-E211-AF49-003048FFCC0A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CC5C7C56-BF60-E211-A08C-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CCB928D7-A360-E211-8462-003048678FA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CCC49828-AA60-E211-9503-002618943916.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CCEF59C9-C260-E211-AC20-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CCFBF4A4-9A60-E211-9773-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CE0F355A-B760-E211-A192-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CE75CEDB-A960-E211-9DA8-0025905938AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/CEA006AE-9C60-E211-BB47-003048678E52.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D02DEB94-AB60-E211-87A6-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D04D55F1-B560-E211-AF63-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D0D201BF-AC60-E211-BA6C-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D2026FEB-BD60-E211-9ED4-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D253C617-9460-E211-8D68-003048678F8C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D270E36B-A660-E211-995F-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D2947D3B-BE60-E211-8DEF-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D2DC6F2E-AA60-E211-B321-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D2F393A2-A060-E211-AADA-003048679244.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D40A25E9-A060-E211-A24C-002618943985.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D418E7EE-A260-E211-A699-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D444BC45-CD60-E211-A61D-002590596484.root'


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
process.ecalTimeEleTree.runNum = 99999913
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

