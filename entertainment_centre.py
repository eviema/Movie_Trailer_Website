import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A boy and his toys that come to life",
                        "https://lumiere-a.akamaihd.net/v1/images/pixarcol_telstra_1000x1440_11_e0ed924d.png",
                        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://cdn.traileraddict.com/content/20th-century-fox/avatar-6.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

zootopia = media.Movie("Zootopia",
                       "A rookie bunny cop and a cynical con artist"
                       " fox must work together to uncover a conspiracy",
                       "https://image.tmdb.org/t/p/original/1YzLAWykXzZhydoGJCqoVQ0gVyC.jpg",
                       "https://www.youtube.com/watch?v=jWM0ct-OLsM")

dark_knight = media.Movie("The Dark Knight",
                          "The Dark Knight is forced from his imposed exile"
                          " to save Gotham City",
                          "http://cdn.collider.com/wp-content/uploads/the-dark-knight-rises-teaser-poster.jpg",
                          "https://www.youtube.com/watch?v=g8evyE9TuYk")

lord_of_rings = media.Movie("The Lord of the Rings",
                            "A meek Hobbit from the Shire and eight companions"
                            " set out on a journey to destroy the powerful"
                            " One Ring",
                            "https://projectedrealities.files.wordpress.com/2013/12/lord_of_the_rings_the_fellowship_of2.jpg",
                            "https://www.youtube.com/watch?v=y2rYRu8UW8M")

transformers = media.Movie("Transformers",
                           "An ancient struggle between two Cybertronian races",
                           "https://cdn.traileraddict.com/content/paramount-pictures/transformers-the-last-knight.jpg",
                           "https://www.youtube.com/watch?v=yCOvcyfRPRk")

movies = [toy_story, avatar, zootopia, dark_knight, lord_of_rings, transformers]
fresh_tomatoes.open_movies_page(movies)
