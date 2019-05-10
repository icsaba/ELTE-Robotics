# 2018 ELTE Robotika, Csaba Ivancza

## Features
- adaptiv tempomat: ha valami a lezer utjaba kerul, lassit a robot, kulonben ha egy ideig nem lat semmit, akkor gyorsit
- a lezerek 90 fokban latnak, lezerek kozott 5 fok van, e szerint 3 fele osztottam a lezereket, bal, jobb, es kozep. Balra es jobbra 8-8 darab lezer, kozepre 3.
- a bal es jobb lezerek adatainak atlaga alapjan dol el, hogy melyik oldalra fordul inkabb a robot
- ha valami a megengedett tavolsagon belulre kerul, a robot lassit, es eroteljesebben fordul
- ha valami kritikus tavolsagon belulre kerul, hatarozottan iranyt valtunk.
Kritikus a tavogit initlsag ha a legszelso es a kozepso sensor is minimalis tavolsagot mer