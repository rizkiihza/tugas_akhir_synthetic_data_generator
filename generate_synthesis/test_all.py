import os 
import sys

from sys import argv

if __name__ == '__main__':
    if len(argv) < 3:
        print("need 2 argument")
        sys.exit()
    program_jar = "program.jar"

    start = int(argv[1])
    end = int(argv[2])

    current_file_iterator = start
    while current_file_iterator <= end:
        data_name = "generated_data/data_%d.txt" % (current_file_iterator)
        bug_predicate_name = "generated_predicate_bug/predicate_bug_%d.txt" % (current_file_iterator)

        command = "java -jar %s -s %s %s" % (program_jar, data_name, bug_predicate_name)
        print("################################################################")
        os.system(command)
        print("################################################################")
        current_file_iterator += 1