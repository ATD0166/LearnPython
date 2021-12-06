from prescription_data import*

trial_patients = set(list(patients.keys())[::2])

while trial_patients:
    patient = trial_patients.pop()
    print(patient, end=" : ")
    prescription = patients[patient]
    print(prescription)