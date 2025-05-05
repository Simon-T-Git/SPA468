import os
import platform
import sys
import subprocess
import uuid

def check_python():
    """Check if Python is accessible and its version."""
    python_version = f"{sys.version_info.major}.{sys.version_info.minor}"
    print(f"Python version: {python_version}")
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required.")
        return False
    return True

def check_terminal():
    """Check if running in a terminal/CLI."""
    if sys.stdin.isatty():
        print("You are running this in a terminal/CLI, which is correct.")
        return True
    else:
        print("Warning: This script should be run in a terminal/CLI, not an IDE's 'Run' button or similar interface.")
        return False

def suggest_interface():
    """Suggest the appropriate terminal interface based on OS."""
    system = platform.system()
    if system == "Windows":
        print("On Windows, use Command Prompt, PowerShell, or Windows Terminal:")
        print("1. Press Win + R, type 'cmd' or 'powershell', and press Enter.")
        print("2. Navigate to your script's directory using 'cd path\\to\\your\\folder'.")
    elif system == "Darwin":  # macOS
        print("On macOS, use Terminal:")
        print("1. Open Terminal (search for it in Spotlight with Cmd + T).")
        print("2. Navigate to your script's directory using 'cd path/to/your/folder'.")
    elif system == "Linux":
        print("On Linux, use your preferred terminal (e.g., GNOME Terminal, Konsole):")
        print("1. Open a terminal.")
        print("2. Navigate to your script's directory using 'cd path/to/your/folder'.")
    else:
        print("Unknown OS. Open a command-line interface and navigate to your script's directory.")

def check_files():
    """Check for required files."""
    required_files = ["setup_geopandas_environment.py", "africa_swahili_map.py"]
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    if missing:
        print("Warning: The following files are missing in your current directory:")
        for file in missing:
            print(f"- {file}")
    else:
        print("All required script files are present.")
    # Check for shapefile
    if not os.path.exists("ne_110m_admin_0_countries.shp"):
        print("Warning: Shapefile 'ne_110m_admin_0_countries.shp' is missing.")
        print("Download it from: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/")

def run_command(command):
    """Run a shell command and return success status."""
    try:
        result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e.stderr}")
        return False

def main():
    print(f"Output file: check_environment_{uuid.uuid4().hex}.txt")
    print("\n=== Environment Check for Running Python Scripts ===")
    
    # Check Python
    if not check_python():
        sys.exit(1)
    
    # Check if in terminal
    check_terminal()
    
    # Suggest correct interface
    print("\nWhere to run the scripts:")
    suggest_interface()
    
    # Check for files
    print("\nChecking for required files:")
    check_files()
    
    # Provide instructions
    print("\nSteps to run the scripts:")
    print("1. Ensure you're in a terminal/CLI (as described above).")
    print("2. Navigate to the directory containing 'setup_geopandas_environment.py' and 'africa_swahili_map.py'.")
    print("   Example: cd /path/to/your/folder")
    print("3. Run the setup script first:")
    print("   python setup_geopandas_environment.py")
    print("4. Follow the setup script's instructions to activate the virtual environment.")
    print("5. Run the map script:")
    print("   python africa_swahili_map.py")
    print("\nNote: Ensure the Natural Earth shapefile is in the same directory.")
    print("If you encounter 'ModuleNotFoundError', confirm the virtual environment is activated.")

if __name__ == "__main__":
    main()