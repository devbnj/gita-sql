# main.py

from flask import Blueprint, render_template, json, session
from flask_login import login_required, current_user
import os
from flask import current_app as app
from .models import Gita
from . import db

pagecount = 1
maxpage = 9
advpg = 0
advmax = 70
main = Blueprint('main', __name__)

'''
@main.route('/')
def index():
    return render_template('index.html')
'''

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile/')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name, rigved=current_user.bgcode)

# def
def commonClass(pg):
    if pg == 0:
        pg = 1
    if 'page' in session:
        pg = session['page']
    filename = os.path.join(app.static_folder, ('class%d.json') % pg)
    actdata = {}
    with open(filename) as scriptures_file:
        tdata = json.load(scriptures_file)
        # print (tdata)
        actdata = tdata["data"]
    return render_template('class.html', name=current_user.name, page=pg, posts=actdata)
# end def

# def
def commonDb(page=0, page_size=None):
    gc = db.session.query(Gita)
    
    if page_size:
        gc = gc.limit(page_size)
    if page: 
        gc = gc.offset(page*page_size)
    
    return render_template('class2.html', name=current_user.name, post1=gc)
# end def

# def
@main.route('/class/')
@login_required
def gitaclass():
    global pagecount
    pagecount = 1
    return commonClass(pagecount)
# end def

# def
@main.route('/adv/')
@login_required
def advclass():
    global pagecount
    return commonDb(0, 10)
# end def

# def
@main.route('/prevclass/')
@login_required
def prevclass():
    global pagecount
    if 'page' in session:
        pg = session['page']
    else:
        pg = pagecount
        session['page'] = pg
    # page decrement
    pg = pg - 1
    if pg < 1:
        pg = 1
    session['page'] = pg
    return commonClass(pg)
# end def

# def
@main.route('/advprev/')
@login_required
def advprev():
    global advpg
    advpg = advpg - 1
    if (advpg < 0):
        advpg = 0
    return commonDb(advpg, 10)
# end def

# def
@main.route('/advnext/')
@login_required
def advnext():
    global advpg
    advpg = advpg + 1
    if advpg > advmax:
        advpg = advmax
    return commonDb(advpg, 10)
# end def

@main.route('/nextclass/')
@login_required
def nextclass():
    global pagecount
    if 'page' in session:
        pg = session['page']
    else:
        pg = pagecount
        session['page'] = pg
    if pg < maxpage:
        pg = pg + 1
    session['page'] = pg
    return commonClass(pg)

@main.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@main.errorhandler(500)
def internal_error(error):
    db.session.rollback()
    return render_template('500.html'), 500