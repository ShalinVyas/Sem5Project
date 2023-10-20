import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the directory to monitor
directory_to_monitor = "C:/Users/91997/Documents/B. Tech/5th sem"  # Change this to your target directory

# Define the log file path
log_file = "file_browsing_log.txt"


# Create a custom event handler to log file system events
class FileEventHandler(FileSystemEventHandler):
    def on_any_event(self, event):
        if event.is_directory:
            return
        log_event(event)


# Log the file system event to the specified log file
def log_event(event):
    with open(log_file, "a") as log:
        log.write(f"Action: {event.event_type}\n")
        log.write(f"File: {event.src_path}\n")
        log.write(f"Time: {time.strftime('%Y-%m-%d %H:%M:%S')}\n")
        log.write("=" * 30 + "\n")


if __name__ == "__main__":
    # Ensure the log file is created or cleared
    with open(log_file, "w") as log:
        log.write("File Browsing Log\n")
        log.write("=" * 30 + "\n")

    # Set up the observer and event handler
    event_handler = FileEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=directory_to_monitor, recursive=True)

    try:
        # Start the observer to monitor file system events
        observer.start()
        print(f"Monitoring {directory_to_monitor} for file browsing actions...")

        # Keep the script running
        while True:
            time.sleep(1)

    except KeyboardInterrupt:
        observer.stop()
        observer.join()
