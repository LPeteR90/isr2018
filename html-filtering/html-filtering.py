import argparse
import re
import requests
import os
import sys

def is_url(file_or_url):
    return re.match('^http(s)?:\/\/', file_or_url) != None

def get_data(file_or_url):
    if is_url(file_or_url):
        print('url detected, reading...')
        data = requests.get(file_or_url).text
    else:
        print('file detected, reading...')
        if not os.path.exists(file_or_url):
            sys.exit('file {} doesn\'t exist.'.format(file_or_url))
        with open(file_or_url, 'r') as file:
            data = file.read()
    return data

def print_metadata(data):
    regex_strings = {
        'title': '<title>(?P<title>.*)</title>',
        # todo: improve that attributes don't need to be in that order.
        'keywords': '<meta\s+name="keywords"\s+content="(?P<keywords>.*)"\s*(\/)?>',
        'description': '<meta\s+name="description"\s+content="(?P<description>.*)"\s*(\/)?>'
    }

    for name, regex in regex_strings.items():
        value = re.search(regex, data)
        if value is None:
            value = ''
        else:
            value = value.group(name)
        print('{}: {}'.format(name, value))


def mark_search_term(data, search_term):
    if search_term == '':
        return data
    return re.sub(search_term, '<<{}>>'.format(search_term), data)

def replace_html_tags(data):
    print('filtering html tags...')
    html_tags_regex = re.compile('<(\/)?.*?(\/)?>', re.DOTALL)
    return re.sub(html_tags_regex, '', data)

def html_filtering(input_file_or_url, search_term=''):
    data = get_data(input_file_or_url)
    print_metadata(data)
    data = replace_html_tags(data)
    data = mark_search_term(data, search_term)

    print('result:')
    print(data)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_or_url')
    parser.add_argument('search_term') # todo: make this argument optional
    args = parser.parse_args()
    html_filtering(args.input_file_or_url, args.search_term)

if __name__ == '__main__':
    main()
