import requests
import csv
import argparse
import json
import sys

# PubMed API Base URL
PUBMED_API_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_SUMMARY_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_pubmed_papers(query, max_results=10):
    """Fetch paper IDs from PubMed based on user query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results
    }

    response = requests.get(PUBMED_API_URL, params=params)

    if response.status_code != 200:
        print("Error fetching data from PubMed")
        sys.exit(1)

    data = response.json()
    return data.get("esearchresult", {}).get("idlist", [])


def fetch_paper_details(paper_ids):
    """Fetch detailed information for given PubMed paper IDs."""
    if not paper_ids:
        return []

    params = {
        "db": "pubmed",
        "id": ",".join(paper_ids),
        "retmode": "json"
    }

    response = requests.get(PUBMED_SUMMARY_URL, params=params)

    if response.status_code != 200:
        print("Error fetching paper details")
        sys.exit(1)

    data = response.json()
    return data.get("result", {})


def extract_relevant_info(paper_details):
    """Extract required fields from PubMed response."""
    extracted_data = []

    for paper_id, details in paper_details.items():
        if paper_id == "uids":
            continue  # Skip non-paper data

        title = details.get("title", "N/A")
        pub_date = details.get("pubdate", "N/A")
        authors = details.get("authors", [])

        # Extract non-academic authors and affiliations
        non_academic_authors = []
        company_affiliations = []

        for author in authors:
            if "affiliation" in author:
                affiliation = author["affiliation"]
                if "pharma" in affiliation.lower() or "biotech" in affiliation.lower():
                    non_academic_authors.append(author.get("name", "Unknown"))
                    company_affiliations.append(affiliation)

        # Extract corresponding author's email (mocking as PubMed does not provide it)
        corresponding_email = details.get("email", "N/A")

        extracted_data.append([
            paper_id, title, pub_date,
            "; ".join(non_academic_authors) if non_academic_authors else "N/A",
            "; ".join(company_affiliations) if company_affiliations else "N/A",
            corresponding_email
        ])

    return extracted_data


def save_to_csv(data, filename):
    """Save extracted paper data to a CSV file."""
    headers = ["PubMedID", "Title", "Publication Date", "Non-academic Author(s)", "Company Affiliation(s)",
               "Corresponding Author Email"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data)

    print(f"Results saved to {filename}")


def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed API")

    parser.add_argument("-q", "--query", type=str, required=True, help="Search query for PubMed")
    parser.add_argument("-f", "--file", type=str, default="results.csv", help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print(f"Fetching papers for query: {args.query}")

    paper_ids = fetch_pubmed_papers(args.query)
    paper_details = fetch_paper_details(paper_ids)
    extracted_data = extract_relevant_info(paper_details)

    if args.debug:
        print(json.dumps(extracted_data, indent=2))

    save_to_csv(extracted_data, args.file)


if __name__ == "__main__":
    main()
