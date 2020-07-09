from collections import deque
import heapq

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
