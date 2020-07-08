from collections import deque

def arbitrary_len (some_seq, form=None):
    """Function crops sequences, leaving a first, middle or last part

    Args:
        some_seq (sequence): sequence of any type
        form (string, None): "firt", "middle", "last". Defaults to None.

    Returns:
        [object]: elements of cropped sequence
    """
    
    if form == "first":
        answer, *_ = some_seq
    elif form == "middle":
        _, *answer, _ = some_seq
    elif form == "last":
        *_, answer = some_seq

    return answer

def search_and_scrop(some_seq, pattern, N=5):
    """Function search for N last elements

    Args:
        some_seq (sequence): sequence of any type
        pattern (obj): object same type, as sequence elements
        N (int): Number of last elements. Defaults to 5.

    Yields:
        obj: N previous elements of sequence
    """

    prev_elem = deque(maxlen=N)
    for elem in some_seq:
        if pattern in elem:
            yield elem, prev_elem
        prev_elem.append(elem)
