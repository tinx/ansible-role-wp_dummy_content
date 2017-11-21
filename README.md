# Ansible Role 'wp_dummy_content'

Provides generated dummy content for WordPress blogs.

## Requirements

There are no special requirements for the role itself.

The test playbook for this role depends on WP-CLI for setting up the test
environment. WP-CLI will be downloaded during the test run. The tests
also require testinfra, Vagrant and Virtualbox.

## Notes

In principle, this role can be run in Ansible local mode, but if you run it on
remote machines it can more easily be run in parallel. This matters if you
want to fill hundreds of blogs with dummy content.

## Role Variables

| Variable                             | Default  | Comments (type)                                   |
| :---                                 | :---     | :---                                              |
| `wp_dummy_content_blog_url`    |           | Where to find the Wordpress blog.                             |
| `wp_dummy_content_username`    |           | The username to use to log in into Wordpress                  |
| `wp_dummy_content_password`    |           | The password to use to log in into Wordpress                  |
| `wp_dummy_content_pages`       | '5-100+'  | The number of pages that the blog should contain              |
| `wp_dummy_content_posts`       | '5-100+'  | The number of posts that the blog should contain              |
| `wp_dummy_content_comments`    | '1-30+'   | The number of comments per post or page                       |

Many further parameters would be possible. (image sizes, taxonomies, tags,
size of posts, number of links and their destinatins, etc.)  These might
be added when needed.  Contributions are always welcome, or course.

### Amount value ranges

The value ranges can be used to indicate the amount of content desired.

You can specify:

* whether to remove currently existing items ('!')
* minimum number of items
* maximum number of items
* whether to keep existing surplus items ('+')

Example ranges:

* `5` means: make sure there are exactly five posts/pages/comments.
* `10+` means: at least ten. If more than that already exist, keep them.
* `3-10` means: random amount between 3 and 10.
* `!3-10` means: three to ten, but first delete every item that already exists.
* `3-10+` means: three to ten, but if there are already more than ten don't remove the extra ones.

The option to remove all existing entries (value ranges beginnig with '!')
is occasionally useful, for example if you wish to use Ansible as a load
generator. It will, of course, always result in a 'changed' status.

## Dependencies

none

## Example Playbook

To create some content using the default settings use:

    - hosts: webheads
      roles:
        - { role: tinx.wordpress_dummy_content,
            wordpress_dummy_content_url: 'http://www.example.com/blog/',
            wordpress_dummy_content_username: 'larry',
            wordpress_dummy_content_password: 'saturn' }

## Testing

Molecule tests are provided. Naturally, they require additional dependencies.

## Contributing

Ideas, feedback, issues and pull requests are always welcome.

For pull requests, please maintain backwards compatibility, run the tests
and add new ones before you issue the pull request. Thank you!

## License

BSD

## Author Information

 - [Andreas Jaekel](https://github.com/tinx/)

