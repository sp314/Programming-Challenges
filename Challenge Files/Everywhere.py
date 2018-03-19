def Everywhere():
    cityList = []
    distinctCities = 0
    ncities = int(input())
    for cities in range(ncities):
        city = input()
        if city not in cityList:
            distinctCities += 1
        cityList.append(city)
    return distinctCities

def RunEveryWhereCase():
    testcase = int(input())
    for case in range(testcase):
        print(Everywhere())

RunEveryWhereCase()