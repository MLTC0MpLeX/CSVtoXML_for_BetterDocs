import csv
import xml.etree.cElementTree as ET

# Load data from CSV file
filename = input("Enter source file name:")
with open('', 'r', encoding='utf-8') as f:
    reader = csv.reader(f)
    next(reader)  # skip header row
    data = list(reader)

print("Data Loaded")
siteurl = input("Enter your website url:")

# Create root element
root = ET.Element('rss', version='2.0', **{'xmlns:excerpt': 'http://wordpress.org/export/1.2/excerpt/', 'xmlns:content': 'http://purl.org/rss/1.0/modules/content/', 'xmlns:wfw': 'http://wellformedweb.org/CommentAPI/', 'xmlns:dc': 'http://purl.org/dc/elements/1.1/', 'xmlns:wp': 'http://wordpress.org/export/1.2/'})

# Create channel element
channel = ET.SubElement(root, 'channel')

# Add metadata elements to channel
title = ET.SubElement(channel, 'title')
title.text = 'AWordPressSite'

link = ET.SubElement(channel, 'link')
link.text = siteurl

description = ET.SubElement(channel, 'description')
description.text = ''

pubDate = ET.SubElement(channel, 'pubDate')
pubDate.text = 'Tue, 07 Mar 2023 08:40:23 +0000'

language = ET.SubElement(channel, 'language')
language.text = 'en-GB'

wxr_version = ET.SubElement(channel, 'wp:wxr_version')
wxr_version.text = '1.2'

base_site_url = ET.SubElement(channel, 'wp:base_site_url')
base_site_url.text = siteurl

base_blog_url = ET.SubElement(channel, 'wp:base_blog_url')
base_blog_url.text = siteurl

