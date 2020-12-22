import yaml
import json
import os
import re


"""
Specify the Jekyll post directory (relative to this file's location)
and the output file name.
"""

post_directory = '_posts/'
new_filename = 'jekyll_to_ghost.json'


"""
Get list of .md or .markdown files from that directory.
(Modify if source files have different extensions.)
"""

file_list = []
for f in os.listdir(post_directory):
    if '.md' in f or '.markdown' in f or '.html' in f:
        file_list.append(f)


"""
Build an empty dictionary structure for the output file.
"""

json_object = {}
json_object['db'] = []
posts_object = {}
posts_object['meta'] = {}
"""
posts_object['meta']['exported_on'] = 1594529598998
"""
posts_object['meta']['version'] =  "3.0.0"
posts_object['data'] = {}
posts_object['data']['posts'] = []


"""
Create a JSON object for each markdown file in the posts directory.
This section assumes certain names for YAML parameters.
Edit as necessary to fit YAML parameters used by your blog/theme.
"""

for filename in file_list:
    original = open(post_directory + filename, 'r', encoding='utf-8')
    parsed = ''

    for line in original:
        parsed += line

    parsed = parsed.split('---\n')
    header = yaml.load(parsed[1])
    header['content'] = parsed[2].replace('/assets/images/', '/content/images/')

    post_object = {
    "id": 0,
    "title": "",
    "slug": "",
    "html": "",
    "status": "published",
    "author_id": 1,
    "created_at": "",
    "updated_at": "",
    "published_at": "",
    }

    post_object['title'] = post_object['og_title'] = post_object['twitter_title'] = header['title']
    post_object['slug'] = filename[11:].split('.')[0]
    try:
        post_object['created_at'] = post_object['updated_at'] = post_object['published_at'] = str(header['modified'])
    except:
        post_object['created_at'] = post_object['updated_at'] = post_object['published_at'] = str(header['date'])
    # post_object['html'] = header['content']

    mymobiledoc = {}
    mymobiledoc['version'] = '0.3.1'
    mymobiledoc['markups'] = []
    mymobiledoc['atoms'] = []

    myhtml = {}
    myhtml['cardName'] = 'html'
    myhtml['html'] = header['content'].replace('{{ site.url }}','/content/images')

    mymobiledoc['cards'] = [['html', myhtml]]
    mymobiledoc['sections'] = [[10, 0]]
    post_object['mobiledoc'] = json.dumps(mymobiledoc, separators=(',', ':'))
    if "img src" in header['content']:
        raw_image = re.search('img src="(.*?)" ',header['content'])
        post_object['feature_image'] = raw_image[1].replace('{{ site.url }}','/content/images')
        # print(post_object['feature_image'])
        pass

    posts_object['data']['posts'].append(post_object)


"""
Insert all post objects into the blank database created above, following
the structure expected by Ghost. Write to file (name provided above).
"""

json_object['db'].append(posts_object)

with open(new_filename, 'w') as new_file:
    # new_file.write(str(header))
    json.dump(json_object, new_file, indent = 4)