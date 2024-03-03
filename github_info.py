import requests


def fetch_user_repositories(username):
    url = f"https://api.github.com/users/{username}/repos"
    response = requests.get(url)

    if response.status_code == 200:
        repositories = response.json()
        return repositories
    else:
        print("Error")
        return None


def display_repository_info(repositories):
    print("\nUser's Repositories:")
    for repo in repositories:
        print("\nRepository Name:", repo["name"])
        print("\nDescription:", repo["description"])
        print("\nLanguage:", repo["language"])
        print("\nStars:", repo["stargazers_count"])


def main():
    username = input("Enter GitHub username: ")
    repositories = fetch_user_repositories(username)
    if repositories:
        display_repository_info(repositories)
    else:
        print("The user has no public repositories.")


if __name__ == "__main__":
    main()
