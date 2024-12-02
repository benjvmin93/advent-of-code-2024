INPUT_PATH = "./input.csv"

def isReportSafe(report: list[int]):
    # Check if list is sorted in ascending order:
    if report == sorted(report):
        return all(
            report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] > 0 
            for i in range(len(report) - 1)
        )
      
    if report == sorted(report, reverse=True):
        return all(
            report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] > 0 
            for i in range(len(report) - 1)
        )

    return False

def test():
    cases = [
        ([29, 31, 34, 37, 39], True),
        ([50, 52, 54, 57, 60, 63, 64], True),
        ([7, 8, 9, 12, 15, 17], True),
        ([15, 13, 12, 9, 7, 4, 2], True),
        ([7, 6, 4, 2, 1], True),
        ([1, 2, 7, 8, 9], False),
        ([9, 7, 6, 2, 1], False),
        ([1, 3, 2, 4, 5], False),
        ([8, 6, 4, 4, 1], False),
        ([1, 3, 6, 7, 9], True)
    ]
    
    for (report, isSafe) in cases:
        assert(isReportSafe(report) == isSafe)

def main():
    test()
    reports = []
    with open(INPUT_PATH, 'r') as file:
        for line in file:
            elts = line.split()
            reports.append(list(map(int, elts)))
    result = 0
    for report in reports:
        if isReportSafe(report):
            print("safe")
            result += 1
    
    print(result)
    return result

if __name__ == "__main__":
    main()