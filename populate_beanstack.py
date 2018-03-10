import os

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'beanstack.settings')
import django

django.setup()
from bean_app.models import CoffeeBean, Review, Vendor, TagType, Tag, UserProfile
from django.contrib.auth.models import User

tag_groups = [
    ('sour', 'sweet', 'salt', 'bitter', 'enzymatic', 'sugar', 'browning', 'dry distillation', 'flowery', 'fruity',),
    ('herby', 'nutty', 'caramel', 'chocolate', 'carbon', 'spicy', 'carbon', 'harsh', 'sharp', 'bland', 'pungent'),
    ('mellow', 'acid', 'wine', 'sour', 'floral', 'fragrant', 'citrus', 'berry-like', 'leguminous', 'nut', 'malt', 'candy'),
    ('syrup', 'vanilla', 'turpin', 'medicinal', 'warming', 'smokey', 'ashey', 'rough', 'neutral', 'soft', 'delicate'),
    ('mild', 'nippy', 'piquant', 'tangy', 'tart', 'hard', 'acrid', 'coffee blossom', 'tea rose', 'cardamon', 'caraway'),
    ('coriander seeds', 'lemon', 'apple', 'apricot', 'black berry', 'onion', 'garlic', 'cucumber', 'garden peas')
]
extra_tags = [
    'roasted peanuts', 'walnuts', 'balsamic rice', 'toast', 'roasted hazelnut', 'roasted almond', 'honey', 'maple',
    'syrup', 'dark chocolate', 'swiss chocolate', 'butter', 'pine', 'black-current', 'cedar', 'pepper', 'clove',
    'thyme', 'pipe tobacco', 'burnt', 'charred'
]
names = ["Frank", "Phil J", "Utku", "Andrew P", "Valerie W", "Ingrid M", "Dave", "Susan", "Maggie", "Alpha",
         "John", "Paul", "George", "Ringo", "Samantha"]

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

    "The quality of the packaging speaks volumes about the company's obvious focus on producing the very best coffees, "
    "like this. First rate product & service",

    "First rate coffee, good price and rapid delivery. What's not to like?",

    "Delicious all-round blend on sweeter and milder side of an italian roast. An ideal Latte coffee, but an "
    "interesting espresso also.",

    "Been drinking this blend all my adult life and the day I no longer want to, it's game over. "
    "Life is way too short to drink bad coffee.",

    "Perfect for anytime of the day. A 5 star cup of coffee.",

    "Excellent ! My husband used to bring some home every week when he was at Caledonian University. "
    "Moved away from area and discovered the town centre shop had closed during a return visit. "
    "Found the website though and ordered up supplies. Tastes even better than I remembered. "
    "Ordered a few other to taste. Will let you know once I've tried them ! Thanks.",

    "All varieties excellent - will purchase again.",

    "Delicious and smooth coffee with low acidity. You can drink it all day and I do!",

    "IT IS VERY EASY TO MAKE THIS COFFEE AS SUCH A GOOD BLEND, THERE'S NO BITTERNESS. VERY LOW ACIDITY SO SWEET "
    "AND MELLOW TASTE. UNECONOMICAL, AS YOU CAN DRINK IT ALL DAY !",

    "great coffee and perfect service."

    "I would thank you for your very efficient delivery of the coffee. Ordered oh Monday and delivered on "
    "Tuesday. My wife is the coffee drinker in the house and has been buying your coffee for a long number of "
    "years. When your shop closed in the town I purchased a large supply which has now run out and I thought we would "
    "try the online shop. It is great to know I can now get my supplies from you on line. My coffee loving guests over "
    "Christmas will all be enjoying your coffee.",

    "We have tried other blends( and even other providers) but Thomsons half & half does it for us."
    "My wife thinks I'm Superman for using the espresso machine, when its Thomsons who should take the "
    "credit for a superb all-day coffee.",

    "A good base as a double shot in a large cappuccino.MID roasted with little aftertaste. Personally "
    "I prefer their Italian roast.It is more like the authentic Italian coffee with that fine aftertaste and "
    "chocolate body.Both are great.It's a matter of what style you prefer.",

    "A great medium tasting coffee that could soon become your everyday favourite.The blend of beans and roast "
    "means that this coffee would be forgiving to any brew method you care to throw at it. It's flavour profile is "
    "not as pronounced as other roasts here, and you do get hints of chocolate coming through. As a softer flavour "
    "it doesn't leave a strong after taste.If Tiger Stripe is too strident for you, and the Colombian Light"
    " too floral for you, this one might just be the coffee you are looking for.",

    "Brilliant swift delivery. Haslf & half has a mature ripeness that I found quite sumptuous!",

    "First had this coffee and holiday and have ordered it twice subsequently- best coffee I’ve ever tasted",

    "First of all, we were impressed with the packing and the speed of delivery. We bought Blue Mountain blend "
    "and a decaffeinated coffee, and I would happily recommend both to friends. Thank you for your prompt and "
    "easy service.",

    "Have been buying coffee from Thomsons for over 25years, quality of coffee superb.",

    "This coffee is exceptionally good. I had bought a Mormora from another roaster and wanted to buy more, but was "
    "sold out. Luckily I found Mormora at Thomsons and wasn't disappointed. This has such a wonderful aroma, akin to"
    " strawberry candy floss, it's an absolutely delight.",

    "Superb Coffee - creamy, plenty of body - delicious any time of the day!! This is my 3rd purchase of this coffee"
    " - 12 kgs in all - MUST BE GOOD!!",

    "Best F*@king coffee I've ever tasted!! 4 stars"
]

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
    },

    {
        'name': "RULI MUSASA",
        'description': "We have returned to the west of Rwanda this season, and are very happy to once again "
                       "have a truly delicious coffee from the Ruli Musasa washing station, owned by the Dukunde"
                       " Kawa co-operative.  Dukunde Kawa run three washing stations in the Gakenke District serving "
                       "around two thousand farmers in total.  Ruli Musasa is the most southerly of these, perched at "
                       "the dizzying height of 1999 metres above sea level and over looking the coffee trees "
                       "surrounding it.   The local farmers, of which nine hundred deliver their coffee to Ruli "
                       "Musasa on average own around a quarter of an acre of land on which they may grow up to three "
                       "hundred coffee trees.  ",
        'location': "Rwanda",
        'price': 7.50,
        'average_rating': 1,
        'tags': tag_groups[0]
    },

    {
        'name': "SAN AUGUSTIN",
        'description': "The city of Antigua in Guatemala is one of the most stunning coffee growing regions "
                       "in world to visit, and the coffee has built an enviable reputation for excellent quality "
                       "over many many years. The city itself is steeped in the history of the old Central American "
                       "colonial capital and still retains a unique mix of Spanish and Mayan culture. If you look up "
                       "from the criss-cross of cobbled streets Antigua’s unique geography that defines the coffee "
                       "from the micro-region is inescapable. Three vast volcanoes, Fuego, Agua, and Acetenango "
                       "form a ring around the region and their shelter provides a cool and dry micro-climate perfect "
                       "for coffee growing. The edge of the city merges seamlessly with the surrounding coffee "
                       "farms which rise up onto the lower slopes of the volcanoes to heights of around 1900m above "
                       "sea level.  ",
        'location': "Guatemala",
        'price': 7.50,
        'average_rating': 2,
        'tags': tag_groups[1]
    },

    {
        'name': "CETEC",
        'description': "CETEC is a quirkily-named and high-quality-focused coffee farm in the heart of Brazil's main "
                       "coffee production state, Minas Gerias. CETEC stands for 'Center of Technology of the City of "
                       "Lavras' which sheds light both on the unusual story behind the farm and the goals of its owner "
                       "and his late brother. Márcio Custódio set up a school called CETEC with his brother Izonel "
                       "Junior a decade ago; since then, it has trained over 5000 students in work-related technical "
                       "skills. The brothers then turned to coffee farming (an ever-present career in Minas Gerias) "
                       "and bought a medium sized farm.  After Izonel died suddenly his brother named the farm in "
                       "honour of the school they had started together.  CETEC is now beginning to get recognition for"
                       " accessible, full-flavoured, high-quality coffee, and its success serves as a tribute to the"
                       " memory of Izonel.",
        'location': "Guatemala",
        'price': 7.50,
        'average_rating': 3,
        'tags': tag_groups[2]
    },

    {
        'name': "JASZOON",
        'description': "Our house blend Janzsoon has been around since we first started and has remained one of our "
                       "most popular coffees til this day. It's big, full-bodied and syrupy sweet. it's a perfect "
                       "coffee for pulling espressos at home or for a really punchy filter to get you going in the "
                       "morning. It's comprised of exquisite high altitude  Arabica beans  roasted to two distinct "
                       "profiles, the main bean in the blend is a wet hulled Northern Sumatran from the Aceh Province."
                       "  The Sumatran bean gives the blend the deep chocolate bass notes and heady tropical fruit "
                       "notes. This Sumatran bean just bursts through milk and is a great base espresso. The semi "
                       "washed Brazilian bean from the Minas Gerais gives the blend a bright citric snap and red "
                       "fruit note. This really comes through when served as a clean espresso or long black."
                       "Together, these beans complement each other and the result is a balanced, syrupy espresso "
                       "with massive chocolate notes, bright fruity finish and a wonderful crema.",
        'location': "Guatemala",
        'price': 5.80,
        'average_rating': 4,
        'tags': tag_groups[3]
    },

    {
        'name': "MUSASA MBILIMA A1 RED BOURBON ESPRESSO",
        'description': "The Musasa Dukunde Kawa cooperative has three washing stations lying high in "
                       "Rwanda’s rugged northwest. Mbilima – the cooperative’s second washing station - "
                       "was built by the co-op in 2005 with profits earned from their first washing station, "
                       "Ruli, constructed only two years prior. Constructed at a vertiginous 2,020 metres above sea "
                       "level, it is one of Rwanda’s highest washing stations.",
        'location': "Rwanda",
        'price': 9.50,
        'average_rating': 4,
        'tags': tag_groups[3]
    },
]

