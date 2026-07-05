import tempfile
import unittest
from io import StringIO
from unittest.mock import patch
from fastapi.testclient import TestClient

from main import (
    InputInformation,
    add_contact_from_input,
    app,
    init_database,
    list_contacts,
    populate_sample_data,
    remove_contact_from_input,
    search_contacts_from_input,
)


def sample_contact(**overrides):
    contact = {
        "first_name": "Taylor",
        "middle_initial": "A",
        "last_name": "Morgan",
        "age": 31,
        "date_of_birth": "1995-04-12",
        "email": "taylor.morgan@example.com",
        "favorite_color": "green",
        "pronouns": "they/them",
    }
    contact.update(overrides)
    return contact


class ContactApplicationTests(unittest.TestCase):
    def setUp(self):
        self.original_database_path = app.state.database_path
        self.temp_directory = tempfile.TemporaryDirectory()
        init_database(f"{self.temp_directory.name}/contacts.db")
        self.client = TestClient(app)

    def tearDown(self):
        self.client.close()
        app.state.database_path = self.original_database_path
        self.temp_directory.cleanup()

    def test_input_information_getters_and_setters(self):
        contact = InputInformation(**sample_contact())

        self.assertEqual(contact.get_first_name(), "Taylor")
        self.assertEqual(contact.get_middle_initial(), "A")
        self.assertEqual(contact.get_last_name(), "Morgan")
        self.assertEqual(contact.get_age(), 31)
        self.assertEqual(contact.get_date_of_birth(), "1995-04-12")
        self.assertEqual(contact.get_email(), "taylor.morgan@example.com")
        self.assertEqual(contact.get_favorite_color(), "green")
        self.assertEqual(contact.get_pronouns(), "they/them")

        contact.set_first_name("Jordan")
        contact.set_middle_initial("B")
        contact.set_last_name("Rivera")
        contact.set_age(28)
        contact.set_date_of_birth("1998-09-02")
        contact.set_email("jordan.rivera@example.com")
        contact.set_favorite_color("blue")
        contact.set_pronouns("she/her")

        self.assertEqual(contact.first_name, "Jordan")
        self.assertEqual(contact.middle_initial, "B")
        self.assertEqual(contact.last_name, "Rivera")
        self.assertEqual(contact.age, 28)
        self.assertEqual(contact.date_of_birth, "1998-09-02")
        self.assertEqual(contact.email, "jordan.rivera@example.com")
        self.assertEqual(contact.favorite_color, "blue")
        self.assertEqual(contact.pronouns, "she/her")

    def test_create_print_list_and_search_contacts(self):
        response = self.client.post("/contacts", json=sample_contact())

        self.assertEqual(response.status_code, 201)
        created_contact = response.json()
        self.assertEqual(created_contact["id"], 1)
        self.assertEqual(created_contact["first_name"], "Taylor")

        print_response = self.client.get("/contacts/1")
        self.assertEqual(print_response.status_code, 200)
        self.assertEqual(print_response.json()["email"], "taylor.morgan@example.com")

        list_response = self.client.get("/contacts")
        self.assertEqual(list_response.status_code, 200)
        self.assertEqual(list_response.json(), [created_contact])

        search_response = self.client.get("/contacts/search", params={"q": "green"})
        self.assertEqual(search_response.status_code, 200)
        self.assertEqual(search_response.json(), [created_contact])

    def test_populate_sample_data_adds_twenty_contacts_once(self):
        populate_sample_data()

        contacts = list_contacts()
        self.assertEqual(len(contacts), 20)
        self.assertEqual(len({contact["email"] for contact in contacts}), 20)

        populate_sample_data()
        self.assertEqual(len(list_contacts()), 20)

    def test_update_contact_fields(self):
        self.client.post("/contacts", json=sample_contact())

        response = self.client.put(
            "/contacts/1",
            json={"email": "new.email@example.com", "favorite_color": "purple"},
        )

        self.assertEqual(response.status_code, 200)
        updated_contact = response.json()
        self.assertEqual(updated_contact["email"], "new.email@example.com")
        self.assertEqual(updated_contact["favorite_color"], "purple")
        self.assertEqual(updated_contact["first_name"], "Taylor")

    def test_delete_contact(self):
        self.client.post("/contacts", json=sample_contact())

        response = self.client.delete("/contacts/1")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"message": "Contact deleted"})
        self.assertEqual(self.client.get("/contacts/1").status_code, 404)

    def test_rejects_invalid_contact_data(self):
        response = self.client.post("/contacts", json=sample_contact(middle_initial="AB"))

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()["detail"], "middle_initial must be one character")

    def test_missing_contact_returns_not_found(self):
        response = self.client.delete("/contacts/99")

        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()["detail"], "Contact not found")

    def test_cli_add_contact_validates_input_and_creates_contact(self):
        user_input = [
            "Taylor",
            "AB",
            "A",
            "Morgan",
            "invalid age",
            "31",
            "not-a-date",
            "1995-04-12",
            "invalid-email",
            "taylor.morgan@example.com",
            "green",
            "they/them",
        ]

        with patch("builtins.input", side_effect=user_input), patch("sys.stdout", new_callable=StringIO) as output:
            add_contact_from_input()

        contacts = list_contacts()
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]["email"], "taylor.morgan@example.com")
        self.assertIn("Invalid input: Middle initial must be one character.", output.getvalue())
        self.assertIn("Contact added successfully.", output.getvalue())

    def test_cli_search_and_remove_contact(self):
        self.client.post("/contacts", json=sample_contact())

        with patch("builtins.input", return_value="green"), patch("sys.stdout", new_callable=StringIO) as output:
            search_contacts_from_input()

        self.assertIn("taylor.morgan@example.com", output.getvalue())

        with patch("builtins.input", return_value="1"), patch("sys.stdout", new_callable=StringIO) as output:
            remove_contact_from_input()

        self.assertEqual(list_contacts(), [])
        self.assertIn("Contact removed successfully.", output.getvalue())


if __name__ == "__main__":
    unittest.main()