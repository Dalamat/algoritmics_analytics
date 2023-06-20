import subprocess

def execute_script(script_path):
    result = subprocess.run(["python", script_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    if result.returncode == 0:
        print("Script executed successfully. Transaction committed.")
        print("Output:", result.stdout)
        return True
    elif result.returncode == 1:
        print("Script executed, but transaction rolled back. Error:", result.stdout)
        return False
    else:
        print("Script execution failed. General error:", result.stderr)
        return False

#Test Run
#execute_script("C:\\Cream\\Scripts\\python\\refresh_db_groups_check_errors.py")