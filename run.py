from app import create_app, db, config


app = create_app(config)
app.app_context().push()
db.create_all()
