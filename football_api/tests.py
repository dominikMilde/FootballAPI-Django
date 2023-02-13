from django.contrib.auth.models import User
from rest_framework.test import APITestCase


# TESTS
class TestCountry(APITestCase):
    def test_get_empty_country_list(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_post_country_200(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        data = {
            "name": "Croatia",
            "name_short": "CRO",
            "population": 3892135,
            "currency": "HRK"
        }
        response = self.client.post('/api/country/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name"], "Croatia")

    def test_post_country_400_no_enough_data(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        data = {
            "name": "Croatia",
            "population": 3892135,
            "currency": "HRK"
        }
        response = self.client.post('/api/country/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_country_list_1(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        self.create_croatia()
        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["name_short"], "CRO")

    def test_get_country_list_2(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        self.create_croatia()
        self.create_germany()

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["name_short"], "CRO")
        self.assertEqual(response.json()[1]["name"], "Germany")

    def test_get_country_by_id(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        self.create_croatia()
        self.create_germany()

        response = self.client.get('/api/country/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["name_short"], "CRO")

    def test_get_country_by_id_doestn_exist(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        response = self.client.get('/api/country/1/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "Country doesnt exist")

    def test_put_country(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        self.create_croatia()
        self.create_germany()

        response = self.client.put('/api/country/1/', {
            "name": "Croatia",
            "name_short": "CRO",
            "population": 3892136,
            "currency": "HRK"
        })

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["name_short"], "CRO")
        self.assertEqual(response.json()[0]["population"], 3892136)  # changed
        self.assertEqual(response.json()[1]["name"], "Germany")

    def test_put_country_doesnt_exist(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        self.create_croatia()
        self.create_germany()

        response = self.client.put('/api/country/3/', {
            "name": "Croatia",
            "name_short": "CRO",
            "population": 3892136,
            "currency": "HRK"
        })

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "Country doesnt exist")

    def test_delete_country(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        self.create_croatia()
        self.create_germany()

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)

        response = self.client.delete('/api/country/2/')
        self.assertEqual(response.status_code, 204)

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)  # changed to 1

    # HELPERS
    def create_croatia(self):
        data_cro = {
            "name": "Croatia",
            "name_short": "CRO",
            "population": 3892135,
            "currency": "HRK"
        }
        response = self.client.post('/api/country/', data_cro)

    def create_germany(self):
        data_de = {
            "name": "Germany",
            "name_short": "DE",
            "population": 83130652,
            "currency": "EUR"
        }
        response = self.client.post('/api/country/', data_de)


# TESTS
class TestPlayer(APITestCase):
    def test_get_empty_player_list(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        response = self.client.get('/api/player/list/')
        self.assertEqual(response.json(), [])
        self.assertEqual(response.status_code, 200)

    def test_post_player_200(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        TestCountry.create_croatia(self)

        data = {
            "first_name": "Luka",
            "last_name": "Modrić",
            "d_o_b": "1981-02-24",
            "position": "MID",
            "country": 1
        }
        response = self.client.post('/api/player/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "Luka")

    def test_post_player_400_no_enough_data(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        data = {
            "first_name": "Luka",
            "last_name": "Modrić",
            "d_o_b": "1981-02-24",
        }
        response = self.client.post('/api/player/', data)
        self.assertEqual(response.status_code, 400)

    def test_get_player_list_1(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        TestCountry.create_croatia(self)
        self.create_modric()

        response = self.client.get('/api/player/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["last_name"], "Modrić")
        self.assertEqual(response.json()[0]["country"]["name_short"], "CRO")

    def test_get_player_by_id(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        TestCountry.create_croatia(self)
        TestCountry.create_germany(self)
        self.create_modric()
        self.create_livakovic()
        self.create_neuer()
        response = self.client.get('/api/player/3/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["last_name"], "Neuer")
        self.assertEqual(response.json()["country"]["name_short"], "DE")

    def test_get_player_by_id_doestn_exist(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        response = self.client.get('/api/player/1/')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["error"], "Player doesnt exist")

    def test_put_player(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        TestCountry.create_croatia(self)
        TestCountry.create_germany(self)

        self.create_modric()

        response = self.client.put('/api/player/1/', {
            "first_name": "Luka",
            "last_name": "Modrić",
            "d_o_b": "1981-02-24",
            "position": "FR",
            "country": 2
        })

        response = self.client.get('/api/player/1/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["first_name"], "Luka")
        self.assertEqual(response.json()["position"], "FR")  # changed
        self.assertEqual(response.json()["country"]["name"], "Germany") # changed

    def test_delete_player(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        TestCountry.create_croatia(self)
        TestCountry.create_germany(self)

        self.create_modric()
        self.create_livakovic()
        self.create_neuer()

        response = self.client.get('/api/player/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 3)

        response = self.client.delete('/api/player/2/')
        self.assertEqual(response.status_code, 204)

        response = self.client.get('/api/player/list/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)  # changed to 2

    # HELPERS
    def create_modric(self):
        data_modric = {
            "first_name": "Luka",
            "last_name": "Modrić",
            "d_o_b": "1981-02-24",
            "position": "MID",
            "country": 1
        }
        response = self.client.post('/api/player/', data_modric)

    def create_livakovic(self):
        data_livakovic = {
            "first_name": "Dominik",
            "last_name": "Livaković",
            "d_o_b": "1998-03-21",
            "position": "GK",
            "country": 1
        }
        response = self.client.post('/api/player/', data_livakovic)

    def create_neuer(self):
        data_neuer = {
            "first_name": "Manuel",
            "last_name": "Neuer",
            "d_o_b": "1988-11-21",
            "position": "GK",
            "country": 2
        }
        response = self.client.post('/api/player/', data_neuer)


# TESTS
class TestCountryPlayers(APITestCase):
    def test_get_players_of_country(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        TestCountry.create_croatia(self)
        TestCountry.create_germany(self)

        TestPlayer.create_modric(self)
        TestPlayer.create_livakovic(self)
        TestPlayer.create_neuer(self)

        response = self.client.get('/api/country/1/player/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
        self.assertEqual(response.json()[0]["first_name"], "Luka")
        self.assertEqual(response.json()[1]["first_name"], "Dominik")

        response = self.client.get('/api/country/2/player/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]["first_name"], "Manuel")

    def test_get_players_of_country(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        response = self.client.get('/api/country/1/player/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), [])


# TESTS
class TestAuth(APITestCase):
    def test_get_unauth(self):
        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 403)

    def test_get_players_countries_logged_in_then_logout(self):
        my_admin = User.objects.create_user('dominik', 'myemail@test.com', 'asdfQWER1234!')
        self.client.login(username='dominik', password='asdfQWER1234!')

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 200)

        response = self.client.get('/api/player/list/')
        self.assertEqual(response.status_code, 200)

        self.client.logout()

        response = self.client.get('/api/country/list/')
        self.assertEqual(response.status_code, 403)

        response = self.client.get('/api/player/list/')
        self.assertEqual(response.status_code, 403)




