from bs4 import BeautifulSoup
import requests

post_text = ""
url = "https://scholarslab.lib.virginia.edu/blog/"
html  = requests.get(url).text
soup = BeautifulSoup(html, features="html.parser")
old_posts = soup.find("section",id="previous_posts")
for i in old_posts.find_all("li"):
    # the post links are relative links, so we need to append the domain to make it an absolute link
    post_url = "https://scholarslab.lib.virginia.edu"+i.contents[0]["href"]
    post  = requests.get(post_url).text
    soup = BeautifulSoup(post, features="html.parser")
    post_text+=soup.find("div", class_="post__content").get_text()
    # Let's write out all the posts every time so we can interrupt it at any point
    f = open("posts.txt", "w")
    f.write(post_text)
    f.close()
    