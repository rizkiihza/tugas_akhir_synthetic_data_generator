from random import randint
from random import shuffle

from math import floor
if __name__ == '__main__':
    num_predicate = int(input("number of total predicates: "))


    bug_predicates = set(map(int, input("bug predicates: ").split()))
    bug_predicate_list = list(bug_predicates)

    num_test_case = int(input("number of test case: "))

    filename = input("filename: ")

    result_data = []

    bug_case_proportion = randint(5, 8) / 10

    num_bug_case = floor(bug_case_proportion * num_test_case)
    num_correct_case = num_test_case - num_bug_case

    for i in range(num_bug_case):

        must_bug = bug_predicate_list[randint(0, len(bug_predicate_list) - 1)]
        row = []
        for j in range(num_predicate):
            if i + 1 == must_bug:
                row.append(1)
            else:
                row.append(randint(0, 1))

        row.append(-1)
        result_data.append(row)

    for i in range(num_correct_case):
        row = []

        for j in range(num_predicate):
            if j + 1 in bug_predicates:
                row.append(0)
            else:
                row.append(randint(0, 1))

        row.append(1)
        result_data.append(row)

    shuffle(result_data)

    data_file_dir = "generated_data/data_%s.txt" % (filename)
    with open(data_file_dir, "w") as f:
        for row in result_data:
            row = list(map(str, row))
            
            result = ",".join(row) 
            f.write(result+"\n")

    bug_predicate_file_dir = "generated_predicate_bug/predicate_bug_%s.txt" % (filename)
    with open(bug_predicate_file_dir, "w") as f:
        list_bug_predicate = sorted(list(bug_predicates))
        string_list = list(map(str, list_bug_predicate))
        f.write(",".join(string_list) + "\n")

    

    