import pandas as pd

def calculate_priority(amount, days_overdue, last_contact):
    """
    Simple logic to rank cases. 
    High Priority = High Amount + High Overdue + Low recent contact.
    """
    # Simple heuristic-based score (can be replaced with ML later)
    score = (amount * 0.4) + (days_overdue * 0.5) - (last_contact * 0.1)
    
    if score > 5000:
        return "High (Assign to Top Agency)"
    elif score > 2000:
        return "Medium"
    else:
        return "Low (Automated Reminder)"

# Example usage
print(calculate_priority(amount=10000, days_overdue=45, last_contact=2))
