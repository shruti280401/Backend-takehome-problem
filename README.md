# Research Paper Fetcher

## Overview
This Python program fetches research papers from the **PubMed API** based on a user-specified query. It identifies papers with at least one author affiliated with a **pharmaceutical** or **biotech** company and returns the results as a **CSV file**.

## Features
- Fetches research papers using the **PubMed API**.
- Supports **PubMed's full query syntax**.
- Filters results to include only papers with authors affiliated with **pharmaceutical/biotech companies**.
- Outputs results in **CSV format**.
- Provides command-line options for **debugging** and **saving results**.

## Installation
### Prerequisites
Ensure you have **Python 3.8+** installed.

### Setup
1. Clone this repository:
   ```sh
   git clone https://github.com/your-username/research-paper-fetcher.git
   cd research-paper-fetcher
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

## Usage
Run the script using the following command:
```sh
poetry run python script.py -q "cancer research" -f results.csv
```

### Command-line Options
| Option | Short | Description |
|--------|-------|-------------|
| `--help` | `-h` | Display usage instructions |
| `--debug` | `-d` | Print debug information during execution |
| `--file` | `-f` | Specify the filename to save results (default: print to console) |

### Example Commands
1. Display help:
   ```sh
   poetry run python script.py -h
   ```
2. Run with debug mode:
   ```sh
   poetry run python script.py -q "stem cells" -f output.csv -d
   ```
3. Print results to console:
   ```sh
   poetry run python script.py -q "AI in medicine"
   ```

## Output Format
The results will be saved as a **CSV file** with the following columns:
- **PubmedID**: Unique identifier for the paper.
- **Title**: Title of the paper.
- **Publication Date**: Date the paper was published.
- **Non-academic Author(s)**: Authors affiliated with non-academic institutions.
- **Company Affiliation(s)**: Names of pharmaceutical/biotech companies.
- **Corresponding Author Email**: Email of the corresponding author.

## Code Organization
- **script.py**: Main script to fetch and process research papers.
- **README.md**: Documentation (this file).


## Contributing
Feel free to submit **pull requests** or open **issues** for bug fixes and improvements.

## Contact
For any questions, reach out to **shruti280401@gmail.com** or open an issue in the GitHub repository.

