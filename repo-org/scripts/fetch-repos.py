import requests
from datetime import datetime
import csv
import os

def get_github_repos(username):
    # GitHub API endpoint for user repositories
    url = f"https://api.github.com/users/{username}/repos"
    
    # Make API request
    response = requests.get(url)
    
    if response.status_code == 200:
        # Parse JSON response
        repos = response.json()
        
        # Sort repositories by creation date (newest first)
        sorted_repos = sorted(repos, key=lambda x: x['created_at'], reverse=True)
        
        return sorted_repos
    else:
        print(f"Error accessing GitHub API: {response.status_code}")
        return None

def write_repos_to_csv(repos, output_path):
    # Generate timestamp for filename
    timestamp = datetime.now().strftime("%d-%m-%Y")
    filename = f"RepoList_{timestamp}.csv"
    
    # Combine path and filename
    full_path = os.path.join(output_path, filename)
    
    # Ensure directory exists
    os.makedirs(output_path, exist_ok=True)
    
    # Write to CSV
    with open(full_path, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Repository Name', 'URL', 'Description', 'Creation Date']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for repo in repos:
            writer.writerow({
                'Repository Name': repo['name'],
                'URL': repo['html_url'],
                'Description': repo['description'] if repo['description'] else 'No description',
                'Creation Date': datetime.strptime(repo['created_at'], 
                                                 '%Y-%m-%dT%H:%M:%SZ').strftime('%Y-%m-%d %H:%M:%S')
            })
    
    print(f"Repository list has been written to: {full_path}")

def main():
    # Configuration
    username = "danielrosehill"
    output_path = "/home/daniel/Git/just-some-ai-ideas/repo-org/repo-list"
    
    # Get repositories
    repos = get_github_repos(username)
    
    if repos:
        # Write to CSV
        write_repos_to_csv(repos, output_path)
    else:
        print("Failed to fetch repositories")

if __name__ == "__main__":
    main()