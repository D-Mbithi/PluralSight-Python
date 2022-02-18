"""Retrieves and prints words from a documentself.

    Usage:
        python words.py 'http://sixty-north.com/c/t.txt'
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch a list fo words from a URL.

        Args:
            url: The url of utf-8 deocument.

        Returns:
            A list of string containing words from the document.

    """
    story = urlopen(url)

    story_words = []

    for line in story:
        line_words = line.decode('utf-8').split()

        for word in line_words:
            story_words.append(word)

    story.close()

    return story_words


def print_items(story_words):
    """ Prints items one per line.

        Args:
            A iterable series of printable items.

    """
    for word in story_words:
        print(word)


def main(url):
    """Prints each word in one line.

        Args:
            url: The url of a utf-8 document.
    """
    words = fetch_words(url)

    print_items(words)


if __name__ == "__main__":
    main(sys.argv[1])
