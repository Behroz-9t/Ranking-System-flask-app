# my-flask-app
# OOPs Mid Term Results – Student Ranking System (Web)

A modern, user-friendly web application for ranking students based on their exam scores. Built with Python, Flask, and OOP principles, this project allows teachers and students to easily search for results, view top performers, and display all rankings in a clean, tabular format.

---

## Features

- **Web-based Interface:** Access results from any browser.
- **Search by Seat Number:** Enter only the last three digits; the system auto-completes the seat number.
- **Top Positions:** Instantly view the top 4 ranked students.
- **All Results:** Display the complete ranked list of students by a key.
- **Tie Handling:** Students with equal scores share the same rank.
- **Responsive Design:** Clean, readable tables and forms.
- **CSV Data Loading:** Student data is loaded from a CSV file for easy updates.

---

## How It Works

1. **Home Page:**  
   - Shows a search form for the last three digits of the seat number.
   - Displays the top 4 students by default.

2. **Search:**  
   - Enter the last three digits 
   - The app auto-prepends the default prefix (e.g., `B24110006`) to form the full seat number.
   - Displays the student’s details and rank.

3. **All Results:**  
   - With a key command , view the full ranked list of all students.

---

## Project Structure
my-flask-app
│
├── App_Controller.py
├── File.py
├── index.py
├── main.py
├── Procfile
├── requirements.txt
├── StudentList.py
├── Student.py
├── Teacher.py
├── results.csv
└── README.md

---

- **App_Controller.py:** Main logic for ranking, searching, and rendering HTML.
- **Teacher.py / StudentList.py:** OOP models for teacher and students.
- **File.py:** Loads student data from CSV.
- **index.py:** Flask app entry point.

---

## Key Code Highlights

- **Seat Number Handling:**  
  Prefix is automatically attached:
  - **Ranking Logic:**  
  Handles ties and sorts by total score.

---

## Setup & Usage

1. **Clone the repository:**

2. **Install dependencies:**

3. **Run the Flask app:**

---

## Example

- **Search:**  
  Enter `last digit seat number` → Finds student .

- **Top 4:**  
  Automatically displayed on the home page.

---

## Credits

- **Teacher:** Dr. Humera Tariq
- **Developed By:** Behroz

---

## License

Karachi University (UBIT) License

---

## Links

- [Live Demo](  )

---
