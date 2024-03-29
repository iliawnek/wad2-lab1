import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango-with-django.settings')
django.setup()

from rango.models import Category, Page


def populate():
    python_cat = add_cat(name="Python",
                         likes=64333,
                         views=1282571)

    add_page(cat=python_cat,
             title="Official Python Tutorial",
             url="http://docs.python.org/2/tutorial/")

    add_page(cat=python_cat,
             title="How to Think like a Computer Scientist",
             url="http://www.greenteapress.com/thinkpython/")

    add_page(cat=python_cat,
             title="Learn Python in 10 Minutes",
             url="http://www.korokithakis.net/tutorials/python/")

    django_cat = add_cat(name="Django",
                         likes=32212,
                         views=254754)

    add_page(cat=django_cat,
             title="Official Django Tutorial",
             url="https://docs.djangoproject.com/en/1.5/intro/tutorial01/")

    add_page(cat=django_cat,
             title="Django Rocks",
             url="http://www.djangorocks.com/")

    add_page(cat=django_cat,
             title="How to Tango with Django",
             url="http://www.tangowithdjango.com/")

    frame_cat = add_cat(name="Other Frameworks",
                        likes=165123,
                        views=322456)

    add_page(cat=frame_cat,
             title="Bottle",
             url="http://bottlepy.org/docs/dev/")

    add_page(cat=frame_cat,
             title="Flask",
             url="http://flask.pocoo.org")

    cat_cat = add_cat(name="Cats",
                      likes=10,
                      views=11)

    # Print out what we have added to the user.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print "- {0} - {1}".format(str(c), str(p))


def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url = url
    p.views = views
    p.save()
    return p


def add_cat(name, likes, views):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes = likes
    c.views = views
    c.save()
    return c


# Start execution here!
if __name__ == '__main__':
    print "Starting Rango population script..."
    populate()
