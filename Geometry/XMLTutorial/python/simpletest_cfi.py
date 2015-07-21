import FWCore.ParameterSet.Config as cms

#ideal geometry
XMLIdealGeometryESSource = cms.ESSource("XMLIdealGeometryESSource",
    geomXMLFiles = cms.vstring('Geometry/CMSCommonData/data/materials.xml', 
        'Geometry/CMSCommonData/data/rotations.xml', 
        'Geometry/CMSCommonData/data/extend/cmsextent.xml', 
        'Geometry/CMSCommonData/data/cms.xml', 
        'Geometry/CMSCommonData/data/PhaseI/beampipe.xml', 
        'Geometry/CMSCommonData/data/cmsBeam.xml', 
        'Geometry/CMSCommonData/data/cmsMother.xml', 
        'Geometry/CMSCommonData/data/mgnt.xml', 
        'Geometry/ForwardCommonData/data/forward.xml', 
        'Geometry/ForwardCommonData/data/totemRotations.xml', 
        'Geometry/ForwardCommonData/data/totemMaterials.xml', 
        'Geometry/ForwardCommonData/data/totemt1.xml', 
        'Geometry/ForwardCommonData/data/totemt2.xml', 
        'Geometry/ForwardCommonData/data/ionpump.xml', 
        'Geometry/TotemRPData/data/RP_Box.xml', 
        'Geometry/TotemRPData/data/RP_Box/RP_Box_000.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_001.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_002.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_003.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_004.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_005.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_020.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_021.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_022.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_023.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_024.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_025.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_100.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_101.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_102.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_103.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_104.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_105.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_120.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_121.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_122.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_123.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_124.xml',
        'Geometry/TotemRPData/data/RP_Box/RP_Box_125.xml', 
        'Geometry/TotemRPData/data/RP_Hybrid.xml', 
        'Geometry/TotemRPData/data/RP_Materials.xml', 
        'Geometry/TotemRPData/data/RP_Transformations.xml', 
        'Geometry/TotemRPData/data/RP_Detectors_Assembly.xml', 
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_000.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_001.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_002.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_003.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_004.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_005.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_020.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_021.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_022.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_023.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_024.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_025.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_100.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_101.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_102.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_103.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_104.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_105.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_120.xml',
         'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_121.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_122.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_123.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_124.xml',
        'Geometry/TotemRPData/data/RP_Detectors_Assembly/RP_Detectors_Assembly_125.xml', 
        'Geometry/TotemRPData/data/RP_Device.xml', 
        'Geometry/TotemRPData/data/RP_Vertical_Device.xml', 
        'Geometry/TotemRPData/data/RP_Horizontal_Device.xml', 
        'Geometry/TotemRPData/data/RP_220_Right_Station.xml', 
        'Geometry/TotemRPData/data/RP_220_Left_Station.xml', 
        'Geometry/TotemRPData/data/RP_147_Right_Station.xml', 
        'Geometry/TotemRPData/data/RP_147_Left_Station.xml', 
        'Geometry/TotemRPData/data/RP_Stations_Assembly.xml', 
        'Geometry/TotemRPData/data/RP_Sensitive_Dets.xml', 
        'Geometry/TotemRPData/data/RP_Cuts_Per_Region.xml', 
        'Geometry/TotemRPData/data/TotemRPGlobal.xml', 

        'Geometry/TotemRPData/data/RP_Param_Beam_Region.xml',
        'Geometry/TotemRPData/data/RP_Beta_90/RP_Dist_Beam_Cent.xml'),
#        'Geometry/PPSCommonData/data/mystation.xml',

    #rootNodeName = cms.string('TotemRPGlobal:OTOTEM')
rootNodeName = cms.string('cms:OCMS')
)

# real geometry
TotemRPGeometryESModule = cms.ESProducer("TotemRPGeometryESModule") # DIFF: TOTEM only

