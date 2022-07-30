from sys import stderr 
from enum import Enum
import math

# Save humans, destroy zombies!
class Pos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def print(self):
        print(f"X:{self.x}, Y:{self.y}", file=stderr, flush=True)

class Entity(Pos):
    def __init__(self, x: int, y: int, id: int):
        super().__init__(x, y)
        self.id = id

    def print(self):
        print(f"Entity Id:{self.id}, X:{self.x}, Y:{self.y}", file=stderr, flush=True)

    def update(self, x: int, y: int): 
        self.x = x
        self.y = y

class Human(Entity):
    def __init__(self, x: int, y: int, id: int):
        super().__init__(x, y, id)

    def print(self):
        print(f"Human Id:{self.id}, X:{self.x}, Y:{self.y}", file=stderr, flush=True)

class Ash(Human):
    def __init__(self, x: int, y: int, id: int):
        super().__init__(x, y, id)
        self.speed = 1000
        self.radius = 2000
        self.target = None

    def changeTarget(self, target):
        self.target = target

class Zombie(Entity):
    def __init__(self, x: int, y: int, id: int, nx: int, ny: int):
        super().__init__(x, y, id)
        self.next = Pos(nx, ny)
        self.target = None
        self.speed = 400
        
        # Angle is in Radians
        self.angleToTarget = 0
        self.distToTarget = 0
        self.estimatedSteps = []

    def print(self):
        print(f"Zombie Id:{self.id}, X:{self.x}, Y:{self.y}, NX:{self.next.x}, NY:{self.next.y}", file=stderr, flush=True)
        if self.target:
            print(f"Zombie Id:{self.id}, Target Id: {self.target.id}, Target X:{self.target.x}" +
                    f", Target Y:{self.target.y}, Angle:{self.angleToTarget / (math.pi / 180) }, distance:{self.distToTarget}", file=stderr, flush=True)
            turn = 1
            if self.estimatedSteps:
                for step in self.estimatedSteps:
                    print(f"Turn#{turn}, Zombie Id:{self.id}, Next X:{step.x}, Next Y:{step.y}", file=stderr, flush=True)
                    turn += 1

    def newTarget(self, target, angle, distance, steps):
        self.target = target
        self.angleToTarget = angle
        self.distToTarget = distance
        self.estimatedSteps = steps
        # print(f"Zombie Id:{self.id}, Target Id: {self.target.id}, Target X:{self.target.x}" +
        #             f", Target Y:{self.target.y}, Angle:{self.angleToTarget / (math.pi / 180) }, distance:{self.distToTarget}", file=stderr, flush=True)

    def update(self, x: int, y: int, nx: int, ny: int): 
        super().update(x, y)
        self.next.x = nx
        self.next.y = ny

class Board:
    def __init__(self, w: int, h: int ):
        self.width = w
        self.height = h

    def printError(self, target):
        print(target, file=stderr, flush=True)


    # Y Positive and Negative poles are flipped (ie postive is down)
    def findAngle(self, y2, y1, x2, x1):
        dx = x2 - x1
        dy = -1 * (y2 - y1)

        # self.printError("X: " + str(dx))
        # self.printError("Y: " + str(dy))

        # Straight up or down
        if dx == 0:
            # Down
            if dy > 0:
                return (3 * math.pi) / 2
            # Up
            else:
                return math.pi / 2

        # Has X value
        angle = math.atan(dy/dx)
        if dx >= 0 and dy >= 0:
            theta = (2 * math.pi) - angle
        # Second Quad or Third Quad
        else:
            theta = math.pi + angle

        return theta

class State(Enum):
    FIND = 1
    PROTECT = 2
    HUNT = 3

class Game:
    def __init__(self, board):
        self.board = board
        self.humans = []
        self.zombies = []
        self.state = State.FIND

    def nextStep(self, speed, angle, x, y):
        ny = int(round(speed * math.sin(angle), 0))
        nx = int(round(speed * math.cos(angle), 0))
        return (x + nx, y - ny)

    # O(n^2)
    def updateZombies(self):
        for zombie in self.zombies:
            # zombie.print()
            # Setup min bounds
            min_dist = self.board.width * self.board.height 
            min_human = None

            # Find closest human
            for human in self.humans:
                distance = dist(zombie.y, human.y, human.x, zombie.x)
                if distance < min_dist:
                    min_dist = distance
                    min_human = human

            # self.printError(min_human)
            # Update zombie's target

            theta = self.board.findAngle(min_human.y, zombie.y, min_human.x, zombie.x)

            # self.printError(theta)
            # Add zombie's next step
            steps = []
            stepX = zombie.next.x
            stepY = zombie.next.y
            steps.append(Pos(stepX, stepY))

            # while (dist(stepY, min_human.y, min_human.x, stepX)) >= 400:
            #     stepX, stepY = self.nextStep(zombie.speed, theta, stepX, stepY)
            #     steps.append(Pos(stepX, stepY))

            zombie.newTarget(min_human, theta, min_dist, steps)

    def printError(self, target):
        print(target, file=stderr, flush=True)
        
def dist(y2: int, y1: int, x2: int, x1: int):
    return math.sqrt((y2 - y1)**2 + (x2 - x1)**2)

def centroid(ys: list, xs: list):
    avg_y = 0
    for i in ys:
        avg_y += i
    avg_y = int(avg_y / len(ys))

    avg_x = 0
    for i in xs:
        avg_x += i
    avg_x = int(avg_x / len(xs))

    return Pos(avg_x, avg_y)

