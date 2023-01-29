import math
import random

from SortFunctions import quickSortIterative, quicksort
import csv


def main():
    movies_by_genre = []
    with open('movies.csv', newline='\n') as csvfile:
        movie_reader = csv.reader(csvfile, delimiter=",")
        # renaming genres that are titled "no genres listed" to "no genres listed"
        # since the former parenthesis makes it get sorted before letter "A"
        for row in movie_reader:
            if row[2] != "(no genres listed)":
                movies_by_genre.append((row[2].split('|')[0], row[1]))
            else:
                movies_by_genre.append(("No genres listed", row[1]))

    choice = input("Should I sort the movies? (y/n)")
    if choice == 'y':
        #  quicksort using the iterative method
        n = len(movies_by_genre)
        quickSortIterative(movies_by_genre, 0, n - 1)
        print("------Sorted movies list--------------")
        print(movies_by_genre)
        print("------list ends here--------------")

        # Quicksort using the recursive
        # movies_sorted_by_genre = quicksort(movies_by_genre)
        # print(movies_sorted_by_genre)

        no_of_movies = int(input("How many movie recommendations do you want?"))
        rand_index = random.randint(0, len(movies_by_genre) - 1)
        lower_index = 0
        upper_index = 1

        def rand_lower_upper_limit(n):
            # conditional statement to check if the no of movies can be divided into equal halves
            lower_class = rand_index - int(n / 2) if n % 2 != 0 else rand_index - int(n / 2)+1
            upper_class = rand_index + int(n / 2)
            # print(f'lower: {lower_class} and rand: {rand_index} and upper: {upper_class}')
            return lower_class, upper_class
        # end of def rand_lower_upper_limit(n):

        # conditional statement to check if the user input is within 3 and 7 and any invalid input becomes 3
        if 3 <= no_of_movies <= 7:
            lower_index, upper_index = rand_lower_upper_limit(no_of_movies)
        else:
            lower_index, upper_index = rand_lower_upper_limit(3)
        for x in range(lower_index, upper_index + 1):
            print(movies_by_genre[x])
    else:
        print(movies_by_genre)


if __name__ == "__main__":
    main()
