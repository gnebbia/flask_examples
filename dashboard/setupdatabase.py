from basic import db,Puppy

db.create_all()


sam = Puppy('Sammy', 3)
frank = Puppy('Frankie', 4)


# Here None it will be printed since they still do not
# have an ID
print(sam.id)
print(frank.id)


db.session.add_all([sam,frank])


# we can also add elements individually
# db.session.add(sam)

db.session.commit()

# Now they have an ID
print(sam.id)
print(frank.id)
