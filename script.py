import os
import sys

from parser import result


CONFIG_ALIASES_NAME = 'resources/config-aliases.json'


def main(input_file_name, output_directory):
    current_script_path = os.path.dirname(os.path.abspath(__file__)).replace('\\', '/')
    config_path = f'{current_script_path}/{CONFIG_ALIASES_NAME}'

    result.execute(input_file_name, output_directory, config_file_name=config_path)

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])


