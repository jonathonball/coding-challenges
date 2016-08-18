import getpass
import os
import sys
import json
import re


class ConfigManager():

    def __init__(self):
        # Local user
        self.local_user = getpass.getuser()
        # Path to config file information
        self.config_file_name = 'config.json'
        self.config_path = '/home/' + self.local_user + '/.config/coding-challenge/'
        self.config_full_path = self.config_path + self.config_file_name
        # Major directories needed
        self.dirs = ['bin', 'input', 'output']
        # Dictionary of all paths used
        self.paths = {}
        self.paths['python'] = sys.executable
        self.paths['base'] = os.path.abspath(os.path.join(os.path.dirname(__file__), '..')) + '/'

    def get_user_config(self):
        if os.path.isfile(self.config_full_path):
            config_file_handle = open(self.config_full_path, 'r')
            self.paths = json.load(config_file_handle)
            config_file_handle.close()
            self.add_runtime_paths()
            if self.verify_paths():
                return self.paths
        else:
            self.install_user_config()

    def verify_paths(self):
        # check that everything in the paths dict actually exists
        for paths_key, paths_value in self.paths.items():
            if not os.path.exists(paths_value):
                print('Error locating: ', paths_key, paths_value)
                sys.exit(1)
        return True

    def add_runtime_paths(self):
        for dir in self.dirs:
            self.paths[dir] = self.paths['base'] + dir + '/'
        self.paths['regurge'] = self.paths['base'] + 'regurge.py'

    def install_user_config(self):
        if self.boolean_prompt('Configuration not found would you like to install? [Yes/No]: '):
            if not os.path.exists(self.config_path):
                os.mkdir(self.config_path)
            config_file_handle = open(self.config_full_path, 'w')
            json.dump(self.paths, config_file_handle, indent=4)
            config_file_handle.close()
            print("Configuration file installed, please run the script again")
        else:
            print("Configuration installation declined")
        sys.exit(0)

    @staticmethod
    def boolean_prompt(self, msg):
        response = input(msg)
        if re.match("ye?s?", response, re.IGNORECASE):
            return True
        else:
            return False


if __name__ == "__main__":
    import sys
    print("Please do not call this script directly")
    sys.exit(1)