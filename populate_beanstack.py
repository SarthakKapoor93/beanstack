import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beanstack.settings')
import django
django.setup()
from bean_app.models import CoffeeProduct, ProductReview

# This is obviously just a basic version of the script. It will have to be changed depending on
# the models. But it gives us a starting point anyway.


coffee_products = [
     {
        'name': "BRAZIL DATERRA MASTERPIECES FRANCISCA - COFFEE BEANS",
        'description': "Daterra sets the benchmark for sustainable coffee farming and over its 216 small "
                       "plantations in the Cerrado region they have the perfect growing conditions for speciality "
                       "coffee. Each year our masterful Cuppers search the vast potential of Daterra for unique small "
                       "lots of coffee, Our Masterpieces.",
        'origin': "Brazil",
        'price': 12.50
     },

    {
        'name': "BRAZIL DATERRA SUNRISE - COFFEE BEANS",
        'description': "Grown in Cerrado, Mogiana at an altitude of 1150 metres, this delightful coffee has a"
                       " beautiful creamy milk chocolate and vanilla flavour with a caramel sweetness.  "
                       "It is smooth and well balanced with soft acidity.",
        'origin': "Brazil",
        'price': 5.75
    },

    {
        'name': "EL SALVADOR CERRO LAS RANAS - COFFEE BEANS",
        'description': "Produced by San Antonio Salaverria, Cerro Las Ranas means ‘hill of the frogs’ "
                       "the finca taking its name from a lagoon high in the reserve that is populated by "
                       "thousands of frogs.  Depending on the time of year, you can see them jumping into "
                       "the lagoon. The farm is located between the Apenaca and Ateno mountain ranges at "
                       "an altitude between 1450 and 1780 meters in the region of the Santa Ana volcano, "
                       "El Salvador. The family also own the washing station, Las Cruces.",
        'origin': "El Salvador",
        'price': 5.50
    },

    {
        'name': "COLOMBIA 'EL NOGAL' - COFFEE BEANS",
        'description': "A beautiful aroma of amaretto and honeycomb on grinding with sweet plum notes "
                       "and a soft clementine acidity. A smooth and satisfying cup with depth of body and "
                       "a nutty and balanced flavour.",
        'origin': "Columbia",
        'price': 5.75
    },

    {
        'name': "COLOMBIA GRANJA LA ESPERANZA GEISHA CERRO AZUL - COFFEE BEANS",
        'description': "Owned by the Herrera Family, La Esperanza (meaning hope) in El Valle del "
                       "Cauca, enjoys rich volcanic soils due to its elevated location of 1600-1990m."
                       " The team at Esperanza are dedicated to the science and business of growing quality "
                       "coffee beans and studied the Geisha variety in Boquete, Panama before taking it back to "
                       "grow in Colombia.  It is a relatively low yielding variety but makes up for that in "
                       "flavour and quality.",
        'origin': "Panama",
        'price': 25.00
    },
]

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

reviewer_names = [
    "Mrs B",
    "Phil J",
    "Utku",
    "Andrew P",
    "Valerie W",
    "Ingrid M",
    "Dave",
    "Susan",
    "Maggie",
    "Alpha"
]


def populate():
    # Create the list of coffee objects
    products = []
    for product in coffee_products:
        cp = CoffeeProduct.objects.get_or_create(**product)[0]
        cp.save()
        list.append(cp)

    # Create two reviews for each coffee product
    iterator = 0
    for cp in products:
        kwargs = {
            'coffee_product': cp,
            'description': review_texts[iterator],
            'rating': 5,
            'reviewer': reviewer_names[iterator]
        }
        pr_1 = ProductReview.objects.get_or_create(**kwargs)[0]
        pr_1.save()
        iterator += 1

        kwargs['description'] = review_texts[iterator]
        kwargs['rating'] = 4
        kwargs['reviewer'] = reviewer_names[iterator]
        pr_2 = ProductReview.objects.get_or_create(**kwargs)[0]
        pr_2.save()
        iterator += 1


if __name__ == '__main__':
    print("Stacking on the beans...")
    populate()
    print("All stacked up nice and high.")