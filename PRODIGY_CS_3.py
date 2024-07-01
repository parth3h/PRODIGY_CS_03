def password_strength(password):
    # Check password length
    if len(password) < 8:
        return "Weak"
    elif 8 <= len(password) < 12:
        return "Medium"
    else:
        # Count occurrences of uppercase, lowercase, digits, and symbols
        upper_count = sum(1 for char in password if char.isupper())
        lower_count = sum(1 for char in password if char.islower())
        digit_count = sum(1 for char in password if char.isdigit())
        symbol_count = sum(1 for char in password if not char.isalnum())

        # Determine strength based on character types
        total_count = upper_count + lower_count + digit_count + symbol_count
        if total_count < 3:
            return "Weak"
        else:
            return "Strong"

# Example usage:
user_password = input("Enter your password: ")
print(f"Password strength: {password_strength(user_password)}")