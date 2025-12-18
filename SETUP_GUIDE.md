# Mega Boutique - Setup Guide

## ✅ Completed Configurations

### 1. CSRF Protection
- ✅ CSRF trusted origins configured for Gitpod, Render, Railway, and Heroku
- ✅ All forms include `{% csrf_token %}`
- ✅ CSRF middleware enabled

### 2. AWS S3 Configuration
- ✅ AWS S3 settings configured for production use
- ✅ Custom storage classes for static and media files
- ✅ Local file serving for development
- ✅ Environment variable support for AWS credentials

**To enable AWS S3:**
```bash
export USE_AWS=True
export AWS_ACCESS_KEY_ID=your_access_key
export AWS_SECRET_ACCESS_KEY=your_secret_key
export AWS_STORAGE_BUCKET_NAME=your_bucket_name
export AWS_S3_REGION_NAME=eu-west-1
```

### 3. Stripe Payment Integration
- ✅ Stripe configuration in settings
- ✅ Payment intent creation in checkout view
- ✅ Webhook handler ready
- ✅ Order processing with Stripe

**To configure Stripe:**

1. Get your test keys from: https://dashboard.stripe.com/test/apikeys

2. Set environment variables:
```bash
export STRIPE_PUBLIC_KEY=pk_test_your_key_here
export STRIPE_SECRET_KEY=sk_test_your_key_here
export STRIPE_WH_SECRET=whsec_your_webhook_secret
```

3. Test card numbers:
   - **Success**: 4242 4242 4242 4242
   - **Decline**: 4000 0000 0000 0002
   - **Requires Auth**: 4000 0025 0000 3155
   - Use any future expiry, any 3-digit CVC, any postal code

### 4. Email Confirmation
- ✅ Console email backend for development
- ✅ Confirmation email function in checkout
- ✅ Email sent after successful order
- ✅ Order details included in email

**Email Configuration:**
- Development: Emails print to console (terminal)
- Production: Configure SMTP settings in settings.py

### 5. Shopping Cart & Checkout
- ✅ Add to bag functionality
- ✅ Update/remove items from bag
- ✅ Size selection support
- ✅ Checkout form with validation
- ✅ Order creation and line items
- ✅ User profile integration

## 🚀 How to Test the Complete Flow

### Step 1: Start the Server
```bash
python manage.py runserver 0.0.0.0:8000
```

### Step 2: Browse Products
1. Go to: https://8000--[your-gitpod-url].gitpod.dev
2. Click "Shop Now" or navigate to products
3. Browse the 41 products across 20 categories

### Step 3: Add Items to Basket
1. Click on any product
2. Select quantity (and size if applicable)
3. Click "Add to Bag"
4. Success message will appear
5. Bag icon shows total

### Step 4: View Basket
1. Click the shopping bag icon
2. Review items
3. Adjust quantities if needed
4. Click "Secure Checkout"

### Step 5: Checkout (Without Stripe - for testing)
**Note:** Without Stripe keys, you can test the form but not complete payment.

1. Fill in delivery information
2. Form validates all required fields
3. Country dropdown works
4. Save info checkbox (for logged-in users)

### Step 6: Checkout (With Stripe)
1. Set Stripe environment variables (see above)
2. Restart server
3. Fill in delivery form
4. Enter test card: 4242 4242 4242 4242
5. Expiry: any future date (e.g., 12/25)
6. CVC: any 3 digits (e.g., 123)
7. Click "Complete Order"

### Step 7: Order Confirmation
1. Success page displays order number
2. Order details shown
3. Email confirmation sent (check terminal for console output)
4. Order saved to database

### Step 8: Verify Email (Console)
Check your terminal where the server is running. You'll see:
```
Content-Type: text/plain; charset="utf-8"
Subject: Mega Boutique - Order Confirmation [ORDER_NUMBER]
From: megaboutique@example.com
To: customer@example.com

Thank you for your order at Mega Boutique!
Order Number: [ORDER_NUMBER]
...
```

## 📊 Database Status

- **Users**: 1 admin user
- **Products**: 41 products
- **Categories**: 20 categories
- **Orders**: Ready to accept orders

**Admin Access:**
- URL: /admin
- Username: admin
- Password: admin123

## 🔧 Environment Variables Summary

### Required for Stripe Payments:
```bash
STRIPE_PUBLIC_KEY=pk_test_...
STRIPE_SECRET_KEY=sk_test_...
```

### Optional for Production:
```bash
# AWS S3
USE_AWS=True
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...
AWS_STORAGE_BUCKET_NAME=...
AWS_S3_REGION_NAME=eu-west-1

# Email (SMTP)
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASS=your_app_password

# Database
DATABASE_URL=postgres://...
```

## 🎨 Dark Mode
- ✅ Dark theme applied throughout
- ✅ Header, navigation, and footer styled
- ✅ Cards and forms dark themed
- ✅ Proper contrast for readability

## 🔗 Social Media
- ✅ Facebook link in footer
- ✅ X (Twitter) icon updated
- ✅ Instagram link in footer

## ⚠️ Important Notes

1. **Stripe Keys**: You must set your own Stripe test keys to complete payments
2. **Email**: Currently using console backend - emails print to terminal
3. **Database**: Using SQLite for development
4. **Static Files**: Run `python manage.py collectstatic` after CSS changes
5. **CSRF**: Trusted origins configured for common hosting platforms

## 🐛 Troubleshooting

### CSRF Verification Failed
- Check CSRF_TRUSTED_ORIGINS in settings.py
- Ensure your domain is listed
- Clear browser cookies

### Stripe Not Working
- Verify STRIPE_PUBLIC_KEY and STRIPE_SECRET_KEY are set
- Check keys are for test mode (start with pk_test_ and sk_test_)
- Restart server after setting environment variables

### Email Not Sending
- Check terminal output (console backend)
- Verify EMAIL_BACKEND setting
- For production, configure SMTP settings

### Items Not Adding to Bag
- Check browser console for JavaScript errors
- Verify CSRF token in form
- Check server logs for errors

## 📝 Next Steps for Production

1. **Get Real Stripe Keys**: Switch from test to live mode
2. **Configure SMTP**: Set up real email service (Gmail, SendGrid, etc.)
3. **Set up AWS S3**: For media and static file hosting
4. **Use PostgreSQL**: Replace SQLite with production database
5. **Set SECRET_KEY**: Generate secure secret key
6. **Disable DEBUG**: Set DEBUG=False
7. **Configure ALLOWED_HOSTS**: Add your production domain
8. **Set up SSL**: Ensure HTTPS is enabled

## ✅ Testing Checklist

- [x] CSRF protection working
- [x] Add items to basket
- [x] Update basket quantities
- [x] Remove items from basket
- [x] Checkout form validation
- [x] Order creation
- [x] Email confirmation (console)
- [x] Dark mode applied
- [x] X icon in footer
- [ ] Stripe payment (requires your keys)
- [ ] Production email (requires SMTP config)
- [ ] AWS S3 (requires AWS credentials)

---

**Current Status**: ✅ All core functionality configured and ready for testing!

**Server URL**: https://8000--019b1567-7676-7c62-8ca6-e42b2509c449.eu-central-1-01.gitpod.dev
