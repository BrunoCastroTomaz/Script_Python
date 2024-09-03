import os
import shutil

def file_handler_v1(command):
    match command.split():
        case ['show']:
            print('List all files and directories:')
            # List all files and directories in the current directory
            for item in os.listdir('.'):
                print(item)
                
        case ['remove', *files]:
            print('Removing files: {}'.format(files))
            # Remove the specified files or directories
            for file in files:
                if os.path.isfile(file):
                    os.remove(file)
                    print(f'File {file} removed.')
                elif os.path.isdir(file):
                    shutil.rmtree(file)
                    print(f'Directory {file} removed.')
                else:
                    print(f'{file} not found.')

        case ['enter', directory]:
            try:
                os.chdir(directory)
                print(f'Entered directory: {directory}')
            except FileNotFoundError:
                print(f'Directory {directory} not found.')
            except NotADirectoryError:
                print(f'{directory} is not a directory.')
            except PermissionError:
                print(f'Permission denied to enter {directory}.')
        
        case _:
            print('Command not recognized')
            return False
    return True

def main():
    while True:
        command = input()
        if not file_handler_v1(command):
            break

main()
# Example usage:
# file_handler_v1('show')
# file_handler_v1('remove file1.txt dir1')
# file_handler_v1('enter dir1')
