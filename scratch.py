from website import db, models

if __name__ == "__main__":
    # db.session.add(models.User(username="chris", email="chrisalexeev@gmail.com", password="1234"))
    # db.session.commit()
    db.create_all()