# Loop through data and create item elements
for row in data:
    title = row[0]
    content = row[1]
    category = row[2]

    item = ET.SubElement(channel, 'item')

    title_element = ET.SubElement(item, 'title')
    title_element.text = title

    link = ET.SubElement(item, 'link')
    link.text = ''

    pubDate = ET.SubElement(item, 'pubDate')
    pubDate.text = ''

    creator = ET.SubElement(item, 'dc:creator')
    creator.text = ''

    guid = ET.SubElement(item, 'guid', isPermaLink='false')
    guid.text = ''

    description = ET.SubElement(item, 'description')

    content_encoded = ET.SubElement(item, 'content:encoded')
    content_encoded.text = content

    excerpt_encoded = ET.SubElement(item, 'excerpt:encoded')

    post_id = ET.SubElement(item, 'wp:post_id')
    post_id.text = ''

    post_date = ET.SubElement(item, 'wp:post_date')
    post_date.text = ''

    post_date_gmt = ET.SubElement(item, 'wp:post_date_gmt')
    post_date_gmt.text = ''

    post_modified = ET.SubElement(item, 'wp:post_modified')
    post_modified.text = ''

    post_modified_gmt = ET.SubElement(item, 'wp:post_modified_gmt')
    post_modified_gmt.text = ''

    comment_status = ET.SubElement(item, 'wp:comment_status')
    comment_status.text = 'open'

    ping_status = ET.SubElement(item, 'wp:ping_status')
    ping_status.text = 'closed'

    post_name = ET.SubElement(item, 'wp:post_name')
    post_name.text = ''

    status = ET.SubElement(item, 'wp:status')
    status.text = 'publish'
    post_parent = ET.SubElement(item, 'wp:post_parent')
    post_parent.text = '0'

    menu_order = ET.SubElement(item, 'wp:menu_order')
    menu_order.text = '0'

    post_type = ET.SubElement(item, 'wp:post_type')
    post_type.text = 'docs'

    post_password = ET.SubElement(item, 'wp:post_password')

    is_sticky = ET.SubElement(item, 'wp:is_sticky')
    is_sticky.text = '0'

    category_element = ET.SubElement(item, 'category', domain='doc_category', nicename=category)
    category_element.text = ''

    postmeta1 = ET.SubElement(item, 'wp:postmeta')
    meta_key1 = ET.SubElement(postmeta1, 'wp:meta_key')
    meta_key1.text = '_edit_last'
    meta_value1 = ET.SubElement(postmeta1, 'wp:meta_value')
    meta_value1.text = '1'

    postmeta2 = ET.SubElement(item, 'wp:postmeta')
    meta_key2 = ET.SubElement(postmeta2, 'wp:meta_key')
    meta_key2.text = 'plan_title'
    meta_value2 = ET.SubElement(postmeta2, 'wp:meta_value')
    meta_value2.text = ''

    postmeta3 = ET.SubElement(item, 'wp:postmeta')
    meta_key3 = ET.SubElement(postmeta3, 'wp:meta_key')
    meta_key3.text = 'plan_description'
    meta_value3 = ET.SubElement(postmeta3, 'wp:meta_value')
    meta_value3.text = ''

    postmeta4 = ET.SubElement(item, 'wp:postmeta')
    meta_key4 = ET.SubElement(postmeta4, 'wp:meta_key')
    meta_key4.text = 'plan_image_attach'
    meta_value4 = ET.SubElement(postmeta4, 'wp:meta_value')
    meta_value4.text = ''

    postmeta5 = ET.SubElement(item, 'wp:postmeta')
    meta_key5 = ET.SubElement(postmeta5, 'wp:meta_key')
    meta_key5.text = 'plan_image'
    meta_value5 = ET.SubElement(postmeta5, 'wp:meta_value')
    meta_value5.text = ''

    postmeta6 = ET.SubElement(item, 'wp:postmeta')
    meta_key6 = ET.SubElement(postmeta6, 'wp:meta_key')
    meta_key6.text = 'plan_size'
    meta_value6 = ET.SubElement(postmeta6, 'wp:meta_value')
    meta_value6.text = ''

    postmeta7 = ET.SubElement(item, 'wp:postmeta')
    meta_key7 = ET.SubElement(postmeta7, 'wp:meta_key')
    meta_key7.text = 'plan_rooms'
    meta_value7 = ET.SubElement(postmeta7, 'wp:meta_value')
    meta_value7.text = ''

    postmeta8 = ET.SubElement(item, 'wp:postmeta')
    meta_key8 = ET.SubElement(postmeta8, 'wp:meta_key')
    meta_key8.text = 'plan_bath'
    meta_value8 = ET.SubElement(postmeta8, 'wp:meta_value')
    meta_value8.text = ''

    postmeta9 = ET.SubElement(item, 'wp:postmeta')
    meta_key9 = ET.SubElement(postmeta9, 'wp:meta_key')
    meta_key9.text = 'plan_price'
    meta_value9 = ET.SubElement(postmeta9, 'wp:meta_value')
    meta_value9.text = ''

    postmeta10 = ET.SubElement(item, 'wp:postmeta')
    meta_key10 = ET.SubElement(postmeta10, 'wp:meta_key')
    meta_key10.text = 'adv_filter_search_action'
    meta_value10 = ET.SubElement(postmeta10, 'wp:meta_value')
    meta_value10.text = ''

    postmeta11 = ET.SubElement(item, 'wp:postmeta')
    meta_key11 = ET.SubElement(postmeta11, 'wp:meta_key')
    meta_key11.text = 'adv_filter_search_category'
    meta_value11 = ET.SubElement(postmeta11, 'wp:meta_value')
    meta_value11.text = ''

    postmeta12 = ET.SubElement(item, 'wp:postmeta')
    meta_key12 = ET.SubElement(postmeta12, 'wp:meta_key')
    meta_key12.text = 'current_adv_filter_city'
    meta_value12 = ET.SubElement(postmeta12, 'wp:meta_value')
    meta_value12.text = ''

    postmeta13 = ET.SubElement(item, 'wp:postmeta')
    meta_key13 = ET.SubElement(postmeta13, 'wp:meta_key')
    meta_key13.text = 'current_adv_filter_county'
    meta_value13 = ET.SubElement(postmeta13, 'wp:meta_value')
    meta_value13.text = ''

    postmeta14 = ET.SubElement(item, 'wp:postmeta')
    meta_key14 = ET.SubElement(postmeta14, 'wp:meta_key')
    meta_key14.text = 'current_adv_filter_area'
    meta_value14 = ET.SubElement(postmeta14, 'wp:meta_value')
    meta_value14.text = ''
tree = ET.ElementTree(root)
tree.write('output.xml', encoding='utf-8', xml_declaration=True)





