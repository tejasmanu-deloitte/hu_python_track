class StringClass:

    def __init__(self, str1):
        self.str1 = str1

    def strlen(self):
        length = len(self.str1)
        return length

    def str_to_lis(self):
        characters = list(self.str1)
        return characters


obj1 = StringClass("12314532")
print(obj1.strlen())
print(obj1.str_to_lis())


class PairsPossible(StringClass):

    def possible_pairs(self):
        lis2 = list()

        lis = StringClass.str_to_lis(self)
        for element in range(0, StringClass.strlen(self), 1):
            for next_element in range(0, StringClass.strlen(self), 1):
                if element != next_element:
                    lis2.append((lis[element], lis[next_element]))

        return lis2

    def print_possible_pair(self):
        print(*self.possible_pairs())


obj2 = PairsPossible("1357935")
print(obj2.possible_pairs())
print(obj2.print_possible_pair())


class SearchCommonElements():

    def __init__(self, a, b):
        self.StringClass_string = a
        self.PossiblePair_string = b
        self.common_list = list()

    def find_common(self):
        dict= {}

        for ele in self.StringClass_string:
            if ele in dict:
                continue
            else:
                dict[ele] = 1

        for element1 in self.PossiblePair_string:
            if element1 in dict:
                self.common_list.append(element1)