import json
from blog.models import Post

with open('orders.json', encoding='utf-8') as f:
   posts_json = json.load(f)

for post in posts_json:
   post = Post(purchaser=post['purchaser'], order_num=post['order_num'], title=post['title'])
   post.save()
