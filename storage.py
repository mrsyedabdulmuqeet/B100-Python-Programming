"""
Module: storage.py
Description: Handles file input and output operations for the Heritage Tourism System.
Reads from a manually created CSV data file and writes transactions to a text log.
"""

import csv
import os
from models import Landmark

def load_landmarks(file_path: str) -> dict:
    """
    Reads the manually curated landmarks.csv file and converts 
    each row into a Landmark object.
    
    Returns:
        A dictionary mapping landmark_id to Landmark objects.
    """
    landmarks = {}
    
    # Exception Handling: Checks if the file exists before attempting to read
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)  # DictReader uses the first row as dictionary keys
            
            for row in reader:
                # Instantiate a Landmark object for each row
                landmark = Landmark(
                    landmark_id=row['landmark_id'],
                    name=row['name'],
                    location=row['location'],
                    max_capacity=int(row['max_capacity'])
                )
                landmarks[landmark.landmark_id] = landmark
                
    except FileNotFoundError:
        print(f"CRITICAL ERROR: The data file '{file_path}' was not found.")
        print("Please ensure your manually created CSV is in the correct directory.")
    except KeyError as e:
        print(f"DATA ERROR: The CSV is missing a required column: {e}")
    except ValueError:
        print("DATA ERROR: 'max_capacity' must be an integer in the CSV.")
        
    return landmarks

def log_transaction(log_path: str, message: str) -> None:
    """
    Appends a successful booking or system event to a continuous text log.
    """
    try:
        with open(log_path, mode='a', encoding='utf-8') as file:
            file.write(message + "\n")
    except IOError as e:
        print(f"SYSTEM ERROR: Could not write to the log file. Details: {e}")