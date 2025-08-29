Videos :
https://www.youtube.com/watch?v=H09PmP5tsy8&pp=ygUaaG93IHRvIGNyZWF0ZSBweXRob24gZ2FtZXM%3D
https://www.youtube.com/watch?v=waY3LfJhQLY
https://www.youtube.com/watch?v=vVGTZlnnX3U&t=2198s

Planification
- Mars - Avril : recherches et finir le Pong basique (raquettes et balle qui bougent sans physique particulière)
- Mai : faire rebondir la balle (pas que à 45°, ajout de physique)
- Juin : faire l'IA adversaire (plusieurs niveaux de difficultés)
- Juillet - fin aout : écrire et rendre premier jet TM
- Novembre - décembre : présentation orale

choix du pygame 
- c'est bien pour les débutants contrairement aux autres modules comme tkinter et pyopenGL

01.02.2025 
- création du git

25.02.2025 
-  création d'une petite fenetre qui tourne avec pygame
critique : pas assez de contenu à montrer au premier rdv de TM, le TM commence lentement
02.04.2025 : ajout des raquettes (+ mouvement) et de la balle

29.04.2025 
- fini le pong (la balle rebondit sur les raquettes, deux joueurs peuvent jouer et score) + essai de physique du pong mais ça ne marche pas très bien, peut être changer l'idée de la [physique](https://gamedev.stackexchange.com/questions/147773/what-is-original-pong-ball-behaviour) --> physique du pong original

10.06.2025 
- ajout d'IA avec plusieurs niveaux, amélioration du code (moins de redondance) et ajout de changer quelques options du jeu
critique : un peu trop desorganisé, je n'ai pas beaucoup pensé au TM pendant ce temps, je n'arrive pas a tenir les commits tous les 1-2 semaines

13.06.2025 
- moins de redondance dans la fonction movement du Paddle (une fonction pour les deux paddles avec des touches modifiables au lieu de deux fontions pour deux paddles avec des touches fixes)
29.06.2025
- ajout du menu avec difficultés, IA plus humaine (marges d'erreur qui dépend de la difficulté de l'IA), essai de réparer le bug (la balle rebondit sur le haut et le bas du paddle), ça marche un peu mais un bug autre apparait quelques fois?
26.08.2025
- jeu est independant du framerate (https://www.youtube.com/watch?v=XuyrHE6GIsc), ia plus humaine (elle ne "bug" plus, ne bouge plus bizarrement quand la balle arrive vers elle)