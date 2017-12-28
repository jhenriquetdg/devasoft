from app import app, db
from app.models import User, Post

from mixer.backend.flask import mixer


def tb_print(Table=[]):
    """
        Generic Table Printer
    """
    contents = Table.query.all()
    for c, content in enumerate(contents):
        print('#', 'Number', '\t', 'Entry')
        print('#', c, '\t', content)


def tb_wipe(Table=[]):
    """
        Generic Table Wiper
    """
    contents = Table.query.all()
    for content in contents:
        db.session.delete(content)


def populate(db=db, app=app):
    """
    Pouplate the whole database with fake data
    """
    mixer.init_app(app)

    tb_wipe(User)
    tb_wipe(Post)

    db.session.commit()

    users = mixer.cycle(5).blend(User, username=mixer.FAKE, email=mixer.FAKE)
    posts = mixer.cycle(30).blend(Post, author=mixer.SELECT, body=mixer.FAKE)


@app.shell_context_processor
def make_shell_context():
    """
    This instances the table models in
    the flask shell context.
    """

    context = dict()

    context['db'] = db
    context['User'] = User
    context['Post'] = Post

    context['tb_print'] = tb_print
    context['tb_wipe'] = tb_wipe
    context['populate'] = populate

    return context

populate()