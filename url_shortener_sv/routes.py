from flask import Blueprint, render_template, request, redirect, url_for
from .extensions import db
from .models import Link
from dotenv import load_dotenv
import string
from random import choices
import qrcode
import os

shortener = Blueprint('shortener', __name__)

@shortener.route('/<short_url>')
def redirect_to_url(short_url):
    link =  Link.query.filter_by(short_url=short_url).first_or_404()
    link.views = link.views + 1
    db.session.commit()
    return redirect(link.original_url)

@shortener.route('/create_link', methods=['POST'])
def create_link():
    original_url = request.form['original_url']
    link = Link(original_url=original_url)
    db.session.add(link)
    db.session.commit()

    # QR code module-----
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url_for('shortener.redirect_to_url', short_url=link.short_url, _external=True))
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    qr_directory = 'static/qr_codes'
    os.makedirs(qr_directory, exist_ok=True)
    qr_filename = os.path.join(qr_directory, f'{link.short_url}.png')
    img.save(qr_filename)

    return render_template('link_success.html', new_url=link.short_url, original_url=link.original_url, qr_filename=qr_filename)

@shortener.route('/')
def index():
    return render_template('index.html')

@shortener.route('/links')
def links():
    links = Link.query.all()

    return render_template('links.html', links=links)

@shortener.errorhandler(404)
def page_not_found(e):
    return '<h1>Sorry Page Not Found 404</h1>', 404
