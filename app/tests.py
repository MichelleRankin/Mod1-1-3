from django.test import SimpleTestCase

# Create your tests here.

class TestCloseTo100(SimpleTestCase):
    def test_around_100(self):
        response = self.client.get("/near-hundred/98")
        self.assertContains(response, "True")

    def test_above_100(self):
        response = self.client.get("/near-hundred/109")
        self.assertContains(response, "True")

    def test_above_200(self):
        response = self.client.get("/near-hundred/220")
        self.assertContains(response, "False")


class TestStringSplosion(SimpleTestCase):
    def test_code_word(self):
        response = self.client.get("/string-splosion/Code")
        self.assertContains(response, "CCoCodCode")

    def test_Dog_word(self):
        response = self.client.get("/string-splosion/Dog")
        self.assertContains(response, "DDoDog")

    def test_pizza_word(self):
        response = self.client.get("/string-splosion/Pizza")
        self.assertContains(response, "PPiPizPizzPizza")


class TestCatDog(SimpleTestCase):
    def test_count_dog_cat(self):
        response = self.client.get("/cat-dog/catdogcatcat")
        self.assertContains(response, "False")

    def test_count_cat(self):
        response = self.client.get("/cat-dog/catcatcat")
        self.assertContains(response, "False")

    def test_count_even(self):
        response = self.client.get("/cat-dog/catdog")
        self.assertContains(response, "True")
    


class TestLoneSum(SimpleTestCase):
    def test_count_even(self):
        response = self.client.get("/lone-sum/5/4/5")
        self.assertContains(response, "4")


    def test_count_odd(self):
        response = self.client.get("/lone-sum/3/3/7")
        self.assertContains(response, "7")

    def test_count_same(self):
        response = self.client.get("/lone-sum/4/4/4")
        self.assertContains(response, "0")
