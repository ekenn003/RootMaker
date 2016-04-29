// VertexCollectionBranches.cc
// create functions fo fill branches of reco-vertex-derived classes with ints or floats
#include "RootMaker/RootMaker/interface/VertexCollectionBranches.h"

template<typename T>
VertexCollectionFunction<T>::VertexCollectionFunction(TTree *tree, std::string functionName, std::string functionString):
    function_(functionString),
    vectorBranch_(tree->Branch(functionName.c_str(), &values_))
{
}

template<typename T>
void VertexCollectionFunction<T>::evaluate(const reco::VertexCollection& candidates)
{
    values_.clear();
    for (const auto &candidate: candidates) {
        values_.push_back(function_(candidate));
    }
}

// _________________________________________________________________________________
VertexCollectionBranches::VertexCollectionBranches(TTree *tree, std::string collectionName, const edm::ParameterSet &iConfig, edm::ConsumesCollector cc):
    collectionToken_(cc.consumes<reco::VertexCollection>(iConfig.getParameter<edm::InputTag>("collection"))),
    branches_(iConfig.getParameter<edm::ParameterSet>("branches"))
{
    std::set<std::string> allBranches;
    std::string countBranch = getLowercaseSingular(collectionName) + "_count";
    allBranches.insert(countBranch);
    collectionCountBranch_ = tree->Branch(countBranch.c_str(), &collectionCount_);
    // the functions
    for (auto functionName : branches_.getParameterNames()) {
        auto functionParams = branches_.getParameter<std::vector<std::string> >(functionName);
        auto functionString = functionParams[0];
        auto functionType = functionParams[1];
        auto branchName = getLowercaseSingular(collectionName) + "_" + functionName;
        if (functionType=='F') {
            floatFunctions_.emplace_back(new VertexCollectionFloatFunction(tree, branchName, functionString));
        } else if (functionType=='I') {
            intFunctions_.emplace_back(new VertexCollectionIntFunction(tree, branchName, functionString));
        }
        allBranches.insert(branchName);
    }
}

// _________________________________________________________________________________
void VertexCollectionBranches::fill(const edm::Event& iEvent)
{
    edm::Handle<reco::VertexCollection> candidates;
    iEvent.getByToken(collectionToken_, candidates);
    collectionCount_ = candidates->size();

    for (auto &f : floatFunctions_) {
        f->evaluate(*candidates);
    }
    for (auto &f : intFunctions_) {
        f->evaluate(*candidates);
  }
}

// _________________________________________________________________________________
std::string VertexCollectionBranches::getLowercaseSingular(std::string collectionName)
{
    if (collectionName == "vertices") return ("primvertex");
    else return collectionName;
}
