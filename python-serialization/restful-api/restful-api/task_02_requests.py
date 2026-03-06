#!/usr/bin/python3
"""
Fetching and processing data from an API using the requests library.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    print("Status Code: {}".format(response.status_code))

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts and saves them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)

    if response.status_code == 200:
        posts = response.json()
        
        # Siyahını strukturlaşdırırıq (yalnız id, title və body götürülür)
        structured_data = [
            {'id': p['id'], 'title': p['title'], 'body': p['body']}
            for p in posts
        ]

        # CSV faylına yazırıq
        with open('posts.csv', mode='w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            
            writer.writeheader()
            writer.writerows(structured_data)
