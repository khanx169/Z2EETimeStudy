// already included via EcalObjectTime.h
//#include "CalibCalorimetry/EcalTiming/interface/EcalTimeTreeContent.h"

#include "ECALTime/EcalTimePi0/interface/EcalObjectTime.h"

#include "CommonTools/UtilAlgos/interface/TFileService.h"
#include "TH1.h"
#include "TH2.h"
#include "TProfile.h"
#include "TGraphErrors.h"
#include "TF1.h"
#include "TMath.h"
#include "DataFormats/Math/interface/LorentzVector.h"

#include <sstream>


// based on range and bins, the bin width is 50 ps
float rangeTDistro_ = 3;
float incrementForDelayedGamma_ = 1;
int   binsTDistro_  = 120; // 1-E4/E1


// ---------------------------------------------------------------------------------------
// -------------------- struct holding sed of  histograms  -------------------------------
struct HistSet {

  // set pointer to the tree which is used to get data from
  void setTree(EcalTimePhyTreeContent * treeVars_);
  
  //book histogram set w/ common suffix inside the provided TFileDirectory
  //void book(edm::Service<TFileService>& td,const std::string&);
  void book(TFileDirectory subDir,const std::string&);
  
  // fill all histos of the set with the two electron candidates
  int fill(int sc1, int sc2, int cl1, int cl2);
  int fill(int sc1, int sc2, int bc1, int bc2, std::pair<float,float>& globalPhases );
  int fill(int sc1, int sc2, int bc1, int bc2, std::pair<float,float>& globalPhases, timeCorrector& theCorrector );
  // fill all histos of the set with the two electron candidates; using the last two arguments to implements some specific selections
  // "type" allows to have different usages for 'cut'
  // "cut"  is what you really cut on 
  int fill(int sc1, int sc2, int cl1, int cl2, int type, float cut);
  int fill(int sc1, int sc2, int bc1, int bc2, int type, float cut, std::pair<float,float>& globalPhases);
  int fill(int sc1, int sc2, int bc1, int bc2, int type, float cut, std::pair<float,float>& globalPhases, timeCorrector& theCorrector);

  // fill specifically single-cluster related quantities
  int fillSingle(int sc1, int cl1, ClusterTime bcTime1);
  int fillSingle(int sc1, int bc1, ClusterTime bcTime1, std::pair<float,float>& globalPhases);  
  int fillSingle(int sc1, int bc1, ClusterTime bcTime1, std::pair<float,float>& globalPhases, timeCorrector& theCorrector);  
  int fillSingle(int sc1, int cl1, ClusterTime bcTime1,int type,float cut);
  int fillSingle(int sc1, int bc1, ClusterTime bcTime1, int type, float cut , std::pair<float,float>& globalPhases);
  int fillSingle(int sc1, int bc1, ClusterTime bcTime1, int type, float cut , std::pair<float,float>& globalPhases, timeCorrector& theCorrector);

  TH1 * nVertices_;
  TH1F* mass_;
  TH1F* dZvertices_;
  TH1F* Zvertices_;
  TH1F* redAmplitudePair_;
  TH1F* chi2_;
  TH1F* chi2ndf_;
  TH1F* seedTime_;
  TH1F* seedTimeTOF_;
  TH1F* secondTime_;
  TH1F* secondTimeTOF_;
  TH1F* clusterTime_;
  TH1F* clusterTimeTOF_;
  TH1F* seedTimeDiffHist_;
  TH1F* TOFsingle_;
  TH1F* TOFcorrections_;
  TH1F* seed2secSingleClus_;
  TH2F* seedTimeVSchi2_, /* *seedTimeVSsecondTime_,*/ * seedTimeVSseedMsecond_;
  TH2F* TOFcorrectionsVSdeltaEta_;
  TH2F* zPairVsTPair_;
  TH2F* clusTimeDiffHistTOFVSdeltaEtaRightVertex_, *clusTimeDiffHistTOFVSdeltaEtaWrongVertex_;
  TH1F* tColl_, *tCollseeds_, *tCollsecs_;
  TH2F* tCollVSdeltaEtaRightVertex_, * tCollVStimeDiffHistTOF_;
  TH1F* seedTimeDiffHistTOF_;
  TH1F* secondTimeDiffHist_;
  TH1F* secondTimeDiffHistTOF_;
  TH1F* seed2secondTimeDiffHist_;
  TH1F* seed2secondTimeDiffHistTOF_;
  TH1F* clusTimeDiffHist_;
  TH1F* clusTimeDiffHistTOF_, *clusTimeDiffHistTOFwrongVertex_;
  TH1F* numCryBC1, *numCryBC2;
  TH2F* timeVsEtaLead_, *timeVsEtaSub_, *timeVsEta_, *outliersVsEtaPhi_; 
  TH1F* seedAmpli_;
  TH1F* secondAmpli_;
  TH1F* diffSeedOther_, *diffSeedOtherOverErr_;
  TH1F* diffSeedSecond_, *diffSeedSecondOverErr_;
  TH2F* seedVSSecond_;  

  TH1F* tofCorrDiEleBySM[36], *diEleBySM[36], *tofCorrEleBySM[36], *eleBySM[36];
  
  EcalTimePhyTreeContent * treeVars_;

} theHists;
// ---------------------------------------------------------------------------------------
// ------------------ Function to compute time and error for a cluster -------------------


std::string convertInt(int number)
{
  std::stringstream ss;   //create a stringstream
  ss << number;      //add number to the stream
  return ss.str();   //return a string with the contents of the stream
}
