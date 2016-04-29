// ObjectCollectionBranches.cc
// create functions fo fill branches of reco-candidate-derived classes with ints or floats
// Original author: Devin Taylor, U. Wisconsin
#include "RootMaker/RootMaker/interface/ObjectCollectionBranches.h"

template<typename T>
ObjectCollectionFunction<T>::ObjectCollectionFunction(TTree *tree, std::string functionName, std::string functionString):
    function_(functionString),
    vectorBranch_(tree->Branch(functionName.c_str(), &values_)) 
{
}

template<typename T>
void ObjectCollectionFunction<T>::evaluate(const reco::CandidateView &candidates)
{
    values_.clear();
    for (const auto &candidate: candidates) {
        values_.push_back(function_(candidate));
    }
}

// _________________________________________________________________________________
ObjectCollectionBranches::ObjectCollectionBranches(TTree *tree, std::string collectionName,  const edm::ParameterSet &iConfig, edm::ConsumesCollector cc):
    collectionToken_(cc.consumes<reco::CandidateView>(iConfig.getParameter<edm::InputTag>("collection"))),
    branches_(iConfig.getParameter<edm::ParameterSet>("branches")),
    collectionName_(collectionName)
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
            floatFunctions_.emplace_back(new ObjectCollectionFloatFunction(tree, branchName, functionString));
        } else if (functionType=='I') {
            intFunctions_.emplace_back(new ObjectCollectionIntFunction(tree, branchName, functionString));
        }
        allBranches.insert(branchName);
    }
}

// _________________________________________________________________________________
void ObjectCollectionBranches::fill(const edm::Event &iEvent)
{
    edm::Handle<reco::CandidateView> candidates;
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
std::string ObjectCollectionBranches::getLowercaseSingular(std::string collectionName)
{
    std::string smallCollectionName = collectionName;
    if (collectionName.substr(collectionName.length() - 1) == "s") smallCollectionName.pop_back();
    return smallCollectionName;
}

// _________________________________________________________________________________
std::string ObjectCollectionBranches::getUppercaseSingular(std::string collectionName)
{
    std::string bigCollectionName = collectionName;
    if (collectionName.substr(collectionName.length() - 1) == "s") bigCollectionName.pop_back();
    bigCollectionName[0] = std::toupper(bigCollectionName[0]);
    return bigCollectionName;
}
