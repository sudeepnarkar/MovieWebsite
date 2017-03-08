import media
import fresh_tomatoes

Toystory = media.Movie("Toy Story",
                       "Story of a boy and his toys which come to life",
                       "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                       "https://www.youtube.com/watch?v=KYz2wyBy3kc")

#print(Toystory.storyline)

Into_the_wild = media.Movie("Into the wild",
                     "Story of a breaking away from the shackles of slavery called society",
                     "https://upload.wikimedia.org/wikipedia/en/8/8a/Into-the-wild.jpg",
                     "https://www.youtube.com/watch?v=2LAuzT_x8Ek")


Shawshank_Redemption = media.Movie("ShawShank Redemption",
                     "Story of an innocent victims escape. A story of resilence and determination.Hope is a good thing. Probably the best of all things",
                     "https://upload.wikimedia.org/wikipedia/en/8/81/ShawshankRedemptionMoviePoster.jpg",
                     "https://www.youtube.com/watch?v=6hB3S9bIaco")
 



#print(Avatar.storyline)

movies = [Toystory,Into_the_wild,Shawshank_Redemption]
fresh_tomatoes.open_movies_page(movies)
#print(media.Movie .VALID_RATINGS)
#print(media.Movie.__doc__)

#print(media.Movie.__module__)
