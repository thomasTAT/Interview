# sands internships

## Job description & Intern’s responsibilities.

Inventory Sands' backup data tapes and record them on excel. And maintain the data in excel.

Scan all the data backup tapes stored in different properties of Sands China with QR code scanners. Then record the backup tapes code and location into Excel spreadsheets. This is a huge job that requires a lot of time and effort, because Sands China has more than 20,000 backup data tapes in total. Precision is crucial throughout the process.

![Untitled](sands%20internships%202ec69556e9624f99b6facec4ae8ef6bf/Untitled.png)

In the this step, a high degree of precision is essential. When scanning backup tapes, it is common to encounter challenges such as double scanning caused by hand tremors. To mitigate this issue, we use the conditional formatting to height the duplicate tap.

conditional formatting →high-light cell rules → duplicate values.

![Untitled](sands%20internships%202ec69556e9624f99b6facec4ae8ef6bf/Untitled%201.png)

The formula checks if the last two characters of a tape code in cell A1 match any of the specified values. If there is a match, the formula uses the RIGHT function to extract the last two characters, representing the tape type. Otherwise, it returns an empty string. By applying this formula to the designated column, we can automatically extract and store the tape types, significantly improving efficiency and accuracy.

`=IF(OR(條件1, 條件2, ...), 條件為真的結果, 條件為假的結果)`

```sql
=IF(OR(RIGHT(A2, 2)="L1", RIGHT(A2, 2)="L2", RIGHT(A2, 2)="L3", RIGHT(A2, 2)="L4", RIGHT(A2, 2)="L5"), RIGHT(A2, 2), "")
```

After completing step 1, the next task involves obtaining an Excel file containing the previous stock take records. The purpose of this step is to compare the previous records with the most recent ones to determine which tapes have been added and which ones are missing. In this step, the VLOOKUP function in Excel is utilized to identify backup data tapes that exist in the old stock take Excel file but are not present in the new Excel table. 

`=VLOOKUP(lookup_value, table_array, col_index_num, false/ true)`

![Untitled](sands%20internships%202ec69556e9624f99b6facec4ae8ef6bf/Untitled%202.png)

In step 2, we encountered difficulties due to inconsistencies in the old stock take record. Specifically, some tape numbers did not include the type number at the end. This posed a challenge when attempting to perform a VLOOKUP between the old and new Excel data, as the new data relied on the presence of the type number. 
To address this issue, we implemented the following solution: We created an additional column in the old Excel that combined the code column and the type column. By merging these two columns into a single identifier, we ensured consistency with the new Excel data. 

```sql
=IF(OR(RIGHT(A1,2)="l1",RIGHT(A1,2)="l2",RIGHT(A1,2)="l3",RIGHT(A1,2)="l4"),A1,CONCAT(A1,B1))
```

The fourth step involves separating the Excel data from the backup data tape into different Excel files based on their respective locations. This can be achieved using the filter function in Excel.

![Untitled](sands%20internships%202ec69556e9624f99b6facec4ae8ef6bf/Untitled%203.png)

The final step involves maintaining the data. If the backup tapes have been relocated, it is important to update their location to reflect the most recent one and document who made the change. This ensures that the information about the backup tapes is accurate and up to date.