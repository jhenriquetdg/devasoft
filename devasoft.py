from app import create_app, db, cli
from app.models import User, Post

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    context = dict()

    context['db'] = db
    context['User'] = User
    context['Post'] = Post

    return context
