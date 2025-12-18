# BYYOUANDIANDAI - Luxury Fashion E-Commerce

<div align="center">

![BYYOUANDIANDAI](https://img.shields.io/badge/BYYOUANDIANDAI-Luxury%20Fashion-black?style=for-the-badge)
![Django](https://img.shields.io/badge/Django-6.0-green?style=for-the-badge&logo=django)
![PWA](https://img.shields.io/badge/PWA-Ready-blue?style=for-the-badge)
![Mobile](https://img.shields.io/badge/Mobile-Optimized-orange?style=for-the-badge)

**Discover Curated Luxury Fashion and Accessories**

[Live Demo](#) | [Features](#features) | [Installation](#installation) | [Mobile App](#mobile-app)

</div>

---

## 🌟 Overview

BYYOUANDIANDAI is a modern, luxury fashion e-commerce platform built with Django. Featuring a curated selection of high-end fashion items, the platform offers a seamless shopping experience across all devices with Progressive Web App (PWA) capabilities.

### ✨ Key Highlights

- 🎨 **Modern Design** - Luxury-inspired interface with dark mode
- 📱 **PWA Ready** - Install as mobile app (iOS & Android)
- 🛒 **Full E-Commerce** - Complete shopping cart and checkout
- ⭐ **Customer Reviews** - 5-star rating system
- ❤️ **Wishlist** - Save favorite items
- 💳 **Stripe Integration** - Secure payments
- 📧 **Email Confirmations** - Order notifications
- 🎯 **Responsive** - Optimized for all screen sizes

---

## 🚀 Features

### Shopping Experience
- **Curated Collection** - 2 products per category for focused selection
- **Size Selection** - Small, Medium, Large, Extra Large options
- **Product Reviews** - Customer ratings and comments
- **Wishlist** - Save items for later
- **Shopping Cart** - Real-time updates
- **Secure Checkout** - Stripe payment processing

### User Features
- **User Accounts** - Registration and authentication
- **Profile Management** - Save delivery information
- **Order History** - Track past purchases
- **Email Notifications** - Order confirmations

### Admin Features
- **Product Management** - Add, edit, delete products
- **Order Management** - View and process orders
- **Review Moderation** - Manage customer reviews
- **Wishlist Analytics** - See popular products

### Technical Features
- **Progressive Web App** - Install on mobile devices
- **Service Worker** - Offline functionality
- **Responsive Design** - Mobile, tablet, desktop
- **Dark Mode** - Eye-friendly interface
- **SEO Optimized** - Meta tags and descriptions

---

## 📱 Mobile App

### Progressive Web App (PWA)

BYYOUANDIANDAI can be installed as a mobile app on both iOS and Android devices:

#### iOS Installation
1. Open Safari and navigate to the website
2. Tap the Share button
3. Select "Add to Home Screen"
4. Tap "Add"

#### Android Installation
1. Open Chrome and navigate to the website
2. Tap the menu (three dots)
3. Select "Add to Home Screen"
4. Tap "Add"

### Features When Installed
- ✅ App icon on home screen
- ✅ Full-screen experience
- ✅ Offline functionality
- ✅ Fast loading
- ✅ Push notifications (coming soon)

---

## 🛠️ Technologies Used

### Backend
- **Django 6.0** - Web framework
- **Python 3.12** - Programming language
- **PostgreSQL** - Production database
- **SQLite** - Development database

### Frontend
- **HTML5** - Structure
- **CSS3** - Styling
- **JavaScript** - Interactivity
- **Bootstrap 4.6** - UI framework
- **jQuery** - DOM manipulation

### Payment & Email
- **Stripe** - Payment processing
- **Django Email** - Email notifications

### Storage & Deployment
- **AWS S3** - Media and static files
- **WhiteNoise** - Static file serving
- **Gunicorn** - WSGI server
- **Heroku** - Deployment platform

### PWA
- **Service Worker** - Offline functionality
- **Web App Manifest** - App configuration
- **Cache API** - Asset caching

---

## 📦 Installation

### Prerequisites
- Python 3.12+
- pip
- Virtual environment (recommended)

### Local Development Setup

1. **Clone the repository**
```bash
git clone https://github.com/mg747/mega-boutique.git
cd mega-boutique
```

2. **Create virtual environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set environment variables**
```bash
export STRIPE_PUBLIC_KEY="your_stripe_public_key"
export STRIPE_SECRET_KEY="your_stripe_secret_key"
```

5. **Run migrations**
```bash
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Load sample data**
```bash
python manage.py loaddata products/fixtures/categories.json
python manage.py loaddata products/fixtures/products.json
```

8. **Collect static files**
```bash
python manage.py collectstatic
```

9. **Run development server**
```bash
python manage.py runserver
```

10. **Access the application**
- Website: http://localhost:8000
- Admin: http://localhost:8000/admin

---

## 🎨 Design

### Color Scheme
- **Primary**: #000000 (Black)
- **Background**: #1a1a1a (Dark Gray)
- **Cards**: #2a2a2a (Medium Gray)
- **Text**: #e0e0e0 (Light Gray)
- **Borders**: #444444 (Border Gray)
- **Accent**: #ffc107 (Gold)

### Typography
- **Headings**: Lato, sans-serif
- **Body**: Lato, sans-serif
- **Logo**: Lato, 300 weight, 2px letter-spacing

### Layout
- **Mobile-first** responsive design
- **Grid system** for product layouts
- **Flexbox** for component alignment
- **Dark mode** throughout

---

## 🧪 Testing

### Manual Testing
- ✅ User registration and login
- ✅ Product browsing and search
- ✅ Add to cart functionality
- ✅ Checkout process
- ✅ Payment processing (Stripe test mode)
- ✅ Email confirmations
- ✅ Wishlist functionality
- ✅ Product reviews
- ✅ Mobile responsiveness
- ✅ PWA installation

### Test Cards (Stripe)
- **Success**: 4242 4242 4242 4242
- **Decline**: 4000 0000 0000 0002
- **Requires Auth**: 4000 0025 0000 3155

---

## 📊 Database Schema

### Models
- **Product** - Product information
- **Category** - Product categories
- **ProductReview** - Customer reviews
- **Wishlist** - User wishlists
- **Order** - Customer orders
- **OrderLineItem** - Order details
- **UserProfile** - User profiles

---

## 🔐 Security

- CSRF protection enabled
- Secure password hashing
- Environment variables for secrets
- HTTPS in production
- Stripe secure payments
- SQL injection protection

---

## 🚀 Deployment

### Heroku Deployment

1. **Create Heroku app**
```bash
heroku create your-app-name
```

2. **Set environment variables**
```bash
heroku config:set STRIPE_PUBLIC_KEY=your_key
heroku config:set STRIPE_SECRET_KEY=your_key
heroku config:set SECRET_KEY=your_secret_key
```

3. **Deploy**
```bash
git push heroku main
```

4. **Run migrations**
```bash
heroku run python manage.py migrate
```

### Alternative Platforms
- **Railway** - Easy deployment
- **Render** - Free tier available
- **DigitalOcean** - App Platform

---

## 📝 Environment Variables

Required environment variables:

```bash
# Django
SECRET_KEY=your_secret_key
DEBUG=False

# Database
DATABASE_URL=your_database_url

# Stripe
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...

# AWS S3 (Optional)
USE_AWS=True
AWS_ACCESS_KEY_ID=your_key
AWS_SECRET_ACCESS_KEY=your_secret
AWS_STORAGE_BUCKET_NAME=your_bucket

# Email (Optional)
EMAIL_HOST_USER=your_email
EMAIL_HOST_PASS=your_password
```

---

## 📚 Documentation

- [Setup Guide](SETUP_GUIDE.md)
- [Stripe Setup](STRIPE_SETUP.md)
- [New Features](NEW_FEATURES.md)
- [Fixes Applied](FIXES_APPLIED.md)
- [Redesign Plan](REDESIGN_PLAN.md)

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**BYYOUANDIANDAI Team**

- Website: [byyouandiandai.com](#)
- Email: hello@byyouandiandai.com

---

## 🙏 Acknowledgments

- Django documentation
- Bootstrap framework
- Stripe payment platform
- Font Awesome icons
- Google Fonts

---

## 📈 Roadmap

### Upcoming Features
- [ ] Social media login
- [ ] Product comparison
- [ ] Advanced filtering
- [ ] Live chat support
- [ ] Multi-currency support
- [ ] Multi-language support
- [ ] Push notifications
- [ ] Loyalty program
- [ ] Gift cards
- [ ] Product recommendations

---

## 📞 Support

For support, email hello@byyouandiandai.com or open an issue on GitHub.

---

<div align="center">

**Made with ❤️ by BYYOUANDIANDAI**

[Back to Top](#byyouandiandai---luxury-fashion-e-commerce)

</div>
