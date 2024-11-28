# AUTHOR: ServerLite
# DATE: 11/28/24
# NOTE: I am tired, I want to go to bed...

### LIBRARIES ###
import time
import os
import sys

### TIMER CLASS ###
class Timer:
    # Clears the terminal, depending on the operating system
    def __clear():
        platform_type = sys.platform
        if platform_type == "win32" or platform_type == "cygwin": # Windows
            os.system("cls")
        elif platform_type == "linux" or platform_type == "darwin": # Mac or Linux
            os.system("clear")

    # Converts hours to minutes
    def hours_to_minutes(hours):
        return hours * 60

    # Converts minutes to seconds
    def minutes_to_seconds(minutes):
        return minutes * 60

    # Main countdown function
    def countdown(hours=0,minutes=0,seconds=0,clearable=True):
        # Some pretty long/weird code, don't worry about it
        total_seconds = Timer.minutes_to_seconds(Timer.hours_to_minutes(hours) + minutes) + seconds
        
        for _ in range(total_seconds+1):
            if clearable: Timer.__clear() # If user wants countdown to clear terminal...

            # Outputting the result
            print(f"\nClock Time: {hours:02d}:{minutes:02d}:{seconds:02d}")
            print(f"Seconds Time: {total_seconds}")

            # Exchanging things with time of hours -> minutes -> seconds...
            if seconds == 0:
                if minutes > 0:
                    minutes -= 1
                    seconds += 60
            elif minutes == 0:
                if hours > 0:
                    hours -= 1
                    minutes += 60

            # Minus the time, because it would go on forever if it didn't
            total_seconds -= 1
            seconds -= 1

            # Wait one second, because a second is one second. >:)
            time.sleep(1)

        # Times UP!
        print("\nTime's up!")

# Adding this so it doesn't run when you import this class into your code
if __name__ == "__main__":
    Timer.countdown(0,0,5,True) # Funny truth statement
