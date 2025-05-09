#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

#define MAX_USERS 100
#define MAX_MOVIES 10
#define MAX_NAME_LENGTH 50
#define MAX_LINE_LENGTH 100

// Struct to represent a movie
struct Movie {
    char title[MAX_NAME_LENGTH];
    char genre[MAX_NAME_LENGTH];
    float rating;
};

// Struct to represent a user
struct User {
    char name[MAX_NAME_LENGTH];
    float ratings[MAX_MOVIES]; // Ratings for each movie
};

// Global variables
struct User users[MAX_USERS];
struct Movie movies[MAX_MOVIES];
int num_users = 0;
int num_movies = 0;

// Function prototypes
void readUserData();
void readMovieData();
void displayMainMenu();
void registerUser();
void displayMovies();
void rateMovie();
void getMovieRecommendations();
void writeUserData();
void writeUserRatings();

int main() {
    readUserData();
    readMovieData();

    int choice;
    do {
        displayMainMenu();
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                registerUser();
                break;
            case 2:
                displayMovies();
                break;
            case 3:
                rateMovie();
                break;
            case 4:
                getMovieRecommendations();
                break;
            case 5:
                printf("Exiting...\n");
                writeUserData(); // Write user data to file before exiting
                writeUserRatings(); // Write user ratings to file before exiting
                exit(0);
            default:
                printf("Invalid choice. Please try again.\n");
        }
    } while (choice != 0);

    return 0;
}

// Read user data from file
void readUserData() {
    FILE *file = fopen("user_data.txt", "r");
    if (file == NULL) {
        printf("Error reading user data file.\n");
        exit(1);
    }

    while (fscanf(file, "%s", users[num_users].name) == 1) {
        num_users++;
    }

    fclose(file);
}

// Read movie data from file
void readMovieData() {
    FILE *file = fopen("movie_database.txt", "r");
    if (file == NULL) {
        printf("Error reading movie data file.\n");
        exit(1);
    }

    while (fscanf(file, "%s %s %f", movies[num_movies].title, movies[num_movies].genre, &movies[num_movies].rating) == 3) {
        num_movies++;
    }

    fclose(file);
}

// Display main menu
void displayMainMenu() {
    printf("\nMain Menu:\n");
    printf("1. Register User\n");
    printf("2. Display Movies\n");
    printf("3. Rate a Movie\n");
    printf("4. Get Movie Recommendations\n");
    printf("5. Exit\n");
    printf("Enter your choice: ");
}

// Register a new user
void registerUser() {
    char name[MAX_NAME_LENGTH];
    printf("Enter your name: ");
    scanf("%s", name);

    // Convert name to lowercase for case-insensitive comparison
    for (int i = 0; name[i]; i++) {
        name[i] = tolower(name[i]);
    }

    // Check if the user already exists
    for (int i = 0; i < num_users; i++) {
        if (strcmp(users[i].name, name) == 0) {
            printf("User already exists. Please choose a different name.\n");
            return;
        }
    }

    // Add the new user
    strcpy(users[num_users].name, name);
    num_users++;
    printf("User is successfully registered.\n");

    // Write the new user to the file
    writeUserData();
}

// Display list of movies
void displayMovies() {
    printf("\nList of Movies:\n");
    for (int i = 0; i < num_movies; i++) {
        printf("%d. %s (%s) - Rating: %.1f\n", i + 1, movies[i].title, movies[i].genre, movies[i].rating);
    }
}

// Rate a movie
void rateMovie() {
    // Implementation of the rateMovie function (unchanged)
}

// Get movie recommendations
void getMovieRecommendations() {
    // Implementation of the getMovieRecommendations function (unchanged)
}

// Write user data to file
void writeUserData() {
    FILE *file = fopen("user_data.txt", "w");
    if (file == NULL) {
        printf("Error writing user data file.\n");
        exit(1);
    }

    for (int i = 0; i < num_users; i++) {
        fprintf(file, "%s\n", users[i].name);
    }

    fclose(file);
}

// Write user ratings to file
void writeUserRatings() {
    FILE *file = fopen("user_ratings.txt", "w");
    if (file == NULL) {
        printf("Error writing user ratings file.\n");
        exit(1);
    }

    // Iterate through users and movies and write ratings
    for (int i = 0; i < num_users; i++) {
        for (int j = 0; j < num_movies; j++) {
            fprintf(file, "%s %s %.1f\n", users[i].name, movies[j].title, users[i].ratings[j]);
        }
    }

    fclose(file);
}
