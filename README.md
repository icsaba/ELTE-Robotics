# 2018 ELTE Robotika, Csaba Ivancza

## Log

- 2018.04.09. Gazebo telepitese, elso model kiprobalasa
- 2018.04.10. Gazebo tutorialok tanulmanyozasa
- 2018.04.14 - 15. ROS vs Player. felesleges nekunk
- 2018.04.24 - 25. Gazebo tutorialok, gave up
- 2018.04.28 - Valtas Morse-ra, sokkal letisztultabb es kevesbe komplikalt, vannak ertelmes peldak
- 2018.04.30 - Robot elakad a szekben, es neha belat a huto ala...
- 2018.05.06 - sandboxban ugyesen laviroz utkozes es elakadas nelkul

## Features
- adaptiv tempomat: ha valami a lezer utjaba kerul, lassit a robot, kulonben ha egy ideig nem lat semmit, akkor gyorsit
- a lezerek 90 fokban latnak, lezerek kozott 5 fok van, e szerint 3 fele osztottam a lezereket, bal, jobb, es kozep. Balra es jobbra 8-8 darab lezer, kozepre 3.
- a bal es jobb lezerek adatainak atlaga alapjan dol el, hogy melyik oldalra fordul inkabb a robot
- ha valami a megengedett tavolsagon belulre kerul, a robot lassit, es eroteljesebben fordul
- ha valami kritikus tavolsagon belulre kerul, hatarozottan iranyt valtunk.
Kritikus a tavolsag ha a legszelso es a kozepso sensor is minimalis tavolsagot mer