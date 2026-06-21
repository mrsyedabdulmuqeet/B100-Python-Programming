"""
Module: models.py
Description: Core object-oriented data models for the Heritage Tourism Booking System.
This module defines the primary entities: Landmark, Visitor, TourGuide, and BookingSystem.
"""

class Landmark:
    """Represents a historical landmark available for tours."""
    
    def __init__(self, landmark_id: str, name: str, location: str, max_capacity: int):
        self.landmark_id = landmark_id
        self.name = name
        self.location = location
        self.max_capacity = max_capacity
        self.current_bookings = 0

    def get_details(self) -> str:
        """Returns a formatted string of the landmark's details."""
        return f"{self.name} ({self.location}) - Capacity: {self.current_bookings}/{self.max_capacity}"

    def book_slot(self) -> bool:
        """Increments current bookings if capacity allows. Returns True if successful."""
        if not self.is_full():
            self.current_bookings += 1
            return True
        return False

    def cancel_slot(self) -> bool:
        """Decrements current bookings if greater than zero. Returns True if successful."""
        if self.current_bookings > 0:
            self.current_bookings -= 1
            return True
        return False

    def is_full(self) -> bool:
        """Checks if the landmark has reached maximum capacity."""
        return self.current_bookings >= self.max_capacity


class Visitor:
    """Represents a user booking tours at various landmarks."""
    
    def __init__(self, visitor_id: str, name: str, contact_info: str):
        self.visitor_id = visitor_id
        self.name = name
        self.contact_info = contact_info
        self.itinerary = []  # List of booked landmark names

    def purchase_ticket(self, landmark: Landmark) -> str:
        """Attempts to book a slot at a landmark and updates the itinerary."""
        if landmark.book_slot():
            self.itinerary.append(landmark.name)
            return f"Success: Ticket purchased for {landmark.name}."
        return f"Error: {landmark.name} is currently at full capacity."

    def view_itinerary(self) -> list:
        """Returns the list of currently booked tours."""
        return self.itinerary

    def refund_ticket(self, landmark: Landmark) -> str:
        """Removes a landmark from the itinerary and cancels the slot."""
        if landmark.name in self.itinerary:
            landmark.cancel_slot()
            self.itinerary.remove(landmark.name)
            return f"Success: Ticket refunded for {landmark.name}."
        return f"Error: No active booking found for {landmark.name}."

    def update_contact(self, new_contact: str) -> None:
        """Updates the visitor's contact information."""
        self.contact_info = new_contact


class TourGuide:
    """Represents a guide who can be assigned to specific landmark tours."""
    
    def __init__(self, guide_id: str, name: str, specialization: str):
        self.guide_id = guide_id
        self.name = name
        self.specialization = specialization
        self.assigned_tours = []

    def assign_tour(self, landmark_name: str) -> str:
        """Assigns the guide to a specific landmark tour."""
        if landmark_name not in self.assigned_tours:
            self.assigned_tours.append(landmark_name)
            return f"Guide {self.name} assigned to {landmark_name}."
        return f"Guide {self.name} is already assigned to this tour."

    def remove_tour(self, landmark_name: str) -> str:
        """Removes a landmark from the guide's schedule."""
        if landmark_name in self.assigned_tours:
            self.assigned_tours.remove(landmark_name)
            return f"Tour {landmark_name} removed from {self.name}'s schedule."
        return f"Tour {landmark_name} not found in schedule."

    def view_schedule(self) -> list:
        """Returns the guide's current tour assignments."""
        return self.assigned_tours

    def check_availability(self, date_time: str) -> bool:
        """
        Placeholder method for scheduling logic. 
        Currently returns True, but can be expanded to check specific date conflicts.
        """
        return True


class BookingSystem:
    """Master controller that aggregates objects and manages system logic."""
    
    def __init__(self):
        self.landmarks = {}  # Dictionary mapping ID to Landmark objects
        self.guides = {}     # Dictionary mapping ID to TourGuide objects
        self.total_transactions = 0

    def register_landmark(self, landmark: Landmark) -> None:
        """Adds a new landmark to the system database."""
        self.landmarks[landmark.landmark_id] = landmark

    def register_guide(self, guide: TourGuide) -> None:
        """Adds a new tour guide to the system database."""
        self.guides[guide.guide_id] = guide

    def search_available_guides(self, specialization: str) -> list:
        """Returns a list of guides matching a specific specialization."""
        available = []
        for guide in self.guides.values():
            if guide.specialization.lower() == specialization.lower():
                available.append(guide.name)
        return available

    def process_transaction(self, visitor: Visitor, landmark_id: str) -> str:
        """High-level method to process a visitor booking via the system."""
        landmark = self.landmarks.get(landmark_id)
        if landmark:
            result = visitor.purchase_ticket(landmark)
            if "Success" in result:
                self.total_transactions += 1
            return result
        return "Error: Landmark ID not found."