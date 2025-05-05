import os
import platform
import subprocess
import sys
import uuid

def run_command(command, shell=True):
    """Run a shell command and handle errors."""
    try:
        result = subprocess.run(command, shell=shell, check=True, text=True, capture_output=True)
        print(result.stdout)
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error running command '{command}': {e.stderr}")
        return False

def check_files():
    """Check for required files."""
    base_dir = r"C:\Users\17692\Desktop\GHY 468\Final Project\Final Project 2"
    required_files = [
        os.path.join(base_dir, "us_swahili_map.py"),
        os.path.join(base_dir, "ne_110m_admin_1_states_provinces.shp")
    ]
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    if missing:
        print("Error: The following required files are missing:")
        for file in missing:
            print(f"- {file}")
        print("\nPlease ensure the files are located at:")
        print(r"C:\Users\17692\Desktop\GHY 468\Final Project\Final Project 2")
        print("Download the shapefile from: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/")
        sys.exit(1)
    print("All required files are present.")

def main():
    print(f"Output file: run_us_map_script_{uuid.uuid4().hex}.txt")
    print("\n=== Running the U.S. Swahili Map Script ===")

    # Verify operating system
    if platform.system() != "Windows":
        print("Error: This script is tailored for Windows. Please run on a Windows system.")
        sys.exit(1)

    # Check working directory
    expected_dir = r"C:\Users\17692\Desktop\GHY 468\Final Project\Final Project 2"
    if os.getcwd().lower() != expected_dir.lower():
        print(f"Error: Please run this script from: {expected_dir}")
        print(f"Current directory: {os.getcwd()}")
        print("Change directory using: cd \"C:\\Users\\17692\\Desktop\\GHY 468\\Final Project\\Final Project 2\"")
        sys.exit(1)

    # Check for required files
    print("\nChecking for required files...")
    check_files()

    # Define virtual environment details
    env_name = r"C:\Users\17692\Desktop\GHY 468\Final Project\Final Project 2\us_map_env_82a50236"
    activate_cmd = f"{env_name}\\Scripts\\activate.bat"
    python_cmd = f"{env_name}\\Scripts\\python.exe"

    # Instructions for manual steps
    print("\nFollow these steps to run the map script:")
    print("\nStep 1: Open Command Prompt")
    print("   - Press Win + R, type 'cmd', and press Enter.")
    print(f"\nStep 2: Navigate to your working directory")
    print(f"   - Run: cd \"C:\\Users\\17692\\Desktop\\GHY 468\\Final Project\\Final Project 2\"")
    print(f"\nStep 3: Activate the virtual environment")
    print(f"   - Run: \"{activate_cmd}\"")
    print("   - You should see '(us_map_env_82a50236)' in your prompt.")
    print(f"\nStep 4: Run the map script")
    print(f"   - Run: python us_swahili_map.py")
    print("   - This will generate the map as a PNG file in the current directory.")
    print("\nStep 5: Deactivate the environment")
    print("   - Run: deactivate")
    print("\nNote: If you encounter 'ModuleNotFoundError', ensure the virtual environment is activated.")
    print("The shapefile is already in place.")

    # Attempt to run the script programmatically
    print("\nAttempting to run the script programmatically (may require manual steps if it fails)...")
    run_script_cmd = f'call "{activate_cmd}" && "{python_cmd}" us_swahili_map.py && deactivate'
    if run_command(run_script_cmd):
        print("Map script executed successfully.")
    else:
        print("Programmatic execution failed. Please follow the manual steps above.")

if __name__ == "__main__":
    main()