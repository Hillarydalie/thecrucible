from flask_script import Manager,Server
from flask_migrate import Migrate,MigrateCommand
from app import create_app,db
from app.models import Author,Blog, Blogcomment

app = create_app('production')

manager =  Manager(app)
migrate = Migrate(app,db)
manager.add_command('runserver',Server(use_debugger=True))
manager.add_command('db',MigrateCommand)

@manager.shell
def add_shell_context():
    return {"db":db,"Author":Author}

if __name__=="__main__":
    manager.run()