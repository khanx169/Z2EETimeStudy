import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D4D20175-AC60-E211-A233-003048678F74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D4D87237-AA60-E211-B102-002618943916.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D4FA4ACE-AA60-E211-801A-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D6515605-BA60-E211-A658-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D663B083-C060-E211-A18A-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D67B8039-9B60-E211-A112-003048D15E02.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D6B4CDCD-CB60-E211-9074-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D6FF424D-C360-E211-8031-003048679080.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D80A575C-A260-E211-A689-003048678FE0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D876EFAD-A660-E211-80F2-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/D8D5D41F-C860-E211-BE98-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DA0C5862-A660-E211-986A-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DA109685-BE60-E211-B395-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DA767A35-C460-E211-9BA4-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DA838711-BF60-E211-8E67-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DA96C7A0-AF60-E211-9C85-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DAAC3721-A460-E211-984C-00261894388F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DAE7E2AC-9660-E211-A294-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DC384D18-B960-E211-8170-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DC41AA83-B060-E211-8659-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DC901211-B760-E211-AA7A-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DC961D6E-C660-E211-9516-0025905964A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DCD95B80-B060-E211-8D50-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DE0D215C-A260-E211-BBCF-003048678BC6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DE4767BA-AA60-E211-A175-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DE4ACBA3-A060-E211-A04E-003048678FE0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DED836B0-A460-E211-B1C4-00304867D836.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DEDC263E-B460-E211-80F6-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DEE3A038-CF60-E211-9F7D-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/DEEAE9ED-AB60-E211-9FC6-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E00154B4-A860-E211-AABD-002590596490.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E00BD497-A960-E211-8A57-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E07FC6CC-B860-E211-A88C-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E08F2F5A-C160-E211-BDED-003048678ED4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0918EBD-C060-E211-A630-002618943800.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0A3B5C7-B460-E211-9F69-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0C493F8-CA60-E211-A0F0-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0C544AB-CA60-E211-B76E-0026189438CF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0D335C9-BC60-E211-B4A6-0025905938AA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0DACBF5-9860-E211-B187-00248C55CC40.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0E70533-B060-E211-8D36-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E0F76CA7-9C60-E211-8120-003048678A80.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E22A989C-AB60-E211-A56E-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E244D9E2-A560-E211-B7BE-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2570D5F-A660-E211-93EB-0026189437EC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E26A723F-A360-E211-A6AD-0026189438E8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2A2B500-9960-E211-85D7-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2A31A37-C060-E211-B392-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2A5C5C8-C260-E211-AA5D-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2CAC4C1-BE60-E211-AE2E-002618943875.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2E372D4-9960-E211-9BBC-003048678F78.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E2E5E95B-B760-E211-8D2E-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E40C7ED4-A960-E211-8E2C-002618943945.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E41A299F-AD60-E211-97DB-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E41F4AD6-AA60-E211-80A0-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E61D0835-B660-E211-A424-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E66FCD7A-9F60-E211-9C3E-00261894387D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E6D17B95-B060-E211-AFDF-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E6F993B5-AA60-E211-84C7-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E8043612-9A60-E211-9FC2-003048678B04.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E8118041-A560-E211-B13A-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E82FAB01-AB60-E211-844A-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E856D3C9-B660-E211-B753-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E877308A-A560-E211-B0AB-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E8D01A3F-A360-E211-B4B1-003048678B1A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/E8FBA1A3-AF60-E211-9354-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA12DA22-9460-E211-9771-002618943925.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA1AE475-AC60-E211-8075-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA31665F-A260-E211-B9F3-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA57A386-9560-E211-BD54-00261894398C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA88838A-A360-E211-B060-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA91CAD8-9160-E211-8121-00261894387A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EA9FDB1F-B360-E211-A9C0-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EAA8A4D9-AE60-E211-91E4-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EAE74687-A760-E211-B240-002618FDA204.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EAF22B13-BD60-E211-B94F-003048FFD744.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC0D6913-B360-E211-857D-0025905964C0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC327E10-BD60-E211-AC88-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC417E5D-BB60-E211-A0C7-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC594B4F-AD60-E211-A388-003048678B0C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC77D3DF-7660-E211-95BA-00304867901A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC7AE683-B260-E211-988E-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC88361C-9460-E211-A8C9-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EC9BA877-C260-E211-B6D2-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/ECB7D4C0-AE60-E211-B53D-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/ECEDE7D7-9960-E211-81D9-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/ECF98E80-9D60-E211-A304-002618943921.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EE96FBD4-C960-E211-9062-002590593878.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EEA1C136-A160-E211-BF0D-00261894398A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/EEB9D251-AD60-E211-A32E-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F00A62EB-BD60-E211-AE9C-0026189438C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F015A3F4-A460-E211-BCAD-003048678FA6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F02280AA-9660-E211-8EC7-002354EF3BDD.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F065C668-CC60-E211-9432-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F093B7DF-D660-E211-8789-003048FFCB96.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F0ABE014-A260-E211-B467-002618943975.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F0B53135-C260-E211-A20F-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F0BB3139-AE60-E211-9031-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F0D17BCA-B260-E211-A4E8-003048679168.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F0F0FC9C-A960-E211-A1F2-002618943916.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F2174667-B360-E211-8184-003048FFD760.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F23FF1F7-BD60-E211-B388-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F24515FC-B760-E211-A672-00259059642A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F247AAF4-C860-E211-808E-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F24DAADE-BA60-E211-AEB2-0025905964C4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F274C91B-B560-E211-A154-00259059391E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F2A658A7-9A60-E211-945D-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F2B4AB7F-B660-E211-8E9B-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F2BDE47E-AC60-E211-8DE3-0025905964BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F2EEC485-9960-E211-99AC-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F4779BB0-9E60-E211-AC22-002618943944.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F4981497-C360-E211-900C-002590593876.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F4D949C6-B460-E211-9FFF-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F607A80B-AF60-E211-B029-003048FFCBFC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F64A11CB-A760-E211-87DB-003048678F74.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F657D289-9360-E211-92AE-003048678F78.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F6865172-AC60-E211-8177-003048678BEA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F6B5D0B6-AA60-E211-8781-00304867BFB0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F6D21BE9-BF60-E211-9DF8-0025905964C2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F6D68CCD-B660-E211-8AF8-0025905964CC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F8356A93-CB60-E211-8ACC-003048FFD79C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F8563E9A-C560-E211-8FF9-003048FFCC1E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F86AE3D0-BC60-E211-BF43-00259059642E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F8B290A2-A060-E211-98F9-00304867BEC0.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/F8FA5597-E960-E211-B828-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA319732-A260-E211-96C6-003048678B38.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA3379A3-B160-E211-B8BC-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA5561AC-EE60-E211-8AD1-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA73AF09-AD60-E211-87FD-002618943868.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA77B2A9-A660-E211-8457-003048678CA2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA84CEE7-8F60-E211-874E-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA970B37-AA60-E211-A992-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA97EA20-B861-E211-B860-003048FFCB6A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FA9F77B4-A460-E211-9E51-003048678B84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FACAFD0A-B160-E211-AA5F-0026189438CB.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FAD6B806-AD60-E211-8658-002590593902.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FAD934ED-CE60-E211-B4CD-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FC038A5D-B560-E211-91EB-002590593920.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FC107D86-BE60-E211-BDE0-003048FFD744.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FC2D6B35-9B60-E211-BE4D-002618943831.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FCF2071B-CC60-E211-AE81-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FE5166FC-A860-E211-8D16-003048678FE4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FE70191C-A860-E211-A479-003048FF9AC6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FE9BDD54-D060-E211-B883-0025905964B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10000/FEAB45A0-C160-E211-B6DD-002590596498.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/12463AF6-8C60-E211-B64D-003048FFD732.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/1E897B10-8D60-E211-BBAD-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/20A0606C-8D60-E211-8A3F-002590596468.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/22F7771A-8D60-E211-899F-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/2AA7C7A9-8C60-E211-969F-002618FDA259.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/3AC0341D-8D60-E211-95A3-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/3C22D112-8D60-E211-AFF6-003048FFCB84.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/46E2B5F0-8C60-E211-AE2B-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/52BADF00-8D60-E211-A5A2-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/5C38D41F-8D60-E211-A710-0025905822B6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/5C505471-6765-E211-8246-00261894395F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/6CD27213-8D60-E211-B60F-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/76D6B454-8D60-E211-A8A0-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/98836F57-8D60-E211-9A99-0025905964BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/E2514FE2-8C60-E211-A333-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/F0A530D6-8C60-E211-9DB5-003048FFD796.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012D/DoubleElectron/RECO/16Jan2013-v1/10001/F8CFA63C-8D60-E211-B8C2-0025905964B2.root',
# RUN2012 C
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00132192-DE67-E211-B4E4-003048FFCBA4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/001B197A-E267-E211-A54F-003048678B00.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/001F7329-DF67-E211-B1E6-003048678ADA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0096FF5D-3F75-E211-AA30-003048D15DDA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/009BAE5A-DD67-E211-B0CE-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00B6A5E3-3E75-E211-B395-00248C0BE005.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00BD0DE9-E167-E211-B124-0026189438ED.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00BECC38-E167-E211-A352-002618943905.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00C69C08-E467-E211-9175-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00DC2730-DF67-E211-81AE-003048FFD71A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/00E6724A-E367-E211-875E-0025905964A6.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02055588-DE67-E211-B3EB-002354EF3BE1.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/021C9769-1970-E211-BBB8-003048678C06.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/021E363B-E667-E211-AECC-002590596486.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0237FAA1-DE67-E211-AFF5-00304867BED8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/024EED74-3F75-E211-8CE7-00261894394D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/026907FF-DD67-E211-AF3E-003048679084.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/029015B9-DF67-E211-83FE-002618943910.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02B8867E-4B70-E211-9EBD-002618943838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02C0D9B1-3F75-E211-817C-00261894396F.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02CF0695-E267-E211-B365-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02D00681-E167-E211-922B-003048FFD7BE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02DA087E-E267-E211-8F85-003048FFD728.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/02F271D0-E667-E211-B0C4-002618943974.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04069784-3F75-E211-A024-0025905964B2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04258A37-DD67-E211-9397-00304867D838.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/042CFFA0-3F75-E211-84D8-003048678B7C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0446B277-E067-E211-9C0F-002618943961.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/044C9E79-E267-E211-8A05-002618943919.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/045828E9-E167-E211-8D3B-00304867918E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04790A35-3F75-E211-87B3-002618943884.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0492F82E-DD67-E211-A41D-003048678E6E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04A15C39-E267-E211-B199-003048FFD75C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04C01B3D-3E75-E211-979A-003048FFD71E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04C6E026-3E75-E211-A88E-003048678EE2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04C9DEAB-B167-E211-98DC-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04DF8F7A-E467-E211-A609-0025905938B4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04E5AD30-E267-E211-A34A-002618943960.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04FB1474-E567-E211-BEEB-0030486791DC.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04FBB052-3F75-E211-AABF-003048678DA2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/04FDAE1D-E667-E211-A938-00261894391B.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/06024779-DC67-E211-AAD4-002618943924.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/060642B8-1870-E211-8856-002618943946.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0606F17E-3E75-E211-9A5D-002618FDA211.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/061EBBC7-1870-E211-BFC3-002618FDA277.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/066C931D-E167-E211-817C-002590596484.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0672E581-E367-E211-B844-002618943874.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0681FF3D-E567-E211-8C39-002618943946.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/06AD45D3-E267-E211-B427-00261894394D.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/06B69CE0-1770-E211-BB22-00248C55CC97.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/086A4D7A-E367-E211-B1FB-002618943963.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08798A07-E267-E211-A534-003048678B70.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08ACCD22-E267-E211-844B-003048FFCBA8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08B24C7F-E767-E211-B4E5-00261894387C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08CBBE6F-E467-E211-892C-003048FFD736.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08E3E9E4-E567-E211-A2D4-003048FFCC2C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08E42C3F-E367-E211-988B-003048FFD744.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/08E4D342-E367-E211-A801-003048FF86CA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0A00436A-3F75-E211-A7AD-0026189438BA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0A383936-E467-E211-B70A-00261894383C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0A6B9882-E767-E211-90AD-00261894390A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0A6ED8B1-4E70-E211-8F08-0026189438EF.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0A8EA7D6-E367-E211-870C-003048D15D22.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0A8EE931-3E75-E211-A0A2-003048678B7C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0AABBF88-E367-E211-8BDC-003048FFD7A2.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0AC3C3B4-6868-E211-877B-003048678B7C.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0AD5A03C-3F75-E211-B355-003048679248.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0AE719DE-E367-E211-8257-003048678B5E.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0AE7E454-E367-E211-A072-0026189438DA.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0AF2922D-3F75-E211-A68A-0026189438D7.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0C0C30ED-E267-E211-85E0-0025905938D4.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0C2C3AB8-DE67-E211-AF57-003048678FB8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0C366C3F-E467-E211-9226-00304867920A.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0CB142EA-E767-E211-8D5C-002618943970.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0CB92C66-3F75-E211-875C-003048678FB8.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0CD4D442-DF67-E211-8B2E-003048D15E14.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E0A6A0D-E367-E211-8FF2-003048FFD744.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E4FA40F-DF67-E211-B5BF-002354EF3BDE.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E5E568B-3F75-E211-9D30-002618943947.root',
'dcache:/pnfs/cms/WAX/11/store/data/Run2012C/DoubleElectron/RECO/22Jan2013-v1/20000/0E60CEE4-DD67-E211-A403-003048FF9AA6.root'

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
process.ecalTimeEleTree.runNum = 99999914
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

