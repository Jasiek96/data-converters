# Data Converters

## General Information

This repository contains three Python programs designed to address specific challenges encountered during data export/import from scientific equipment.

### Problem Statement

- **Dielectric Measurements**:  
  Measurements of electrical properties are performed as a function of frequency and temperature. The Novocontrol software exports data either as individual files for each temperature or as a single large file with all values in one column. This structure complicates efficient data analysis and visualization in external tools.

- **Magnetic Measurements**:  
  Magnetic properties are measured as a function of frequency, temperature, and field strength. The exported files are poorly structured, often containing empty lines and unnecessary information. For PPMS, this issue is particularly pronounced.

### Solution

To streamline workflows (e.g., plotting and processing data in OriginPro), these programs restructure the data into a multi-column format. Each column corresponds to a specific temperature, with rows organized by frequency or other relevant parameters. This format simplifies data import and enables rapid generation of comparative plots and analytical workflows.

---

## Input and Output Files

### Input Files

- Supported formats: `.csv`, `.txt`, `.dat`
- The input file must be in the same directory as the program.

### Output Files

- Format: `.txt` files with space (` `) as a separator (modifiable if needed).
- The output file is saved in the same directory as the program.

---

## How to Run the Programs

1. Open the program in a text editor (e.g., Notepad).
2. Modify the file names:
   - Update the source file name:
     ```python
     with open("file_name.txt", "r", newline="") as source:
     ```
   - Update the target file name:
     ```python
     with open("file_name.txt", "+w") as target:
     ```
3. Save the changes.
4. Open a terminal in the program's directory.
5. Run the program using one of the following commands:
   ```bash
   python.exe Converter_dielectric_data_V1.py
   python.exe Converter_magnetic_data_PPMS_V2.py
   python.exe Converter_magnetic_data_SQUID_V2.py
   ```
6. Done! 

---

## Equipment

- **BDS**: Broadband Dielectric Spectroscopy  
  Measured on the Concept 11 dielectric spectrometer by Novocontrol.

- **PPMS**: Physical Property Measurement System  
  Measured on the PPMS® DynaCool system by Quantum Design.

- **SQUID**: Superconducting Quantum Interference Device  
  Measured on the MPMS®3 SQUID by Quantum Design.

---

## Repository Structure

```
├── BDS
│   ├── BDS_data_converted.txt
│   ├── BDS_data.txt
│   └── Converter_dielectric_data_V1.py
├── PPMS
│   ├── acdH_1_9K_converted.txt
│   ├── acdH_1_9K.dat
│   └── Converter_magnetic_data_PPMS_V2.py
├── README.md
└── SQUID
    ├── ac_dc.dat
    ├── ac_dc.out
    └── Converter_magnetic_data_SQUID_V2.py
```

---

## Notes

- You dont need any additional liberies.
- Examples of input and output files are provided in their respective directories.
- Feel free to use, adapt, and improve these tools for your scientific workflows.
