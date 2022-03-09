from flask import render_template, flash, redirect, url_for
from app.product import prod_bp as p
from app.product.models import Product

@p.get("/no/<int:no>")
def show_prod(no):
    #prod = Product.objects.filter(no=no).first_or_404()
    return render_template("prod.html")
