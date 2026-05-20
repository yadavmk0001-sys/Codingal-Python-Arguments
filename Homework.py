import os
import sys
import platform

def shutdown_system():
    """Shuts down the system based on the operating system."""
    os_name = platform.system()

    try:
        if os_name == "Windows":
            os.system("shutdown /s /t 0")  # Immediate shutdown
        elif os_name == "Linux" or os_name == "Darwin":  # Darwin = macOS
            os.system("sudo shutdown now")
        else:
            print(f"Unsupported OS: {os_name}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    # Check if argument is provided
    if len(sys.argv) != 2:
        print("Usage: python shutdown.py shutdown")
        sys.exit(1)

    command = sys.argv[1].lower()

    if command == "shutdown":
        confirm = input("Are you sure you want to shut down? (yes/no): ").strip().lower()
        if confirm == "yes":
            shutdown_system()
        else:
            print("Shutdown cancelled.")
    else:
        print("Invalid argument. Use: shutdown")

if __name__ == "__main__":
    main()