#!/usr/bin/python

import os
import xmlrpclib

def get_all_posts(wp_api, post_type):
    """Get a list of all published posts of the given type in the blog.
       WordPress does not offer a way to get all posts in one call. The php
       function accepts "-1" as "no limit", but this does not work
       via XML-RPC."""
    posts = []
    offset = 0
    while True:
        next_batch = wp_api.wp.getPosts(1, 'admin', 'admin',
                                           {"post_type": post_type,
                                            "post_status": "publish",
                                            "number": 100,
                                            "offset": offset},
                                           ['post_title', 'comment_status'])
        if len(next_batch) <= 0:
            break
        posts += next_batch
        offset += 100
    return posts

def get_all_comments_for_post(wp_api, post):
    """Get a list of all comments of the given post.
       WordPress does not offer a way to get all comments in one call. The php
       function accepts "-1" as "no limit", but this does not work
       via XML-RPC."""
    comments = []
    offset = 0;
    while True:
        next_batch = wp_api.wp.getComments(1, 'admin', 'admin',
                                              { "post_id": post['post_id'],
                                                "number": 100,
                                                "offset": offset })
        if len(next_batch) <= 0:
            break
        comments += next_batch
        offset += 100
    return comments


def print_stats(post_type):
    wp_api = xmlrpclib.ServerProxy('http://wp1.example.com/xmlrpc.php',
                                   use_datetime=True)
    posts = get_all_posts(wp_api, post_type)
    print post_type + " amount: " + str(len(posts))
    comments = []
    for p in posts:
        comments += get_all_comments_for_post(wp_api, p)
    print post_type + " comments: " + str(len(comments))

def main():
    print_stats('post')
    print_stats('page')

if __name__ == '__main__':
    main()

