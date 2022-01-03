from app import app, db
import os

print(os.environ.get('POO'))
print(os.environ.get('SQLALCHEMY_DATABASE'))
print(os.environ.get('FLASK_APP'))
print(os.environ.get('SECRET_KEY'))
print(os.environ.get('RAPIDAPI_HOST'))
print(os.environ.get('RAPIDAPI_KEY'))


from app.models import User, Tranche

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Tranche': Tranche}
