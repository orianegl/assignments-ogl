from bs4 import BeautifulSoup
import requests

# Initialize a variable to accumulate content
url = "https://scholarslab.lib.virginia.edu/blog/"
html = requests.get(url).text
soup = BeautifulSoup(html, features="html.parser")

# Find the section containing the previous posts
old_posts = soup.find("section", id="previous_posts")
if old_posts is None:
    print("No previous posts found")
else:
    print(f"Found {len(old_posts.find_all('li'))} posts")

# Open the file once before the loop for appending
with open("posts.txt", "a") as f:
    # Iterate through each post link
    for i, post in enumerate(old_posts.find_all("li"), start=1):
        post_url = "https://scholarslab.lib.virginia.edu" + post.contents[0]["href"]
        print(f"Scraping post #{i}: {post_url}")

        # Fetch the full post content
        post_html = requests.get(post_url).text
        soup = BeautifulSoup(post_html, features="html.parser")

        # Find the author of the post
        author = soup.find("span", class_="author")
        if author:
            print(f"Author found: {author.get_text().strip()}")

        # Check if the author is "Brandon Walsh"
        if author and author.get_text().strip() == "Brandon Walsh":
            # If the author is Brandon Walsh, extract the post content
            post_content = soup.find("div", class_="content")
            if post_content:
                post_text = post_content.get_text()
                f.write(post_text)
                print(f"Written to posts.txt: {post_text[:100]}...")  # Print first 100 characters of written content
            else:
                print("No post content found.")

print("Finished scraping. Check posts.txt for results.")