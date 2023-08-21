#!/usr/bin/env python3
import matplotlib.pyplot as plt
from Bio import SeqIO
from collections import Counter
import sys


def extract_sequences_from_fasta(data_file_path):
    '''
    Extract sequences from a FASTA file, without header lines.

    Parameters:
    data_file_path (str): The path to the FASTA file.

    Returns:
    str: Sequences from the file as a single string without spaces.
    '''

    try:
        sequences = [str(record.seq) for record in SeqIO.parse(data_file_path, "fasta")]
        return ''.join(sequences)
    except FileNotFoundError:
        print(f"File not found: {data_file_path}")
    except Exception as e:
        print(f"Error while processing the file: {e}")
    exit(1)


def count_sequence_pairs(sequence):
    '''
    Count pairs of DNA bases in a sequence.

    Parameters:
    sequence (str): Input sequence.

    Returns:
    Counter: Dictionary-like object containing pair counts.
    '''

    pairs = [sequence[i:i + 2] for i in range(len(sequence) - 1)]
    return Counter(pairs)


def plot_histogram(pair_counter):
    '''
    Plot a histogram of pair counts and save the image as a PNG file.

    Parameters:
    pair_counter (Counter): Counter object containing pair counts.

    Saves:
    PNG file: Histogram plot saved as 'histogram_pairs.png'
    '''

    pairs = list(pair_counter.keys())
    counts = list(pair_counter.values())

    plt.bar(pairs, counts)
    plt.xlabel('Pairs')
    plt.ylabel('Counts')
    plt.title('Pair Counts Histogram')
    plt.xticks(rotation=45)
    plt.tight_layout()
    image_path = '../../../histogram_pairs_results.png'
    plt.savefig(image_path)


def main():
    # Extract sequences, count pairs and plot histogram
    data_path = str(sys.argv[1])
    sequences = extract_sequences_from_fasta(data_path)
    pairs = count_sequence_pairs(sequences)
    plot_histogram(pairs)


if __name__ == '__main__':
    main()