def main():
    board = Board(16000, 9000)
    game = Game(board)
    ash = Ash(0, 0, -1)
    turn = 1
    # game loop
    while True:
        x, y = [int(i) for i in input().split()]
        ash.update(x, y)
        ash.print()

        # Get all humans that are alive this turn
        # game.printError("Getting humans")
        hs = []
        human_count = int(input())
        for i in range(human_count):
            human_id, human_x, human_y = [int(j) for j in input().split()]
            new = Human(human_x, human_y, human_id)
            new.print()
            hs.append(new)
        
        hs.append(ash)
        # Get all zombies that are still dead this turn
        # game.printError("Getting zombies")
        zs = []
        zombie_count = int(input())
        for i in range(zombie_count):
            zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [int(j) for j in input().split()]
            new = Zombie(zombie_x, zombie_y, zombie_id, zombie_xnext, zombie_ynext)
            # new.print()
            zs.append(new)

        game.humans = hs
        game.zombies = zs

        # game.printError("Updating zombies")
        game.updateZombies()


        # If Ash is supposed to find someone to protect
        game.printError(game.state)
        if game.state == State.FIND:
            # Identify human farthest from zombie 
            if ash.target == None or ash.target not in game.humans:
                far_human = None
                far_dist = 0

                print(*game.humans, file=stderr, flush=True)

                for human in game.humans:
                    # print(F"Human Id:{human.id}", file=stderr, flush=True)
                    if human.id != -1:
                        closest_zom = None
                        close_dist = 1000000
                        for zombie in game.zombies:
                            zom_dist = dist(zombie.y, human.y, zombie.x, human.x)
                            print(F"Distance from zombie#{zombie.id}: {zom_dist}", file=stderr, flush=True)
                            
                            if zom_dist < close_dist:
                                close_dist = zom_dist

                            print(F"Closest distance: {close_dist}", file=stderr, flush=True)

                        if close_dist > far_dist:
                            far_dist = close_dist
                            far_human = human

                        print(F"Farthest zombie distance: {far_dist}", file=stderr, flush=True)
                    # print(F"Zombie Id:{zombie.id}, Human Id:{zombie.target.id} Distance:{zombie.distToTarget}", file=stderr, flush=True)
                far_human.print()
                ash.changeTarget(far_human)
            game.printError("Ash target id: " + str(ash.target.id))
            game.printError("Ash distance: " + str(round(dist(ash.target.y, ash.y, ash.x, ash.target.x), 2)))

            if dist(ash.target.y, ash.y, ash.x, ash.target.x) < 1500:
                game.state = State.PROTECT
            else:
                print(f"{ash.target.x} {ash.target.y}")

        # Ash is protecting someone 
        game.printError(game.state)
        if game.state == State.PROTECT:
            # Get all zombies to worry about rn
            cur_zom = []
            for zombie in game.zombies:
                if zombie.target == ash.target:
                    cur_zom.append(zombie)

            must_kill = []
            x = [ash.x]
            y = [ash.y]

            for zombie in cur_zom:
                if zombie.distToTarget < 2000:
                    must_kill.append(zombie)
                    x.append(zombie.x)
                    y.append(zombie.y)
                game.printError(round(zombie.distToTarget, 2))
                game.printError(round(dist(ash.y, zombie.y, zombie.x, ash.x), 2))
            
            game.printError("Print Xs")
            for i in x:
                game.printError(i)

            game.printError("Print Ys")
            for i in y:
                game.printError(i)

            cent = centroid(y, x)

            if cent.x == ash.x and cent.y == ash.y:
                game.state = State.HUNT
            else:
                print(f"X: {cent.x}, Y: {cent.y}", file=stderr, flush=True)
                print(f"{cent.x} {cent.y}")

        # Only zombies that are kite-able remain 
        game.printError(game.state)
        if game.state == State.HUNT:
            # if only one zombie remains
            if len(game.zombies) == 1:
                zom = game.zombies[0]
                print(f"{zom.x} {zom.y}")
                continue
            else:
                zy = [ash.y]
                zx = [ash.x]
                for zom in game.zombies:
                    if dist(zom.next.y, ash.y, zom.next.x, ash.x) < 2500:
                        print(F"Zom Id:{zom.id}, NX:{zom.next.x}, NY:{zom.next.y}", file=stderr, flush=True)
                        zy.append(zom.next.y)
                        zx.append(zom.next.x)
                        game.printError("Dist: " + str(dist(zom.next.y, ash.y, zom.next.x, ash.x)))
                if len(zy) <= 2:
                    target = None
                    distance = 123123123
                    for zom in game.zombies:
                        diff = dist(zom.y, ash.y, zom.x, ash.x)
                        if diff < distance:
                            target = zom
                            distance = diff

                    print(f"{target.x} {target.y}")
                else:
                    cent = centroid(zy, zx)
                    print(F"Cent X:{cent.x}, Cent Y:{cent.y}", file=stderr, flush=True)

                    for zom in game.zombies:
                        if dist(zom.next.y, ash.y, zom.next.x, ash.x) < 2500:
                            print(F"Zom Id:{zom.id}, dist:{dist(cent.y, zom.y, cent.x, zom.x)}", file=stderr, flush=True)
                    print(f"{cent.x} {cent.y}")
        #     pass
        # Write an action using print
        # To debug: print("Debug messages...", file=sys.stderr, flush=True)
        # Your destination coordinates


if __name__ == "__main__":
    main()