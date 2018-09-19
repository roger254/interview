class Simple_Pig_Latin_Converter(object):

    def pig_latin_converter(self, word):
        # create an empty list to store the digits
        digit_list = []
        # keep count of the '?' character
        counter = 0
        # returns if word passed the conditions
        valid = False
        # loop through the string "word"
        for c in range(len(word) - 1):
            # the current character of the string
            char = word[c]
            # check if it is a digit
            if char.isdigit():
                # add to digit list if it is digit
                digit_list.append(char)
            # check if it a '?'
            elif char == '?':
                # check if there is already one digit
                if len(digit_list) == 1:
                    # increase count of '?'
                    counter += 1
            # check if there are already two digits
            if len(digit_list) == 2:
                # find sum of the digits
                total = int(digit_list[0]) + int(digit_list[1])
                if total == 10:
                    if counter == 3:
                        # set valid to true
                        valid = True
                        # store the last digit from the digit list
                        previous_digit = digit_list[1]
                        # empty digit_list to start with a new one
                        del digit_list[:]
                        # if the next character is not the last
                        if (c + 1) != len(word):
                            digit_list.append(previous_digit)
                        # set counter back to zero
                        counter = 0
                    elif counter != 3:
                        valid = False
                        break
                else:
                    if counter == 3:
                        valid = False
                        break
                    else:
                        # set counter back to 0
                        counter = 0
                        # get the current digit
                        previous_digit = digit_list[1]
                        # clear digit list
                        del digit_list[:]
                        # if next character is not the last
                        if (c + 1) != len(word) - 1:
                            # add previous list item as the first digit
                            digit_list.append(previous_digit)

            if (c + 1) == len(word) - 1:
                if len(digit_list) > 0:
                    if word[c + 1].isdigit():
                        total = int(digit_list[0]) + int(word[c + 1])
                        if counter != 3 and total == 10:
                            valid = False
                            break
        # if the next character is the lase
        #
        return valid
