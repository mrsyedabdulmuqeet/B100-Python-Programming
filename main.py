"""
Module: main.py
Description: Execution root and interactive terminal for the Heritage Tourism System.
"""

from models import Visitor, TourGuide, BookingSystem
from storage import load_landmarks, log_transaction

# Define file paths
DATA_FILE = "landmarks.csv"
LOG_FILE = "transactions.txt"

def initialize_system() -> BookingSystem:
    """Bootstraps the system by loading the manual CSV data."""
    sys = BookingSystem()
    
    # Load landmarks from the manually created CSV via storage.py
    loaded_landmarks = load_landmarks(DATA_FILE)
    
    # Populate the system database
    for landmark in loaded_landmarks.values():
        sys.register_landmark(landmark)
        
    # Register a few guides
    sys.register_guide(TourGuide("G001", "Rahul", "History"))
    sys.register_guide(TourGuide("G002", "Yash", "Architecture"))
    
    return sys

def run_application():
    """Main execution function featuring a while-loop for user interaction."""
    system = initialize_system()
    
    # Check if data loaded correctly; if not, halt execution.
    if not system.landmarks:
        print("System halted due to missing or empty data file.")
        return

    # Create a session visitor
    current_visitor = Visitor("V001", "John Doe", "john.doe@email.com")
    
    while True:
        print("\n" + "="*50)
        print("HERITAGE TOURISM & BOOKING SYSTEM".center(50))
        print("="*50)
        print("1. View All Landmarks")
        print("2. Book a Tour Ticket")
        print("3. View My Itinerary")
        print("4. Exit System")
        print("="*50)
        
        # Exception Handling: Ensuring the user types an integer
        try:
            choice = int(input("Please enter a menu option (1-4): "))
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
            
        if choice == 1:
            print("\n--- Available Heritage Sites ---")
            for l_id, landmark in system.landmarks.items():
                print(f"[{l_id}] {landmark.get_details()}")
                
        elif choice == 2:
            landmark_id = input("\nEnter the Landmark ID you wish to book (e.g., L001): ").strip().upper()
            result = system.process_transaction(current_visitor, landmark_id)
            print("\n" + result)
            
            # Log successful transactions to the text file
            if "Success" in result:
                log_transaction(LOG_FILE, f"Visitor {current_visitor.visitor_id} booked {landmark_id}")
                
        elif choice == 3:
            print("\n--- Current Itinerary ---")
            itinerary = current_visitor.view_itinerary()
            if itinerary:
                for item in itinerary:
                    print(f"- {item}")
            else:
                print("Your itinerary is currently empty.")
                
        elif choice == 4:
            print("\nThank you for using the Heritage Tourism System. Goodbye!")
            break
            
        else:
            print("Invalid selection. Please choose an option from the menu.")

if __name__ == "__main__":
    run_application()
