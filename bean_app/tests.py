from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from bean_app.models import UserProfile, CoffeeBean, TagType, Tag, Review


tag_groups = [
        ('sour', 'sweet', 'salt', 'bitter', 'enzymatic', 'sugar', 'browning', 'dry distillation', 'flowery',
         'fruity',),
        ('herby', 'nutty', 'caramel', 'chocolate', 'carbon', 'spicy', 'carbon', 'harsh', 'sharp', 'bland',
         'pungent'),
    ]

coffee_beans = [
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
    ]


def add_test_beans():
    '''
    Create four coffee objects and their tags for testing
    '''
    for bean in coffee_beans:

        # Create the coffee bean and the tags that are associated with it
        b = CoffeeBean.objects.create(name=bean['name'],
                                      description=bean['description'],
                                      location=bean['location'],
                                      price=bean['price'],
                                      average_rating=bean['average_rating'])

        # Create the tags and tag types for the bean
        for tag_name in bean['tags']:
            tag_type = TagType.objects.get_or_create(name=tag_name)[0]
            tag = Tag.objects.get_or_create(tag_type=tag_type,
                                      value=len(tag_name),
                                      coffee_bean=b)[0]
        b.save()


class UserSignupTests(TestCase):

    def test_beanstack_user_has_userprofile(self):
        '''
        Ensure that a beanstack user (non facebook user) has a
        user profile attached when created.
        '''

        # Create the user data
        data = {'username': 'test_user',
                'email': 'test_user@tesing.com',
                'password1': 'password123*',
                'password2': 'password123*'}

        # Submit the new user data
        self.client.post(reverse('registration_register'), data=data)

        # Get the user that was just created
        test_user = User.objects.get(username='test_user')

        # Get the user profile for the user
        profile = UserProfile.objects.get(user=test_user)
        self.assertEqual(test_user.userprofile, profile)

    def test_facebook_user_has_userprofile(self):
        '''
        When a user logs in with facebook, they don't automatically have a user profile object
        associated with their user object. For these users the UserProfile object is created only
        when they access the pages that need it.
        '''
        fb_user = User.objects.create(username='test_user', first_name='Test', last_name='Testing')

        # Login the facebook user
        self.client.force_login(fb_user)

        # Create a coffee bean object in the test database so that we can assess it's page
        add_test_beans()

        # Go to the page (and create the user profile)
        self.client.get('/bean_app/product/ruli-musasa/')

        # Check that the user now has a profile
        self.assertIsNotNone(UserProfile.objects.get(user=fb_user))


class HomePageTests(TestCase):

    def test_successful_load_of_home_page(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)


class AboutPageTests(TestCase):

    def test_successful_load_of_about_page(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)


class BrowsePageTests(TestCase):

    def test_successful_load_of_browse_page(self):
        response = self.client.get(reverse('browse'))
        self.assertEqual(response.status_code, 200)

    def test_user_cant_access_add_review_when_not_logged_in(self):
        add_test_beans()
        response = self.client.get(reverse('browse'))
        self.assertNotContains(response, "Add review")

    def test_user_can_access_add_review_when_logged_in(self):
        # Add some beans so that there will be data on the page
        add_test_beans()
        # Create and log the user in
        user = User.objects.create(username='test_user')
        self.client.force_login(user)
        response = self.client.get(reverse('browse'))
        self.assertContains(response, "Add review")


class ProductPageTests(TestCase):

    def test_successful_load_of_product_page(self):
        add_test_beans()
        response = self.client.get(reverse('product', args=('ruli-musasa',)))
        self.assertEqual(response.status_code, 200)

    def test_user_cant_write_a_review_when_not_logged_in(self):
        add_test_beans()
        response = self.client.get(reverse('product', args=('ruli-musasa',)))
        self.assertNotContains(response, "Add Review")

    def test_user_cant_add_to_beanstack_when_not_logged_in(self):
        add_test_beans()
        response = self.client.get(reverse('product', args=('ruli-musasa',)))
        self.assertNotContains(response, "Add to my BeanStack")

    def test_user_can_write_review_when_logged_in(self):
        add_test_beans()
        user = User.objects.create(username='test_user')
        self.client.force_login(user)
        response = self.client.get(reverse('product', args=('ruli-musasa',)))
        self.assertContains(response, "Add Review")

    def test_user_can_add_to_beanstack_when_logged_in(self):
        add_test_beans()
        user = User.objects.create(username='test_user')
        self.client.force_login(user)
        response = self.client.get(reverse('product', args=('ruli-musasa',)))
        self.assertContains(response, "Add to my BeanStack")

    def test_user_cant_make_two_reviews_for_one_coffee(self):
        add_test_beans()
        user = User.objects.create(username='test_user')
        self.client.force_login(user)

        bean = CoffeeBean.objects.get(slug='ruli-musasa')

        data = {'coffee-bean': 'ruli-musasa',
                'comment': "This is a test review",
                'rating': 5}

        response = self.client.post(reverse('product', args=('ruli-musasa',)), data=data)
        self.assertEqual(response.status_code, 200)
        response = self.client.post(reverse('product', args=('ruli-musasa',)), data=data)
        self.assertEqual(response.status_code, 200)
        # How many reviews from this user for this coffee are in the database?
        reviews = Review.objects.filter(user=user, coffee_bean=bean)
        self.assertEqual(len(reviews), 1)


class SearchPageResults(TestCase):

    def test_search_for_tag(self):
        '''
        Ensure that the search for tag works
        '''
        add_test_beans()
        response = self.client.get(reverse('search') + '?q=sweet')
        self.assertEqual(len(response.context['beans']), 3)

    def test_search_for_location(self):
        '''
        Ensure that the search for location works
        '''
        add_test_beans()
        response = self.client.get(reverse('search') + '?q=brazil')
        self.assertEqual(len(response.context['beans']), 3)

    def test_search_for_tag_and_location(self):
        '''
        Ensure that the search for the two tags returns four results
        '''
        add_test_beans()
        response = self.client.get(reverse('search') + '?q=brazil+sweet')
        self.assertEqual(len(response.context['beans']), 4)

    def test_unsuccessful_search(self):
        '''
        Ensure that search with no results returns nothing
        '''
        add_test_beans()
        response = self.client.get(reverse('search') + '?q=nothing')
        self.assertEqual(len(response.context['beans']), 0)

    def test_search_for_empty_query_string(self):
        '''
        Ensure that a search for an empty query string results all the
        coffees in the database
        '''
        add_test_beans()
        response = self.client.get(reverse('search') + '?q=')
        self.assertEqual(len(response.context['beans']), 4)
