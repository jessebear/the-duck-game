def on_a_pressed():
    global projectile
    projectile = sprites.create_projectile_from_sprite(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . 4 4 . . . . . . . 
                    . . . . . . 4 5 5 4 . . . . . . 
                    . . . . . . 2 5 5 2 . . . . . . 
                    . . . . . . . 2 2 . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . . 
                    . . . . . . . . . . . . . . . .
        """),
        myHero,
        50,
        0)
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def on_on_overlap(sprite, otherSprite):
    sprites.destroy(myHero)
sprites.on_overlap(SpriteKind.enemy, SpriteKind.player, on_on_overlap)

def on_on_overlap2(sprite2, otherSprite2):
    global myEnemy
    sprites.destroy(projectile)
    sprites.destroy(myEnemy, effects.confetti, 500)
    myEnemy = sprites.create(img("""
            ........................
                    ........................
                    ........................
                    ........................
                    .........fffff..........
                    ........f11111ff........
                    .......fb111111bf.......
                    .......f1111111dbf......
                    ......fd111111dddf......
                    ......fd11111ddddf......
                    ......fd11dddddddf......
                    ......f111dddddddf......
                    ......f11fcddddddf......
                    .....fb1111bdddbf.......
                    .....f1b1bdfcfff........
                    .....fbfbffffffff.......
                    ......fffffffffff.ff....
                    ...........ffffffff.....
                    ........f1b1bffffff.....
                    ........fbfbffffff......
                    ........................
                    ........................
                    ........................
                    ........................
        """),
        SpriteKind.enemy)
    myEnemy.set_position(149, randint(0, 120))
sprites.on_overlap(SpriteKind.projectile, SpriteKind.enemy, on_on_overlap2)

projectile: Sprite = None
myEnemy: Sprite = None
myHero: Sprite = None
tiles.set_current_tilemap(tilemap("""
    level2
"""))
myHero = sprites.create(img("""
        . . . . . . . . . . b 5 b . . . 
            . . . . . . . . . b 5 b . . . . 
            . . . . . . b b b b b b . . . . 
            . . . . . b b 5 5 5 5 5 b . . . 
            . . . . b b 5 d 1 f 5 5 d f . . 
            . . . . b 5 5 1 f f 5 d 4 c . . 
            . . . . b 5 5 d f b d d 4 4 . . 
            . b b b d 5 5 5 5 5 4 4 4 4 4 b 
            b d d d b b d 5 5 4 4 4 4 4 b . 
            b b d 5 5 5 b 5 5 5 5 5 5 b . . 
            c d c 5 5 5 5 d 5 5 5 5 5 5 b . 
            c b d c d 5 5 b 5 5 5 5 5 5 b . 
            . c d d c c b d 5 5 5 5 5 d b . 
            . . c b d d d d d 5 5 5 b b . . 
            . . . c c c c c c c c b b . . . 
            . . . . . . . . . . . . . . . .
    """),
    SpriteKind.player)
for myEnemy2 in range(5):
    myEnemy2 += 1
scene.camera_follow_sprite(myHero)
controller.move_sprite(myHero, 100, 100)
myEnemy = sprites.create(img("""
        ........................
            ........................
            ........................
            ........................
            .........fffff..........
            ........f11111ff........
            .......fb111111bf.......
            .......f1111111dbf......
            ......fd111111dddf......
            ......fd11111ddddf......
            ......fd11dddddddf......
            ......f111dddddddf......
            ......f11fcddddddf......
            .....fb1111bdddbf.......
            .....f1b1bdfcfff........
            .....fbfbffffffff.......
            ......fffffffffff.ff....
            ...........ffffffff.....
            ........f1b1bffffff.....
            ........fbfbffffff......
            ........................
            ........................
            ........................
            ........................
    """),
    SpriteKind.enemy)
myHero.set_position(10, 54)
myEnemy.set_position(149, 82)

def on_forever():
    myEnemy.set_velocity(-42, 0)
forever(on_forever)

def on_forever2():
    if myEnemy.is_hitting_tile(CollisionDirection.LEFT):
        game.game_over(False)
forever(on_forever2)
