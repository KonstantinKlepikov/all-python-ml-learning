from collections import deque
import heapq
from collections import Counter
from operator import itemgetter
from itertools import groupby
from collections import defaultdict


def arbitrary_len (some_seq, mode=None):
    """Function crops sequences, leaving a first, middle or last part

    Args:
        some_seq (sequence): sequence of any type
        mode (string, optional): "firt", "middle", "last". Defaults to None.

    Returns:
        obj: element or list of elements of cropped sequence
    """

    if mode == "first":
        answer, *_ = some_seq
    elif mode == "middle":
        _, *answer, _ = some_seq
    elif mode == "last":
        *_, answer = some_seq

    return answer


def search_and_scrop(some_seq, pattern, N=5):
    """Function search for N last elements

    Args:
        some_seq (sequence): sequence of any type
        pattern (obj, optional): object same type, as sequence elements
        N (int): Number of last elements. Defaults to 5.

    Yields:
        list: N previous elements of sequence
    """

    prev_elem = deque(maxlen=N)
    for elem in some_seq:
        if pattern in elem:
            yield elem, prev_elem
        prev_elem.append(elem)


def searc_for_minmax(some_seq, mode=None, key=None, N=3):
    """Serach smallest or largest elements in smll sets of data with heapq

    Args:
        some_seq (sequence): sequence of any type
        mode (str, optional): "min", "max". Defaults to None.
        key (func, optional): function to sort option. Defaults to None.
        N (int, optional): Number of searched elements. Defaults to 3.

    Returns:
        list: list of N objects
    """

    if mode == "min":
        answer = heapq.nsmallest(N, some_seq, key=key)
    elif mode == "max":
        answer = heapq.nlargest(N, some_seq, key=key)
    
    return answer


class PriorityQueue:
    """Queue with priority
    """

    def __init__(self):
        self._queue = []
        self._index = 0

    def push(self, item, priority):
        """Ad element into queue

        Args:
            item (obj): element, added into queue
            priority (int): priority number

        """

        heapq.heappush(self._queue, (-priority, self._index, item))
        # first argument has - for reverse heap
        # index is used for determining priority when items priorities are equal
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item:
    """OTest objects for queue
    """

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item({!r})'.format(self.name)


def dict_val_comparison(some_seq, mode=None):
    """Computate metrics of dict values and return keys

    Args:
        some_seq (dict): nonempty dict
        mode (str, optional): type of metric, 'min', 'max', 'sorted'. Defaults to None.

    Returns:
        tuple: result of calculation
    """

    if mode == 'min':
        answer = min(zip(some_seq.values(), some_seq.keys()))
    elif mode == 'max':
        answer = max(zip(some_seq.values(), some_seq.keys()))
    elif mode == 'sorted':
        answer = sorted(zip(some_seq.values(), some_seq.keys()))

    return answer


class DictValComparison:
    """Some as dict_val_comparison, but with class
    """

    def __init__(self, some_seq):
        self.some_seq = some_seq

    def compMin(self):
        return min(zip(self.some_seq.values(), self.some_seq.keys()))

    def compMax(self):
        return max(zip(self.some_seq.values(), self.some_seq.keys()))
    
    def compSort(self):
        return sorted(zip(self.some_seq.values(), self.some_seq.keys()))

class Deuduliacate(DictValComparison):
    """Dedublicate objects in sequence

    Args:
        DictValComparison (obj): sequence
    """
 
    def dedubl_hash(self):
        """Dedublicate objects in hashable sequence

        Yields:
            obj: dedublicated element
        """

        seen = set()
        for item in self.some_seq:
            if item not in seen:
                yield item
                seen.add(item)

    def dedubl_nonhash(self, key=None):
        """Dedublicate objects in non-hashable sequence

        Args:
            key (func, optional): function to rule of dedublication. Defaults to None.

        Yields:
            obj: dedublicated element
        """

        seen = set()
        for item in self.some_seq:
            val = item if key is None else key(item)
            if val not in seen:
                yield item
                seen.add(val)

class CountsOfItems(DictValComparison):
    """Score any numbers of items
    """

    def most_freq(self, N=1):
        """Return N most common items of sequence

        Args:
            N (int, optional): number of items. Defaults to 1.

        Returns:
            list of tupples: finded items of sequence
        """

        count = Counter(self.some_seq)

        return count.most_common(N)

    def most_freq_operation(self, another_seq, N=1, mode='sum'):
        """Mathematic opertion with Counter objects

        Args:
            another_seq (obj): sequence same type as some_seq
            NN (int, optional): number of items. Defaults to 1.
            mode (str, optional): "sum", "diff". Defaults to 'sum'.

        Returns:
            list of tupples: finded items of sequences
        """

        count1 = Counter(self.some_seq)
        count2 = Counter(another_seq)

        if mode == 'sum':
            s = count1 + count2
        elif mode == 'diff':
            s = count1 - count2

        return s.most_common(N)

class Member:

    def __init__(self, member_id):
        self.member_id = member_id

    def __repr__(self):
        return 'Member({0})'.format(self.member_id) 

class SortSeqOfDicts:
    """Sort a sequence of dicts
    """

    def __init__(self, seq_of_dict):
        """Class constructor

        Args:
            seq_of_dict (sequence fo dicts): one of the dicts key is 'date'
        """

        self.some_seq = seq_of_dict

    def sort_and_group_by_date(self):
        """Sort sequence of dict by 'date' and print sorted result
        """

        self.some_seq.sort(key=itemgetter('date'))

        for date, items in groupby(self.some_seq, key=itemgetter('date')):
            print(date)
            for i in items:
                print(' ', i)

    def sort_and_group_in_large_structure(self, date):
        """Sort sequence of dict and print only dicts with given 'date'

        Args:
            date (str): 'date' value in dicts
        """

        seq_by_date = defaultdict(list)

        for row in self.some_seq:
            seq_by_date[row['date']].append(row)

        for r in seq_by_date[date]:
            print(r)
