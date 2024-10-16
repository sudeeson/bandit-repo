# import hashlib

# def hardcoded_password():
#     password = "supersecret"  # Hardcoded password
#     return password

# def insecure_hash(data):
#     return hashlib.md5(data.encode()).hexdigest()  # Using MD5, which is insecure

# # Example of using the functions
# if __name__ == "__main__":
#     print("Using a hardcoded password: ", hardcoded_password())
#     user_data = "sensitive information"
#     print("Insecure hash of user data: ", insecure_hash(user_data))
