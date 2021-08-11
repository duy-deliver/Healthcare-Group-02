import csv
import os
import random
import datetime
from datetime import datetime
from decimal import Decimal
from faker import Faker
import numpy as np

fake = Faker()
DateExp = []

def create_csv_file_Insurance():
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    
    with open(f'{raw_path}\Insurance-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Insurance_ID', 'Insurance_Cover_Amount', 'Insurance_Type', 'Insurance_Expired']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 3000
        writer.writeheader()
        Insurance = []
        TypeInsu = []

        for i in range(0,1001):
            DateExp.append(fake.date_between_dates(date_start=datetime(2022,1,1), date_end=datetime(2025,12,31)))
            Insurance.append(random.choice([6000, 9000]))
            if (Insurance[i] == 6000):
                TypeInsu.append("HMO")
            else:
                TypeInsu.append("PMO")
        for i in range(2000, RECORD_COUNT):
            writer.writerow(
                {
                    'Insurance_ID': 'I' + str(i),
                    'Insurance_Cover_Amount': Insurance[i-2000],
                    'Insurance_Type': TypeInsu[i-2000],
                    'Insurance_Expired': DateExp[i-2000]

                }
            )

Patient_ID = []
# Create Patient
def create_csv_file_Patient():

    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\Patient-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Patient_ID','Insurance_ID','Patient_Name','Patient_Gender','Patient_Age',
                      'Patient_Bloodtype','Patient_Weight_kg','History_Covid','Blood_Pressure_mmHG','Blood_Sugar_mgdL',
                      'Patient_Zip','Patient_State']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 1000
        writer.writeheader()
        for i in range(RECORD_COUNT):
            Patient_ID.append('P' + str(i+1))
            writer.writerow(
                {
                    'Patient_ID': 'P' + str(i+1),
                    'Insurance_ID': 'I' + str(i+2000),
                    'Patient_Name': fake.name(),
                    'Patient_Gender': random.choice(['Male', 'Female']),
                    'Patient_Age': fake.random_int(20,80),
                    'Patient_Bloodtype': random.choice(['A', 'B', 'AB', 'O']),
                    'Patient_Weight_kg': fake.random_int(40, 120),
                    'History_Covid': random.choice([0,1]),
                    'Blood_Pressure_mmHG': fake.random_int(120,200),
                    'Blood_Sugar_mgdL': fake.random_int(100, 200),
                    'Patient_Zip' : fake.zipcode(),
                    'Patient_State': fake.state(),

                }
            )

#Create Disease:
Disease_name = ['Heart Cancer', 'Liver Cancer', 'Skin Cancer', 'Lymphoma', 'Lung Cancer']

Blood_Pressure_mmHg = ['>140' ,'>130' ,'<120' , '>140' ,'<120']

Blood_Sugar_mgdL = ['>140','>140','<140','>140','>140']

def create_csv_file_Disease():

    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\Disease-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Disease_ID','Disease_Name','Blood_Pressure_mmHg','Blood_Sugar_mgdL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 5
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Disease_ID': 'D' + str(i),
                    'Disease_Name': Disease_name[i],
                    'Blood_Pressure_mmHg': Blood_Pressure_mmHg[i],
                    'Blood_Sugar_mgdL': Blood_Sugar_mgdL[i]

                }
            )

Symptom =[ 'Chest pain or pressure', 'Irregular heart rhythm', 'Shortness of breath', 'Unexpected weight gain or loss'
,'Swelling in the feet and ankles','Coughing-up blood','Rapid heart rate','Choking','Abdominal swelling','Back pain','Pain near the right shoulder blade'
,'Easy bruising or bleeding' ,'Not having an appetite' ,'Pale bowel movements or dark urine'
,'An open sore that bleeds','Crusts and remains open for several weeks'
,'A reddish raised patch','A pink growth with an elevated border'
,'crusted central indentation','A scar-like white yellow or waxy area','Swollen Lymph Nodes'
,'Chills and Unexpected Body Temperature Changes'
,'Running a High Fever','Heavy Sweating During the Night'
,'Itchy Skin','Altered Skin','A cough for more than 2 or 3 weeks'
,'An ache or pain when breathing or coughing'
,'Swelling in the face or neck'
,'Bone pain','Jaundice' ,'Lumps in the neck or collarbone region' ]

Disease_Fake_ID = []
Symptom_ID = []
for i in range(1,33):
    Symptom_ID.append('S' + str(i))
    if i <=8:
        Disease_Fake_ID.append('D1')
    elif i >8 and i <=14:
        Disease_Fake_ID.append('D2')
    elif i > 14 and i <=20:
        Disease_Fake_ID.append('D3')
    elif i>20 and i <= 26:
        Disease_Fake_ID.append('D4')
    else:
        Disease_Fake_ID.append('D5')
def create_csv_file_Symtom():
    Symptom_Stge = []
    Symtom_Stage_Desc = []
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\Symptom-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Symtom_ID', 'Disease_ID', 'Symptom_Name', 'Symptom_Stage', 'Symptom_Stage_Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 32
        writer.writeheader()
        for i in range(0, 33):
            Symptom_Stge.append(fake.random_int(1, 3))
            if (Symptom_Stge[i] == 1):
                Symtom_Stage_Desc.append("Having one or two of the symptoms does not mean you have heart disease")
            else:
                Symtom_Stage_Desc.append("Can be life threatening")
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Symtom_ID': Symptom_ID[i],
                    'Disease_ID': Disease_Fake_ID[i],
                    'Symptom_Name': Symptom[i],
                    'Symptom_Stage': Symptom_Stge[i],
                    'Symptom_Stage_Desc': Symtom_Stage_Desc[i]
                }
            )
def create_csv_file_Medical():

    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\Medical-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Medical_ID','Patient_ID','Appointment_Date','Spouse_Name','Spouse_Phone','Spouse_Occupation',
                      'Social_Security_Last_4','Surgery_Status']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT =5000
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Medical_ID': 'M' + str(i),
                    'Patient_ID': random.choice(Patient_ID),
                    'Appointment_Date': fake.date_between_dates(date_start=datetime(2019,1,1), date_end=datetime(2021,8,9)),
                    'Spouse_Name': fake.name(),
                    'Spouse_Phone': fake.phone_number(),
                    'Spouse_Occupation' : fake.random_int(100,200),
                    'Social_Security_Last_4' : fake.random_int(1000,9999),
                    'Surgery_Status' : random.choice([0,1])
                }
            )

def create_csv_file_MedicalDetail():

    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.path.dirname(__file__)
    with open(f'{raw_path}\MedicalDetail-{time_stampe}.csv', 'w', newline='') as csvfile:
        fieldnames = ['Medical_ID','Symptom_ID','Doctor_Name','Allergies','Work_Phone']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT =5000
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Medical_ID': 'M' + str(i),
                    'Symptom_ID': random.choice(Symptom_ID),
                    'Doctor_Name': fake.name(),
                    'Allergies': random.choice([0,1]),
                    'Work_Phone': fake.phone_number(),
                }
            )

if __name__ == '__main__':
    print('Creating a Insurance data...')
    create_csv_file_Insurance()
    print('Creating a Patient data...')
    create_csv_file_Patient()
    print('Creating a Disease data...')
    create_csv_file_Disease()
    print('Creating a Symptom data...')
    create_csv_file_Symtom()
    print('Creating a Medial data...')
    create_csv_file_Medical()
    print('Creating a Medial Detail data...')
    create_csv_file_MedicalDetail()