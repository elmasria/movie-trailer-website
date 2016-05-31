import media
import fresh_tomatoes

toy_story = media.Movie("School of Rock",
                        "A story of a boy and his toys that come to life",
                        "http://resizing.flixster.com/dN13_DunKL1U-qm-QUIWPOID6So=/800x1200/v1.bTsxMTE2ODk2NTtqOzE2OTY5OzIwNDg7ODAwOzEyMDA",
                        "https://youtu.be/LqEszt5wG9I")

the_martian = media.Movie("The Martian",
                        "An artist and a CIA agent go on an anti-terrorist mission in France..",
                        "https://upload.wikimedia.org/wikipedia/en/3/39/Bastille_Day_(film).png",
                        "https://www.youtube.com/watch?v=ej3ioOneTy8")

bastille_day = media.Movie("Bastille Day",
                        "During a manned mission to Mars, Astronaut Mark Watney is presumed dead after a fierce storm and left behind by his crew. But Watney has survived and finds himself stranded and alone on the hostile planet. With only meager supplies, he must draw upon his ingenuity, wit and spirit to subsist and find a way to signal to Earth that he is alive. Millions of miles away, NASA and a team of international scientists work tirelessly to bring \"the Martian\" home, while his crewmates concurrently plot a daring, if not impossible, rescue mission. As these stories of incredible bravery unfold, the world comes together to root for Watney's safe return.",
                        "https://upload.wikimedia.org/wikipedia/en/c/cd/The_Martian_film_poster.jpg",
                        "https://www.youtube.com/watch?v=U5R0bI8EJCQ")

point_break = media.Movie("Point Break",
                        "Thrill-seeking criminals perform a series of daredevil stunts to steal money and gems, only to give it away to the poor and less fortunate. Training for a job with the FBI, young recruit Johnny Utah suspects that only extreme athletes could pull off these heists. Utilizing his own special skills, Utah infiltrates the gang of thieves after befriending their charismatic leader, Bodhi. As Johnny experiences the rush of their lifestyle, his superiors fear that his loyalties are being tested..",
                        "http://t2.gstatic.com/images?q=tbn:ANd9GcQcLALWSWoRWBqqqcLCJYsOs4RssX33SSVlN1GGb3AzdW2wlM6e",
                        "https://www.youtube.com/watch?v=ncvFAm4kYCo")

# List of movies that will be available on the website
movies = [toy_story, the_martian, bastille_day, point_break]

# fresh_tomatoes library help to create the required HTML
# and open it in the browser
fresh_tomatoes.open_movies_page(movies)
