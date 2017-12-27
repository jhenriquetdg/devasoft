from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Zetdg'}
    posts = [
    	{
    		'author': {'username': 'John'},
			'body': 'Deus é forte!'
    	},

    	{
    		'author': {'username': 'Susan'},
    		'body': 'Cristo salva.'    		
    	}
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
