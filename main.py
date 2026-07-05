import os
import sqlite3
from datetime import date
from typing import Any, Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field


DEFAULT_DATABASE_PATH = os.environ.get("CONTACTS_DATABASE_PATH", "contacts.db")

app = FastAPI(title="Contact Management Application")
app.state.database_path = DEFAULT_DATABASE_PATH


class InputInformation:
    def __init__(
        self,
        first_name: str,
        middle_initial: str,
        last_name: str,
        age: int,
        date_of_birth: str,
        email: str,
        favorite_color: str,
        pronouns: str,
    ):
        self.set_first_name(first_name)
        self.set_middle_initial(middle_initial)
        self.set_last_name(last_name)
        self.set_age(age)
        self.set_date_of_birth(date_of_birth)
        self.set_email(email)
        self.set_favorite_color(favorite_color)
        self.set_pronouns(pronouns)

    def get_first_name(self) -> str:
        return self._first_name

    def set_first_name(self, first_name: str) -> None:
        self._first_name = first_name

    def get_middle_initial(self) -> str:
        return self._middle_initial

    def set_middle_initial(self, middle_initial: str) -> None:
        self._middle_initial = middle_initial

    def get_last_name(self) -> str:
        return self._last_name

    def set_last_name(self, last_name: str) -> None:
        self._last_name = last_name

    def get_age(self) -> int:
        return self._age

    def set_age(self, age: int) -> None:
        self._age = age

    def get_date_of_birth(self) -> str:
        return self._date_of_birth

    def set_date_of_birth(self, date_of_birth: str) -> None:
        self._date_of_birth = date_of_birth

    def get_email(self) -> str:
        return self._email

    def set_email(self, email: str) -> None:
        self._email = email

    def get_favorite_color(self) -> str:
        return self._favorite_color

    def set_favorite_color(self, favorite_color: str) -> None:
        self._favorite_color = favorite_color

    def get_pronouns(self) -> str:
        return self._pronouns

    def set_pronouns(self, pronouns: str) -> None:
        self._pronouns = pronouns

    @property
    def first_name(self) -> str:
        return self.get_first_name()

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        self.set_first_name(first_name)

    @property
    def middle_initial(self) -> str:
        return self.get_middle_initial()

    @middle_initial.setter
    def middle_initial(self, middle_initial: str) -> None:
        self.set_middle_initial(middle_initial)

    @property
    def last_name(self) -> str:
        return self.get_last_name()

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        self.set_last_name(last_name)

    @property
    def age(self) -> int:
        return self.get_age()

    @age.setter
    def age(self, age: int) -> None:
        self.set_age(age)

    @property
    def date_of_birth(self) -> str:
        return self.get_date_of_birth()

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: str) -> None:
        self.set_date_of_birth(date_of_birth)

    @property
    def email(self) -> str:
        return self.get_email()

    @email.setter
    def email(self, email: str) -> None:
        self.set_email(email)

    @property
    def favorite_color(self) -> str:
        return self.get_favorite_color()

    @favorite_color.setter
    def favorite_color(self, favorite_color: str) -> None:
        self.set_favorite_color(favorite_color)

    @property
    def pronouns(self) -> str:
        return self.get_pronouns()

    @pronouns.setter
    def pronouns(self, pronouns: str) -> None:
        self.set_pronouns(pronouns)

    def to_dict(self) -> dict[str, Any]:
        return {
            "first_name": self.first_name,
            "middle_initial": self.middle_initial,
            "last_name": self.last_name,
            "age": self.age,
            "date_of_birth": self.date_of_birth,
            "email": self.email,
            "favorite_color": self.favorite_color,
            "pronouns": self.pronouns,
        }


class ContactCreate(BaseModel):
    first_name: str
    middle_initial: str
    last_name: str
    age: int = Field(..., ge=0)
    date_of_birth: str
    email: str
    favorite_color: str
    pronouns: str


class ContactUpdate(BaseModel):
    first_name: Optional[str] = None
    middle_initial: Optional[str] = None
    last_name: Optional[str] = None
    age: Optional[int] = Field(default=None, ge=0)
    date_of_birth: Optional[str] = None
    email: Optional[str] = None
    favorite_color: Optional[str] = None
    pronouns: Optional[str] = None


