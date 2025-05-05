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
    required_files = ["africa_swahili_map.py", "ne_110m_admin_0_countries.shp"]
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    if missing:
        print("Error: The following required files are missing:")
        for file in missing:
            print(f"- {file}")
        sys.exit(1)
    print("All required files are present.")

def main():
    print(f"Output file: run_map_script_{uuid.uuid4().hex}.txt")
    print("\n=== Running the Africa Swahili Map Script ===")

    # Verify operating system
    if platform.system() != "Windows":
        print("Error: This script is tailored for Windows. Please run on a Windows system.")
        sys.exit(1)

    # Check for required files
    print("\nChecking for required files...")
    check_files()

    # Define virtual environment details
    env_name = "geo_env_0cd3666f"  # From your output
    activate_cmd = f"{env_name}\\Scripts\\activate.bat"
    python_cmd = f"{env_name}\\Scripts\\python.exe"

    # Instructions for manual steps
    print("\nFollow these steps to run the map script:")
    print("\nStep 1: Open Command Prompt")
    print("   - Press Win + R, type 'cmd', and press Enter.")
    print(f"\nStep 2: Navigate to your working directory")
    print(f"   - Run: cd \"C:\\Users\\17692\\Desktop\\GHY 468\\Final Project\"")
    print(f"\nStep 3: Activate the virtual environment")
    print(f"   - Run: {activate_cmd}")
    print("   - You should see '(geo_env_0cd3666f)' in your prompt.")
    print(f"\nStep 4: Run the map script")
    print(f"   - Run: python africa_swahili_map.py")
    print("   - This will generate the map as a PNG file.")
    print("\nStep 5: Deactivate the environment")
    print("   - Run: deactivate")
    print("\nNote: If you encounter errors, ensure you're in the correct directory and the virtual environment is activated.")

    # Attempt to run the script programmatically (optional, may require manual activation)
    print("\nAttempting to run the script programmatically (may require manual steps if it fails)...")
    run_script_cmd = f'call {activate_cmd} && "{python_cmd}" africa_swahili_map.py && deactivate'
    if run_command(run_script_cmd):
        print("Map script executed successfully.")
    else:
        print("Programmatic execution failed. Please follow the manual steps above.")

if __name__ == "__main__":
    main()