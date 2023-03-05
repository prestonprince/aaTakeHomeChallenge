from app.models import db, Post


def seed_posts():
    #1
    first = Post(
        title='The First Cup', coffee_id=1, 
        text="I can't quite remember what it was, but it was made by Ann, I loved it because of that.",
        rating=5.0
    )

    #2
    second = Post(
        title='The Second Cup', coffee_id=2, 
        text="She always makes the best coffee. I don't think there is any other like it.",
        rating=5.0
    )

    #3
    third = Post(
        title='The Third Cup', coffee_id=3, 
        text="Ann made me a latte, this time with honey and cinnamon. She always puts so much of herself into the coffee she makes.",
        rating=5.0
    )

    db.session.add_all([ first, second, third ])
    db.session.commit()


def undo_posts():
    db.session.execute("DELETE FROM posts")
    db.session.commit()