SAMPLE_CONTACTS = [
    {
        "first_name": "Taylor",
        "middle_initial": "A",
        "last_name": "Morgan",
        "age": 31,
        "date_of_birth": "1995-04-12",
        "email": "taylor.morgan@example.com",
        "favorite_color": "green",
        "pronouns": "they/them",
    },
    {
        "first_name": "Jordan",
        "middle_initial": "B",
        "last_name": "Rivera",
        "age": 28,
        "date_of_birth": "1998-09-02",
        "email": "jordan.rivera@example.com",
        "favorite_color": "blue",
        "pronouns": "she/her",
    },
    {
        "first_name": "Casey",
        "middle_initial": "C",
        "last_name": "Patel",
        "age": 42,
        "date_of_birth": "1983-01-21",
        "email": "casey.patel@example.com",
        "favorite_color": "purple",
        "pronouns": "he/him",
    },
    {
        "first_name": "Riley",
        "middle_initial": "D",
        "last_name": "Nguyen",
        "age": 35,
        "date_of_birth": "1990-06-15",
        "email": "riley.nguyen@example.com",
        "favorite_color": "red",
        "pronouns": "they/them",
    },
    {
        "first_name": "Avery",
        "middle_initial": "E",
        "last_name": "Johnson",
        "age": 24,
        "date_of_birth": "2001-03-08",
        "email": "avery.johnson@example.com",
        "favorite_color": "yellow",
        "pronouns": "she/her",
    },
    {
        "first_name": "Quinn",
        "middle_initial": "F",
        "last_name": "Brooks",
        "age": 39,
        "date_of_birth": "1986-11-30",
        "email": "quinn.brooks@example.com",
        "favorite_color": "orange",
        "pronouns": "he/him",
    },
    {
        "first_name": "Skyler",
        "middle_initial": "G",
        "last_name": "Chen",
        "age": 27,
        "date_of_birth": "1998-02-17",
        "email": "skyler.chen@example.com",
        "favorite_color": "teal",
        "pronouns": "they/them",
    },
    {
        "first_name": "Morgan",
        "middle_initial": "H",
        "last_name": "Garcia",
        "age": 45,
        "date_of_birth": "1980-07-04",
        "email": "morgan.garcia@example.com",
        "favorite_color": "black",
        "pronouns": "she/her",
    },
    {
        "first_name": "Jamie",
        "middle_initial": "I",
        "last_name": "Williams",
        "age": 33,
        "date_of_birth": "1992-12-19",
        "email": "jamie.williams@example.com",
        "favorite_color": "white",
        "pronouns": "he/him",
    },
    {
        "first_name": "Alex",
        "middle_initial": "J",
        "last_name": "Smith",
        "age": 29,
        "date_of_birth": "1996-05-23",
        "email": "alex.smith@example.com",
        "favorite_color": "silver",
        "pronouns": "they/them",
    },
    {
        "first_name": "Sam",
        "middle_initial": "K",
        "last_name": "Brown",
        "age": 50,
        "date_of_birth": "1975-10-09",
        "email": "sam.brown@example.com",
        "favorite_color": "gold",
        "pronouns": "he/him",
    },
    {
        "first_name": "Drew",
        "middle_initial": "L",
        "last_name": "Davis",
        "age": 22,
        "date_of_birth": "2003-08-14",
        "email": "drew.davis@example.com",
        "favorite_color": "pink",
        "pronouns": "she/her",
    },
    {
        "first_name": "Charlie",
        "middle_initial": "M",
        "last_name": "Miller",
        "age": 37,
        "date_of_birth": "1988-04-03",
        "email": "charlie.miller@example.com",
        "favorite_color": "navy",
        "pronouns": "they/them",
    },
    {
        "first_name": "Emerson",
        "middle_initial": "N",
        "last_name": "Wilson",
        "age": 41,
        "date_of_birth": "1984-09-27",
        "email": "emerson.wilson@example.com",
        "favorite_color": "maroon",
        "pronouns": "she/her",
    },
    {
        "first_name": "Finley",
        "middle_initial": "O",
        "last_name": "Moore",
        "age": 26,
        "date_of_birth": "1999-01-05",
        "email": "finley.moore@example.com",
        "favorite_color": "gray",
        "pronouns": "he/him",
    },
    {
        "first_name": "Harper",
        "middle_initial": "P",
        "last_name": "Taylor",
        "age": 30,
        "date_of_birth": "1995-11-11",
        "email": "harper.taylor@example.com",
        "favorite_color": "violet",
        "pronouns": "they/them",
    },
    {
        "first_name": "Reese",
        "middle_initial": "Q",
        "last_name": "Anderson",
        "age": 34,
        "date_of_birth": "1991-06-01",
        "email": "reese.anderson@example.com",
        "favorite_color": "cyan",
        "pronouns": "she/her",
    },
    {
        "first_name": "Rowan",
        "middle_initial": "R",
        "last_name": "Thomas",
        "age": 47,
        "date_of_birth": "1978-03-18",
        "email": "rowan.thomas@example.com",
        "favorite_color": "lime",
        "pronouns": "he/him",
    },
    {
        "first_name": "Sage",
        "middle_initial": "S",
        "last_name": "Martinez",
        "age": 25,
        "date_of_birth": "2000-12-02",
        "email": "sage.martinez@example.com",
        "favorite_color": "indigo",
        "pronouns": "they/them",
    },
    {
        "first_name": "Parker",
        "middle_initial": "T",
        "last_name": "Lee",
        "age": 36,
        "date_of_birth": "1989-07-29",
        "email": "parker.lee@example.com",
        "favorite_color": "brown",
        "pronouns": "she/her",
    },
]


