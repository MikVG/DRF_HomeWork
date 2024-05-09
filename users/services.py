from config.settings import STRIPE_API_KEY

import stripe
stripe.api_key = STRIPE_API_KEY


def create_stripe_product(name):
    """Функция создания продукта в Stripe"""
    product = stripe.Product.create(name=name)
    return product['id']


def create_stripe_price(product_id, amount):
    """Функция создания цены в Stripe"""

    price = stripe.Price.create(
        currency="rub",
        unit_amount=amount * 100,
        product=product_id,
    )
    return price['id']


def create_stripe_session(price_id):
    """Функция создания сессии для оплаты через Stripe"""

    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": price_id, "quantity": 1}],
        mode="payment",
    )
    return session['id'], session['url']
