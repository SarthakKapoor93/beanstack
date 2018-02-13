import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beanstack.settings')
import django

django.setup()
from bean_app.models import CoffeeBean, Review, Customer, Vendor, Tag


tag_groups = [
            ("sweet", "salt", "mellow"),
            ("acidic", "wine", "sour"),
            ("flowery", "fruity", "herby"),
            ("nutty", "caramel", "chocolate"),
            ("spicy", "honey", "buttery", "bitter"),
            ("pepper", "cedar", "dark chocolate", "roasted peanuts")
    ]


names = ["Frank", "Phil J", "Utku", "Andrew P", "Valerie W", "Ingrid M", "Dave", "Susan", "Maggie", "Alpha"]
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

coffee_beans_2 = [

    {
        'name': "TRIGONOMETRY BLEND",
        'description': "These Brazilian and two Ethiopians coffees come together beautifully in this "
                       "blend to give a robust and transparent brew that works as well for espresso as "
                       "it does for a pour over.Brazilian Irmãs Pereira is a high quality focused coffee "
                       "farm lying in the heart of one of Brazil's most recognised and awarded growing areas, "
                       "the Mantiqueira hills. Now in the second generation of ownership since it's planting "
                       "in the 1970s the has been a beacon for quality and sustainability for many years. "
                       "Before being renamed Irmãs Pereira (The Pereira Sisters) to represent the sisters' "
                       "joint management, the farm won several awards in the Cup of Excellence programme under "
                       "it's original name Fazenda do Serrado. The commitment to quality that led to these awards "
                       "continues and the quality produced on the farm represents the very best that Brazil produces.",
        'location': "Brazil",
        'price': 6.27,
        'average_rating': 3,
        'tags': tag_groups[0]
    },

    {
        'name': "TONO COSTA RICA/HONEY",
        'description': "The collective Aguilera family own a number of small farms across the West Valley in "
                       "Costa Rica and process them at their micro-mill.  This particular micro-lot,Toño, is "
                       "Los Robles de Naranjo, north of the family's main base in Naranjo town.  Like the majority "
                       "of the coffee from the Aguileras, this is a yellow honey process where a little water is used "
                       "to assist pulping of the cherries and any additional fermentation is kept to a minimum.  This "
                       "produces an accessible and interesting balance of clarity, sweetness and flavour where "
                       "fermentation and process sit harmoniously with terroir. This particular micro-lot is a Villa "
                       "Sarchi, a bourbon cultivar selected from a natural mutation in the West Valley itself.  "
                       "This example from Finca Toño leads with a dense sweetness as is so often the case with the "
                       "best of the West Valley honey processed coffees. Alongside the sweetness there are a range "
                       "of flavours to be found.  Brewed as a filter sugar cane, fig, honey and dried apricot are the "
                       "dominant flavours.  These are supported by a medium intensity zesty mandarin acidity and more "
                       "subtle characteristics including papaya and red berries. ",
        'location': "Costa Rica",
        'price': 27.50,
        'average_rating': 3,
        'tags': tag_groups[1]
    },

    {
        'name': "NGUGU-INI AB KENYA / WASHED",
        'description': "The Kirinyaga region of the Kenya highlands grows high-quality coffee in the red, "
                       "volcanic soil of Mt. Kenya Ngugu-ini washing station (or Factory) is one of eight that "
                       "form part of the larger  Kibirigwi Cooperative Society.  Other members of this larger "
                       "group include Ragati and Kiangai which have developed a similarly respected name as Nguni-ini "
                       "for producing excellent quality.This Kenya micro-lot has an outstanding taste balance between "
                       "a dense, mouth-filling sweetness and a bold effervescent acidity. Flavours in the brew are "
                       "lead by toffee, candied lenons and honey. Underneath these flavours notes of physalis, "
                       "vanilla and honey assert themselves as the coffee cools.  A syrupy mouthfeel helps enhance "
                       "the sweetness and toffee-like nature of the coffee further.  Look for some phosphoric acid "
                       "too, a classic attribute of Kenyan coffee, that adds intensity and complexity to the lemon "
                       "citrus and apple-like malic acidity. This phosphoric acidity is often very present in coffees "
                       "from this part of Kenya because the plants uptake naturally occurring phosphorus from the "
                       "soils which in turn modifies the taste of coffees once brewed.",
        'location': "Kenya",
        'price': 9.00,
        'average_rating': 3,
        'tags': tag_groups[2]
    },

    {
        'name': "COBBLESTONE V2.5 BLEND",
        'description': "Cobblestone is a fresh, juicy espresso blend with a medium body and harmonious balance of "
                       "caramel sweetness with bright citrus acidity.  It's inspired by the beauty and diversity of "
                       "Latin America, the ever changing landscapes, cultures and people, the seemingly endless "
                       "range of coffee flavours to be found throughout the region, and of course Latin vibrance.  "
                       "Throughout this diversity a constant that harmonises the coffeelands bringing a sense of "
                       "cohesiveness to the region are idyllic rural towns, draped in history with brightly "
                       "painted houses that line ever present cobbled streets",
        'location': "Latin America",
        'price': 7.50,
        'average_rating': 3,
        'tags': tag_groups[3]
    },

    {
        'name': "Decaf Swiss Water Artisan Roast",
        'description': "We use the Swiss Water® decaffeination process for our coffee, a chemical free process"
                       " developed in Switzerland, hence the name, that nowadays takes place in Vancouver.  "
                       "The company are not only world leaders in decaffeination, but also very good in selecting "
                       "green coffee suitable for decaffeination.  This is a skill in itself because the usual rules "
                       "for selecting delicious coffee don't always work when when beans are decaffeinated. The coffee "
                       "we roast is a special selection of the finest Southern Brazilian arabicas. Roasted a little "
                       "fuller to a medium dark roast brings out a rich nuttiness and a sweet molasses like flavour "
                       "that develops during the decaffeination process.",
        'location': "Latin America",
        'price': 7.25,
        'average_rating': 3,
        'tags': tag_groups[4]
    }


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

vendors = [
    {
        'owner_name': "Robert Roaster",
        'business_name': 'Artisan Beans',
        'description': "Conceived in the Highlands, Founded in Glasgow. "
                       "Artisan Beans are Speciality Coffee Shops in "
                       "Glasgow with big heart and eager ambitions.",
        'products': (1, 3),
        'lat': 55.860081,
        'long': -4.254018
    },
    {
        'owner_name': "Kate Cappuccino",
        'business_name': 'Papercup Coffee',
        'description': "Papercup Coffee Company is a specialty coffee roaster "
                       "located in Glasgow, Scotland. We opened in 2012 and our"
                       " motivation was to give folk a place to drink world class "
                       "coffee and get amazing service. Our home is in Glasgow's "
                       "West End where we operate our cafe and our coffee roasting "
                       "facility close by.",
        'products': (2, 4),
        'lat': 55.866500,
        'long': -4.270674
    },
    {
        'owner_name': "Mike Macchiato",
        'business_name': 'Kember and Jones',
        'description': "The doors to K & J were opened on June 4th 2004 by owners "
                       "Claire Jones from Glasgow and Phil Kember from Portsmouth. "
                       "We set up our Fine Food Emporium to provide a destination "
                       "for people to enjoy high quality food to eat and buy.",
        'products': (3, 5),
        'lat': 55.861418,
        'long': -4.253596
    }
]


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

        # There are 10 customers and only 5 coffees, so each coffee gets two reviews
        j = int(i % (len(names) / 2))

        c = Customer.objects.get_or_create(fullname=customer_name,
                                           email=customer_name.replace(' ', '').lower() + "@gmail.com",
                                           favourite_coffee=CoffeeBean.objects.get(name=coffee_beans[j]['name']))[0]
        print("\t", c)

        b = CoffeeBean.objects.get_or_create(name=coffee_beans[j]['name'])[0]

        r = Review.objects.get_or_create(customer=c,
                                         coffee_bean=b,
                                         rating=5,
                                         comment=review_texts[0])[0]
        print("\t", r)

    print("Creating the vendors...")
    for vendor in vendors:
        v = Vendor.objects.get_or_create(owner_name=vendor['owner_name'],
                                         business_name=vendor['business_name'],
                                         email=vendor['owner_name'].replace(' ', '').lower() + "@" + vendor['business_name'].replace(' ', '').lower() + ".com",
                                         description=vendor['description'],
                                         lat=vendor['lat'],
                                         long=vendor['long'])[0]
        start, end = vendor['products']
        for bean in CoffeeBean.objects.all()[start: end + 1]:
            v.products_in_stock.add(bean)
        v.save()
        print("\t", v)


if __name__ == '__main__':
    print("Stacking up all those lovely beans...")
    populate()
    print("... that's some BeanStack you've got there!")