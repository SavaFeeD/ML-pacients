### Tables:
1. Pacients (Пациент)
2. PacientStats (Измерения показатилей пациента)
3. HospitalStats (Целевые переменные)

## Formation table: HospitalStats
Формируем таблицу с целевыми переменными с полями:

1. RecordID - уникальный идентификационный номер пациента
2. Survival - целевая переменная, содержит информацию сколько дней прожил пациент после попадания в отделение интенсивной терапии (например, 575б 918, 5 и т. д.), -1 означает что пациент жив до сих пор.
3. In-hospital_death - целевая переменная, содержит информацию умер человек в отделение интенсивной терапии (1) или нет (0).

## Formation table: Pacients
У пациента будут поля:

1. RecordID - уникальный идентификационный номер пациента.
2. Age - возраст пациента в годах.
3. Gender - пол пациента (0: female, or 1: male).
4. Height - рост пациента в сантиметрах.
5. ICUType - тип отделения интенсивной терапии куда был доставлен пациент (1: Coronary Care Unit, 2: Cardiac Surgery Recovery Unit, 3: Medical ICU, or 4: Surgical ICU).
6. Weight - вес пациента в киллограммах (Обратите внимание, что вес является как общим дескриптором (записывается при поступлении), так и переменной временного ряда (часто измеряется ежечасно для оценки баланса жидкости)).

Меняем формат всех файлов в папке "data/set" с .txt на .csv

## Formation table: PacientStats
Таблица с показателями пациентов (по времени снятия показателей):

1. Albumin (g/dL).
2. ALP [Alkaline phosphatase (IU/L)].
3. ALT [Alanine transaminase (IU/L)].
4. AST [Aspartate transaminase (IU/L)].
5. Bilirubin (mg/dL).
6. BUN [Blood urea nitrogen (mg/dL)].
7. Cholesterol (mg/dL).
8. Creatinine [Serum creatinine (mg/dL)].
9. DiasABP [Invasive diastolic arterial blood pressure (mmHg)].
10. FiO2 [Fractional inspired O2 (0-1)].
11. GCS [Glasgow Coma Score (3-15)].
12. Glucose [Serum glucose (mg/dL)].
13. HCO3 [Serum bicarbonate (mmol/L)].
14. HCT [Hematocrit (%)].
15. HR [Heart rate (bpm)].
16. K [Serum potassium (mEq/L)].
17. Lactate (mmol/L).
18. Mg [Serum magnesium (mmol/L)].
19. MAP [Invasive mean arterial blood pressure (mmHg)].
20. MechVent [Mechanical ventilation respiration (0:false, or 1:true)].
21. Na [Serum sodium (mEq/L)].
22. NIDiasABP [Non-invasive diastolic arterial blood pressure (mmHg)].
23. NIMAP [Non-invasive mean arterial blood pressure (mmHg)].
24. NISysABP [Non-invasive systolic arterial blood pressure (mmHg)].
25. PaCO2 [partial pressure of arterial CO2 (mmHg)].
26. PaO2 [Partial pressure of arterial O2 (mmHg)].
27. pH [Arterial pH (0-14)].
28. Platelets (cells/nL).
29. RespRate [Respiration rate (bpm)].
30. SaO2 [O2 saturation in hemoglobin (%)].
31. SysABP [Invasive systolic arterial blood pressure (mmHg)].
32. Temp [Temperature (°C)].
33. TropI [Troponin-I (μg/L)].
34. TropT [Troponin-T (μg/L)].
35. Urine [Urine output (mL)].
36. WBC [White blood cell count (cells/nL)].
37. Weight (kg).

+

38. RecordID - индентификатор пациента
39. Time - время снятия показателей

Таски:

1. Избавляемся от основных показателей из временного ряда
2. Выстраиваем строки в таблице в соответсвии с временем снятия показателей
3. Заполняем пропуски по соседним полям для использования приблезительно точные значения

# Формируем базу данных и отправляем туда данные

Создаем сущности:
1. Pacients (Пациент)
2. PacientStats (Измерения показатилей пациента)
3. HospitalStats (Целевые переменные)

После заполняем данными и проверяем чтобы все правильно залилось.