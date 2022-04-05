class StringClass:

    def __init__(self, str1):
        self.str1 = str1

    def strlen(self):
        length = len(self.str1)
        return length

    def str_to_lis(self):
        characters = list(self.str1)
        return characters


class PairsPossible(StringClass):

    def possible_pairs(self):
        lis2 = list()

        lis = StringClass.str_to_lis(self)
        for element in range(0, StringClass.strlen(self)-1, 1):
            for next_element in range(element+1, StringClass.strlen(self), 1):
                if element != next_element:
                    lis2.append(lis[element] + lis[next_element])

        return lis2

    def print_possible_pair(self):
        print(*self.possible_pairs())


class SearchCommonElements:

    def __init__(self, a, b):
        self.StringClass_string = a
        self.PossiblePair_string = b
        self.common_list = list()

    def find_common(self):
        dict = {}

        for ele in self.StringClass_string:
            if (ele in self.PossiblePair_string):
                if ele in dict:
                    continue
                else:
                    dict[ele] = 1

        for key in dict:
            self.common_list.append(key)

        return self.common_list


class EqualSumPairs():

    def print_equal_sum_pairs(self, lis):

        dict1 = {}

        for pair in lis:
            pairs_list = list(pair)
            sum = 0
            for num in pairs_list:
                sum = sum + int(num)

            if sum in dict1:
                dict1[sum] = dict1[sum] + 1
            else:
                dict1[sum] = 1

        for key in dict1:
            if dict1[key] == 1:
                print(key, end=" ")

obj1 = StringClass("12314532")
print(obj1.strlen())
print(obj1.str_to_lis())

obj2 = PairsPossible("1357359")
print(obj2.possible_pairs())
print(obj2.print_possible_pair())
lis = obj2.possible_pairs()

obj3 = SearchCommonElements(obj1.str1, obj2.str1)
print(obj3.find_common())

obj4 = EqualSumPairs()
obj4.print_equal_sum_pairs(lis)
