from sys import argv


def my_func(work_time, stavka_hour, premium):
    return work_time * stavka_hour + premium


file_path, work_time, stavka_hour, premium = argv
print(my_func(int(work_time), int(stavka_hour), int(premium)))
