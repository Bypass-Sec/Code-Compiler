import os
import subprocess
import tempfile
import uuid

def execute_code(language, code):
    language = language.lower()
    random = uuid.uuid4().hex[:7]
    
    with tempfile.TemporaryDirectory() as temp_dir:
        file_path = os.path.join(temp_dir, f"{random}.{language}")
        
        with open(file_path, "w") as program_file:
            program_file.write(code)
        
        output = ""
        
        if language == "php":
            output = subprocess.run(["C:\\wamp64\\bin\\php\\php5.6.40\\php.exe", file_path], 
                                    capture_output=True, text=True).stdout
        
        elif language == "python":
            output = subprocess.run(["C:\\Users\\KOUSIK\\AppData\\Local\\Programs\\Python\\Python39\\python.exe", file_path], 
                                    capture_output=True, text=True).stdout
        
        elif language == "node":
            js_file_path = f"{file_path}.js"
            os.rename(file_path, js_file_path)
            output = subprocess.run(["node", js_file_path], 
                                    capture_output=True, text=True).stdout
        
        elif language == "c":
            output_exe = os.path.join(temp_dir, f"{random}.exe")
            subprocess.run(["gcc", file_path, "-o", output_exe], 
                           capture_output=True, text=True)
            output = subprocess.run([output_exe], 
                                    capture_output=True, text=True).stdout
        
        elif language == "cpp":
            output_exe = os.path.join(temp_dir, f"{random}.exe")
            subprocess.run(["g++", file_path, "-o", output_exe], 
                           capture_output=True, text=True)
            output = subprocess.run([output_exe], 
                                    capture_output=True, text=True).stdout
        
        return output

# Example usage (you would typically call this function from your web framework)
if __name__ == "__main__":
    # This is just for demonstration purposes
    test_code = "print('Hello, World!')"
    result = execute_code("python", test_code)
    print(result)

