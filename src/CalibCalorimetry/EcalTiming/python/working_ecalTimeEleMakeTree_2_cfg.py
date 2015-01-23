import FWCore.ParameterSet.Config as cms

process = cms.Process("TIMECALIBANALYSISELE")

filelist = cms.untracked.vstring()
filelist.extend([
#'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/548BD0EF-5F67-E211-AB31-00261894393F.root'
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/54C2D4FC-8A67-E211-89C3-002590593902.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/54D479E6-CB67-E211-83F8-0026189437F2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/560B0D07-7167-E211-A89B-0026189437F5.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/56986818-6867-E211-BF38-0025905964BC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/56988744-5E67-E211-9A84-003048FFD7C2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/569AD667-8F67-E211-A396-003048FFCB84.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/56A3B647-7667-E211-AAB2-002590596490.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5809F06B-7467-E211-848A-00259059642E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5843A7EF-7C67-E211-A5DD-0026189438D9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5872DC81-5967-E211-8494-0025905964BC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/58A36E15-7B67-E211-A617-003048FFD79C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/58F4CE0F-6167-E211-B4EB-00261894385D.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5A305564-7A67-E211-ACAA-0025905964BA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5A480B15-5167-E211-8381-003048FFCBFC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5A6C81DA-5F67-E211-B210-002618943920.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5A809FFA-8F67-E211-A015-00261894389E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5AB0EA0E-4767-E211-BAB6-003048678A80.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5AE1470D-9767-E211-AEEB-00304866C398.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5AF1A49D-B767-E211-AE01-003048678FB4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5C05CECE-B067-E211-97C1-0026189437ED.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5C08BA89-6B67-E211-BB10-0025905964BA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5C250C68-D767-E211-A724-00304867924A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5C33C4DC-8867-E211-ADDA-00261894385D.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5C69EFAE-5F67-E211-BA41-003048D15DCA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5C8415B0-5467-E211-85FE-0026189438C9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5CD6AB87-5867-E211-8C1F-0026189438FF.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5CD82A1F-9A67-E211-9F87-003048FFCB9E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5CDCD112-5667-E211-B964-00261894392D.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5CE04125-7067-E211-9C58-002618FDA211.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5E0AA310-5C67-E211-BAEE-003048678B0A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/5EC5298E-7E67-E211-9793-0026189438FD.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/603C0F17-8D67-E211-80AD-00261894387E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/60421D41-5E67-E211-8DAC-00248C0BE013.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/60CD1276-8F67-E211-9E69-003048FFCBA4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/60D41BCB-6167-E211-B09A-003048FFCB96.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/60E6A4B2-9367-E211-BB45-00261894391C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/60E85D36-9667-E211-9182-002618943932.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/622CB03F-5E67-E211-962F-0030486790A6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/625B0DEC-6167-E211-9E37-00261894397D.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/62A5CAFC-8067-E211-846C-002618943836.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/62AA6247-8067-E211-BEE3-003048F9EB46.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/62BA2BA4-9A67-E211-9323-003048FFCC2C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/62CA78F8-6B67-E211-AFF0-0026189438B0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/62D1EC61-6E67-E211-B88B-0025905938B4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/64293A73-9C67-E211-A0E9-002590593872.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6446BA58-7467-E211-A168-002590593920.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/64E7B623-9867-E211-8A6C-003048FFCB6A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/64E8470F-8E67-E211-876A-00304867BED8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6625B166-9D67-E211-863F-00304867918A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/662B7801-8167-E211-AFB6-003048FFCB6A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6646B5F6-6A67-E211-BF55-0025905964A6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/66629302-6567-E211-9E22-002618943845.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/666D8949-7C67-E211-9AE4-002590596468.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/668AA557-A367-E211-B60A-0026189438E1.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/66A62FC1-6167-E211-B8F1-002618943858.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/66B6F18E-5867-E211-9A37-0026189438F9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/66DE45E9-8B67-E211-B478-002618943984.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/66F2861F-8367-E211-B2B0-0025905938D4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/680C3B69-0468-E211-B5E1-0025905938A4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6A9D279A-9A67-E211-A9D1-002618FDA250.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6AB6D0FF-8167-E211-A850-002354EF3BDC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6ADA1BFA-7267-E211-86A4-00304867929E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6AE83FA9-4667-E211-8384-003048678BAA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6C289530-5567-E211-B4FE-0026189438A9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6C3EFD7B-B867-E211-B606-003048FFD7BE.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6C638141-5E67-E211-8785-0025905822B6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6C79DEAD-7967-E211-95E6-00304867C0EA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6C7B0542-7667-E211-B414-0026189437FC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6CD5EAF6-A967-E211-A05F-0026189438E4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6CD792DB-7567-E211-8702-003048D15DCA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6CEF0E11-7A67-E211-BFEA-003048678BC6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6E06B673-A767-E211-9FD9-0025905938B4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6E19663C-5867-E211-BEA0-00304867901A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6E2022D7-6367-E211-9B80-003048FFD740.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6E828C60-8167-E211-B11B-0026189438D6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6E869662-6267-E211-9189-002618943807.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6E86D7AC-B367-E211-B213-003048FFCBFC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6EA17EF9-9067-E211-8AB7-0026189438CF.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6EA908DC-8A67-E211-91A3-002618943956.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/6EB6B6D9-5967-E211-B322-00259059642A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/70979E30-8867-E211-9227-002618943914.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/70AD8BC2-9867-E211-A551-0025905964A6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/70CBBED4-8567-E211-9DD7-00248C55CC97.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/72091BFC-7B67-E211-A605-0025905964BA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7226F5D1-5967-E211-8852-0026189438DD.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/72362EAC-6367-E211-BCE7-002618943934.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7260C647-6A67-E211-8A70-0026189438CB.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/726DBD0D-6467-E211-BA01-002618943976.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/72A61927-A667-E211-A5EE-003048678FEA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7436003C-7D67-E211-8888-0030486790BE.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7448ACB1-6767-E211-859C-003048679012.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74702065-6867-E211-9356-003048FFD752.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/749582CB-C067-E211-9D1D-0025905964B2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/749EAA7F-B367-E211-8E33-0026189438EF.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74BABB22-9867-E211-85DE-002618943862.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74BD20BF-9867-E211-8D98-003048678BB2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74CE20F8-8067-E211-86E8-0030486790C0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74DAB855-7F67-E211-A95F-00304867924E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74DBBEA5-9B67-E211-97BD-00261894392D.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/74F82139-6067-E211-B2BF-00261894386A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/760C2B0C-7867-E211-8298-0025905964C0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/761085AC-5167-E211-8C00-0025905964B4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/761D63DD-5367-E211-9A9D-0026189438C9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/762324A7-9A67-E211-815B-0026189438F5.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/76562D85-C167-E211-A19E-003048FFD736.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7668918C-9467-E211-BAB1-0025905964B2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/76A70E8E-9567-E211-833D-0026189438EB.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/76C18A05-6067-E211-A8C8-002618943915.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/78640764-6767-E211-90DA-0026189438A2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/78D05E45-5E67-E211-BFB7-003048FFCC1E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/78D6045B-7467-E211-A52E-002590596468.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/78F1E24D-6A67-E211-9FA6-00304867929E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7A56CBDB-7867-E211-B596-002590596490.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7AABE980-8367-E211-835B-002354EF3BE4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7AEBB0D6-8567-E211-895C-00248C0BE005.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7AFF01B9-8467-E211-BF53-002618943975.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7C5DD23F-7D67-E211-A4C8-003048FFCC0A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7C6908E3-6067-E211-BE91-002618FDA211.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7C877938-5E67-E211-BEBB-00304867904E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7CFD08DC-5A67-E211-8924-0030486790BE.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7E1118FA-8067-E211-B3D1-0026189437F0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7E8D8D75-6467-E211-8056-0025905964A2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7E966CD1-9867-E211-849A-002590596486.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7EB4067E-8967-E211-A918-00304867BFA8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7EDF8C8E-9567-E211-86F1-003048678C62.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7EF3AB51-7C67-E211-85DB-00259059642A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/7EFB482D-9267-E211-94AD-002618943960.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/803A5CFA-5767-E211-88D8-00248C55CC62.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/806D32DF-7867-E211-8861-002590596484.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/809B4AE7-5267-E211-8A39-002618943967.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/80B487EC-8D67-E211-8CE5-002354EF3BD0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/80C01EFD-7067-E211-BC24-0026189438DC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/80D531B1-9E67-E211-9C02-003048678BB8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/80D91F1C-5B67-E211-B82F-00261894387A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/80E4B71D-7067-E211-93C5-002618FDA211.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/82103C95-5F67-E211-A464-002618FDA21D.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/821BB3C0-8467-E211-9379-002618943947.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/824DB984-8D67-E211-B6EF-002618943856.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8278894C-5767-E211-A109-003048FFD720.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8296E698-9467-E211-8823-002618943882.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/829C28BA-5367-E211-8BBE-0026189438D8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/82A9787F-5E67-E211-9CBB-0026189438E8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/82E2916C-5167-E211-89E1-00259059642E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/82E657C4-8D68-E211-9CBA-003048678FAE.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/841A9D12-A267-E211-A7A8-00259059642A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/842A972E-5967-E211-987D-003048678B34.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/842CB5E6-6C67-E211-AA3A-002590593920.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/843F2774-A067-E211-B582-002590596484.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/844E3547-9C67-E211-A5CB-0026189438E6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/84B23603-AD67-E211-8459-003048FFCB9E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/84BB042C-8A67-E211-934A-0026189438D9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/84DBDE3D-6067-E211-A5C1-002618943967.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8638A4E2-A067-E211-B8DE-0026189438A9.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/863CEFDA-8B67-E211-B7BD-0025905964BC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/864880BB-8667-E211-AF18-003048678B30.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/86EE2A41-A667-E211-AE04-003048678E92.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/88569834-5E67-E211-A79F-003048678B84.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/888104F6-9667-E211-806A-002618943944.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/88814973-6667-E211-945D-0026189438B4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/88916E19-7767-E211-944A-0026189438DA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/889FE003-7167-E211-88BB-003048FF86CA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/88B86DC4-B467-E211-9B45-003048678B5E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/88C0CAAF-A067-E211-BE2D-003048678F8E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8A52317A-4567-E211-81B4-002618943900.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8A527AF0-9967-E211-A523-003048678FF8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8A7B2599-9A67-E211-9FA3-00261894394B.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8AC9F4B1-7367-E211-A249-00259059642A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8C66782F-8867-E211-8BFC-002618943972.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8C68FBC0-9467-E211-BF7C-00304867BF18.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8C7D12FA-7567-E211-ABED-003048678B5E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8C80AD20-8467-E211-9DE0-0026189437FA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8C947B3D-8A67-E211-821E-002354EF3BDD.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8CA3B0AD-9E67-E211-9E80-003048FFCB9E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8CDEF4A1-6C67-E211-A715-00261894384F.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8CE860DD-6067-E211-A775-0026189438CC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8E1E0071-8267-E211-A841-0025905964B4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8E3F030C-7867-E211-B1DA-002590593878.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8E3FF4FA-8D67-E211-9F2D-003048678FAE.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8E4FB60F-5C67-E211-93D3-00248C0BE014.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8E6103C9-6167-E211-A92C-003048FFD754.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8E8E488A-9767-E211-A375-0026189438A7.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/8EEE1688-6B67-E211-83CD-003048678B1A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9032CC30-8B67-E211-A753-003048678DA2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/904E491F-7767-E211-8B75-003048678A6C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/90CE0F47-8B67-E211-AEC2-00304867915A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/90DFD40F-4767-E211-8E0D-0026189438DA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/926BC45F-9C67-E211-B1EF-0025905938A4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/92C6D0D0-8C67-E211-9ED8-00259059649C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/92D041E2-7867-E211-B7BA-003048678BAC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/92E79CCB-4567-E211-B9DB-0030486792AC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9410A05F-9C67-E211-A2EE-0025905964B4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/94285478-AD67-E211-BBBF-0026189437ED.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/944C9E02-5667-E211-8F70-002618943953.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/948AA962-5C67-E211-A557-00261894386E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/963687B1-5467-E211-BA6F-003048679236.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/964BA562-8E67-E211-AB53-002618943908.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9651909C-5E67-E211-AA6F-003048678E92.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/966C400D-6467-E211-AE43-0026189438A2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/967FF386-9267-E211-B3E9-002618943864.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9682BEF0-AA67-E211-99A3-00304867D446.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/96AAC222-8467-E211-87E2-002618943937.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/96E6D5E0-8A67-E211-8610-002618943860.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/981DCC90-A167-E211-9E70-0026189438E1.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/98B9BA54-8F67-E211-93CB-0026189438E0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/98D052F1-7567-E211-9BE3-0026189437FA.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/98D18C3A-6067-E211-B887-00261894383C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/98D28725-6F67-E211-AA8F-0026189438C0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/98E490C7-6167-E211-AD67-0025905964CC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/98F16A2F-5467-E211-95CA-003048678D86.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9A1374E4-6C67-E211-9378-00304867BFC6.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9A16BB57-6967-E211-88F5-003048D15E14.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9A24623E-7D67-E211-94D4-00261894383E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9A75AA36-8C67-E211-902D-00304867BF9A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9AA04564-5C67-E211-AA47-002354EF3BE1.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9AAB8320-7067-E211-8F95-003048FFD79C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9ABE7C68-6267-E211-BC24-0026189438E7.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9AC9F4B2-A367-E211-94A4-002618943885.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9AE089F2-6267-E211-A9DE-002590593920.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9C2336B1-6767-E211-B3A5-00261894384F.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9C2CDDE6-9067-E211-BB67-003048678FC4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9C43F30E-9167-E211-B8AA-002354EF3BD0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9CE5245A-8167-E211-8569-00304867918A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9CFCA064-8E67-E211-83B6-002590596484.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9E14DF97-B267-E211-9DA3-003048FFCBA4.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9E3CB87E-9367-E211-A91B-003048678E80.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9E560A72-4D67-E211-8C61-002590593902.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9EAEEC86-A367-E211-9919-002590593902.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9EB37CD0-5B67-E211-9FC7-002618943829.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9EB7605A-8067-E211-94A0-002590596468.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9ED90BBE-8667-E211-8225-003048678E8A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/9EE7FB0D-9367-E211-97C5-002618943944.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A01A5292-7E67-E211-9BD7-002618943982.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A03D6F2C-5967-E211-A197-00248C55CC40.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A0544EB1-5167-E211-9BAF-00304867D838.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A05917F9-4A67-E211-9EB7-0025905964C0.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A0A59E68-6267-E211-9898-00261894384A.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A20B7B77-6967-E211-A6F3-002618943882.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A224B9AE-9E67-E211-A785-003048679180.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A22B5D70-8267-E211-B491-002618943811.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A23FA375-6368-E211-B411-00261894386C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A2452D48-5767-E211-9FFC-002618943910.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A2AA0AC4-6167-E211-A2B5-003048678AE2.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A2B35AAF-5467-E211-A370-00248C55CC3C.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A2F7D045-5E67-E211-A4F4-003048FFCBA8.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A4513509-6C67-E211-AB92-0026189438AC.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A46D6A86-6B67-E211-A47D-00261894384F.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A47D4B4D-7C67-E211-B674-0026189437F5.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A4FD3649-6A67-E211-9BE1-002618FDA210.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A4FFA752-8E67-E211-9577-002618943963.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A615A910-7B67-E211-A87F-00261894387E.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A6576FC7-6167-E211-804C-003048FFD760.root',
'file:/hdfs/cms/phedex/store/data/Run2012A/DoubleElectron/AOD/22Jan2013-v1/20000/A6AFC00F-6167-E211-AB47-002618943985.root',


])





