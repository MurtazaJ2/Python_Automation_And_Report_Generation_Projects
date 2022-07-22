import subprocess


def test_command(cmd):
    command_execution = subprocess.run([cmd], encoding='utf-8', stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE, text=True, shell=True)
    if command_execution.stderr == '':
        result = command_execution.stdout
        result = result.strip("\n")
        return result
    elif command_execution.stderr != '':
        result_error = command_execution.stderr
        result_error = result_error.strip("\n")
        return result_error