def get_database_path() -> str:
    return app.state.database_path


def get_connection() -> sqlite3.Connection:
    connection = sqlite3.connect(get_database_path())
    connection.row_factory = sqlite3.Row
    return connection


def init_database(database_path: Optional[str] = None) -> None:
    if database_path is not None:
        app.state.database_path = database_path

    with get_connection() as connection:
        connection.execute(
            """
            CREATE TABLE IF NOT EXISTS contacts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                first_name TEXT NOT NULL,
                middle_initial TEXT NOT NULL,
                last_name TEXT NOT NULL,
                age INTEGER NOT NULL,
                date_of_birth TEXT NOT NULL,
                email TEXT NOT NULL,
                favorite_color TEXT NOT NULL,
                pronouns TEXT NOT NULL
            )
            """
        )


def populate_sample_data() -> None:
    for contact_data in SAMPLE_CONTACTS:
        validate_contact_data(contact_data)

    with get_connection() as connection:
        for contact_data in SAMPLE_CONTACTS:
            existing_contact = connection.execute(
                "SELECT id FROM contacts WHERE email = ?",
                (contact_data["email"].strip(),),
            ).fetchone()
            if existing_contact is not None:
                continue

            connection.execute(
                """
                INSERT INTO contacts (
                    first_name,
                    middle_initial,
                    last_name,
                    age,
                    date_of_birth,
                    email,
                    favorite_color,
                    pronouns
                )
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """,
                (
                    contact_data["first_name"].strip(),
                    contact_data["middle_initial"].strip(),
                    contact_data["last_name"].strip(),
                    contact_data["age"],
                    contact_data["date_of_birth"].strip(),
                    contact_data["email"].strip(),
                    contact_data["favorite_color"].strip(),
                    contact_data["pronouns"].strip(),
                ),
            )
        connection.commit()


def model_to_dict(model: BaseModel, exclude_unset: bool = False) -> dict[str, Any]:
    if hasattr(model, "model_dump"):
        return model.model_dump(exclude_unset=exclude_unset)
    return model.dict(exclude_unset=exclude_unset)


