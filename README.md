# Jacob Gaudet's Pokedex
Gotta fetch 'em all!

## About
This website is meant to emulate a Pokedex built with Python and Flask that fetches data from the [PokéAPI](https://pokeapi.co/) to display the original 151 Pokemon as cards and categorized by type. Each card features a clickable flip animation to reveal the classic Pokemon card backside in order to make the ui feel more like you're browsing cards and not just the Pokemons data. The site also includes a nav menu for quickly jumping between types and a "Back to top" button for easy browsing.

## Features
- **Pokemon Cards:** Each card displays a Pokemon's image, stats, abilities, id, weight, height, and base xp.
- **Type Categorization:** Pokemon are grouped by their type.
- **Interactive Flip Animation:** Click a card to flip it to view the classic pokemon card backside.
- **User-Friendly Navigation:** Includes a type-based navigation menu and a "Back to Top" button.

## Running Locally
To run this project on your local machine, follow these steps:

1. **Clone the Repository:**
    Clone through your IDE (I used vscode for this project) or in your terminal with this command:
    `git clone <https://github.com/JacobGaudet/Pokedex.git>`
    cd to the project folder (Pokedex) in your IDE/terminal

2. **Install Dependencies:**
    Make sure you have Flask and Requests installed with this command:
    `pip install flask requests`

3. **Run the project locally:**
    In your terminal run this command:
    `python app.py`
    Open the local instance in your web browser if it doesnt automatically pop up:
    http://127.0.0.1:5000