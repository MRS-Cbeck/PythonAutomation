import pyautogui
import pygetwindow as gw
import time
import logging


# Configure logging
logging.basicConfig(
    filename="MisysWindowTracker.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def show_error_message(message):
    try:
        pyautogui.alert(text=message, title="Error", button="OK")
    except Exception as alert_error:
        logging.error("Failed to show error message: %s", alert_error)
        print("Error:", message, "\nPlease check the log file for details.")


def get_capslock_state():
    import ctypes
    # Check the state of the Caps Lock key
    return ctypes.windll.user32.GetKeyState(0x14) != 0


def track_active_window(target_title, interval=0.5):
    last_active_window = None
    try:
        while True:
            try:
                active_window = gw.getActiveWindow()
                if active_window:
                    title = active_window.title
                    if title != last_active_window:
                        print("Active window changed:", title)
                        last_active_window = title
                        if target_title.lower() in title.lower() and "Login" not in title:
                            caps_lock_state = get_capslock_state()
                            if caps_lock_state is False:
                                print("Misys Manufacturing window detected. Enabling Caps Lock.")
                                pyautogui.press('capslock')
                            else:
                                print("Caps Lock is ON, no action taken.")
                        else:
                            caps_lock_state = get_capslock_state()
                            if caps_lock_state is True:
                                pyautogui.press('capslock')
                else:
                    print("No active window detected.")
            except Exception as e:
                print("Error retrieving active window:", e)
            # Wait for the specified interval before checking again
            time.sleep(interval)
    except KeyboardInterrupt:
        print("Tracking stopped.")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        print("[Cleanup] Exiting tracking loop.")


if __name__ == "__main__":
    print("Starting to track active window changes...")
    track_active_window(" - MRS")