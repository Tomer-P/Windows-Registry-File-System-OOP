# Windows Registry & File System OOP

A Python object-oriented programming project that provides a common abstraction for working with both regular file-system entries and Windows Registry entries.

The project was originally created as an educational operating-systems/OOP assignment in 2020.

## What it does

- Defines abstract base classes for generic entries and data entries.
- Reads file and directory paths and checks read/write permissions.
- Reads from and writes to regular files.
- Uses Python's `winreg` module to access the Windows Registry.
- Checks Registry read/write permissions with `KEY_READ` and `KEY_WRITE`.
- Reads and updates Registry values under `HKEY_CURRENT_USER`.
- Enumerates Registry subkeys.

## Project structure

- `entry.py` — abstract base class for entries.
- `dataentry.py` — abstract interface for readable/writable entries.
- `DirectoryEntry.py` — directory path, permission, and listing operations.
- `FileDataEntry.py` — file read/write and permission operations.
- `registrydataentry.py` — Registry value read/write operations.
- `registrydirectoryentry.py` — Registry key permission and subkey enumeration.
- `test.py` — demonstration script for the different entry types.

## Technologies

- Python
- Object-Oriented Programming
- Abstract Base Classes (`abc`)
- File-system operations (`os`, `pathlib`)
- Windows Registry API (`winreg`)

## Running the project

This project requires **Windows**, because the Registry components use Python's built-in `winreg` module.

The demonstration script expects a Registry path under `HKEY_CURRENT_USER`. Before running it, review the path configured in `test.py` and the setup note in `registrydataentry.py` so it matches a safe test key on your machine.

```bash
python test.py
```

> Note: The original project contains hard-coded example paths from its development environment. Update those paths before running the demo on another machine.

## Author

Tomer Pinhas
