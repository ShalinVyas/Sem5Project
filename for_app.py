import psutil
import time
import csv

# Define the list of applications to monitor
applications_to_monitor = ["chrome.exe", "firefox.exe", "POWERPNT.EXE", "EXCEL.EXE", "notepad.exe"]

# Define the CSV file path
csv_file = "application_action_log.csv"

# Create a dictionary to store the start times of monitored applications
start_times = {}

def log_event(action, application, start_time, end_time, time_spent):
    with open(csv_file, "a", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow([action, application, start_time, end_time, time_spent, time.strftime('%Y-%m-%d')])

if __name__ == "__main__":
    # Ensure the CSV file is created with headers
    with open(csv_file, "w", newline='') as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(["Action", "Application", "Start Time", "End Time", "Time Spent", "Date"])

    while True:
        # Get a list of currently running processes
        current_processes = [p for p in psutil.process_iter(attrs=["name"])]

        for process in current_processes:
            process_name = process.info["name"].lower()

            if process_name in applications_to_monitor:
                if process_name not in start_times:
                    # This is a new instance of the application
                    start_times[process_name] = time.time()
                else:
                    # The application is still running; calculate and log time spent
                    end_time = time.time()
                    time_spent = end_time - start_times[process_name]
                    log_event("Started", process_name, time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(start_times[process_name])), time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(end_time)), round(time_spent, 2))
                    del start_times[process_name]

        # Sleep for a while before checking again (adjust as needed)
        time.sleep(5)
