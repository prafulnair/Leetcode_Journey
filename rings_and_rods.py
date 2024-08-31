class Solution:
    def countPoints(self, rings: str) -> int:
        
        data = list(rings)
        dataMap = {}
        for i in range(1, len(data),2):
            if data[i] in dataMap:
                dataMap[data[i]] += data[i-1]
            else:
                dataMap[data[i]] = data[i-1]

        count = 0
        good_set = set(list("BGR"))
        print(dataMap)
        for value in dataMap.values():
            if set(list(value)) == good_set:
                count += 1

        return count
