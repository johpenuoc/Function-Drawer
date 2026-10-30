import pygame
from math import sin, cos, tan, radians, pi, sqrt
phi = (1 + sqrt(5)) / 2

GOLDEN_ANGEL = 137.5
AMNT = 41000

'''class Funcs:
    def __init__(self):
        self.fibs = []

        # funcs
        self.func = {
            'fib' : self.retfib,
            'counter' : self.retcounter,
            'pi' : self.retpi
        }

        # inits
        self.fib_init = False

    # retrieve funcs
    def retfib(self, p):
        if not self.fib_init:
            self.fib_init = True

            self.init_fib() 
        return self.fibs[p]

    def retcounter(self, p):
        return p

    def retpi(self, p):
        return pi * p
    
    # init funcs
    def init_fib(self):
        fib = 0
        prev = 1
        for _ in range(AMNT):
            self.fibs.append(fib)
            fib += prev
            prev = fib - prev'''

class Spiral:
    def __init__(self, Main):
        self.main = Main
        self.scale = 1
        #self.func_name = 'pi'
        #self.funcs = Funcs()

        def spiral():
            nodes = []
            pnode = 0
            for id in range(AMNT):
                nodes.append(self.nodegen(pnode, id))
                pnode = nodes[-1]
    
            return nodes

        self.nodes = spiral()

        self.animation_finished = False
        self.counter = 1

    def remap(self, pos):
        return (
            pos[0] + (self.main.win.get_width() / 2), 
            pos[1] + (self.main.win.get_height() / 2)
            )

    def tocart(self, r, theta):
        return (
            r * cos(radians(theta)),
            r * sin(radians(theta))
        )


    def nodegen(self, pnode, begin):
        if begin:
            pr = pnode[0]
            pt = pnode[1]
            pid = pnode[2]
        else:
            return (
                self.funcs.func[self.func_name](0),
                1,
                0
            )

        r = sin(radians(pid + 1)) * 50
        t = pi * (pid + 1)
        id = pid + 1

        return (
            r,
            t,
            id
        )

    def draw(self, anim=False):
        ww = self.main.win.get_width() * 2
        wh = self.main.win.get_height() * 2
        nodes_len = len(self.nodes) - 1
        for id, node in enumerate(self.nodes[:int(self.counter)]):
            if anim and not self.animation_finished:
                self.counter += 1 * self.main.dt
                if int(self.counter) >= nodes_len:
                    self.animation_finished = True

            pos = self.remap(self.tocart(node[0] / self.scale, node[1]))
            if node[2] != 0 and not node[0] / self.scale < 1:
                pnode = self.nodes[id - 1]
                ppos = self.remap(self.tocart(pnode[0] / self.scale, pnode[1]))
                if ppos[0] > -ww and ppos[0] < ww and pos[0] > -ww and pos[0] < ww and ppos[1] > -wh and ppos[1] < wh and pos[1] > -wh and pos[1] < wh:
                    pygame.draw.line(
                        self.main.win, (255, 255, 255), ppos, pos
                    )