# Output - dummy
process.out = cms.OutputModule(
    "PoolOutputModule",
    outputCommands = cms.untracked.vstring(),
    fileName = cms.untracked.string('file:pippo.root'),
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
process.GlobalTag = GlobalTag( process.GlobalTag, 'GR_R_53_V18::All' )
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



#------------------
#Load PAT sequences
process.load("PhysicsTools.PatAlgos.patSequences_cff")
process.load("PhysicsTools.PatAlgos.tools.pfTools")
#
## THis is NOT MC => remove matching
removeMCMatching(process, ['All'])
#
#
## bugfix for DATA Run2011 (begin)
removeSpecificPATObjects( process, ['Taus'] )
process.patDefaultSequence.remove( process.patTaus )

#
###
process.patElectrons.isoDeposits = cms.PSet()
#
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
process.patElectronIDs = cms.Sequence(process.simpleEleIdSequence)
process.makePatElectrons = cms.Sequence(process.patElectronIDs *
                                        process.patElectrons)
process.makePatCandidates = cms.Sequence( process.makePatElectrons   )
process.patMyDefaultSequence = cms.Sequence(process.makePatCandidates)



# this is the ntuple producer
process.load("CalibCalorimetry.EcalTiming.ecalTimeEleTree_cfi")
process.ecalTimeEleTree.OutfileName = 'EcalTimeTree'
process.ecalTimeEleTree.muonCollection = cms.InputTag("muons")
process.ecalTimeEleTree.runNum = 999991
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
 #       'file:/hdfs/cms/phedex/store/data/Run2012C/SinglePhoton/RECO/EXODisplacedPhoton-PromptSkim-v3/000/198/941/00000/0EA7C91A-B8CF-E111-9766-002481E150EA.root'

 #   )
    
 )



