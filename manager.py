from flask_script import Manager
from flask_script.commands import ShowUrls
from application.app import app

manager = Manager(app)

manager.add_command("showurls", ShowUrls())

if __name__ == '__main__':
    manager.run()