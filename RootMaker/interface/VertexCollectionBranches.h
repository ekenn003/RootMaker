// VertexCollectionBranches.h
#include "CommonTools/Utils/interface/StringObjectFunction.h"
#include "DataFormats/VertexReco/interface/Vertex.h"
#include "DataFormats/VertexReco/interface/VertexFwd.h"
#include "FWCore/Framework/interface/ConsumesCollector.h"
#include "FWCore/Framework/interface/Event.h"
#include "FWCore/Framework/interface/Frameworkfwd.h"
#include "FWCore/ParameterSet/interface/ParameterSet.h"
#include "TTree.h"

using namespace std;

template<typename T>
class VertexCollectionFunction
{
  public:
    VertexCollectionFunction(TTree *tree, string functionName, string functionString);
    void evaluate(const reco::VertexCollection &candidates);

  private:
    StringObjectFunction<reco::Vertex, true> function_;
    TBranch *vectorBranch_;
    vector<T> values_;
};

typedef VertexCollectionFunction<int> VertexCollectionIntFunction;
typedef VertexCollectionFunction<float> VertexCollectionFloatFunction;

class VertexCollectionBranches
{
  public:
    VertexCollectionBranches(TTree *tree, string collectionName, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc);
    void fill(const edm::Event &iEvent);
    string getLowercaseSingular(string collectionName);

  private:
    edm::EDGetTokenT<reco::VertexCollection> collectionToken_;
    edm::ParameterSet branches_;
    vector<unique_ptr<VertexCollectionFloatFunction> > floatFunctions_;
    vector<unique_ptr<VertexCollectionIntFunction> > intFunctions_;
    TBranch *collectionCountBranch_;
    UInt_t collectionCount_;
};
