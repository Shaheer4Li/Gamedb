<div align="center">

# 🎮 GameDB


**A personal game-tracking library for collecting, organizing, and keeping track of the games you play.**

<br>

![Flask](https://img.shields.io/badge/Flask-Backend-000000?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/Python-Powered-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Structure-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Interaction-F7DF1E?style=for-the-badge&logo=javascript&logoColor=111111)

<br>

[Features](#-features) · [Tech Stack](#-tech-stack) · [Getting Started](#-getting-started) · [Project Structure](#-project-structure)

</div>

---

## 🕹️ About the Project

GameDB is a personal game library web application that lets you keep a record of the games in your gaming journey. Instead of relying on memory or scattered lists, you can store games in one place, organize them by genre and platform, and track your progress through each title.

The goal is simple: **make your gaming history feel like your own collection.**

Whether you've completed a story-driven adventure, are currently playing an RPG, or have a game waiting in your backlog, GameDB gives you a place to keep track of it.

## ✨ Features

<table>
<tr>
<td width="50%">

### 📚 Personal Game Collection
Add games to your own library and browse them through a visual collection of game cards.

</td>
<td width="50%">

### 📝 Game Details
Give each entry a title, cover image, genre, platform, status, and description or review.

</td>
</tr>
<tr>
<td width="50%">

### 🔄 Track Your Progress
Organize games by their status: **Starting**, **Playing**, or **Completed**.

</td>
<td width="50%">

### 📊 Statistics Dashboard
See your total number of games, status breakdown, and collection distribution by genre and platform.

</td>
</tr>
<tr>
<td width="50%">

### ✏️ Manage Your Library
Open a game's details, edit its information, or delete an entry from your collection.

</td>
<td width="50%">

### 🎨 Dark Gaming UI
A dark interface with purple accents, bold display typography, glowing card edges, and large cover artwork.

</td>
</tr>
</table>


## 🧰 Tech Stack

| Technology | Role |
|---|---|
| **HTML5** | Page structure and templates |
| **CSS3** | Layout, responsive styling, colors, and visual effects |
| **Python + Flask** | Application routes and server-side logic |
| **SQLite** | Persistent storage for game entries |

## ⚙️ Getting Started

Follow these steps to run GameDB locally.

### Prerequisites

- Python 3.10 or later recommended
- `pip`
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/Shaheer4Li/GameDB.git
cd GameDB
```

> If your repository has a different name or URL, replace the clone URL and folder name with your actual repository details.

### 2. Create a virtual environment

**Windows**
```bash
python -m venv venv
venv\Scripts\activate
```

**macOS / Linux**
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

If the project includes a `requirements.txt` file:

```bash
pip install -r requirements.txt
```

Otherwise, install the packages your application imports. For a basic Flask + Flask-SQLAlchemy setup:

```bash
pip install Flask Flask-SQLAlchemy Flask-WTF
```

### 4. Run the application

If your main Python file is named `app.py`:

```bash
python app.py
```

Open the local address shown in your terminal, commonly:

```text
http://127.0.0.1:5000
```

> **Note:** These commands assume your entry file is `app.py` and that your dependencies match the examples. Adjust them if your project uses different filenames or packages.

## 🗂️ Project Structure

A typical Flask layout for this project could look like this:

```text
GameDB/
├── app.py
├── database.db
├── requirements.txt
├── static/
│   ├── style.css
│   └── ...
├── templates/
│   ├── base.html
│   ├── index.html
│   ├── add.html
│   ├── collection.html
│   ├── game.html
│   └── statistics.html
```



## 🧠 What I Practiced

GameDB brings together several core web development concepts in one project:

- Building pages with HTML and Flask templates.
- Styling a multi-page interface with CSS.
- Handling forms and user-submitted data.
- Connecting a Flask application to an SQLite database.
- Performing CRUD operations: create, read, update, and delete game entries.
- Organizing database records into collection views and summary statistics.
- Designing a consistent interface across multiple pages.

## 🚀 Possible updates

- ⭐ Add personal ratings and more structured reviews.
- 🔎 Search, filter, and sort the collection.
- 🏷️ Add custom tags and favorites.
- 👤 Introduce user accounts and separate libraries.
- 📅 Track play dates or create a yearly gaming recap.
- 🔗 Fetch game metadata from a public game database API.


<div align="center">

**Built for the games that stay with you. 🎮**

If you find this project interesting, feel free to explore the code and share your feedback.

</div>

