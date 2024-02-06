# djangoCRUD


To install Django on Ubuntu, you can use the following steps:

1. **Update Package Lists:**
   
   Ensure that your package lists are up-to-date:

   ```bash
   sudo apt update
   ```

2. **Install Python and pip:**

   Django requires Python, and pip is the package installer for Python. If you don't have them installed, you can install them using:

   ```bash
   sudo apt install python3 python3-pip
   ```

3. **Install Django:**

   Once Python and pip are installed, you can install Django using pip:

   ```bash
   pip3 install django
   ```

   This will install the latest version of Django.

4. **Verify the Installation:**

   After installation, you can check the Django version to verify that it was installed correctly:

   ```bash
   python3 -m django --version
   ```

   This should print the installed Django version.

Now, you're ready to create Django projects and applications. If you encounter any permission issues, you may need to use `sudo` with the `pip` commands, but it's generally recommended to use virtual environments to avoid potential conflicts with system packages.
