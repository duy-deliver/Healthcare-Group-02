import csv
import os
import random
import datetime
from datetime import datetime
from decimal import Decimal
from faker import Faker
import numpy as np
import pandas as pd
from tqdm import tqdm 

fake = Faker()
Patient_ID = []
Medical_ID = []
NumState = 50  # Number of state. DO not change the number of state, it will affect the patient state
NumPatient = 100000
NumMedical = 1000000


#Create Disease Paramter

Disease_Fake_ID = []

Disease_name = ['Heart Cancer', 'Liver Cancer', 'Skin Cancer', 'Lymphoma', 'Lung Cancer']

Blood_Pressure_mmHg = ['>140' ,'>130' ,'<120' , '>140' ,'<120']

Blood_Sugar_mgdL = ['>140','>140','<140','>140','>140']

#Create Location Parameter

Climate = ['Hot humid continental', 'Humid subtropical', 'Warm humid continental', 'Cold semi-arid', 'Warm-summer Mediterranean']



#Create Symptom Parameter
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

#Create Patient Parameter
Race = ["European American", "African American", "Asian American", "American Indian/Alaska Native", "Native Hawaiian/Pacific Islander"]
Education = ['Middle school', 'High school', 'College', 'Bachelor', 'Master']

def create_csv_file_Location(NumState, Climate, Total_Patient_State):
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.getcwd()
    with open(os.path.join(raw_path, 'Location-{}.csv'.format(time_stampe)), 'w', newline='') as csvfile:
        fieldnames = ['State_ID', 'State_Name', 'State_Climate', 'State_TotalPopulation', 'State_AgingPopulation']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in range(NumState):
            writer.writerow(
                {
                    'State_ID': int(i+1),
                    'State_Name': fake.unique.state(),
                    'State_Climate': random.choice(Climate),
                    'State_TotalPopulation': round(int(Total_Patient_State[i])*fake.random_int(140,200)/100),
                    'State_AgingPopulation': round(int(Total_Patient_State[i])*fake.random_int(35,60)/100),
                }
            )

# Create Patient
def create_csv_file_Patient(NumPatient, Race, Education):
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.getcwd()
    with open(os.path.join(raw_path, 'Patient-{}.csv'.format(time_stampe)), 'w', newline='') as csvfile:
        fieldnames = ['Patient_ID','Patient_Name','Patient_Gender','Patient_Age',
                      'Patient_Bloodtype','Patient_Weight_kg','History_Covid','Blood_Pressure_mmHG','Blood_Sugar_mgdL',
                      'Patient_State','Patient_Race','Patient_Income','Patient_Education','Patient_Zip']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in tqdm(range(NumPatient)):
            Patient_ID.append('P' + str(fake.unique.random_int(1125,2738+NumPatient)))
            writer.writerow(
                {
                    'Patient_ID': Patient_ID[i],
                    'Patient_Name': fake.unique.name(),
                    'Patient_Gender': random.choice(['Male', 'Female']),
                    'Patient_Age': fake.random_int(20,80),
                    'Patient_Bloodtype': random.choice(['A', 'B', 'AB', 'O']),
                    'Patient_Weight_kg': fake.random_int(40, 120),
                    'History_Covid': random.choice([0,1]),
                    'Blood_Pressure_mmHG': fake.random_int(120,200),
                    'Blood_Sugar_mgdL': fake.random_int(100, 200),
                    'Patient_State': fake.random_int(1,50),
                    'Patient_Race' : random.choice(Race),
                    'Patient_Income' : fake.random_int(20, 1000),
                    'Patient_Education': random.choice(Education),
                    'Patient_Zip' : fake.zipcode(),

                }
            )
    df_patient = pd.read_csv(os.path.join(raw_path, 'Patient-{}.csv'.format(time_stampe)))
    Total_Patient_State = df_patient['Patient_State'].value_counts().sort_values(axis =0, ascending = False).to_list()
    return Total_Patient_State

def create_csv_file_Disease():

    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.getcwd()
    with open(os.path.join(raw_path, 'Disease-{}.csv'.format(time_stampe)), 'w', newline='') as csvfile:
        fieldnames = ['Disease_ID','Disease_Name','Blood_Pressure_mmHg','Blood_Sugar_mgdL']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 5
        writer.writeheader()
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Disease_ID': 'D' + str(i+1),
                    'Disease_Name': Disease_name[i-1],
                    'Blood_Pressure_mmHg': Blood_Pressure_mmHg[i-1],
                    'Blood_Sugar_mgdL': Blood_Sugar_mgdL[i-1]

                }
            )

