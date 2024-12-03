INPUT_PATH = "./input.csv"

def isSafeAscending(report):
    return all(
            report[i + 1] - report[i] <= 3 and report[i + 1] - report[i] > 0 
            for i in range(len(report) - 1)
    )
    
def isSafeDescending(report):
    return all(
            report[i] - report[i + 1] <= 3 and report[i] - report[i + 1] > 0 
            for i in range(len(report) - 1)
    )

def isReportSafe(report: list[int]):
    # Check if list is sorted in ascending order:
    if report == sorted(report):
        print(f"Report already sorted in ascending order")
        if isSafeAscending(report):
            return True

    elif report == sorted(report, reverse=True):
        print(f"Report already sorted in descending order")
        if isSafeDescending(report):
            return True

    for i in range(len(report)):
        new_report = report[:i] + report[i + 1:]
        print(new_report)
        if new_report == sorted(new_report) and isSafeAscending(new_report):
            return True
        if new_report == sorted(new_report, reverse=True) and isSafeDescending(new_report):
            return True

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
        ([1, 3, 2, 4, 5], True),
        ([8, 6, 4, 4, 1], True),
        ([1, 3, 6, 7, 9], True)
    ]
    
    for (report, isSafe) in cases:
        print(report, isSafe)
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
            result += 1
        else:
            print(report)
    
    print(result)
    return result

if __name__ == "__main__":
    main()