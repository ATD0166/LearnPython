from prescription_data import *

trial_patients = list(patients.keys())[::3]

# Remove Warfarin and add Edoxaban
for patient in trial_patients:
    prescription = patients[patient]
    # print(perscription)
    try:
        prescription.remove(warfarin)
        prescription.add(edoxaban)
    except KeyError:
        print(f"{patient} is not taking Warfarin."
              f"Remove {patient} from trial list.")
    print(patient, prescription)
    