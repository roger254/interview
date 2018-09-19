class Additive_Seqeuence(object):
    def return_additive_list(self, test_list):
        """return a list if it is an additive sequence"""
        checker = True
        list_length = len(test_list)
        if list_length > 2:
            for item in range(list_length - 2):
                first_item = test_list[item]
                second_item = test_list[item + 1]
                third_item = test_list[item + 2]
                sum = first_item + second_item
                if sum != third_item:
                    checker = False
                    break
            if checker:
                return True
            else:
                return "" + str(test_list) + " is not an additive list "
        else:
            return False
