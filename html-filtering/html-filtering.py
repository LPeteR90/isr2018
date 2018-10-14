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

def replace_html_tags(data):
    print('filtering html tags...')
    html_tags_regex = re.compile('<(\/)?.*?(\/)?>', re.DOTALL)
    return re.sub(html_tags_regex, '', data)

def html_filtering(input_file_or_url):
    data = get_data(input_file_or_url)
    data = replace_html_tags(data)

    print('result:')
    print(data)




def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('input_file_or_url')
    args = parser.parse_args()
    html_filtering(args.input_file_or_url)

if __name__ == '__main__':
    main()
