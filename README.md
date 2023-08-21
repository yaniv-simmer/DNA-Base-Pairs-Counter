# DNA Sequence Base-Pairs Histogram Generator


## Overview

**My Workflow** is a [Nextflow](https://www.nextflow.io/) pipeline designed to analyze DNA sequences from a given FASTA file, count pairs of DNA bases, and create a histogram plot to visualize the pair counts. This workflow includes a Nextflow script (`my_workflow.nf`) and a Python script (`plot_histogram.py`) for processing and plotting the data.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before using **My Workflow**, ensure you have the following software and packages installed:

- [Python 3](https://www.python.org/downloads/)
- [Nextflow](https://www.nextflow.io/docs/latest/getstarted.html)
- [Biopython](https://biopython.org/) (Install with `pip install biopython`)
- [matplotlib](https://matplotlib.org/stable/users/installing.html) (Install with `pip install matplotlib`)

## Installation

1. Clone this GitHub repository:

   ```bash
   git clone https://github.com/yaniv-simmer/DNA-Base-Pairs-Counter.git
   cd DNA-Base-Pairs-Counter

   ```

## Usage


1. Run the Nextflow workflow using the following command:

   ```bash
   ./nextflow run ./my_workflow.nf --fasta_file_path <path_to_your_FASTA_file> 
   ```

2. The workflow will process the input FASTA file, count the pairs of DNA bases, and generate a histogram plot.

## Output

Upon successful completion of the workflow, you will find the following outputs:

- `histogram_pairs_results.png`: A histogram plot illustrating the counts of DNA base pairs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please feel free to create a pull request.

## License

This project is licensed under the [MIT License](LICENSE).

---

*Note: This README provides a general overview of the workflow. For detailed usage instructions and customization options, please refer to the comments in the provided scripts (`my_workflow.nf` and `plot_histogram.py`).*

*Created by [Your Name](https://github.com/your-username)*
