import pandas as pd

domains = pd.read_csv('extracted_small_test_output.csv')

TP = domains[domains['eid'] == domains['Harvested_Domain_Owners']]
TN = domains[domains['Harvested_Domain_Owners'] == 'No Owner']
FP = domains[(domains['Harvested_Domain_Owners'] != 'No Owner')
             & (domains['eid'] != domains['Harvested_Domain_Owners'])]

eids = set(domains.eid.tolist())
c_eids = set(TP.eid.tolist())


print('True Postives:', len(TP))
print('True Negatives:', len(TN))
print('False Postives:', len(FP))
print('Missed eids:', len(eids) - len(c_eids))
print('Missed Entities: ', eids - c_eids)

print('True Negatives:\n', TN)

print('False Positives:\n', FP)
