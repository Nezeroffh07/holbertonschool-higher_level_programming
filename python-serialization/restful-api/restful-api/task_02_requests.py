#!/usr/bin/python3
"""
Fetching and processing data from an API.
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches and prints post titles from an API."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    print("Status Code: {}".format(r.status_code))
    if r.status_code == 200:
        for post in r.json():
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches posts and saves them to a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    r = requests.get(url)
    if r.status_code == 200:
        posts = r.json()
        with open('posts.csv', 'w', encoding='utf-8', newline='') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for p in posts:
                writer.writerow({'id': p['id'],
                                 'title': p['title'],
                                 'body': p['body']})
