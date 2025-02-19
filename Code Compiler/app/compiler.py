import os
import subprocess
import tempfile
import uuid
import sys

def execute_code(language, code):
    language = language.lower()
    random_name = uuid.uuid4().hex[:7]

    with tempfile.TemporaryDirectory() as temp_dir:
        file_extensions = {
            "php": ".php",
            "python": ".py",
            "node": ".js",
            "c": ".c",
            "cpp": ".cpp"
        }
        
        if language not in file_extensions:
            return "Unsupported language."

        file_path = os.path.join(temp_dir, f"{random_name}{file_extensions[language]}")

        with open(file_path, "w") as program_file:
            program_file.write(code)

        output = ""

        try:
            if language == "php":
                php_path = "php"  # Ensure PHP is installed in PATH
                result = subprocess.run([php_path, file_path], capture_output=True, text=True)
            
            elif language == "python":
                python_path = sys.executable  # Automatically detect Python
                result = subprocess.run([python_path, file_path], capture_output=True, text=True)

            elif language == "node":
                result = subprocess.run(["node", file_path], capture_output=True, text=True)

            elif language == "c":
                output_exe = os.path.join(temp_dir, f"{random_name}.exe")
                compile_process = subprocess.run(["gcc", file_path, "-o", output_exe], capture_output=True, text=True)
                if compile_process.returncode != 0:
                    return compile_process.stderr
                result = subprocess.run([output_exe], capture_output=True, text=True)

            elif language == "cpp":
                output_exe = os.path.join(temp_dir, f"{random_name}.exe")
                compile_process = subprocess.run(["g++", file_path, "-o", output_exe], capture_output=True, text=True)
                if compile_process.returncode != 0:
                    return compile_process.stderr
                result = subprocess.run([output_exe], capture_output=True, text=True)

            output = result.stdout + result.stderr  # Capture both stdout & stderr

        except Exception as e:
            output = str(e)

        return output

# Example usage
if __name__ == "__main__":
    test_code = "print('Hello, World!')"
    print(execute_code("python", test_code))

