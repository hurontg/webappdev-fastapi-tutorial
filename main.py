from fastapi import FastAPI
from pydantic import BaseModel
import psycopg2
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost:3000",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Book(BaseModel):
    id: int = 0
    title: str = ''
    author: str = ''
    number: int = 0

    def set_number(self, num: int):
        self.number = num

my_class = Book()
my_class.set_number(21)



my_class2 = Book()
my_class2.set_number(21)

class Car(BaseModel):
    car_id: int | None = None
    make: str
    model: str



# class Passport(BaseModel):
#     passport_id: int


# class Person(BaseModel):
#     person_id: int
#     person_name: str
#     passport: Passport




books = []
books.append(Book(id = 1, title = "The Temple Tiger", author = "Jim Corbett"))
books.append(Book(id = 2, title = "Jungle Lore", author = "Jim Corbett"))
books.append(Book(id = 3, title = "Man eating Leopard of Rudraprayag", author = "Jim Corbett"))

@app.get("/")
async def root():
    return {"message": "بِسْمِ اللهِ الرَّحْمٰنِ الرَّحِيْمِ"}


@app.get("/message")
async def get_message():
    return "In His Name"


@app.get("/message1")
async def get_message1():
    return "Now we can handle /message1"

@app.get("/books")
async def get_books():
    return books
    

@app.post("/books")
async def post_books(book: Book):
    book_dict = book.dict()
    print('book_dict', book_dict)

    books.append(book)
    return {'message': 'Book added to collection'}


@app.put("/books/{book_id}")
async def update_book(book_id: int, bk: Book):
    print('book-id', book_id)

    found = False

    for book in books:
        if book.id == book_id:
            print('found>', book.dict())
            book.title = bk.title
            book.author = bk.author
            found = True

    if found:
        return { 'message': 'Book updated successfully'}
    else:
        return { 'message': 'Book id not found'}



@app.get("/books/{book_id}")
async def get_book_by_id(book_id: int):
    for book in books:
        print(book)
        if book.id == book_id:
            return book
    
    return {'message': f'Book with Id({book_id}) not found'}

@app.delete("/books/{book_id}")
async def delete_book(book_id: int):
    # global books
    books_u = list(filter(
        lambda book: book.id != book_id,
        books))
    
    print(books_u)
    books.clear()
    books.extend(books_u)
    
    
    


# @app.get("/test-query-params/")
# async def get_test_query_params(a: int, b: int):
#     return {'a': a, 'b': b}


#
# Second 
# 

@app.get("/cars")
async def get_cars_from_db():
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # Execute a query
    cur.execute("select * from car order by car_id") # DML 

    # Retrieve query results
    cars_read_from_db = cur.fetchall()

    for car in cars_read_from_db:
        print(car)
    
    # Close communication with the database
    cur.close()
    conn.close()

    return cars_read_from_db


# @app.post("/cars")
# async def save_car_to_db(car: Car):
#     # Connect to your postgres DB
#     conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=postgres")

#     # Open a cursor to perform database operations
#     cur = conn.cursor()

#     # insert into car (make, model) values ('Toyota', 'Land Cruiser');
#     cur.execute("INSERT INTO car (make, model) VALUES (%s, %s)", (car.make, car.model))

#     conn.commit()

#     # Close communication with the database
#     cur.close()
#     conn.close()

#     return "OK"

@app.post("/cars")
async def save_car_to_db(car: Car):
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    cur.execute("INSERT INTO car (make, model) VALUES (%s, %s) returning car_id", (car.make, car.model))
    id_of_newly_inserted_car = cur.fetchone()[0]

    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    #  JSON - 
    return { "car_id": id_of_newly_inserted_car }

# {car_id} == path parameter
@app.put("/cars/{car_id}")
async def update_car_in_db(car_id: int, car: Car):
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    # update car set model = 'CRV' where car_id = 4;

    cur.execute("update car set make = %s, model = %s where car_id = %s", (car.make, car.model, car_id))

    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    return { "message": "Car updated successfully" }


@app.delete("/cars/{car_id}")
async def delete_car_from_db(car_id: int):
    # Connect to your postgres DB
    conn = psycopg2.connect("dbname=postgres host=localhost user=postgres password=postgres")

    # Open a cursor to perform database operations
    cur = conn.cursor()

    print(">>>>>>", car_id)
    cur.execute("delete from car where car_id = %s", (car_id,))

    conn.commit()

    # Close communication with the database
    cur.close()
    conn.close()

    return { "message": "Car deleted successfully" }