def validate_contact_data(data: dict[str, Any]) -> None:
    text_fields = [
        "first_name",
        "last_name",
        "date_of_birth",
        "email",
        "favorite_color",
        "pronouns",
    ]

    for field in text_fields:
        if field in data and not str(data[field]).strip():
            raise HTTPException(status_code=400, detail=f"{field} is required")

    if "middle_initial" in data:
        middle_initial = str(data["middle_initial"]).strip()
        if len(middle_initial) != 1:
            raise HTTPException(status_code=400, detail="middle_initial must be one character")

    if "age" in data and data["age"] is not None and data["age"] < 0:
        raise HTTPException(status_code=400, detail="age must be zero or greater")

    if "date_of_birth" in data:
        try:
            date.fromisoformat(str(data["date_of_birth"]))
        except ValueError as exc:
            raise HTTPException(
                status_code=400,
                detail="date_of_birth must use YYYY-MM-DD format",
            ) from exc

    if "email" in data:
        email = str(data["email"]).strip()
        if "@" not in email or "." not in email.split("@")[-1]:
            raise HTTPException(status_code=400, detail="email must be valid")


def row_to_contact(row: sqlite3.Row) -> dict[str, Any]:
    return {
        "id": row["id"],
        "first_name": row["first_name"],
        "middle_initial": row["middle_initial"],
        "last_name": row["last_name"],
        "age": row["age"],
        "date_of_birth": row["date_of_birth"],
        "email": row["email"],
        "favorite_color": row["favorite_color"],
        "pronouns": row["pronouns"],
    }


def create_contact(contact: InputInformation) -> dict[str, Any]:
    validate_contact_data(contact.to_dict())

    with get_connection() as connection:
        cursor = connection.execute(
            """
            INSERT INTO contacts (
                first_name,
                middle_initial,
                last_name,
                age,
                date_of_birth,
                email,
                favorite_color,
                pronouns
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """,
            (
                contact.first_name.strip(),
                contact.middle_initial.strip(),
                contact.last_name.strip(),
                contact.age,
                contact.date_of_birth.strip(),
                contact.email.strip(),
                contact.favorite_color.strip(),
                contact.pronouns.strip(),
            ),
        )
        connection.commit()
        contact_id = cursor.lastrowid

    return print_contact(contact_id)


def list_contacts() -> list[dict[str, Any]]:
    with get_connection() as connection:
        rows = connection.execute("SELECT * FROM contacts ORDER BY last_name, first_name").fetchall()
    return [row_to_contact(row) for row in rows]


def print_contact(contact_id: int) -> dict[str, Any]:
    with get_connection() as connection:
        row = connection.execute("SELECT * FROM contacts WHERE id = ?", (contact_id,)).fetchone()

    if row is None:
        raise HTTPException(status_code=404, detail="Contact not found")
    return row_to_contact(row)


def search_contacts(query: str) -> list[dict[str, Any]]:
    search_term = f"%{query.strip()}%"
    with get_connection() as connection:
        rows = connection.execute(
            """
            SELECT * FROM contacts
            WHERE first_name LIKE ?
               OR middle_initial LIKE ?
               OR last_name LIKE ?
               OR CAST(age AS TEXT) LIKE ?
               OR date_of_birth LIKE ?
               OR email LIKE ?
               OR favorite_color LIKE ?
               OR pronouns LIKE ?
            ORDER BY last_name, first_name
            """,
            (search_term,) * 8,
        ).fetchall()
    return [row_to_contact(row) for row in rows]


def update_contact(contact_id: int, changes: dict[str, Any]) -> dict[str, Any]:
    if not changes:
        raise HTTPException(status_code=400, detail="No fields provided for update")
    validate_contact_data(changes)
    print_contact(contact_id)

    fields = ", ".join(f"{field} = ?" for field in changes)
    values = [value.strip() if isinstance(value, str) else value for value in changes.values()]
    values.append(contact_id)

    with get_connection() as connection:
        connection.execute(f"UPDATE contacts SET {fields} WHERE id = ?", values)
        connection.commit()

    return print_contact(contact_id)


def delete_contact(contact_id: int) -> dict[str, str]:
    print_contact(contact_id)
    with get_connection() as connection:
        connection.execute("DELETE FROM contacts WHERE id = ?", (contact_id,))
        connection.commit()
    return {"message": "Contact deleted"}


