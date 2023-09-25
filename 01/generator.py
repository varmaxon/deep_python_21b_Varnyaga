from io import TextIOWrapper, StringIO


def generator(file_, arr_words: list) -> str:

    def find_line_with_words(file_name) -> str:
        for line in file_name:
            if len(set.intersection(set(map(str.lower, arr_words)),
                                    set(line.strip().lower().split()))) > 0:
                yield line.strip()

    if isinstance(file_, (StringIO, TextIOWrapper)):
        for item in find_line_with_words(file_):
            yield item

    elif isinstance(file_, str):
        with open(file_, 'r', encoding='utf-8') as file_name:
            for item in find_line_with_words(file_name):
                yield item
    else:
        raise TypeError('enter file name or file object')
