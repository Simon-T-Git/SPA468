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

def create_virtual_env(env_name="geo_env"):
    """Create and activate a virtual environment."""
    print(f"Creating virtual environment '{env_name}'...")
    # Quote the Python executable path to handle spaces
    python_exe = f'"{sys.executable}"'
    venv_command = f"{python_exe} -m venv {env_name}"
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

def main():
    # Check Python version
    check_python_version()

    # Create virtual environment
    env_name = f"geo_env_{uuid.uuid4().hex[:8]}"
    activate_cmd, pip_cmd, python_cmd = create_virtual_env(env_name)

    # Install dependencies
    install_dependencies(pip_cmd)

    # Verify installation
    verify_installation(python_cmd)

    # Provide instructions
    system = platform.system()
    print("\nSetup complete! To use the environment:")
    if system == "Windows":
        print(f"1. Activate: {env_name}\\Scripts\\activate")
    else:
        print(f"1. Activate: source {env_name}/bin/activate")
    print("2. Run your script: python africa_swahili_map.py")
    print("3. Deactivate when done: deactivate")
    print("\nNote: Ensure the 'ne_110m_admin_0_countries.shp' shapefile is in your working directory.")
    print("Download it from: https://www.naturalearthdata.com/downloads/110m-cultural-vectors/")

if __name__ == "__main__":
    main()