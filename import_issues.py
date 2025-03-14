import csv        # For reading CSV files
import requests   # For making HTTP requests
import os         # For accessing environment variables

# Retrieve the GitHub Personal Access Token from an environment variable
# If you prefer, you could replace the below with:
# TOKEN = "ghp_yourHardCodedToken"
TOKEN = os.environ.get("GITHUB_TOKEN")

# Define the GitHub repo where issues will be created
REPO_OWNER = "seanr87"
REPO_NAME = "Mars-Project"
API_URL = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/issues"

# Prepare headers for authentication and JSON handling
headers = {
    "Authorization": f"Bearer {TOKEN}",
    "Accept": "application/vnd.github+json"
}

def import_issues_from_csv(csv_file_path):
    """
    Opens a CSV file, reads each row,
    and creates a corresponding GitHub issue using the API.
    Expected CSV columns: Title, Body, Labels.
    """
    with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            # Extract the necessary fields
            title = row.get("Title", "Untitled")
            body = row.get("Body", "")
            # 'Labels' is assumed to be a semicolon-delimited string
            labels_str = row.get("Labels", "")
            labels = [lbl.strip() for lbl in labels_str.split(";") if lbl.strip()]

            # Construct the issue data
            data = {
                "title": title,
                "body": body,
                "labels": labels
            }

            # Make the POST request to create the issue on GitHub
            response = requests.post(API_URL, json=data, headers=headers)

            # Check the response to ensure the issue was created
            if response.status_code == 201:
                print(f"Issue created: {title}")
            else:
                print(f"Failed to create issue '{title}': {response.text}")

if __name__ == "__main__":
    # Set the path for your CSV file
    csv_file = "issues.csv"
    import_issues_from_csv(csv_file)
