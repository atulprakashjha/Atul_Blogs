import json
from blog.models import User, Post
from blog import db


with open('../post.json') as f:
    posts = json.load(f)

for post in posts:
    author = User.query.filter_by(id=post['user_id']).first()
    Post(title=post['title'], content=post['content'], author=author)
    p = Post(title=post['title'], content=post['content'], author=author)
    db.session.add(p)

db.session.commit()