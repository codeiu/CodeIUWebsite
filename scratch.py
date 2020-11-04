from website import db, models, bcrypt

if __name__ == "__main__":
    # db.session.add(models.User(username="chris", email="chrisalexeev@gmail.com", password="1234"))
    # db.session.commit()
    hashed_password = bcrypt.generate_password_hash("1234").decode('utf-8')
    print(hashed_password)
    print(bcrypt.check_password_hash(hashed_password, '1235'))