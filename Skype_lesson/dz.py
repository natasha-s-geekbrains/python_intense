def generate_csv_file(file_name: str, rows: int) -> str:

    return file_name


def save_to_json(func):

    def wrapper(*args, **kwargs):

        result = func(*args, **kwargs)

        return result

    return wrapper


@save_to_json
def find_roots(from_file: str, index_num: int):

    result = ''

    return result


if __name__ == '__main__':
    generate_csv_file("input_data.csv", 5)
    find_roots('input_data.csv', 1)
