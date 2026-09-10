import json
import csv
import time

PARKING_SLOTS = 10  # Total parking slots
occupied_slots = {}  # Dictionary to track vehicle-slot mapping
available_slots = list(range(1, PARKING_SLOTS + 1))  # List of available slots

# File paths
PARKING_LOG_FILE = "data/parking_log.json"
HISTORY_LOG_FILE = "data/vehicle_history.csv"

# Load existing parking data
def load_parking_data():
    try:
        with open(PARKING_LOG_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

# Save updated parking data
def save_parking_data(data):
    with open(PARKING_LOG_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Log vehicle movement history
def log_vehicle_history(plate_number, status, slot=None):
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(HISTORY_LOG_FILE, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([plate_number, status, slot, timestamp])

# Manage vehicle entry & exit
def manage_parking(plate_number):
    parking_data = load_parking_data()

    if plate_number in parking_data:  # If vehicle is exiting
        print(f"{plate_number} is exiting.")
        slot = parking_data[plate_number]["slot"]
        available_slots.append(slot)  # Release the slot
        available_slots.sort()  # Maintain slot order

        log_vehicle_history(plate_number, "Exit", slot)  # Log exit
        del parking_data[plate_number]  # Remove vehicle from active log
    else:  # If vehicle is entering
        if available_slots:
            allocated_slot = available_slots.pop(0)  # Assign lowest free slot
            entry_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

            parking_data[plate_number] = {
                "slot": allocated_slot,
                "entry_time": entry_time
            }

            log_vehicle_history(plate_number, "Entry", allocated_slot)  # Log entry
            print(f"{plate_number} allocated slot {allocated_slot}.")
        else:
            print("🚫 Parking Full!")

    save_parking_data(parking_data)
