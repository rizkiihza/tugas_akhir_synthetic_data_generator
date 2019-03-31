import os 
import sys
import subprocess 

import pandas as pd

from collections import defaultdict
from sys import argv

if __name__ == '__main__':
    if len(argv) < 4:
        print("need 3 argument")
        sys.exit()
    program_jar = "program.jar"

    start = int(argv[1])
    end = int(argv[2])
    file_destination = argv[3]

    current_file_iterator = start

    data = defaultdict(lambda: [])

    while current_file_iterator <= end:
        data_name = "generated_data/data_%d.txt" % (current_file_iterator)
        bug_predicate_name = "generated_predicate_bug/predicate_bug_%d.txt" % (current_file_iterator)

        command = "java -jar %s -s %s %s" % (program_jar, data_name, bug_predicate_name)
        print("################################################################")
        result = subprocess.run(command.split(" "), stdout=subprocess.PIPE).stdout.decode("utf-8")
        print(result)
        result = result.split("\n")
        result = [s for s in result if len(s) > 0]

        for s in result:
            splitted_s = s.split(":")

            while splitted_s[1][0] == " ":
                splitted_s[1] = splitted_s[1][1:]
            
            data[splitted_s[0]].append(splitted_s[1])

        print("################################################################")
        current_file_iterator += 1

    df = pd.DataFrame.from_dict(data)

    df.to_csv(file_destination)
