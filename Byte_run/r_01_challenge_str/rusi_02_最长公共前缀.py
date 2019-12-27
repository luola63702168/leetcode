class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            if strs == []:
                return ""
            import re
            strs_length =len(strs)
            count = 0
            last_list = list()
            while True:
                if count == 0:
                    dynamic_re = re.compile(rf"{strs[0][::]}")
                else:
                    dynamic_re = re.compile(rf"{strs[0][:count:]}")
                for i in range(strs_length):
                    if dynamic_re.match(strs[i]):
                        str_temp = dynamic_re.match(strs[i]).group()
                        last_list.append(str_temp)
                        # print(last_list)
                if len(last_list) == strs_length:
                    return last_list[0]
                else:
                    # if last_list[0] == "":
                    #     return ""
                    last_list.clear()
                    count = count - 1
                    continue

