import FWCore.ParameterSet.Config as cms


def create_ntuple(process, inputs,
        ntuple_list=[
            'event',
            'gen', 'genjet', 'gentau',
            'digis',
            'triggercells',
            'clusters', 'multiclusters'
            ]
        ):
    vpset = []
    for ntuple in ntuple_list:
        pset = getattr(process, 'ntuple_'+ntuple).clone()
        if ntuple=='triggercells':
            pset.TriggerCells = cms.InputTag(inputs[0])
            pset.Multiclusters = cms.InputTag(inputs[2])
        elif ntuple=='clusters':
            pset.Clusters = cms.InputTag(inputs[1])
            pset.Multiclusters = cms.InputTag(inputs[2])
        elif ntuple=='multiclusters':
            pset.Multiclusters = cms.InputTag(inputs[2])
        vpset.append(pset)
    ntuplizer = process.hgcalTriggerNtuplizer.clone()
    ntuplizer.Ntuples = cms.VPSet(vpset)
    return ntuplizer




