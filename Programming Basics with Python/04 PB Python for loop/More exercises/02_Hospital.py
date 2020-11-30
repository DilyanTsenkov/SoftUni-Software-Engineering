days = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0
for period in range(1, days + 1):
    patients_per_day = int(input())
    if period % 3 == 0:
        if untreated_patients > treated_patients:
            doctors +=1
    if patients_per_day <= doctors:
        treated_patients += patients_per_day
    else:
        treated_patients += doctors
        untreated_patients += (patients_per_day - doctors)
print(f'Treated patients: {treated_patients}.')
print(f'Untreated patients: {untreated_patients}.')