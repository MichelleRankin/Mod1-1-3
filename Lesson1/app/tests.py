from django.test import SimpleTestCase

# Create your tests here.
class TestHelloView(SimpleTestCase):
    def test_hello_nate(self):
        response = self.client.get("/hello/nate/")
        self.assertContains(response, "Hello nate")


    def test_hello_world(self):
        response = self.client.get("/hello/world/")
        self.assertContains(response, "Hello world")


class TestAgeView(SimpleTestCase):
    def test_add_1_to_4(self):
        response = self.client.get("/age-in/2500/2431/")
        self.assertContains(response, "69")


class TestOrderTotal(SimpleTestCase):
    def test_3_4_5(self):
        response = self.client.get("/order-total/3/4/5")
        self.assertContains(response, "24")