from datetime import datetime

def execution_time(func):
    def wrapper(*args, **kwargs):
        initial_time = datetime.now()
        result = func(*args, **kwargs)#function decorates with output
        final_time = datetime.now()
        time_elapsed = final_time - initial_time
        print(f'Pasaron {time_elapsed.total_seconds()} segundos')
        return result
    return wrapper


@execution_time
def remove_duplicates(some_list):
    without_duplicates = []
    for element in some_list:
        if element not in without_duplicates:
            without_duplicates.append(element)
    return without_duplicates

@execution_time
def remove_duplicates_with_sets(some_list):
    return list(set(some_list))

def run():
    random_list = [1, 2, 2, 2, 3, "Platzi", "Platzi", True, 4.6, False]
    random_list.extend([x for x in range(100000)])
    print("clasiccal way \n",100*"*")
    remove_duplicates(random_list)
    print("sets way\n",100*"*")
    remove_duplicates_with_sets(random_list)


if __name__ == '__main__':
    run()
