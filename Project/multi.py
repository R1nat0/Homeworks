"""Модуль для многопоточного или многопроцессорного выполнения функции wiki_parser"""

from concurrent.futures import ThreadPoolExecutor
from itertools import repeat
from parser import wiki_parser



def multi(mode, url, base_path, max_workers=5, deep=3):
    """
    Функция, выполняющая функцию wiki_parser многопоточно или многопроцессорно.
    """
    beginning = wiki_parser(url, base_path)
    for _ in range(deep - 2):
        executor = mode(max_workers=max_workers)
        temp = []
        futures = [executor.submit(wiki_parser, url, path)
                   for url, path in zip(beginning, repeat(base_path))]
        for i in futures:
            temp += i.result()
        beginning = temp
        executor.shutdown()


if __name__ == "__main__":
    multi(ThreadPoolExecutor, 'https://ru.wikipedia.org/wiki/Чёрмозский_завод',
          r'/Users/rinathamidullov/Desktop/Project')
          