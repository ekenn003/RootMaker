import FWCore.ParameterSet.Config as cms
from FWCore.ParameterSet.VarParsing import VarParsing
options = VarParsing ('analysis')


dataset = 'GluGlu_HToMuMu_M125_13TeV_powheg_pythia8'
#dataset = 'VBF_HToMuMu_M125_13TeV_powheg_pythia8'
#dataset = 'WMinusH_HToMuMu_M125_13TeV_powheg_pythia8'
#dataset = 'WPlusH_HToMuMu_M125_13TeV_powheg_pythia8'
#dataset = 'ZH_HToMuMu_M125_13TeV_powheg_pythia8'
#dataset = 'ZZTo4L_13TeV-amcatnloFXFX-pythia8'


if dataset == 'VBF_HToMuMu_M125_13TeV_powheg_pythia8':
    options.inputFiles = (
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/46DD6EB9-6246-E611-B4F9-0025909081F2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/7CA99888-1147-E611-8337-0025905C54D8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/88F36E85-244C-E611-A25D-141877344D39.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/A4F03F05-B448-E611-848D-1418773425EA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/AEBC7198-244C-E611-A441-549F3525B220.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/B6AC7C9A-244C-E611-8C10-90B11C0BB9FC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/C008ED8C-244C-E611-946B-842B2B180CC3.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/VBF_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v2/90000/C62DDEA7-244C-E611-BB81-90B11C0BD676.root',
    )


elif dataset == 'WMinusH_HToMuMu_M125_13TeV_powheg_pythia8':
    options.inputFiles = (
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WMinusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/80000/0A9DCB55-B26F-E611-9397-001C23C107AF.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WMinusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/80000/4641BC5C-B26F-E611-85E7-02163E00EA7F.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WMinusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/80000/524AD367-B26F-E611-854D-38EAA7A30576.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WMinusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/80000/60553D58-B26F-E611-9865-0CC47AA989C6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WMinusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/80000/DCF615B1-B86F-E611-99BD-0022198C21D3.root',
    )

elif dataset == 'ZH_HToMuMu_M125_13TeV_powheg_pythia8':
    options.inputFiles = (
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/00028E3B-3972-E611-819F-001E67E71BE1.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/2E509A21-3972-E611-84B7-F04DA275BFB9.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/422A6C2A-3972-E611-B2CC-AC162DACC3F8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/46F43745-3972-E611-B0E7-00304867FD5F.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/5CEBDCFB-DF71-E611-935E-0CC47A7C3636.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/5E680442-3972-E611-A738-A0369F7FC0BC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/643EC22A-3972-E611-ACB3-0CC47A6C06C2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/7AC9EC40-3972-E611-833B-9CB65404ED04.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/A05BAF70-3972-E611-A9EF-0CC47A4D764C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/BED80C4B-3972-E611-978C-002590907802.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/CE655B82-3972-E611-91CA-0CC47A78A4BA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/D85776AC-3972-E611-88BD-FA163E224667.root',
    )

elif dataset == 'WPlusH_HToMuMu_M125_13TeV_powheg_pythia8':
    options.inputFiles = (
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WPlusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/123EA837-3472-E611-B96E-0026B935A46C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WPlusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/3256C839-3472-E611-93C0-002590E7DFFC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WPlusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/4E245F81-3472-E611-98FB-001E67E6F904.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WPlusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/82DCF639-3472-E611-A465-0026B9277A4C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WPlusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/840D9C39-3472-E611-94F6-44A842CF05E6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/WPlusH_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/premix_withHLT_80X_mcRun2_asymptotic_v14-v1/90000/F642953E-3472-E611-870A-A0369F7FC540.root',
    )


elif dataset == 'GluGlu_HToMuMu_M125_13TeV_powheg_pythia8':
    options.inputFiles = (
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/12B931FE-CD3A-E611-9844-0025905C3D98.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/28337269-CE3A-E611-AF6C-0025904C4E2A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/62641E6B-CE3A-E611-944B-0025904CDDEE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/846F91F8-CD3A-E611-A012-0025904C6568.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/8E9E296D-CE3A-E611-B9C0-0025905D1CB6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/GluGlu_HToMuMu_M125_13TeV_powheg_pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/10000/A2910D87-CE3A-E611-9061-0025905C2CBE.root',
    )


