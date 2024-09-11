import argparse

# ____________________________________________
def get_args():
    """ Get command-line arguments """

    parser = argparse.ArgumentParser(
        description = 'Tetranucleotide frequency',
        formatter_class = argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('dna', metavar = 'DNA', help='Input DNA sequence')

    return parser.parse_args()

# ______________________________________________
def main():
    """ Make a jazz noise here """

    args = get_args()
    print(args.dna)


# ______________________________________________
if __name__ == '__main__':
    main()