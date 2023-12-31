

def func_saving_file(copy, func_saving):
    external_file_path = f'{copy}.py'
    permanent_file_path = f'{func_saving}.py'

    with open(external_file_path, 'r') as external_file:
        external_code = external_file.read()

    with open(permanent_file_path, 'a') as permanent_file:
        permanent_file.write('\n\n# External Code\n')
        permanent_file.write(external_code)
