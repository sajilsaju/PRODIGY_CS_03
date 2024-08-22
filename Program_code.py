# Python code to build the password complexity checker tool.


import re

def check_password_strength(password):
    # Define the criteria for password strength
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r"[A-Z]", password) is not None
    lowercase_criteria = re.search(r"[a-z]", password) is not None
    number_criteria = re.search(r"[0-9]", password) is not None
    special_char_criteria = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
    
    # Calculate strength based on the criteria
    strength = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])
    
    # Provide feedback based on the strength
    if strength == 5:
        return "Strong!!"
    elif 3 <= strength < 5:
        return "Moderate!"
    else:
        feedback = "Poor!. Consider the following improvements:\n"
        if not length_criteria:
            feedback += "- Ensure the password is at least 8 characters long\n"
        if not uppercase_criteria:
            feedback += "- Include at least one uppercase letter\n"
        if not lowercase_criteria:
            feedback += "- Include at least one lowercase letter\n"
        if not number_criteria:
            feedback += "- Include at least one digit\n"
        if not special_char_criteria:
            feedback += "- Include at least one special character (!@#$%^&*(),.?\":{}|<>)\n"

        return feedback

# Example usage
password = input("Enter your password: ")
strength = check_password_strength(password)
print(f"Password strength: {strength}")
