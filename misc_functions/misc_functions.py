import os
import time

def _sleep(sleep_text: str = 'Going to sleep now... press any key to wake me up:\n') -> str:
    '''Pauses further processing until user input is received. Returns the user input.'''
    start_time = time.time()

    print(f"{sleep_text}")

    while True:
        user_input = input(prompt)
        if user_input:
            end_time = time.time()
            elapsed_time = end_time - start_time

            days, remainder = divmod(elapsed_time, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"I'm awake! Total time asleep: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds")
            return user_input

def _wait(seconds: int, brb_text: str = 'I will BRB for a bit...'):
    '''Pauses further processing for a given number of seconds.'''
    start_time = time.time()

    print(f"{brb_text}")

    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= seconds:
            days, remainder = divmod(elapsed_time, 86400)
            hours, remainder = divmod(remainder, 3600)
            minutes, seconds = divmod(remainder, 60)

            print(f"I'm back! Total time AFK: {int(days)} days, {int(hours)} hours, {int(minutes)} minutes, and {int(seconds)} seconds")
            break

        time.sleep(1)  # Sleep for 1 second to reduce CPU usage


def _do_nothing(reason: str):
    '''Takes no action (hopefully to think some more and do something more productive)'''

    #Do nothing...

    return f"No Action Taken... Reason: {reason}. Maybe we should try something else or ask for help?"
