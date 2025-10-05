import requests
class IRCTC:
    def __init__(self):
        user_input =input(""" How would you like to proceed?
        1. Check live train status
        2. Check PNR status
        3. Check train schedule
        """)
        if user_input == '1':
            self.check_live_train_status()
        elif user_input == '2':
            self.check_pnr_status()
        elif user_input == '3':
            self.check_train_schedule()
        else:
            print("Invalid input. Please try again.")
            self.__init__()
            
    def check_pnr_status(self):
        pnr_number = input("Enter your PNR number: ")
        # Here you would typically call an API to get PNR status
        print(f"Fetching PNR status for {pnr_number}...")
        # Simulated response
        print(f"PNR {pnr_number} is confirmed. Your seat is 45A in coach B1.")
        def check_live_train_status(self):
        train_number = input("Enter the train number: ")
        date = input("Enter the date (DD-MM-YYYY): ")
        # Here you would typically call an API to get live train status
        print(f"Fetching live status for train {train_number} on {date}...")
        # Simulated response
        print(f"Train {train_number} is currently on time and at station XYZ.")
        
    def check_train_schedule(self):
        train_number = input("Enter the train number: ")
        # Here you would typically call an API to get train schedule
        print(f"Fetching schedule for train {train_number}...")
        # Simulated response
        print(f"Train {train_number} departs from ABC at 10:00 AM and arrives at DEF at 4:00 PM.")
        
    def fetch_data(self, endpoint, params):
        # This is a placeholder for actual API call logic
        print(f"Fetching data from {endpoint} with params {params}")
        return {"status": "success", "data": {}}