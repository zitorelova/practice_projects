import site_code
import media

doctor_strange = media.Movie('Doctor Strange', 115, 'From surgeon to superhero', 
				'https://upload.wikimedia.org/wikipedia/en/c/c7/Doctor_Strange_poster.jpg', 
				'https://www.youtube.com/watch?v=HSzx-zryEgM')


finding_dory = media.Movie('Finding Dory', 105, 'We find Dory instead of Nemo!', 
				'https://upload.wikimedia.org/wikipedia/en/thumb/3/3e/Finding_Dory.jpg/220px-Finding_Dory.jpg', 
				'https://www.youtube.com/watch?v=3JNLwlcPBPI')

star_wars_7 = media.Movie('Star Wars VII - The Force Awakens', 135, 'Star Wars, nuff said', 
				'http://vignette2.wikia.nocookie.net/starwars/images/f/fd/Star_Wars_Episode_VII_The_Force_Awakens.jpg/revision/latest?cb=20151018162823',
				'https://www.youtube.com/watch?v=sGbxmsDFVnE')


jurassic_world = media.Movie('Jurassic World', 125, 'Experimental dinosaurs run loose',
				'https://upload.wikimedia.org/wikipedia/en/6/6e/Jurassic_World_poster.jpg',
				'https://www.youtube.com/watch?v=RFinNxS5KN4')

fantastic = media.Movie('Fantastic Beasts and Where to Find Them', 133, 'New Harry Potter movie!',
				'https://images-na.ssl-images-amazon.com/images/M/MV5BMjMxOTM1OTI4MV5BMl5BanBnXkFtZTgwODE5OTYxMDI@._V1_UX182_CR0,0,182,268_AL_.jpg',
				'https://www.youtube.com/watch?v=Vso5o11LuGU')

suicide_squad = media.Movie('Suicide Squad', 136, 'Villains become heroes',
				'http://static.rogerebert.com/uploads/movie/movie_poster/suicide-squad-2016/large_e1mjopzAS2KNsvpbpahQ1a6SkSn.jpg',
				'https://www.youtube.com/watch?v=CmRih_VtVAs')

movies = [doctor_strange, finding_dory, star_wars_7, jurassic_world, fantastic, suicide_squad]

site_code.open_movies_page(movies)

