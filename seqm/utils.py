# -*- coding: utf-8 -*-
#
# Miscellaneous sequence utilities.
#
# ------------------------------------


# imports
# -------
import random as rnd


# functions
# ---------
def random(length=11, template='ACGT'):
    """
    Generate random sequence of specified length.

    Args:
        length (int): Length of random sequence to generate.
        template (str): String with bases to use in generating sequence.

    Example:
        >>> sequtils.random_sequence()
        CGGACGGTATG
        >>> sequtils.random_sequence(length=5, template='AC')
        CCCAA
    """
    tlen = len(template)
    seq = ''
    for i in range(0, int(length)):
        seq += template[int(rnd.random() * tlen)]
    return seq


def wrap(seq, bases=60):
    """
    Print wrapped sequence.

    Args:
        seq (str): Nucleotide sequence
        bases (int): Number of bases to include on each line.

    Example:
        >>> sequtils.wrap(CGGACGGTATG, bases=3)
        CGG
        ACG
        GTA
        TG
    """
    bases = int(bases)
    count = 0
    ret = ''
    for i in seq:
        if count >= bases:
            ret = ret + '\n'
            count = 0
        ret = ret + i
        count += 1
    return ret
