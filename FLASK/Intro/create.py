from app import db, app, Games, Orders

with app.app_context():
    db.drop_all()
    db.create_all()

    
    testgame = Games(name='The Elder Scrolls: Skyrim', developer='Bethesda', price=20.50, age_rating=16 )
    db.session.add(testgame)
    db.session.commit()
    
    testorder = Orders(order_number='AFS43F2S', gamesbr=testgame)
    db.session.add(testorder)
    db.session.commit()
    
    print(testorder.gamesbr.name)    