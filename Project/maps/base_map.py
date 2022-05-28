"""
Module to make maps data structures properly
"""
from abc import ABC, abstractmethod
from typing import Iterable, Tuple


class BaseMap(ABC):
    """
    Class for maps with abstract methods and some universal method for all maps
    """
    @abstractmethod
    def __getitem__(self, key: str) -> int:
        ...

    @abstractmethod
    def __setitem__(self, key: str, value: int) -> None:
        ...

    @abstractmethod
    def __delitem__(self, key: str) -> None:
        ...

    @abstractmethod
    def __iter__(self) -> Iterable[Tuple[str, int]]:
        ...

    def __contains__(self, key: str) -> bool:
        try:
            _ = self[key]
        except KeyError:
            return False
        return True

    def __eq__(self, other: 'BaseMap') -> bool:
        if len(self) != len(other):
            return False
        for key, value in self:
            try:
                if value != other[key]:
                    return False
            except KeyError:
                return False
        return True

    def __ne__(self, other):
        return not self == other

    def __bool__(self) -> bool:
        return len(self) != 0

    def items(self) -> Iterable[Tuple[str, int]]:
        """Returns iterable with k, v tuples"""
        yield from self

    def values(self) -> Iterable[int]:
        """Returns iterable made from map's values"""
        return (value for key, value in self)

    def keys(self) -> Iterable[str]:
        """Returns iterable made from map's keys"""
        return (key for key, value in self)

    @classmethod
    def fromkeys(cls, iterable, value=None) -> 'BaseMap':
        """Creates a new map with keys from iterable and values set to value"""
        res_map = cls()
        for key in iterable:
            res_map[key] = value
        return res_map

    def update(self, other=None) -> None:
        """Updates values by keys and values from other"""
        if other is None:
            return
        if hasattr(other, "keys"):
            for key in other.keys():
                self[key] = other[key]
        else:
            for key, value in other:
                self[key] = value

    def get(self, key, default=None) -> int:
        """Returns value by key if key exists, else default"""
        try:
            value = self[key]
        except KeyError:
            return default
        return value

    def pop(self, key, default=None):
        """
        If key exists, function will delete key and return its value
        Else returns default
        """
        try:
            value = self[key]
            del self[key]
            return value
        except KeyError as key_err:
            if default is None:
                raise KeyError from key_err
            return default

    def popitem(self):
        """Removes and returns a last (key, value) pair as a 2-tuple"""
        to_del_key = 0
        to_del_value = 0
        for key, value in self:
            to_del_key = key
            to_del_value = value
        del self[to_del_key]
        return to_del_key, to_del_value

    def setdefault(self, key, default=None):
        """
        Inserts key with a value of default if key is not in the map.
        Returns the value for key if key is in the map, else default.
        """
        if key in self:
            return self[key]
        self[key] = default
        return default

    def sum(self):
        """Returns values sum"""
        return sum(value for key, value in self)

    @abstractmethod
    def clear(self):
        """Clears map"""

    def write(self, path: str, mode='a') -> None:
        """Writes map in a file"""
        with open(path, mode, encoding='utf8') as file:
            for key, value in self:
                file.write(f'{key} {value}\n')

    @classmethod
    def read(cls, path: str) -> 'BaseMap':
        """Reads map from a file"""
        my_obj = cls()
        with open(path, 'r', encoding='utf8') as file:
            line = file.readline()
            while line != '':
                key, value = line.split()
                my_obj[key] = value
                line = file.readline()
        return my_obj
        