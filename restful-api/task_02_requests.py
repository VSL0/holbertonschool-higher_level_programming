#!/usr/bin/python3
"""
Consuming and processing data from an API using Python
"""
import requests
import csv


def fetch_and_print_posts():
    """Fetches all posts from JSONPlaceholder and prints their titles"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    print("Status Code: {}".format(r.status_code))
    
    if r.status_code == 200:
        posts = r.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    """Fetches all posts and saves id, title, and body to posts.csv"""
    r = requests.get('https://jsonplaceholder.typicode.com/posts')
    
    if r.status_code == 200:
        posts = r.json()
        # Structure the data
        data_to_save = [
            {'id': p.get('id'), 'title': p.get('title'), 'body': p.get('body')}
            for p in posts
        ]
        
        # Write to CSV
        with open('posts.csv', 'w', newline='', encoding='utf-8') as f:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data_to_save)
