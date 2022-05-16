"""
Подключение бибилотек
"""
import requests

USERS_URL = 'https://jsonplaceholder.typicode.com/users'
POSTS_URL = 'https://jsonplaceholder.typicode.com/posts'
COMMENTS_URL = 'https://jsonplaceholder.typicode.com/comments'

users = requests.get(USERS_URL).json()
posts = requests.get(POSTS_URL).json()
comments = requests.get(COMMENTS_URL).json()

def get_emails(username: str):
    """
    Метод, который для заданного username выведет email авторов /
    всех комментариев к постам пользователя с таким username
    """
    emails = set()
    for user in users:
        if user['username'] == username:
            user_id = user['id']
        for post in posts:
            if post['userId'] == user_id:
                post_id = post['id']
            for comment in comments:
                if comment['postId'] == post_id:   
                    emails.add(comment['email'])
    return emails
