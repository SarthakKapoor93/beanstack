import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beanstack.settings')
import django

django.setup()
from bean_app.models import CoffeeBean, Review, Customer, Vendor, Tag


'''
todo:
create a list of twenty tags
create list of coffee beans
create a list of customers

'''

# list of tags

tag_groups = [
            ("sweet", "salt", "mellow"),
            ("acidic", "wine", "sour"),
            ("flowery", "fruity", "herby"),
            ("nutty", "caramel", "chocolate"),
            ("spicy", "honey", "buttery", "bitter"),
            ("pepper", "cedar", "dark chocolate", "roasted peanuts")
    ]

# list of coffee beans

coffee_beans = [
    {
        'name': "BRAZIL DATERRA MASTERPIECES FRANCISCA - COFFEE BEANS",
        'description': "Daterra sets the benchmark for sustainable coffee farming and over its 216 small "
                       "plantations in the Cerrado region they have the perfect growing conditions for speciality "
                       "coffee. Each year our masterful Cuppers search the vast potential of Daterra for unique small "
                       "lots of coffee, Our Masterpieces.",
        'location': "Brazil",
        'price': 12.50,
        'average_rating': 4,
        'tags': tag_groups[0]
    },

    {
        'name': "BRAZIL DATERRA SUNRISE - COFFEE BEANS",
        'description': "Grown in Cerrado, Mogiana at an altitude of 1150 metres, this delightful coffee has a"
                       " beautiful creamy milk chocolate and vanilla flavour with a caramel sweetness.  "
                       "It is smooth and well balanced with soft acidity.",
        'location': "Brazil",
        'price': 5.75,
        'average_rating': 4,
        'tags': tag_groups[1]
    },

    {
        'name': "EL SALVADOR CERRO LAS RANAS - COFFEE BEANS",
        'description': "Produced by San Antonio Salaverria, Cerro Las Ranas means ‘hill of the frogs’ "
                       "the finca taking its name from a lagoon high in the reserve that is populated by "
                       "thousands of frogs.  Depending on the time of year, you can see them jumping into "
                       "the lagoon. The farm is located between the Apenaca and Ateno mountain ranges at "
                       "an altitude between 1450 and 1780 meters in the region of the Santa Ana volcano, "
                       "El Salvador. The family also own the washing station, Las Cruces.",
        'location': "El Salvador",
        'price': 5.50,
        'average_rating': 4,
        'tags': tag_groups[2]
    },

    {
        'name': "COLOMBIA 'EL NOGAL' - COFFEE BEANS",
        'description': "A beautiful aroma of amaretto and honeycomb on grinding with sweet plum notes "
                       "and a soft clementine acidity. A smooth and satisfying cup with depth of body and "
                       "a nutty and balanced flavour.",
        'location': "Columbia",
        'price': 5.75,
        'average_rating': 4,
        'tags': tag_groups[3]
    },

    {
        'name': "COLOMBIA GRANJA LA ESPERANZA GEISHA CERRO AZUL - COFFEE BEANS",
        'description': "Owned by the Herrera Family, La Esperanza (meaning hope) in El Valle del "
                       "Cauca, enjoys rich volcanic soils due to its elevated location of 1600-1990m."
                       " The team at Esperanza are dedicated to the science and business of growing quality "
                       "coffee beans and studied the Geisha variety in Boquete, Panama before taking it back to "
                       "grow in Colombia.  It is a relatively low yielding variety but makes up for that in "
                       "flavour and quality.",
        'location': "Panama",
        'price': 25.00,
        'average_rating': 4,
        'tags': tag_groups[4]
    },
]

names = ["Frank", "Phil J", "Utku", "Andrew P", "Valerie W", "Ingrid M", "Dave", "Susan", "Maggie", "Alpha"]

review_texts = [

    "smooth silky feel and an unforgettable aftertase that stays in your mouth hours and hours "
    "even if you eat something .This roasting style of a geisha coffee is remarkable.The "
    "lingering taste in my opinion is due to higher temperature in the process of roasting which "
    "makes the coffee grindindg so easy when purchased.I can compare and contrast this coffee "
    "JBM(wallenford,jablum) or maybe with luwaks because so easy to drink which never leaves "
    "the unpleasant bitter aftertase 99 % UN specility coffees in the world have.never easy to "
    "find a coffee like this. Congradulations",

    "Absolutely incredible coffee Delicious; smooth, rich and smells amazing. I can see why it’s "
    "the price it is, but it’s definitely worth it.",

    "A real treat thank you.",

    "La Esperanza Geisha is famous. I think TBS use medium roast to show its real potential, which really "
    "surprise me. I underrated this one compared to the La Esmerald Geisha. I use pour-over to brew this coffee "
    "with 89 degree C of water. I would highly recommend this one with its strong sweetness. Even after you finish "
    "it, you can still feel the aroma of honey and mango. Magnificent.",

    "Fab product, fab delivery, fab EVERYTHING thank you",

    "Fantastic coffee as are all the Bean Shop products!!",

    "Came in a lovely box and lovely packaging. The coffee beans were lovely and I will definitely purchase more",

    "Not my choice for the first hit of the day. For a second coffee later in the day I'm loving it. Packed with"
    " flavour and smooth",

    "one of the best beans I have ever tasted, smooth and deep - will order again",

    "Really nice, smooth tasting. Enjoy it very much, long live the bean!!!!",
]

# owner_name = models.CharField(max_length=128)
# email = models.EmailField(unique=True)
# business_name = models.CharField(max_length=128, unique=True)
# # password = models.CharField()
# url_online_shop = models.URLField()
# address = models.CharField(max_length=128)
# # telephone = models.CharField()
# description = models.CharField(max_length=128, blank=True)
# products_in_stock = models.ManyToManyField(CoffeeBean)


def populate():

    print("Creating the beans and the tags...")
    for bean in coffee_beans:
        b = CoffeeBean.objects.get_or_create(name=bean['name'],
                                             description=bean['description'],
                                             location=bean['location'],
                                             price=bean['price'],
                                             average_rating=bean['average_rating'])[0]
        print("\t", b)

        # For each bean, get the tags, create the tags in the database
        # and then add them to the bean.

        for tag in bean['tags']:
            t = Tag.objects.get_or_create(name=tag)[0]
            b.tags.add(t)
            print("\t", t)
        b.save()

    print("Creating the customers and reviews...")
    for i, customer_name in enumerate(names):

        # There are 10 customers and only 5 reviewers, so each coffee gets two reviews
        j = int(i % (len(names) / 2))

        c = Customer.objects.get_or_create(fullname=customer_name,
                                           email=customer_name + "@gmail.com",
                                           favourite_coffee=CoffeeBean.objects.get(name=coffee_beans[j]['name']))[0]
        print("\t", c)

        b = CoffeeBean.objects.get_or_create(name=coffee_beans[j]['name'])[0]

        r = Review.objects.get_or_create(customer=c,
                                         coffee_bean=b,
                                         rating=5,
                                         comment=review_texts[0])[0]
        print("\t", r)

    print("Creating the vendors...")


if __name__ == '__main__':
    print("Stacking up all those lovely beans...")
    populate()
    print("... that's some BeanStack you've got there!")