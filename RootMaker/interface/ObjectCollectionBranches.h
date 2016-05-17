// ObjectCollectionBranches.h
#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TTree.h"

using namespace std;

template<typename T>
class ObjectCollectionFunction
{
  public:
    ObjectCollectionFunction(TTree *tree, string functionName, string functionString);
    void evaluate(const reco::CandidateView &candidates);

  private:
    StringObjectFunction<reco::Candidate, true> function_;
    TBranch *vectorBranch_;
    vector<T> values_;
};

typedef ObjectCollectionFunction<int> ObjectCollectionIntFunction;
typedef ObjectCollectionFunction<float> ObjectCollectionFloatFunction;

class ObjectCollectionBranches
{
  public:
    ObjectCollectionBranches(TTree *tree, string collectionName, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc);
    void fill(const edm::Event &iEvent);
    string getName() { return collectionName_; }
    UInt_t getCount() { return collectionCount_; }
    string getLowercaseSingular(string collectionName);
    string getUppercaseSingular(string collectionName);

  private:
    edm::EDGetTokenT<reco::CandidateView> collectionToken_;
    edm::ParameterSet branches_;
    vector<unique_ptr<ObjectCollectionFloatFunction> > floatFunctions_;
    vector<unique_ptr<ObjectCollectionIntFunction> > intFunctions_;
    TBranch *collectionCountBranch_;
    string collectionName_;
    UInt_t collectionCount_;
};
