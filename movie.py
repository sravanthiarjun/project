print("Content-type:text/html \n")
import media
import fresh_tomatoes

ranga = media.Movie("rangastalam","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ4SsqOwa_1cewdZrJfbDhSjZDxZSbNcayLRJOWB89_Z6s6UvfuBQ",
                    "https://www.youtube.com/embed/mhhb6JAJKbE")
 ok= media.Movie("ok bangaram","http://4.bp.blogspot.com/-3co37RsjAAU/VgTkmK8qtBI/AAAAAAAAAqQ/lfjOp_f1mO4/s1600/ok%2Bbangaram.jpg",
                  "https://www.youtube.com/embed/UcIL3qsd1-0")
love = media.Movie("lovers","https://2.bp.blogspot.com/-UdxG40G6yNg/VDbUDBLssHI/AAAAAAAAAHU/RK8ROnzyyRk/s1600/lovers-telugu-movie-first-look-posters-1.jpg",
                   "https://www.youtube.com/embed/CnbspuM3jxU")
nenu = media.Movie("nenulocal","https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRJi3VXvUXuYiY44j_hI3KUCPKpI8JdU7GANuXiTfCC_NJNyq9fUw",
                   "https://www.youtube.com/embed/cmf3R2PNMJ0")
gol = media.Movie("golmol","http://allwrestling.2o7bp9kkig5fe.maxcdn-edge.com/wp-content/uploads/2017/10/golmaal-again-2017-movie-640x360.jpg?x48797",
                   "https://www.youtube.com/embed/VgQUwsUHdqc")

movies = [ranga,ok,love,nenu,gol]
fresh_tomatoes.open_page(movies)
