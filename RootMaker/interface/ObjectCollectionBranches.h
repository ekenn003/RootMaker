// ObjectCollectionBranches.h
#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "DataFormats/Candidate/interface/Candidate.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TTree.h"

template<typename T>
class ObjectCollectionFunction
{
  public:
    ObjectCollectionFunction(TTree *tree, std::string functionName, std::string functionString);
    void evaluate(const reco::CandidateView &candidates);

  private:
    StringObjectFunction<reco::Candidate, true> function_;
    TBranch *vectorBranch_;
    std::vector<T> values_;
};

typedef ObjectCollectionFunction<int> ObjectCollectionIntFunction;
typedef ObjectCollectionFunction<float> ObjectCollectionFloatFunction;

class ObjectCollectionBranches
{
  public:
    ObjectCollectionBranches(TTree *tree, std::string collectionName,  const edm::ParameterSet &iConfig, edm::ConsumesCollector cc);
    void fill(const edm::Event &iEvent);
    std::string getName() { return collectionName_; }
    UInt_t getCount() { return collectionCount_; }
    std::string getLowercaseSingular(std::string collectionName);
    std::string getUppercaseSingular(std::string collectionName);

  private:
    edm::EDGetTokenT<reco::CandidateView> collectionToken_;
    edm::ParameterSet branches_;
    std::vector<std::unique_ptr<ObjectCollectionFloatFunction> > floatFunctions_;
    std::vector<std::unique_ptr<ObjectCollectionIntFunction> > intFunctions_;
    TBranch *collectionCountBranch_;
    std::string collectionName_;
    UInt_t collectionCount_;
};