vendors = [
    {
        'owner_name': "Robert Roaster",
        'business_name': 'Artisan Roast',
        'description': "Conceived in the Highlands, Founded in Glasgow. "
                       "Artisan Roast are Speciality Coffee Shops in "
                       "Glasgow with big heart and eager ambitions.",
        'url_online_shop': "https://www.artisanroast.co.uk/",
        'products': (0, 15),
        'address': "Unit 252 254 Byres Road Glasgow"
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
        'url_online_shop': "http://www.papercupcoffee.co.uk/",
        'products': (5, 10),
        'address': "9 Exchange Place Glasgow"
    },
    {
        'owner_name': "Mike Macchiato",
        'business_name': 'Kember and Jones',
        'description': "The doors to K & J were opened on June 4th 2004 by owners "
                       "Claire Jones from Glasgow and Phil Kember from Portsmouth. "
                       "We set up our Fine Food Emporium to provide a destination "
                       "for people to enjoy high quality food to eat and buy.",
        'url_online_shop': "http://www.kemberandjones.co.uk/",
        'products': (1, 8),
        'address': "136-140 Buchanan Street Glasgow"
    },

    {
        'owner_name': "Linda Latte",
        'business_name': "Thompson's Coffee",
        'description': "At Thomson’s we are proud to be an independently-owned Scottish family "
                       "business with a rich heritage. Quality and integrity are at the heart of "
                       "everything we do, and since taking the reins we have pursued the same pioneering "
                       "spirit that our founder David Thomson instilled when he opened his first shop in "
                       "Glasgow all those years ago.",
        'url_online_shop': "https://www.thomsonscoffee.com/",
        'products': (13, 15),
        'address': "City Centre, Buchanan Street Buchanan Galleries Buchanan Street"
    },

    {
        'owner_name': "Armando Americano",
        'business_name': "Williams and Johnson",
        'description': "We are a micro roastery established in 2016 by couple of geeks who know coffee. "
                       "Our passion is in sharing beautiful coffees. We think coffee is a very special "
                       "treat and that every cup should be worth it. It's a pleasure for us to taste heaps "
                       "of new harvest coffees from around the globe and build our offering out of only exceptional "
                       "coffees, produced by people who really care. We love for coffee to be at its best and want "
                       "it to be appreciated as the delicious treat that it is. Grab a bag in our online store or "
                       "visit us at;",
        'url_online_shop': "https://www.williamsandjohnson.com/",
        'products': (3, 15),
        'address': "City Centre 58 West Nile Street Glasgow"
    }
]


