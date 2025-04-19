# 🔗 LinkSnip - Professional URL Shortener with Advanced Analytics

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.3.3-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/SQLAlchemy-3.1.1-red.svg" alt="SQLAlchemy Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/LinkSnip/main/demo.gif" alt="LinkSnip Demo Video" width="800">
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#tech-stack">Tech Stack</a> •
  <a href="#installation">Installation</a> •
  <a href="#configuration">Configuration</a> •
  <a href="#usage">Usage</a> •
  <a href="#screenshots">Screenshots</a> •
  <a href="#contributing">Contributing</a> •
  <a href="#license">License</a>
</p>

---

## ✨ Demo Video

<p align="center">
  <a href="https://youtu.be/demo-video-link">
    <img src="https://img.youtube.com/vi/demo-video-id/maxresdefault.jpg" alt="Watch the demo video" width="500">
  </a>
</p>

> Click the image above to watch a full demonstration of LinkSnip's features!

## 🚀 Features

<table>
  <tr>
    <td align="center" width="33%">
      <strong>🔒 User Authentication</strong><br>
      <img src="https://img.icons8.com/fluency/64/000000/login-rounded-right.png" alt="Authentication" width="40"><br>
      <small>Secure registration and login system<br>with password hashing</small>
    </td>
    <td align="center" width="33%">
      <strong>📊 Advanced Analytics</strong><br>
      <img src="https://img.icons8.com/fluency/64/000000/combo-chart.png" alt="Analytics" width="40"><br>
      <small>Track clicks, referrers, browsers,<br>and geographical data</small>
    </td>
    <td align="center" width="33%">
      <strong>🎨 Dark Mode Interface</strong><br>
      <img src="https://img.icons8.com/fluency/64/000000/moon-symbol.png" alt="Dark Mode" width="40"><br>
      <small>Modern, eye-friendly UI with<br>stunning purple gradient themes</small>
    </td>
  </tr>
  <tr>
    <td align="center" width="33%">
      <strong>⚡ Quick Redirection</strong><br>
      <img src="https://img.icons8.com/fluency/64/000000/lightning-bolt.png" alt="Speed" width="40"><br>
      <small>Lightning-fast URL redirection<br>with efficient database queries</small>
    </td>
    <td align="center" width="33%">
      <strong>📱 Responsive Design</strong><br>
      <img src="https://img.icons8.com/fluency/64/000000/smartphone-tablet.png" alt="Responsive" width="40"><br>
      <small>Fully responsive design works<br>on all devices and screen sizes</small>
    </td>
    <td align="center" width="33%">
      <strong>📋 Copy to Clipboard</strong><br>
      <img src="https://img.icons8.com/fluency/64/000000/copy.png" alt="Copy" width="40"><br>
      <small>One-click copying of shortened<br>URLs for easy sharing</small>
    </td>
  </tr>
</table>

## 🛠 Tech Stack

| Technology | Description | Version |
|------------|-------------|---------|
| ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) | Programming Language | 3.8+ |
| ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white) | Web Framework | 2.3.3 |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-red?style=for-the-badge&logo=sqlalchemy&logoColor=white) | ORM | 3.1.1 |
| ![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white) | CSS Framework | 5.3.0 |
| ![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=for-the-badge&logo=chartdotjs&logoColor=white) | Data Visualization | 3.9.1 |
| ![Font Awesome](https://img.shields.io/badge/Font_Awesome-339AF0?style=for-the-badge&logo=fontawesome&logoColor=white) | Icons | 6.4.0 |

## 📦 Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.8 or higher
- pip (Python package manager)
- Git

### 🔄 Step-by-Step Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/LinkSnip.git
   cd LinkSnip
   ```

2. **Create and activate a virtual environment**
   
   For Windows:
   ```bash
   python -m venv venv
   venv\Scripts\activate
   ```
   
   For macOS/Linux:
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**
   ```bash
   flask init-db
   ```

5. **Run the application**
   ```bash
   flask run
   ```

6. **Access the application**
   
   Open your browser and navigate to: `http://127.0.0.1:5000`

## ⚙️ Configuration

### Environment Variables

Create a `.env` file in the root directory:

```env
FLASK_APP=app.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///urlshortener.db
```

### Database Initialization

For a fresh database setup:
```bash
flask init-db
```

To reset the database (WARNING: This will delete all data):
```bash
rm -f urlshortener.db
flask init-db
```

## 📱 Usage

### Creating an Account
1. Click on "Create New Account" on the homepage
2. Enter a unique username and password
3. Confirm your password
4. Submit the registration form

### Creating a Short URL
1. Log in to your account
2. On the dashboard, enter the URL you want to shorten
3. Click "Shorten URL"
4. Your shortened URL will appear in the table below

### Viewing Analytics
1. From the dashboard, click "Analytics" next to any URL
2. View detailed statistics including:
   - Total clicks
   - Click timeline
   - Referrer distribution
   - Browser usage
   - Individual click details

## 📸 Screenshots

### Homepage
<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/LinkSnip/main/screenshots/homepage.png" alt="Homepage" width="600">
</p>

### Dashboard
<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/LinkSnip/main/screenshots/dashboard.png" alt="Dashboard" width="600">
</p>

### Analytics
<p align="center">
  <img src="https://raw.githubusercontent.com/yourusername/LinkSnip/main/screenshots/analytics.png" alt="Analytics" width="600">
</p>

## 🔧 Advanced Commands

| Command | Description |
|---------|-------------|
| `flask run --host=0.0.0.0` | Run the app accessible on your network |
| `flask run --port=8080` | Run the app on a different port |
| `flask shell` | Open a Python shell with app context |
| `flask routes` | List all available routes |

## 🐛 Debug Mode

For development with auto-reload:
```bash
export FLASK_ENV=development  # Linux/macOS
set FLASK_ENV=development     # Windows
flask run
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Coding Standards
- Follow PEP 8 guidelines
- Write meaningful commit messages
- Add comments for complex logic
- Update documentation as needed

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Profile](https://linkedin.com/in/yourprofile)
- Email: your.email@example.com

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/yourusername">Your Name</a>
</p>

<p align="center">
  <a href="#top">⬆️ Back to Top</a>
</p>
