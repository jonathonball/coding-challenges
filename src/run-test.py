import argparse
import glob
import subprocess
import sys



def validate_file(type, path, test, ext, verbose=False):
    file_name = glob.glob(path + test + ext)
    if file_name:
        file_name = file_name[0]
        if verbose:
            print('Located ' + type + ' file: ' + file_name)
        return file_name
    else:
        print('Fuck you. Wigged out trying to look at this:')
        print(type[0].upper() + type[1:] + ' file: ', path + test + ext)
        sys.exit(1)


def run(file, params, verbose=False):
    f = open(file, 'r')
    result = subprocess.check_output(params, stdin=f)
    if verbose:
        print(result)
    f.close()
    return result

#TODO add in support for multiple test files

config = ConfigManager()
paths = config.get_user_config()

# build out CLI parameters
parser = argparse.ArgumentParser(description='Run challenge tests', usage='%(prog)s [options]')
parser.add_argument('-r', '--hackerrank', action='append', help='Run a hackerrank.com challenge')
parser.add_argument('-v', '--verbose', action='store_true', help='Show debug')
parameters = parser.parse_args()
hr_tests = parameters.hackerrank
LOCAL_DEBUG = parameters.verbose


if hr_tests != None:
    for hr_test in hr_tests:
        if LOCAL_DEBUG:
            print('Starting test for ' + hr_test)

        ####################################################################
        # TODO add in support for multiple test input/output file pairs
        ####################################################################
        test_file = validate_file('test', paths['bin'], hr_test, '.py', LOCAL_DEBUG)
        test_output_file = validate_file('output', paths['output'], hr_test, '.txt', LOCAL_DEBUG)
        test_input_file = validate_file('input', paths['input'], hr_test, '.txt', LOCAL_DEBUG)

        if LOCAL_DEBUG:
            print('Expected output:')
        answer = run(test_output_file, [paths['python3'], paths['regurge']], LOCAL_DEBUG)

        if LOCAL_DEBUG:
            print('Your output:')
        output = run(test_input_file, [paths['python3'], test_file], LOCAL_DEBUG)

        if answer == output:
            print('Test passed.')
        else:
            print('Test failed.')