elif dataset == 'ZZTo4L_13TeV-amcatnloFXFX-pythia8':
    options.inputFiles = (
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/402CFF70-3F51-E611-A148-00259073E41E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/621A1FA8-F84E-E611-AA51-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/6A67CF28-A850-E611-984E-E03F49D6226B.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/6CCC9FA4-284F-E611-A2E7-F0795920ED74.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/7A935987-3C51-E611-8067-0090FAA57630.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/7C2E5C7E-F84E-E611-B087-5065F3812291.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/80B3B099-2452-E611-8C1E-0CC47A1DF616.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/842F40EB-F44D-E611-A27A-7824AFAE696F.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/86ABD267-3C51-E611-9360-0090FAA572E0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/8EDA2DDE-2352-E611-B060-0090FAA57C60.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/9E911897-3C51-E611-9548-0090FAA57470.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/A2133A71-6452-E611-988F-0090FAA57630.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/A87FD17C-F84E-E611-A874-24BE05CEEB31.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/B021031C-4451-E611-9929-20CF305B0584.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/B26337E1-5052-E611-80C0-00259073E4EA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/B2E84957-3F51-E611-90FF-00259073E456.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/C457D50D-F14F-E611-8040-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/CA338EB7-F84E-E611-9BB7-0002C94CDDEA.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/DC4F1014-C151-E611-BABA-20CF305B056F.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/E44174AE-F84E-E611-819B-0002C94D575C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/00000/E6B76E3E-C151-E611-8BCF-00259073E344.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/2CD05FBF-2658-E611-9979-0CC47A4DEEE0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/3CC31AB6-2658-E611-9C0B-0090FAA58D84.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/50DCEEB9-2658-E611-A354-002590D0AFB0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/5CF9CAB9-2658-E611-899B-20CF300E9EB6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/602152BB-2658-E611-A1E4-0CC47A4DEECE.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/80DD88D7-E14F-E611-BE4C-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/9A71C1B7-2658-E611-B086-0090FAA57340.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/C8F5FABE-6D50-E611-8CF1-E03F49D6226B.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/DC7DBD20-144E-E611-A807-F46D0450CEA0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/DCC25CBB-2658-E611-B58F-0CC47A4D9A4C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/20000/DE7692B6-2658-E611-8AEB-0090FAA57780.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/04364EFA-AC51-E611-8804-0CC47A4DEEF0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/04E7909E-9B4D-E611-BF4C-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/0A7D86F6-BF4E-E611-969A-10BF4822C094.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/0AF87764-A651-E611-8293-0090FAA57660.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/124BAC42-C551-E611-B520-002590574604.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/1465923A-9451-E611-901B-002590747DD8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/1AC5616D-A951-E611-BEE6-0090FAA58294.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/1AFAA169-A651-E611-ABA8-0CC47A4DEEF0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/683C10CF-9B4D-E611-A284-4C79BA320083.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/7A3E10CF-9B4D-E611-9356-4C79BA320083.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/7E158D8B-9B4D-E611-ADFA-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/8059E488-BB51-E611-9FA0-0CC47A4DEDF8.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/8A75FABC-B451-E611-8679-0090FAA57560.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/A0CDFBBB-B451-E611-B714-BCAEC50971E3.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/A6953A68-A651-E611-9CA7-0090FAA57F44.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/BC8E3865-A651-E611-9B8D-0090FAA57B20.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/CE26B5F6-AC51-E611-BEBE-00259073E4AC.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/D6A41065-F24D-E611-8947-3085A9262DA0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/DE0F1E92-C851-E611-B8EC-0025907B4F6A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/E0B3BADD-B751-E611-9261-002590D0AFF0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/F02B18D0-9951-E611-A092-0025907B4F88.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/60000/F4C97D77-A951-E611-807B-002590D0B0A0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/12D30B15-0152-E611-9710-00259073E412.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/1A7CB185-0C52-E611-AB17-0025907B4F46.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/249C6F1B-F351-E611-862A-00259073E412.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/36401444-DC4E-E611-9B02-7824AFAE696F.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/42F0CDA2-FA51-E611-BCEB-0CC47A4D99A6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/4404623A-C14E-E611-8B99-24BE05CECDD1.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/44A3C410-1D52-E611-B4C1-0090FAA57660.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/4C79290A-AE4D-E611-A765-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/661CFF0D-AE4D-E611-9769-0002C94CD150.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/70B0380A-0D52-E611-95A5-0CC47A1E0750.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/72259461-0152-E611-9721-0CC47A1E0750.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/7684D401-AE4D-E611-97B7-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/76D64403-AE4D-E611-B9F8-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/782C1E14-1752-E611-8559-00259073E344.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/88871808-AE4D-E611-853D-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/92BBE09E-8952-E611-BEAC-0090FAA57340.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/98DEED17-1752-E611-B237-002590D0AF6C.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/9AE95F6D-1E4E-E611-9495-24BE05C6D731.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/A40BEBE0-0352-E611-926B-00259073E382.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/D079E376-0C4E-E611-ADEF-F46D0450CEA0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/D4672196-034E-E611-8B9D-24BE05CEADD1.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/D4D3FD01-2352-E611-976B-0025907B4F9A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/EA7CC701-AE4D-E611-B739-24BE05CEED81.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/80000/FE47AE14-1752-E611-A8B5-0025907B4F24.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/0EEB8582-D64E-E611-8C1A-F46D042E833B.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/1848C133-C04D-E611-8DDF-A0000420FE80.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/3AEF9021-4051-E611-8DB6-0090FAA58864.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/3EF4BE48-FF51-E611-8707-002590D0AFE6.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/5A197E29-2352-E611-BADA-0CC47A1DFE60.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/6E66E833-884E-E611-BBDA-24BE05CEDCF1.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/7420657A-BF4D-E611-9EB8-24BE05C6E711.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/7C745916-0652-E611-95C6-00259077501E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/8AEB0AF9-F151-E611-8CDF-00259073E42E.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/9CACF281-C251-E611-B02D-0025907B4F5A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/A6F00E67-B451-E611-9F7F-002590D0B074.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/B61BE30A-A751-E611-A732-0090FAA572B0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/B8690174-BF4D-E611-AE98-5065F3818261.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/BA835788-7A4D-E611-9B1F-F46D042E833B.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/C459BB6B-C251-E611-A1A8-0CC47A4D99B2.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/D24A8D6D-C251-E611-A223-002590D0AFB0.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/E463467C-BF4D-E611-8A3D-24BE05C44BC1.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/F2CB45BE-D651-E611-A753-00259073E38A.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/F8BD22CC-EE51-E611-99A2-0CC47A1E0476.root',
        'root://cms-xrd-global.cern.ch//store/mc/RunIISpring16MiniAODv2/ZZTo4L_13TeV-amcatnloFXFX-pythia8/MINIAODSIM/PUSpring16RAWAODSIM_reHLT_80X_mcRun2_asymptotic_v14-v1/90000/FC5B6910-AE51-E611-9A60-0CC47A4D9A08.root',
    )

else:
    options.inputFiles = ()



##elif dataset == '':
##    options.inputFiles = (
##        'root://cms-xrd-global.cern.ch/',
##    )







options.parseArguments()
process = cms.Process('XSec')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(options.maxEvents)
)

process.load('FWCore.MessageService.MessageLogger_cfi')
process.MessageLogger.cerr.FwkReport.reportEvery = 0

maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1) )
secFiles = cms.untracked.vstring() 
process.source = cms.Source ("PoolSource",
    fileNames = cms.untracked.vstring(options.inputFiles), 
    secondaryFileNames = secFiles)
process.xsec = cms.EDAnalyzer("GenXSecAnalyzer")

process.ana = cms.Path(process.xsec)
process.schedule = cms.Schedule(process.ana)

