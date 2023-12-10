import fly

debug_mode = False

fly1 = fly.Fly("../images/flies/big_green1.png", "../images/flies/big_green2.png", 4, 100, 100)
fly2 = fly.Fly("../images/flies/butterfly_red1.png", "../images/flies/butterfly_red2.png", 4, 200, 200)
fly3 = fly.Fly("../images/flies/fly_super_blue1.png", "../images/flies/fly_super_blue2.png", 4, 300, 200)


def step():
    fly1.step()
    fly2.step()
    fly3.step()