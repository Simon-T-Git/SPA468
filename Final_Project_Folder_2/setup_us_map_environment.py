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

def check_python_version():
    """Check if Python version is 3.7 or higher."""
    if sys.version_info < (3, 7):
        print("Python 3.7 or higher is required.")
        sys.exit(1)
    print(f"Python version: {sys.version_info.major}.{sys.version_info.minor}")

def create_virtual_env(env_name="us_map_env"):
    """Create and activate a virtual environment."""
    print(f"Creating virtual environment '{env_name}'...")
    # Quote the Python executable path to handle spaces
    python_exe = f'"{sys.executable}"'
    venv_path = os.path.join(os.getcwd(), env_name)
    venv_command = f"{python_exe} -m venv \"{venv_path}\""
    if not run_command(venv_command):
        sys.exit(1)

    # Determine activation command based on OS
    system = platform.system()
    if system == "Windows":
        activate_cmd = f"{env_name}\\Scripts\\activate.bat"
        pip_cmd = f"{env_name}\\Scripts\\pip.exe"
        python_cmd = f"{env_name}\\Scripts\\python.exe"
    else:  # Linux, macOS
        activate_cmd = f"source {env_name}/bin/activate"
        pip_cmd = f"{env_name}/bin/pip"
        python_cmd = f"{env_name}/bin/python"

    return activate_cmd, pip_cmd, python_cmd

def install_dependencies(pip_cmd):
    """Install geopandas and matplotlib."""
    print("Installing dependencies...")
    dependencies = ["geopandas", "matplotlib"]
    for dep in dependencies:
        # Quote pip_cmd to handle spaces in path
        if not run_command(f'"{pip_cmd}" install {dep}'):
            print(f"Failed to install {dep}.")
            sys.exit(1)
        print(f"Successfully installed {dep}.")

def verify_installation(python_cmd):
    """Verify geopandas installation."""
    print("Verifying geopandas installation...")
    # Use the virtual environment's Python directly to check geopandas
    check_cmd = f'"{python_cmd}" -c "import geopandas; print(geopandas.__version__)"'
    if run_command(check_cmd):
        print("Geopandas is installed correctly.")
    else:
        print("Geopandas verification failed.")
        sys.exit(1)

def check_files():
    """Check for required files."""
    required_files = [
        "us_swahili_map.py",
        "ne_110m_admin_1_states_provinces.shp"
    ]
    missing = []
    for file in required_files:
        if not os.path.exists(file):
            missing.append(file)
    if missing:
        print("Error: The following required files are missing:")
        for file in missing:
            print(f"- {file}")
        print("\nPlease ensure the shapefile 'ne_110m_admin_1_states_provinces.shp' is located at:")
        print(r"C:\Users\17692\Desktop\GHY 468\Final Project\Final Project 2")
        print("Download it from: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/")
        sys.exit(1)
    print("All required files are present.")

def main():
    print(f"Output file: setup_us_map_environment_{uuid.uuid4().hex}.txt")
    print("\n=== Setting Up Virtual Environment for U.S. Swahili Map Project ===")

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

    # Check Python version
    check_python_version()

    # Create virtual environment
    env_name = f"us_map_env_{uuid.uuid4().hex[:8]}"
    activate_cmd, pip_cmd, python_cmd = create_virtual_env(env_name)

    # Install dependencies
    install_dependencies(pip_cmd)

    # Verify installation
    verify_installation(python_cmd)

    # Provide instructions
    print("\nSetup complete! To use the environment:")
    print(f"1. Open Command Prompt")
    print(f"   - Press Win + R, type 'cmd', and press Enter.")
    print(f"2. Navigate to: cd \"C:\\Users\\17692\\Desktop\\GHY 468\\Final Project\\Final Project 2\"")
    print(f"3. Activate: \"{os.path.join(os.getcwd(), env_name)}\\Scripts\\activate\"")
    print(f"4. Run the script: python us_swahili_map.py")
    print(f"5. Deactivate: deactivate")
    print("\nNote: The shapefile is already in place.")
    print("If you encounter 'ModuleNotFoundError', ensure the virtual environment is activated.")

if __name__ == "__main__":
    main()