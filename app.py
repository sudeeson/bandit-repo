
# # #app.py added
# # import subprocess
# # import hashlib
# # import pickle
# # import random
 
# # # 1. Hardcoded password
# # def connect_to_db():
# #     password = "mysecretpassword"  # Hardcoded password
# #     return password
 
# # # 2. Use of eval (dangerous)
# # def unsafe_eval(user_input):
# #     return eval(user_input)  # Evaluates arbitrary input, which can be dangerous
 
# # # 3. Insecure use of subprocess with shell=True
# # def run_command(command):
# #     subprocess.Popen(command, shell=True)  # This allows for shell injection attacks
 
# # # 4. Weak cryptography - use of MD5
# # def weak_hashing(data):
# #     return hashlib.md5(data.encode()).hexdigest()  # MD5 is considered insecure
 
# # # 5. Pickle - Deserialization of untrusted data
# # def load_data(serialized_data):
# #     return pickle.loads(serialized_data)  # Loading untrusted data can lead to arbitrary code execution
 
# # 6. Insecure random number generation
# # def insecure_random():
# #     return random.random()  # Not cryptographically secure for sensitive data

# # # Function to reverse a string
# # def reverse_string(s):
# #     return s[::-1]

# # # Example usage
# # original_string = "Python"
# # reversed_string = reverse_string(original_string)

# print(f"The original string is: {original_string}")
# print(f"The reversed string is: {reversed_string}")
