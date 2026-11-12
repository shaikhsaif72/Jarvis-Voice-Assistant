import subprocess
import ctypes
from datetime import datetime

import psutil


# =========================
# TIME
# =========================

def get_time():

    current_time = datetime.now().strftime(
        "%I:%M %p"
    )

    return f"The current time is {current_time}."


# =========================
# DATE
# =========================

def get_date():

    current_date = datetime.now().strftime(
        "%A, %d %B %Y"
    )

    return f"Today is {current_date}."


# =========================
# BATTERY
# =========================

def get_battery():

    battery = psutil.sensors_battery()

    if battery is None:

        return "I couldn't detect the battery."

    percentage = round(battery.percent)

    if battery.power_plugged:

        return (
            f"Your battery is at {percentage} percent "
            "and the charger is connected."
        )

    return (
        f"Your battery is at {percentage} percent."
    )


# =========================
# OPEN APPLICATION
# =========================

def open_application(app):

    applications = {

        "notepad": [
            "notepad.exe"
        ],

        "calculator": [
            "calc.exe"
        ],

        "chrome": [
            "cmd",
            "/c",
            "start",
            "",
            "chrome"
        ],

        "vs code": [
            "cmd",
            "/c",
            "code"
        ],

        "vscode": [
            "cmd",
            "/c",
            "code"
        ]
    }

    command = applications.get(
        app.lower()
    )

    if not command:

        return False

    try:

        subprocess.Popen(
            command,
            shell=False
        )

        return True

    except Exception as e:

        print(
            f"Application Error: {e}"
        )

        return False


# =========================
# CLOSE APPLICATION
# =========================

def close_application(app):

    processes = {

        "notepad": [
            "notepad.exe"
        ],

        "calculator": [
            "CalculatorApp.exe",
            "calc.exe"
        ],

        "chrome": [
            "chrome.exe"
        ],

        "vs code": [
            "Code.exe"
        ],

        "vscode": [
            "Code.exe"
        ]
    }

    process_names = processes.get(
        app.lower()
    )

    if not process_names:

        return False

    try:

        for process_name in process_names:

            result = subprocess.run(
                [
                    "taskkill",
                    "/IM",
                    process_name,
                    "/F"
                ],
                capture_output=True,
                text=True
            )

            if result.returncode == 0:

                return True

        return False

    except Exception as e:

        print(
            f"Close Application Error: {e}"
        )

        return False


# =========================
# LOCK COMPUTER
# =========================

def lock_computer():

    try:

        ctypes.windll.user32.LockWorkStation()

        return True

    except Exception as e:

        print(
            f"Lock Error: {e}"
        )

        return False