def display_contact(contact: dict[str, Any]) -> None:
    print(
        f"ID: {contact['id']} | "
        f"{contact['first_name']} {contact['middle_initial']}. {contact['last_name']} | "
        f"Age: {contact['age']} | "
        f"DOB: {contact['date_of_birth']} | "
        f"Email: {contact['email']} | "
        f"Favorite color: {contact['favorite_color']} | "
        f"Pronouns: {contact['pronouns']}"
    )


def display_contacts(contacts: list[dict[str, Any]]) -> None:
    if not contacts:
        print("No contacts found.")
        return

    for contact in contacts:
        display_contact(contact)


def prompt_required_text(prompt: str) -> str:
    while True:
        try:
            value = input(prompt).strip()
            if not value:
                raise ValueError("This field is required.")
            return value
        except ValueError as exc:
            print(f"Invalid input: {exc}")


def prompt_middle_initial(prompt: str) -> str:
    while True:
        try:
            middle_initial = prompt_required_text(prom4pt)
            if len(middle_initial) != 1:
                raise ValueError("Middle initial must be one character.")
            return middle_initial
        except ValueError as exc:
            print(f"Invalid input: {exc}")


def prompt_age(prompt: str) -> int:
    while True:
        try:
            age = int(input(prompt).strip())
            if age < 0:
                raise ValueError("Age must be zero or greater.")
            return age
        except ValueError as exc:
            print(f"Invalid input: {exc}")


def prompt_date_of_birth(prompt: str) -> str:
    while True:
        try:
            date_of_birth = prompt_required_text(prompt)
            date.fromisoformat(date_of_birth)
            return date_of_birth
        except ValueError:
            print("Invalid input: Date of birth must use YYYY-MM-DD format.")


def prompt_email(prompt: str) -> str:
    while True:
        try:
            email = prompt_required_text(prompt)
            if "@" not in email or "." not in email.split("@")[-1]:
                raise ValueError("Email must be valid.")
            return email
        except ValueError as exc:
            print(f"Invalid input: {exc}")


def prompt_contact_id(prompt: str = "Contact ID: ") -> int:
    while True:
        try:
            contact_id = int(input(prompt).strip())
            if contact_id <= 0:
                raise ValueError("Contact ID must be greater than zero.")
            return contact_id
        except ValueError as exc:
            print(f"Invalid input: {exc}")


def prompt_contact_information() -> InputInformation:
    return InputInformation(
        first_name=prompt_required_text("First name: "),
        middle_initial=prompt_middle_initial("Middle initial: "),
        last_name=prompt_required_text("Last name: "),
        age=prompt_age("Age: "),
        date_of_birth=prompt_date_of_birth("Date of birth (YYYY-MM-DD): "),
        email=prompt_email("Email: "),
        favorite_color=prompt_required_text("Favorite color: "),
        pronouns=prompt_required_text("Pronouns: "),
    )


def prompt_optional_text(prompt: str) -> Optional[str]:
    value = input(prompt).strip()
    if not value:
        return None
    return value


def prompt_contact_changes() -> dict[str, Any]:
    print("Press Enter to keep the current value for any field.")
    changes: dict[str, Any] = {}

    first_name = prompt_optional_text("First name: ")
    if first_name is not None:
        changes["first_name"] = first_name

    while True:
        try:
            middle_initial = prompt_optional_text("Middle initial: ")
            if middle_initial is None:
                break
            if len(middle_initial) != 1:
                raise ValueError("Middle initial must be one character.")
            changes["middle_initial"] = middle_initial
            break
        except ValueError as exc:
            print(f"Invalid input: {exc}")

    last_name = prompt_optional_text("Last name: ")
    if last_name is not None:
        changes["last_name"] = last_name

    while True:
        try:
            age_text = prompt_optional_text("Age: ")
            if age_text is None:
                break
            age = int(age_text)
            if age < 0:
                raise ValueError("Age must be zero or greater.")
            changes["age"] = age
            break
        except ValueError as exc:
            print(f"Invalid input: {exc}")

    while True:
        try:
            date_of_birth = prompt_optional_text("Date of birth (YYYY-MM-DD): ")
            if date_of_birth is None:
                break
            date.fromisoformat(date_of_birth)
            changes["date_of_birth"] = date_of_birth
            break
        except ValueError:
            print("Invalid input: Date of birth must use YYYY-MM-DD format.")

    while True:
        try:
            email = prompt_optional_text("Email: ")
            if email is None:
                break
            if "@" not in email or "." not in email.split("@")[-1]:
                raise ValueError("Email must be valid.")
            changes["email"] = email
            break
        except ValueError as exc:
            print(f"Invalid input: {exc}")

    favorite_color = prompt_optional_text("Favorite color: ")
    if favorite_color is not None:
        changes["favorite_color"] = favorite_color

    pronouns = prompt_optional_text("Pronouns: ")
    if pronouns is not None:
        changes["pronouns"] = pronouns

    return changes


