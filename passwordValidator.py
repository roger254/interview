class Password_Validator(object):
    def validate_password(self, passwords):
        """return valid passwords from the string input"""
        special_characters = ['$', '#', '@']
        passwords_list = passwords.split(",")
        correct_passwords = []
        for password in passwords_list:
            lower_case_counter = 0
            upper_case_counter = 0
            digit_counter = 0
            special_character_counter = 0
            for char in password:
                if char.islower():
                    lower_case_counter += 1
                elif char.isupper():
                    upper_case_counter += 1
                elif char.isdigit():
                    digit_counter += 1
                elif char in special_characters:
                    special_character_counter += 1
            if (
                    lower_case_counter >= 1 and upper_case_counter >= 1 and digit_counter >= 1 and special_character_counter >= 1):
                if (len(password) > 5 and len(password) < 13):
                    correct_passwords.append(password)
        return_String = ",".join(correct_passwords)
        return return_String
