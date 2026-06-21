# Heritage Tourism & Booking System

**Module:** B100 Introduction to Computer Programming with Python  

## Project Purpose
The Heritage Tourism & Booking System is an interactive, Python-based backend application designed to manage visitor access to high-traffic historical landmarks across Germany. This system addresses the operational complexities of manual ticketing by automating ticket processing, tracking real-time capacity inventory, and managing dynamic visitor itineraries. It operates entirely via a terminal interface and ensures data persistence through a flat-file database approach.

## Key Features
* **Real-Time Capacity Tracking:** Automatically rejects bookings if a landmark (e.g., Neuschwanstein Castle, Brandenburg Gate) has reached its maximum visitor capacity.
* **Dynamic State Management:** Maintains individual visitor itineraries that update seamlessly upon successful transactions.
* **Robust File I/O Operations:** Reads initial landmark data from a locally stored CSV file and appends successful bookings to a continuous text log to ensure data outlives program execution.
* **Defensive Error Handling:** Utilizes `try...except` blocks to prevent fatal runtime crashes caused by unpredictable user inputs (e.g., `ValueError`) or missing data files (`FileNotFoundError`).
* **Object-Oriented Architecture:** Strictly adheres to the Single Responsibility Principle and encapsulation, separating core logic into distinct, manageable modules.

## File Structure
The project is modularly structured to enhance code readability and maintainability:

* `main.py` - The execution root containing the interactive terminal interface and control structures.
* `models.py` - Contains the core Object-Oriented models (`Landmark`, `Visitor`, `TourGuide`, `BookingSystem`).
* `storage.py` - Handles all file input/output mechanisms and transaction logging.
* `data/landmarks.csv` - A manually curated flat-file database containing the master list of 15 German heritage sites and their capacities.
* `data/transactions.txt` - An auto-generated log file that safely stores records of all successful booking transactions.

## Installation and Execution Instructions
This project requires no external libraries (like Pandas or NumPy) and runs purely on Python's standard library.

1.  **Prerequisites:** Ensure you have Python 3.x installed on your machine.
2.  **Download:** Clone this repository or download the ZIP file and extract it to your local machine.
3.  **Directory Setup:** Ensure the `data/` folder containing `landmarks.csv` is located in the same root directory as the Python scripts.
4.  **Execution:** Open your terminal or command prompt, navigate to the project directory, and run the following command:
    ```bash
    python main.py
    ```

## Example Usage
Upon running the program, users are greeted with an interactive terminal menu. 

**Viewing Landmarks:**
Inputting `1` will parse the CSV and display the available sites:
```text
==================================================
        HERITAGE TOURISM & BOOKING SYSTEM         
==================================================
1. View All Landmarks
2. Book a Tour Ticket
3. View My Itinerary
4. Exit System
==================================================
Please enter a menu option (1-4): 1

--- Available Heritage Sites ---
[L001] Brandenburg Gate (Berlin) - Capacity: 0/500
[L002] Neuschwanstein Castle (Bavaria) - Capacity: 0/300
[L003] Cologne Cathedral (Cologne) - Capacity: 0/800