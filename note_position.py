from argparse import ArgumentParser
import sys

def get_fret(target, string):
    """ Finds the fret that will produce a given note on a given string.

    We assume that note names will be one- or two-character strings. The
    first character will be a capital letter between A and G. The second
    character, if any, will be either # or b.

    Args:
        target (str): the note whose position is to be determined.
        string (str): the note of the open string.

    Returns:
        int: the fret that will produce the target note on the specified
        string (0 represents the open string).
    """
    scale = {
        "A" : 0,
        "A#" : 1,
        "Bb" : 1,
        "B" : 2,
        "C" : 3,
        "C#" : 4,
        "Db" : 4,
        "D" : 5,
        "D#" : 6,
        "Eb" : 6,
        "E" : 7,
        "F" : 8,
        "F#" : 9,
        "Gb" : 9,        
        "G" : 10,
        "G#" : 11,
        "Ab" : 11, 
    }
    target_str = scale[target]
    open_str = scale[string]

    final_note = (target_str - open_str)%12

    return final_note


def get_frets(target,strings):
    """ Given a list of strings, finds the fret on each string that will
    produce a given note.

    We assume that note names will be one- or two-character strings. The
    first character will be a capital letter between A and G. The second
    character, if any, will be either # or b.

    Args:
        target (str): the note whose position is to be determined.
        strings (list of str): a list of the notes of open strings.

    Returns:
        dict of (str: int): a dictionary whose keys are the string names
        specified in the strings parameter and whose values are fret
        positions on those strings. For example, if strings has the
        value ['G', 'C', 'E', 'A'], this function will return {'G': 4,
        'C': 11, 'E': 7, 'A': 2}.
    """
    target_fret = {}
    for string in strings:
        target_fret[string] = get_fret(target,string)
    
    return target_fret

def parse_args(arglist):
    """ Parses command-line arguments.

    The following required command-line arguments are defined:

    target: the note whose position the user wants to find
    strings: a list of one or more notes of open strings for which the
        user wishes to find the position of the target note

    Args:
        arglist (list of str): a list of command-line arguments.

    Returns:
        namespace: a namespace with variables target and strings.
    """
    parser = ArgumentParser()

    parser.add_argument("target", help = "the note you want to find" )
    parser.add_argument("strings", nargs="+", help = "list of string you want to find the note of")

    return parser.parse_args(arglist)


if __name__== "__main__":
    args = parse_args(sys.argv[1:])
    
    target = args.target
    strings = args.strings

    
    fin_notes = get_frets(target,strings)
    print(f"{target} is")
    for x,y in fin_notes.items():
        print(f"\t fret {y} of the {x} string")
