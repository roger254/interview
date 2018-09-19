class Tripple_Check(object):
    def get_unique_element(self, sorted_dict):
        """returns unique item from a dictionary"""
        for a in sorted_dict:
            if sorted_dict[a] == 1:
                return (a)

    def sort_into_dict(self, num_list):
        """sorts a list into a dictionary depending on how many times an element appears"""
        item_dict = {}
        for num in num_list:
            if num in item_dict:
                item_dict[num] += 1
            else:
                item_dict[num] = 1
        print("Finished Sorting")
        return item_dict

    def return_unique_element(self, num_list):
        """prints unique element from a list"""
        sorted_dict = self.sort_into_dict(num_list)
        element = self.get_unique_element(sorted_dict)
        return element
