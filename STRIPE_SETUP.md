# 🔐 Stripe Setup - Quick Guide

## Get Your Stripe Test Keys

1. **Sign up/Login to Stripe**: https://dashboard.stripe.com/register
2. **Go to Developers**: https://dashboard.stripe.com/test/apikeys
3. **Copy your keys**:
   - Publishable key (starts with `pk_test_`)
   - Secret key (starts with `sk_test_`)

## Set Environment Variables

### Option 1: Export in Terminal (Temporary)
```bash
export STRIPE_PUBLIC_KEY="pk_test_your_key_here"
export STRIPE_SECRET_KEY="sk_test_your_key_here"
```

### Option 2: Create .env file (Persistent)
```bash
# Create .env file
cat > .env << 'EOF'
STRIPE_PUBLIC_KEY=pk_test_your_key_here
STRIPE_SECRET_KEY=sk_test_your_key_here
EOF

# Load it
source .env
```

### Option 3: Add to .bashrc (Permanent)
```bash
echo 'export STRIPE_PUBLIC_KEY="pk_test_your_key_here"' >> ~/.bashrc
echo 'export STRIPE_SECRET_KEY="sk_test_your_key_here"' >> ~/.bashrc
source ~/.bashrc
```

## Restart Server
```bash
# Kill existing server
pkill -9 -f "python manage.py runserver"

# Start with new environment variables
python manage.py runserver 0.0.0.0:8000
```

## Test Cards

| Purpose | Card Number | Details |
|---------|-------------|---------|
| ✅ Success | 4242 4242 4242 4242 | Any future date, any CVC |
| ❌ Decline | 4000 0000 0000 0002 | Card declined |
| 🔐 Auth Required | 4000 0025 0000 3155 | Requires authentication |
| 💳 Insufficient Funds | 4000 0000 0000 9995 | Insufficient funds |

**For all test cards:**
- Expiry: Any future date (e.g., 12/25)
- CVC: Any 3 digits (e.g., 123)
- Postal Code: Any valid format

## Verify Setup

```bash
# Check if variables are set
echo $STRIPE_PUBLIC_KEY
echo $STRIPE_SECRET_KEY

# Should show your keys starting with pk_test_ and sk_test_
```

## Test the Flow

1. **Add product to basket**
2. **Go to checkout**
3. **Fill in delivery details**
4. **Enter test card**: 4242 4242 4242 4242
5. **Complete order**
6. **Check terminal for confirmation email**

## Troubleshooting

### "Stripe public key is missing"
- Environment variables not set
- Server not restarted after setting variables
- Variables not exported correctly

### Payment fails
- Using wrong card number
- Stripe keys are for live mode (should be test mode)
- Network issues

### No confirmation email
- Check terminal output (console backend)
- Email function may have errors (check server logs)

## Production Setup

When ready for production:

1. **Switch to Live Mode** in Stripe Dashboard
2. **Get Live Keys** (start with `pk_live_` and `sk_live_`)
3. **Set up Webhooks** for payment confirmations
4. **Update environment variables** with live keys
5. **Test thoroughly** with real cards (small amounts)

---

**Quick Start Command:**
```bash
export STRIPE_PUBLIC_KEY="pk_test_YOUR_KEY" && \
export STRIPE_SECRET_KEY="sk_test_YOUR_KEY" && \
python manage.py runserver 0.0.0.0:8000
```

Replace `YOUR_KEY` with your actual Stripe test keys!
