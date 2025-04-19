# app.py
from flask import Flask, render_template, request, redirect, url_for, flash, session, abort
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import datetime
import random
import string
from functools import wraps
import click

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///urlshortener.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy
db = SQLAlchemy(app)

# Initialize LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    urls = db.relationship('URL', backref='user', lazy=True)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<User {self.username}>'

class URL(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_url = db.Column(db.String(20), unique=True, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    clicks = db.relationship('Click', backref='url', lazy=True, cascade="all, delete-orphan")
    
    def __repr__(self):
        return f'<URL {self.short_url}>'

class Click(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
    ip_address = db.Column(db.String(100))
    user_agent = db.Column(db.String(500))
    referrer = db.Column(db.String(500))
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    
    def __repr__(self):
        return f'<Click {self.id}>'

# Helper functions
def generate_short_url(length=6):
    chars = string.ascii_letters + string.digits
    short_url = ''.join(random.choice(chars) for _ in range(length))
    return short_url

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Flask CLI commands for database initialization
@click.command('init-db')
def init_db_command():
    with app.app_context():
        db.create_all()
        click.echo('Database initialized.')

app.cli.add_command(init_db_command)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm_password')
        
        # Input validation
        if not username or not password or not confirm_password:
            flash('All fields are required', 'danger')
            return redirect(url_for('register'))
        
        if password != confirm_password:
            flash('Passwords do not match', 'danger')
            return redirect(url_for('register'))
        
        user_exists = User.query.filter_by(username=username).first()
        if user_exists:
            flash('Username already exists', 'danger')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password=hashed_password)
        
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('login'))
    
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if not username or not password:
            flash('All fields are required', 'danger')
            return redirect(url_for('login'))
        
        user = User.query.filter_by(username=username).first()
        
        if not user or not check_password_hash(user.password, password):
            flash('Invalid credentials', 'danger')
            return redirect(url_for('login'))
        
        login_user(user)
        flash('Login successful!', 'success')
        return redirect(url_for('dashboard'))
    
    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.', 'success')
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    user_urls = URL.query.filter_by(user_id=current_user.id).order_by(URL.created_at.desc()).all()
    return render_template('dashboard.html', urls=user_urls)

@app.route('/create', methods=['POST'])
@login_required
def create_url():
    original_url = request.form.get('url')
    
    if not original_url:
        flash('URL is required', 'danger')
        return redirect(url_for('dashboard'))
    
    # Ensure URL has http:// or https:// prefix
    if not original_url.startswith(('http://', 'https://')):
        original_url = 'https://' + original_url
    
    # Generate a unique short URL
    while True:
        short_url = generate_short_url()
        url_exists = URL.query.filter_by(short_url=short_url).first()
        if not url_exists:
            break
    
    new_url = URL(
        original_url=original_url,
        short_url=short_url,
        user_id=current_user.id
    )
    
    db.session.add(new_url)
    db.session.commit()
    
    flash('Short URL created successfully!', 'success')
    return redirect(url_for('dashboard'))

@app.route('/s/<short_url>')
def redirect_to_url(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    
    # Record click analytics
    click = Click(
        url_id=url.id,
        ip_address=request.remote_addr,
        user_agent=request.user_agent.string,
        referrer=request.referrer if request.referrer else 'Direct'
    )
    
    db.session.add(click)
    db.session.commit()
    
    return redirect(url.original_url)

@app.route('/analytics/<short_url>')
@login_required
def analytics(short_url):
    url = URL.query.filter_by(short_url=short_url).first_or_404()
    
    # Ensure the URL belongs to the current user
    if url.user_id != current_user.id:
        abort(403)
    
    clicks = Click.query.filter_by(url_id=url.id).order_by(Click.timestamp.desc()).all()
    
    # Calculate analytics
    total_clicks = len(clicks)
    
    # Group by date for time-based chart
    clicks_by_date = {}
    for click in clicks:
        date_str = click.timestamp.strftime('%Y-%m-%d')
        if date_str in clicks_by_date:
            clicks_by_date[date_str] += 1
        else:
            clicks_by_date[date_str] = 1
    
    # Sort dates
    sorted_dates = sorted(clicks_by_date.items())
    
    # Group by referrer
    referrers = {}
    for click in clicks:
        if click.referrer in referrers:
            referrers[click.referrer] += 1
        else:
            referrers[click.referrer] = 1
    
    # Group by browser
    browsers = {}
    for click in clicks:
        browser = "Unknown"
        ua = click.user_agent.lower()
        if "chrome" in ua:
            browser = "Chrome"
        elif "firefox" in ua:
            browser = "Firefox"
        elif "safari" in ua and "chrome" not in ua:
            browser = "Safari"
        elif "edge" in ua:
            browser = "Edge"
        elif "opera" in ua:
            browser = "Opera"
        
        if browser in browsers:
            browsers[browser] += 1
        else:
            browsers[browser] = 1
    
    return render_template(
        'analytics.html', 
        url=url,
        clicks=clicks,
        total_clicks=total_clicks,
        dates=[d[0] for d in sorted_dates],
        counts=[d[1] for d in sorted_dates],
        referrers=referrers,
        browsers=browsers
    )

@app.route('/delete/<int:url_id>', methods=['POST'])
@login_required
def delete_url(url_id):
    url = URL.query.get_or_404(url_id)
    
    # Ensure the URL belongs to the current user
    if url.user_id != current_user.id:
        abort(403)
    
    db.session.delete(url)
    db.session.commit()
    
    flash('URL deleted successfully!', 'success')
    return redirect(url_for('dashboard'))

if __name__ == '__main__':
    app.run(debug=True)