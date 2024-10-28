# Blogger

**Blogger** is a simple web application that allows users to create, update, and delete blog posts. Built with Django for the backend and MongoDB for data storage, this project demonstrates full CRUD (Create, Read, Update, Delete) functionality along with seamless integration between Django and MongoDB.

## Features

- **Create Blog Posts**: Users can add new blog posts with a title and description.
- **Read Blog Posts**: View a list of all blog posts with their respective details.
- **Update Blog Posts**: Edit existing blog posts and save the changes.
- **Delete Blog Posts**: Remove blog posts from the database.
- **MongoDB Integration**: All blog posts are stored in a MongoDB database, providing a NoSQL alternative for data management.

## Technologies Used

- **Django**: A high-level Python web framework for rapid development.
- **MongoDB**: A NoSQL database for storing blog data.
- **Bootstrap**: For responsive and modern UI design.
- **HTML/CSS**: Standard web technologies for structuring and styling the application.

## Getting Started

### Prerequisites

- Python 3.x
- Django
- MongoDB
- MongoDB Compass (optional, for database management)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/ishijapriyansha/Blogger.git
   cd Blogger

2. Install required packages:
   ```bash
   pip install -r requirements.txt

3. Set up your MongoDB database and update the connection details in the code as needed.
   The application currently uses 'test' and 'student' as the database and the collection name respectively.

4. Run the Django development server:
    ```bash
    python manage.py runserver

5. Open your browser and go to http://127.0.0.1:8000/ to access the application.


### Usage

- Use the provided interface to add, edit, or delete blog posts.
- The application updates the MongoDB database in real-time with each action.

