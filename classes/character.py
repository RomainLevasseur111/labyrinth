class Character:

1 peut se déplacer sur labyrinth (en utilisant des coordonnées)
2 ne peut pas traverser les murs
3 peut ramasser des objets
    has_item1 = False
    has_item2 = False
    has_item3 = False
    can_beat_ennemy = False
        if has_item1 and has_item2 and has_item3 == True:
            can_beat_ennemy = True

4 commence sur la case départ
5 doit atteidnre la case arrivée avec les trois objets
