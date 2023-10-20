import psutil
import time
import sys

# Define the list of application names you want to monitor
applications_to_monitor = ["chrome.exe", "firefox.exe", "POWERPNT.EXE", "EXCEL.EXE", "WINWORD.EXE"]

# Create a dictionary to track the running processes for each application
running_processes = {app_name: None for app_name in applications_to_monitor}

def is_system_process(process_info):
    # Define a list of system usernames
    system_usernames = ["SYSTEM", "NT AUTHORITY\\SYSTEM"]

    username = process_info.get('username', '')
    if username is not None:
        return any(username.upper() == sys_username for sys_username in system_usernames)
    else:
        # If 'username' is missing, it's not a system process
        return False

def log_running_processes(duration_seconds):
    end_time = time.time() + duration_seconds

    with open('process_log.txt', 'a') as log_file:
        log_file.write("Process Log\n")
        log_file.write("=" * 30 + "\n")

    while time.time() < end_time:
        for process in psutil.process_iter(attrs=['pid', 'name', 'username', 'create_time']):
            try:
                process_info = process.info

                # Check if the process is a system process
                if is_system_process(process_info):
                    continue

                process_name = process_info.get('name', '').lower()

                # Check if the process name is in the list of applications to monitor
                if process_name in applications_to_monitor:
                    if running_processes[process_name] is None:
                        running_processes[process_name] = process_info
                        process_start_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(process_info['create_time']))
                        current_time = time.strftime('%Y-%m-%d %H:%M:%S')
                        process_runtime = round(time.time() - process_info['create_time'], 2)

                        with open('process_log.txt', 'a') as log_file:
                            log_file.write(f"Name: {process_info['name']}\n")
                            log_file.write(f"Username: {process_info['username']}\n")
                            log_file.write(f"Start Time: {process_start_time}\n")
                            log_file.write(f"Current Time: {current_time}\n")
                            log_file.write(f"Runtime: {process_runtime} seconds\n")
                            log_file.write("=" * 30 + "\n")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass

        # Check for ended processes and log their end times
        for app_name, process_info in list(running_processes.items()):
            if process_info is not None:
                try:
                    process = psutil.Process(process_info['pid'])
                    if not process.is_running():
                        end_time = time.strftime('%Y-%m-%d %H:%M:%S')
                        with open('process_log.txt', 'a') as log_file:
                            log_file.write(f"Name: {process_info['name']} (Closed)\n")
                            log_file.write(f"End Time: {end_time}\n")
                            log_file.write("=" * 30 + "\n")
                        running_processes[app_name] = None
                except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                    pass

        time.sleep(1)

if __name__ == "__main__":
    try:
        duration_seconds = int(input("Enter the number of seconds to run the process monitor: "))
        log_running_processes(duration_seconds)
    except ValueError:
        print("Invalid input. Please enter a valid number of seconds.")
        sys.exit(1)
