cmsDriver.py MinBias_13TeV_cfi.py --fileout file:GEN.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions POSTLS170_V5::All --step GEN --magField 38T_PostLS1 --geometry DBExtendedPostLS1 --no_exec -n 1000 --python_filename gen.py
cmsDriver.py MinBias_13TeV_cfi.py --filein file:GEN.root --fileout file:CMS-SIM.root --mc --eventcontent RAWSIM --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions POSTLS170_V5::All --step SIM --magField 38T_PostLS1 --geometry DBExtendedPostLS1 --no_exec -n 10 --python_filename cms-sim.py
cmsDriver.py MinBias_13TeV_cfi.py --filein file:CMS-SIM.root --fileout file:CMS-RECO.root --mc --eventcontent RECO --customise SLHCUpgradeSimulations/Configuration/postLS1Customs.customisePostLS1 --datatier GEN-SIM --conditions POSTLS170_V5::All --step DIGI,L1,DIGI2RAW,HLT:2013,RAW2DIGI,L1Reco --magField 38T_PostLS1 --geometry DBExtendedPostLS1 --no_exec --python_filename cms-reco.py