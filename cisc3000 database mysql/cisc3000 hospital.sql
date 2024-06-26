DROP DATABASE IF EXISTS hospital;
CREATE DATABASE hospital;

use hospital;
CREATE TABLE patients (
patient_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
gender VARCHAR(10),
date_of_birth DATE
);

CREATE TABLE doctors (
doctor_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
first_name VARCHAR(50),
last_name VARCHAR(50),
specialty VARCHAR(50),
phone_number VARCHAR(20)
);

# 預約表
CREATE TABLE appointments (
appointment_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
appointment_date DATE,
appointment_time TIME,
FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

# 診斷信息
CREATE TABLE medical_records (
record_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
medical_date DATE,
diagnosis VARCHAR(255),
FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

#藥單
CREATE TABLE prescriptions (
prescription_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
doctor_id INT,
prescription_date DATE,
medication VARCHAR(255),
FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
FOREIGN KEY (doctor_id) REFERENCES doctors(doctor_id)
);

# 住院部門，住院容量，住院佔用多少，可用床位。
CREATE TABLE wards (
ward_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
ward_name VARCHAR(50),
capacity INT,
occupied_beds INT,
available_beds INT
);

# 病人住院時間
CREATE TABLE admissions (
admission_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
patient_id INT,
ward_id INT,
admission_date DATE,
discharge_date DATE,
FOREIGN KEY (patient_id) REFERENCES patients(patient_id),
FOREIGN KEY (ward_id) REFERENCES wards(ward_id)
);


INSERT INTO patients (first_name, last_name, gender, date_of_birth) VALUES
('John', 'Doe', 'Male', '1985-05-15'),
('Jane', 'Doe', 'Female', '1990-02-20'),
('Bob', 'Smith', 'Male', '1978-10-10'),
('Alice', 'Smith', 'Female', '1982-12-31'),
('Tom', 'Lee', 'Male', '1995-07-01'),
('Linda', 'Lee', 'Female', '1988-03-25'),
('David', 'Brown', 'Male', '1976-01-05'),
('Mary', 'Brown', 'Female', '1980-09-17'),
('Peter', 'Taylor', 'Male', '1992-11-22'),
('Lucy', 'Taylor', 'Female', '1986-06-13'),
('Jack', 'Johnson', 'Male', '1998-08-08'),
('Emily', 'Johnson', 'Female', '1994-04-04');

INSERT INTO doctors (first_name, last_name, specialty, phone_number) VALUES
('Michael', 'Smith', 'Cardiologist', '123-456-7890'),
('Jennifer', 'Lee', 'Dermatologist', '234-567-8901'),
('William', 'Brown', 'Neurologist', '345-678-9012'),
('Elizabeth', 'Taylor', 'Ophthalmologist', '456-789-0123'),
('Robert', 'Johnson', 'Psychiatrist', '567-890-1234'),
('Karen', 'Davis', 'Pediatrician', '678-901-2345'),
('Daniel', 'Wilson', 'General Practitioner', '789-012-3456'),
('manho', 'Wilson', 'General Practitioner', '789-012-3456'),
('jimmy', 'Wilson', 'General Practitioner', '789-012-3456'),
('Aston', 'Wilson', 'General Practitioner', '789-012-3456');

INSERT INTO appointments (patient_id, doctor_id, appointment_date, appointment_time) VALUES
(1, 1, '2023-05-01', '10:00:00'),
(2, 2, '2023-05-02', '11:00:00'),
(3, 3, '2023-05-03', '12:00:00'),
(4, 4, '2023-05-04', '13:00:00'),
(5, 5, '2023-05-05', '14:00:00'),
(6, 6, '2023-05-06', '15:00:00'),
(7, 7, '2023-05-07', '16:00:00'),
(8, 1, '2023-05-08', '17:00:00'),
(9, 2, '2023-05-09', '18:00:00'),
(10, 3, '2023-05-10', '19:00:00');

INSERT INTO medical_records (patient_id, doctor_id, medical_date, diagnosis) VALUES
(1, 1, '2023-05-01', 'Heart disease'),
(1, 1, '2023-05-02', 'covid 19'),
(1, 1, '2023-05-02', 'covid 19'),
(2, 2, '2023-05-02', 'Acne'),
(2, 2, '2023-05-02', 'Heart disease'),
(3, 3, '2023-05-03', 'Migraine'),
(4, 4, '2023-05-04', 'Cataract'),
(5, 5, '2023-05-05', 'Depression'),
(6, 6, '2023-05-06', 'Asthma'),
(7, 7, '2023-05-07', 'Flu'),
(8, 1, '2023-05-08', 'High blood pressure'),
(9, 2, '2023-05-09', 'Eczema'),
(10, 3, '2023-05-10', 'Alzheimer s disease');

INSERT INTO prescriptions (patient_id, doctor_id, prescription_date, medication) VALUES
(1, 1, '2023-05-01', 'Lipitor'),
(2, 2, '2023-05-02', 'Retin-A'),
(3, 3, '2023-05-03', 'Imitrex'),
(4, 4, '2023-05-04', 'Lumigan'),
(5, 5, '2023-05-05', 'Prozac'),
(6, 6, '2023-05-06', 'Ventolin'),
(7, 7, '2023-05-07', 'Tamiflu'),
(8, 1, '2023-05-08', 'Norvasc'),
(9, 2, '2023-05-09', 'Elidel'),
(10, 3, '2023-05-10', 'Aricept');

INSERT INTO wards (ward_name, capacity, occupied_beds, available_beds) VALUES
('Cardiology', 20, 10, 10),
('Dermatology', 30, 20, 10),
('Neurology', 15, 5, 10),
('Ophthalmology', 25, 15, 10),
('Psychiatry', 10, 5, 5);

INSERT INTO admissions (patient_id, ward_id, admission_date, discharge_date) VALUES
(1, 1, '2023-05-01', '2023-05-05'),
(2, 2, '2023-05-02', '2023-05-06'),
(3, 3, '2023-05-03', '2023-05-07'),
(4, 4, '2023-05-04', '2023-05-08'),
(5, 5, '2023-05-05', '2023-05-09'),
(6, 1, '2023-05-06', '2023-05-10'),
(7, 2, '2023-05-07', '2023-05-11'),
(8, 3, '2023-05-08', '2023-05-12'),
(9, 4, '2023-05-09', '2023-05-13'),
(10, 5, '2023-05-10', '2023-05-14');



# show the number of doctors in hospital.
select count(doctor_id)
from doctors;

# show the number of patients corresponding to each doctor.
-- 有些醫生，看 0 個病人，因此要用 left join
SELECT doctors.doctor_id, doctors.first_name, doctors.last_name, COUNT(patient_id)
FROM doctors
LEFT JOIN appointments ON doctors.doctor_id = appointments.doctor_id
GROUP BY doctors.doctor_id;

# check the percentage rate of ward occupation of corresponding department, occupancy rate round off to 3 decimal places.
SELECT wards.ward_id, wards.ward_name, ROUND((occupied_beds / capacity) * 100, 3) AS occupancy_rate
FROM wards;


# show the number of patients whose date of birth is before 1990.
select count(*)
from patients
where date_of_birth < '1990-01-01';

# show the number of patients whose medication are recorded.
-- 一個病人，也許有多個 record， 因此用distinct。
select distinct count(patient_id) 
from medical_records;

# Find the patients who enter hospital before 4th May 2023 and leave after 7th May 2023
-- 一個病人，可能再這期間，多次住院。
SELECT DISTINCT patient_id, first_name, last_name
FROM admissions natural join patients
WHERE admission_date <= '2023-05-06' and discharge_date >= '2023-05-07';

# Find the most common diagnosis in hospital and number of occurrence. 
select count(patient_id), diagnosis
from medical_records
group by diagnosis
order by count(patient_id) desc
limit 3;

# 先獲得每個 病 對應的病人數量。
with diagnose_num_patients as (
    select count(patient_id) as num_patient, diagnosis
    from medical_records
    group by diagnosis
)

select num_patient, diagnosis
from diagnose_num_patients
where num_patient = (
    -- 獲得患某病的最多數量
    select max(num_patient)
    from diagnose_num_patients
);


# show the information of patients who do not have appointmens hospital after March 2023.

SELECT *
FROM patients
WHERE patients.patient_id NOT IN(
SELECT patient_id
FROM appointments
WHERE appointments.appointment_date > '2023-05-05'
);

# Show the number of prescriptions written after February 1, 2023 from the patient and prescription table, grouped by patient first and last name.
SELECT  patients.first_name, patients.last_name, COUNT(*) AS prescription_count
FROM patients
JOIN prescriptions ON patients.patient_id = prescriptions.patient_id
WHERE prescriptions.prescription_date > '2023-02-01'
GROUP BY patients.first_name, patients.last_name;


# Show patients from the patients table who do not have any appointments after May 5th, 2023.
SELECT *
FROM patients
WHERE patients.patient_id NOT IN(
    SELECT patient_id
    FROM appointments
    WHERE appointments.appointment_date > '2023-05-05'
    );