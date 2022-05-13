"""

class Action(_AttributeHolder)

       Action(
            option_strings,
            dest,
            nargs=None,
            const=None,
            default=None,
            type=None,
            choices=None,
            required=False,
            help=None,
            metavar=None
       )
    
        Information about how to convert command line strings to Python objects.
        
        Action objects are used by an ArgumentParser to represent the information
        needed to parse a single argument from one or more strings from the
        command line. The keyword arguments to the Action constructor are also
        all attributes of Action instances.
        
        Keyword Arguments:
        
            - option_strings -- A list of command-line option strings which
                should be associated with this action.
        
            - dest -- The name of the attribute to hold the created object(s)
        
            - nargs -- The number of command-line arguments that should be
                consumed. By default, one argument will be consumed and a single
                value will be produced.  Other values include:
                    - N (an integer) consumes N arguments (and produces a list)
                    - '?' consumes zero or one arguments
                    - '*' consumes zero or more arguments (and produces a list)
                    - '+' consumes one or more arguments (and produces a list)
                Note that the difference between the default and nargs=1 is that
                with the default, a single value will be produced, while with
                nargs=1, a list containing a single value will be produced.
        
            - const -- The value to be produced if the option is specified and the
                option uses an action that takes no values.
        
            - default -- The value to be produced if the option is not specified.
        
            - type -- A callable that accepts a single string argument, and
                returns the converted value.  The standard Python types str, int,
                float, and complex are useful examples of such callables.  If None,
                str is used.
        
            - choices -- A container of values that should be allowed. If not None,
                after a command-line argument has been converted to the appropriate
                type, an exception will be raised if it is not a member of this
                collection.
        
            - required -- True if the action must always be specified at the
                command line. This is only meaningful for optional command-line
                arguments.
        
            - help -- The help string describing the argument.
        
            - metavar -- The name to be used for the option's argument with the
                help string. If None, the 'dest' value will be used as the name.
"""


def get_parser():
    import argparse
    """
    Demonstration of arg parsing with multiple types
    :return: argparse.Namespace
    """

    STORE_TRUE = 'store_true'
    STORE_FALSE = 'store_false'
    STORE_CONST = 'store_const'

    parser = argparse.ArgumentParser(
        prog='arg_parse_demo',
        description='...truncated for brevity...'
    )

    parser.add_argument(
        'query',
        metavar='QUERY',
        type=str,
        nargs='*',
        help='the question to answer'
    )

    parser.add_argument(
        '-p', '--pos',
        help='select answer in specified position (default: 1)',
        default=1,
        type=int
    )

    parser.add_argument(
        '-a', '--all',
        help='display the full text of the answer',
        action=STORE_TRUE
    )

    parser.add_argument(
        '-l', '--link',
        help='display only the answer link',
        action=STORE_TRUE
    )

    parser.add_argument(
        '-c', '--color',
        help='enable colorized output',
        action=STORE_TRUE
    )

    parser.add_argument(
        '-n', '--num-answers',
        help='number of answers to return',
        default=1,
        type=int
    )

    parser.add_argument(
        '-C', '--clear-cache',
        help='clear the cache',
        action=STORE_TRUE
    )

    parser.add_argument(
        '-v', '--version',
        help='displays the current version of howdoi',
        action=STORE_TRUE
    )

    parser.add_argument(
        '-o', '--options',
        help='options can be one of the following [...]',
        choices=['add', 'remove', 'pass'],
        default='add',
    )

    return parser.parse_args()


def has_args():
    import sys
    return len(sys.argv) > 1


if __name__ == '__main__':
    if has_args():
        args = get_parser()
        # do something useful with args...
        # demo will show the instance dictionary
        print(args.__dict__)
    else:
        print('\nYou must input args to run this program.')
        print(__file__, '-h/--help', 'for valid arguments')
