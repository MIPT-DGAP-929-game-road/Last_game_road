# Last_game_road
Exam project on python3 on first semester DGAP MIPT

Plan of GitHub: 
  master
    push here programm parts, that were done
  pictures
    put here pictures, that seem to be good mask for some object also write here what they are for

Plan of creating:
  1) make classes CAR and OTHER_CAR, where we make polygon, that we can move with some velocity on the x-axe and y-axe so each of them takes in (x-coordinate, y-coordinate, x-velocity, y-velocity, parametre in 0 or 1 meaning dead or alive still) difference of classes is that our car should be able to move
  2) make class INFLCC as influence between any car and any other car checks if obj1 and obj2 have union space
  3) choose between ordinary race and postapocalipse race: 
    3.1) ordinary: 
       3.1.1) make class PIT_STOP: the area in front of the main road, where is an object viewing like wheel and petrol bottle 
       3.1.2) make class INFCP for influencing between our car and the object in pit-stop 
       3.1.3) make timer and counter of fuel, quality of wheels 
       3.1.4) do finish line create after out off time of the race, not creating new other car and class INFCL for crossing finish line with our car, car stop if fuel is low, car die if wheels are destroyed
    3.2) postapocalipses: 
        3.2.1) upgrade CAR adding gun, that can rotate (absolutely like inlast lab) 
        3.2.2) input class MONSTER, which we would go along y-axe on our car and we need to shoot them 
        3.2.3) make class SHOOTING with objects boolets, that would kill monsters and disapear if touch other cars, which are state and dead. 
        3.2.4) make quality of car fall if car touched monster and destroy that monster 
        3.2.5) make (timer)"distance counter" and counter of fuel, quality of car 
        3.2.6) do some varient of finish line create after out off (time)distance of the race, not creating new other monsters and class INFCL for crossing finish line with our car, car stop if fuel is low, car die if car's quality is 0
   4)make menu with starting and ending of game, exiting all programm
   5)make table of results, possibility of making settings change car (view, moving buttons, hardness) 
   *6) put on objects skins depending on variant ordinary/postapocalipses 
   *7) make shorts at the starting, pausing, exiting, loosing and winning of game
