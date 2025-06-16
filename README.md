# Hijri to Gregorian Converter

A simple terminal-based Python program that converts **Hijri (Islamic)** dates to **Gregorian** dates using the `hijri-converter` library. The app ensures proper input validation, gives informative error messages, and offers a clean user experience with `colorama` formatting.

---

## Features

* Converts Hijri dates (e.g., `14/03/1442`) to Gregorian format (e.g., `01 November 2020`).
* Accepts flexible input formats such as:

  * `01/01/1444`
  * `1/1/1444`
  * `01/1/1444`
* Validates format and ranges for day, month, and year.
* Provides clear error messages for incorrect inputs.
* Colorful and user-friendly terminal interface.

---

## Usage

```bash
python Date-Converter.py
```

Then follow the on-screen instructions:

* Input Hijri date in the format `dd/mm/yyyy`
* Type `exit` to quit the program

### Example

```bash
Enter Hijri date (dd/mm/yyyy) or 'exit': 01/02/1442
Hijri date: 01/02/1442
Gregorian date: 18 September 2020
```

---

## Dependencies

Install the required packages using:

```bash
pip install -r requirements.txt
```

---

## Files

* `Date-Converter.py` — Main Python script
* `requirements.txt` — Dependency list

---

## License

MIT License — free to use and modify.

---

## Author

Developed to **Hebr SA**
