<h1 align="center" id="title">Online Shop</h1>

<p id="description">Daimond store with payment gateway(Stripe) and internationalization support on en/ru</p>

<h2>🛠️ Installation Steps:</h2>

<p>1. Clone repository</p>

```
git clone https://github.com/vsmrnw/online_shop.git
```

<p>2. Fill .env file you can take most of the data from .env.example except data below</p>

```
SECRET_KEY=
STRIPE_PUBLISHABLE_KEY=
STRIPE_SECRET_KEY=
STRIPE_WEBHOOK_SECRET=
EMAIL_HOST_USER=
EMAIL_HOST_PASSWORD=
ADMINS=
# For local deploment change .prod = .local
DJANGO_SETTINGS_MODULE=conf.settings.prod
```

<p>3. Build image</p>

```
docker compose build
```

<p>4. Run Compose</p>

```
docker compose up
```

<h2>🛡️ License:</h2>

This project is licensed under the Apache-2.0 license