def add_contact_from_input() -> None:
    try:
        contact = create_contact(prompt_contact_information())
        print("Contact added successfully.")
        display_contact(contact)
    except HTTPException as exc:
        print(f"Unable to add contact: {exc.detail}")


def remove_contact_from_input() -> None:
    try:
        contact_id = prompt_contact_id()
        delete_contact(contact_id)
        print("Contact removed successfully.")
    except HTTPException as exc:
        print(f"Unable to remove contact: {exc.detail}")


def edit_contact_from_input() -> None:
    try:
        contact_id = prompt_contact_id()
        display_contact(print_contact(contact_id))
        updated_contact = update_contact(contact_id, prompt_contact_changes())
        print("Contact updated successfully.")
        display_contact(updated_contact)
    except HTTPException as exc:
        print(f"Unable to edit contact: {exc.detail}")


def search_contacts_from_input() -> None:
    query = prompt_required_text("Search contacts: ")
    display_contacts(search_contacts(query))


def list_contacts_from_input() -> None:
    display_contacts(list_contacts())


def run_contact_interface() -> None:
    init_database()
    populate_sample_data()

    while True:
        print("\nContact Management Menu")
        print("1. Add contact")
        print("2. Remove contact")
        print("3. Edit contact")
        print("4. Search contacts")
        print("5. List contacts")
        print("6. Exit")

        try:
            choice = input("Choose an option (1-6): ").strip()
            if choice == "1":
                add_contact_from_input()
            elif choice == "2":
                remove_contact_from_input()
            elif choice == "3":
                edit_contact_from_input()
            elif choice == "4":
                search_contacts_from_input()
            elif choice == "5":
                list_contacts_from_input()
            elif choice == "6":
                print("Goodbye!")
                break
            else:
                raise ValueError("Please choose a number from 1 to 6.")
        except ValueError as exc:
            print(f"Invalid input: {exc}")


@app.on_event("startup")
def startup() -> None:
    init_database()
    populate_sample_data()


@app.get("/")
async def root() -> dict[str, str]:
    return {"message": "Contact Management Application"}


@app.post("/contacts", status_code=201)
async def add_contact(contact: ContactCreate) -> dict[str, Any]:
    contact_data = model_to_dict(contact)
    input_information = InputInformation(**contact_data)
    return create_contact(input_information)


@app.get("/contacts")
async def get_contacts() -> list[dict[str, Any]]:
    return list_contacts()


@app.get("/contacts/search")
async def find_contacts(q: str) -> list[dict[str, Any]]:
    return search_contacts(q)


@app.get("/contacts/{contact_id}")
async def get_contact(contact_id: int) -> dict[str, Any]:
    return print_contact(contact_id)


@app.put("/contacts/{contact_id}")
async def modify_contact(contact_id: int, contact: ContactUpdate) -> dict[str, Any]:
    changes = model_to_dict(contact, exclude_unset=True)
    return update_contact(contact_id, changes)


@app.delete("/contacts/{contact_id}")
async def remove_contact(contact_id: int) -> dict[str, str]:
    return delete_contact(contact_id)


if __name__ == "__main__":
    run_contact_interface()
