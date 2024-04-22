from flask import Blueprint, request, url_for
from flask import render_template

bp=Blueprint("root",__name__,url_prefix="/")
@bp.route('/')
def root():
    return render_template('root.html')