def create_csv_file_Symptom():
    Symptom_Stge = []
    Symptom_Stage_Desc = []
    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.getcwd()
    with open(os.path.join(raw_path, 'Symptom-{}.csv'.format(time_stampe)), 'w', newline='') as csvfile:
        fieldnames = ['Symptom_ID', 'Disease_ID', 'Symptom_Name', 'Symptom_Stage', 'Symptom_Stage_Desc']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        RECORD_COUNT = 32
        writer.writeheader()
        for i in range(0, 33):
            Symptom_Stge.append(fake.random_int(1, 3))
            if (Symptom_Stge[i] == 1):
                Symptom_Stage_Desc.append("Having one or two of the symptoms does not mean you have heart disease")
            else:
                Symptom_Stage_Desc.append("Can be life threatening")
        for i in range(RECORD_COUNT):
            writer.writerow(
                {
                    'Symptom_ID': Symptom_ID[i],
                    'Disease_ID': Disease_Fake_ID[i],
                    'Symptom_Name': Symptom[i],
                    'Symptom_Stage': Symptom_Stge[i],
                    'Symptom_Stage_Desc': Symptom_Stage_Desc[i]
                }
            )


def create_csv_file_Medical(NumMedical):

    time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
    raw_path = os.getcwd()
    with open(os.path.join(raw_path, 'Medical-{}.csv'.format(time_stampe)), 'w', newline='') as csvfile:
        fieldnames = ['Medical_ID','Patient_ID','Symptom_ID','Doctor_Name','Allergies', 
                        'Spouse_Name','Spouse_Phone','Work_Phone','Surgery_Status',
                      'Social_Security_Last_4','Spouse_Occupation','Appointment_Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for i in tqdm(range(NumMedical)):
            Medical_ID.append('M' + str(fake.unique.random_int(123467,983475+NumMedical)))
            writer.writerow(
                {
                    'Medical_ID': Medical_ID[i],
                    'Patient_ID': random.choice(Patient_ID),
                    'Symptom_ID': random.choice(Symptom_ID),
                    'Doctor_Name': fake.company().replace("-"," ").replace(",","").split(" ")[0],
                    'Allergies': random.choice([0,1]),
                    'Spouse_Name': fake.name(),
                    'Spouse_Phone': fake.phone_number(),
                    'Work_Phone': '090' + str(fake.unique.random_int(1221221,9876543)),
                    'Surgery_Status' : random.choice([0,1]),
                    'Social_Security_Last_4' : fake.random_int(1000,9999),
                    'Spouse_Occupation' : fake.random_int(100,200),
                    'Appointment_Date': fake.date_between_dates(date_start=datetime(2019,1,1), date_end=datetime(2021,8,9)),
                }
            )

# def create_csv_file_MedicalDetail():

#     time_stampe = datetime.now().strftime("%Y_%m_%d-%I_%M_%S_%p")
#     raw_path = os.path.dirname(__file__)
#     with open(f'{raw_path}\MedicalDetail-{time_stampe}.csv', 'w', newline='') as csvfile:
#         fieldnames = ['Medical_ID','Symptom_ID','Doctor_Name','Allergies','Work_Phone']
#         writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
#         RECORD_COUNT =200
#         writer.writeheader()
#         for i in range(RECORD_COUNT):
#             writer.writerow(
#                 {
#                     'Medical_ID': 'M' + str(i+1),
#                     'Symptom_ID': random.choice(Symptom_ID),
#                     'Doctor_Name': fake.name(),
#                     'Allergies': random.choice([0,1]),
#                     'Work_Phone': fake.phone_number(),
#                 }
#             )

if __name__ == '__main__':
    print('Creating a Patient data...')
    Total_Patient_State = create_csv_file_Patient(NumPatient, Race, Education)
    print('Creating a Location data...')
    create_csv_file_Location(NumState, Climate, Total_Patient_State)
    print('Creating a Disease data...')
    create_csv_file_Disease()
    print('Creating a Symptom data...')
    create_csv_file_Symptom()
    print('Creating a Medial data...')
    create_csv_file_Medical(NumMedical)
    # print('Creating a Medial Detail data...')
    # create_csv_file_MedicalDetail()