def populate_main_models(reviews):
    for bean, customer_name, review in zip(coffee_beans, names, reviews):

        # Create the coffee bean and the tags that are associated with it
        b = CoffeeBean.objects.get_or_create(name=bean['name'],
                                             description=bean['description'],
                                             location=bean['location'],
                                             price=bean['price'],
                                             average_rating=bean['average_rating'])[0]

        # Create the tags and tag types for the bean
        for tag_name in bean['tags']:
            tag_type = TagType.objects.get_or_create(name=tag_name)[0]
            tag = Tag.objects.get_or_create(tag_type=tag_type,
                                            value=len(tag_name),
                                            coffee_bean=b)[0]
            # b.tags.add(tag)
        b.save()

        # for tag in bean['tags']:
        #     t = Tag.objects.get_or_create(name=tag)[0]
        #     b.tags.add(t)
        # b.save()

        # Now create the customer
        # c = Customer.objects.get_or_create(fullname=customer_name,
        #                                    email=customer_name.replace(' ', '').lower() + "@gmail.com",
        #                                    favourite_coffee=b)[0]

        u = User.objects.get_or_create(username=customer_name,
                                       email=customer_name.replace(' ', '').lower() + "@gmail.com",
                                       password='password123')[0]
        # Create the user profile
        up = UserProfile.objects.get_or_create(user=u)[0]

        # And the review
        r = Review.objects.get_or_create(user=u,
                                         coffee_bean=b,
                                         rating=5,
                                         comment=review)[0]


def populate_vendors():
    for vendor in vendors:
        v = Vendor.objects.get_or_create(owner_name=vendor['owner_name'],
                                         business_name=vendor['business_name'],
                                         email=vendor['owner_name'].replace(' ', '').lower() + "@" + vendor[
                                             'business_name'].replace(' ', '').lower() + ".com",
                                         description=vendor['description'],
                                         url_online_shop=vendor['url_online_shop'],
                                         address=vendor['address'])[0]
        start, end = vendor['products']
        for bean in CoffeeBean.objects.all()[start: end + 1]:
            v.products_in_stock.add(bean)
        v.save()


def populate_extra_tag_types():
    # The extra tags were not needed to be associated with any particular coffee
    # but it is probably good to have them in the system anyway. If we give the
    # user the option to add tags to a coffee, then they have a much bigger choice
    for tag in extra_tags:
        TagType.objects.get_or_create(name=tag)


if __name__ == "__main__":
    print("Stacking up the beans....")
    populate_main_models(review_texts[:15])
    names = names[::-1]
    populate_main_models(review_texts[15:])
    populate_extra_tag_types()
    print("Populating vendors may take a few seconds because the script accesses Googlemaps' geocoding api ...")
    populate_vendors()
    print("... beans all stacked up nice and high!")

