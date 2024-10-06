from datetime import datetime, timedelta

# Function to display the current date and time
def display_current_datetime():
    current_date = datetime.now()  # Get the current date and time
    print("Current date and time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))
    return current_date

# Function to calculate a future date based on user input
def calculate_future_date(current_date):
    number_of_days = int(input("Enter the number of days to add to the current date: "))
    future_date = current_date + timedelta(days=number_of_days)  # Calculate future date
    print("Future date:", future_date.strftime("%Y-%m-%d"))

# Main function to run the script
def main():
    current_date = display_current_datetime()  # Display current date and time
    calculate_future_date(current_date)  # Calculate and display future date

if __name__ == "__main__":
    main()
 
