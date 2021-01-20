import turtle as t


class Breakout():

    def __init__(self):

        self.ball_hit=0
        self.ball_miss=0


        #Setting the main window screen
        self.win = t.Screen()
        self.win.title('Breakout-Demo')
        self.win.bgcolor('#000000')
        self.win.setup(width=600, height=600)
        self.win.tracer(0)

        #Initializing the ball state for the beginning

        self.ball = t.Turtle()
        
        self.ball.shape('circle')
        self.ball.color('red')
        self.ball.penup()
        self.ball.setposition(0, 100)
        self.ball.speed(0)
        self.ball.dx = 3
        self.ball.dy = -3


        # Initialializing the Paddle i.e our agent for  the environment

        self.paddle = t.Turtle()
        self.paddle.shape('square')
        self.paddle.shapesize(stretch_wid=1.5, stretch_len=8)
        self.paddle.color('white')
        self.paddle.penup()
        self.paddle.speed(0)
        self.paddle.setposition(0, -290)

  

        # Score

        self.score = t.Turtle()
        self.score.speed(0)
        self.score.color('white')
        self.score.penup()
        self.score.hideturtle()
        self.score.setposition(0, 0)
        self.score.write("Ball Hit: {}  Ball Missed: {}".format(self.ball_hit, self.ball_miss), align='center', font=(24))
        # -------------------- Keyboard control ----------------------

        self.win.listen()
        self.win.onkey(self.move_Positive_x, 'Right')
        self.win.onkey(self.move_Negative_x, 'Left')


        self.game_over=False
        self.reward_achieved=0 

    # Paddle movement

    def move_Positive_x(self):

        x = self.paddle.xcor()
        if x < 225:
            self.paddle.setx(x+40)

    def move_Negative_x(self):

        x = self.paddle.xcor()
        if x > -225:
            self.paddle.setx(x-40)

    


    # ------------------------ AI control ------------------------

    # 0 move left
    # 1 do nothing
    # 2 move right

    def reset(self):

        self.paddle.setposition(0, -290)
        self.ball.setposition(0, 100)
        return [self.paddle.xcor()*0.01, self.ball.xcor()*0.01, self.ball.ycor()*0.01, self.ball.dx, self.ball.dy]

    def next_iteration(self, action):

        self.reward_achieved = 0
        self.game_over = 0

        if action == 0:
            self.move_Negative_x()
            self.reward_achieved = self.reward_achieved -.1

        if action == 2:
            self.move_Positive_x()
            self.reward_achieved =self.reward_achieved - .1

        self.run_frame()

        state = [self.paddle.xcor()*0.01, self.ball.xcor()*0.01, self.ball.ycor()*0.01, self.ball.dx, self.ball.dy]
        return self.reward_achieved, state, self.game_over

    def run_frame(self):

        self.win.update()

        # Ball moving

        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

        # Ball and Wall collision

        if self.ball.xcor() > 290:
            self.ball.setx(290)
            self.ball.dx = self.ball.dx *-1

        if self.ball.xcor() < -290:
            self.ball.setx(-290)
            self.ball.dx = self.ball.dx *-1

        if self.ball.ycor() > 290:
            self.ball.sety(290)
            self.ball.dy =self.ball.dy * -1

        # Ball Ground contact

        if self.ball.ycor() < -290:
            self.ball.setposition(0, 100)
            self.ball_miss =self.ball_miss + 1
            self.score.clear()
            self.score.write("Ball Hit: {}   Ball Missed: {}".format(self.ball_hit, self.ball_miss), align='center', font=(24))
            self.reward_achieved =self.reward_achieved - 3
            self.game_over = True

        # Ball Paddle collision

        if abs(self.ball.ycor() + 250) < 2 and abs(self.paddle.xcor() - self.ball.xcor()) < 55:
            self.ball.dy =self.ball.dy * -1
            self.ball_hit = self.ball_hit +1
            self.score.clear()
            self.score.write("Ball Hit: {}   Ball Missed: {}".format(self.ball_hit, self.ball_miss), align='center', font=(24))
            self.reward_achieved = self.reward_achieved +3

        count=0    


        #Ball and blocks collision(very painful)
        if block1.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block1.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block2.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block2.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block3.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block3.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block4.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block4.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block5.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block5.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block6.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block6.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block7.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block7.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block8.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block8.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block9.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block9.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block10.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block10.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block11.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block11.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block12.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block12.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block13.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block13.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block14.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block14.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block15.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block15.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block16.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block16.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block17.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block17.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block18.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block18.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block19.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block19.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block20.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block20.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block21.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block21.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block22.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block22.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block23.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block23.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block24.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block24.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block25.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block25.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block26.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block26.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block27.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block27.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block28.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block28.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block29.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block29.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block30.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block30.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block31.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block31.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block32.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block32.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block33.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block33.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block34.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block34.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block35.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block35.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block36.brick_ball(self.ball):
            self.ball.dy *= -1
            block36.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block37.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block37.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block38.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block38.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block39.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block39.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block40.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block40.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block41.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block41.setposition(1000,1000)
            count+=1
            if count==42:
                exit()
        if block42.brick_ball(self.ball):
            self.ball.dy = self.ball.dy *-1
            block42.setposition(1000,1000)
            count+=1
            if count==42:
                exit()




#Main sprite(s) class
class Block(t.Turtle):
    def __init__(self, spriteshape, color, startx, starty):
        t.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.setposition(startx, starty)
        self.speed = 1

    def brick_ball(self, other):
        if (self.xcor() >= (other.xcor() - 50)) and \
        (self.xcor() <= (other.xcor() + 50)) and \
        (self.ycor() >= (other.ycor() - 20)) and \
        (self.ycor() <= (other.ycor() + 20)):
            return True
        else:
            return False
    


#Block class
class Brick(Block):
    def __init__(self, spriteshape, color, startx, starty):
        Block.__init__(self, spriteshape, color, startx, starty)
        self.shapesize(stretch_wid=0.80, stretch_len=5, outline=None)
        self.speed = 0


#EACH LINE HAS 7 BLOCKS
#LINE 1
block1=Brick("square", "red", -340, 280)
block2=Brick("square", "red", -230, 280)
block3=Brick("square", "red", -120, 280)
block4=Brick("square", "red", -10, 280)
block5=Brick("square", "red", 100, 280)
block6=Brick("square", "red", 210, 280)
block7=Brick("square", "red", 320, 280)
#LINE 2
block8=Brick("square", "orange", -340, 255)
block9=Brick("square", "orange", -230, 255)
block10=Brick("square", "orange", -120, 255)
block11=Brick("square", "orange", -10, 255)
block12=Brick("square", "orange", 100, 255)
block13=Brick("square", "orange", 210, 255)
block14=Brick("square", "orange", 320, 255)
#LINE 3
block15=Brick("square", "yellow", -340, 230)
block16=Brick("square", "yellow", -230, 230)
block17=Brick("square", "yellow", -120, 230)
block18=Brick("square", "yellow", -10, 230)
block19=Brick("square", "yellow", 100, 230)
block20=Brick("square", "yellow", 210, 230)
block21=Brick("square", "yellow", 320, 230)
#LINE 4
block22=Brick("square", "olive", -340, 205)
block23=Brick("square", "olive", -230, 205)
block24=Brick("square", "olive", -120, 205)
block25=Brick("square", "olive", -10, 205)
block26=Brick("square", "olive", 100, 205)
block27=Brick("square", "olive", 210, 205)
block28=Brick("square", "olive", 320, 205)
#LINE 5
block29=Brick("square", "green", -340, 180)
block30=Brick("square", "green", -230, 180)
block31=Brick("square", "green", -120, 180)
block32=Brick("square", "green", -10, 180)
block33=Brick("square", "green", 100, 180)
block34=Brick("square", "green", 210, 180)
block35=Brick("square", "green", 320, 180)
#LINE 6
block36=Brick("square", "blue", -340, 155)
block37=Brick("square", "blue", -230, 155)
block38=Brick("square", "blue", -120, 155)
block39=Brick("square", "blue", -10, 155)
block40=Brick("square", "blue", 100, 155)
block41=Brick("square", "blue", 210, 155)
block42=Brick("square", "blue", 320, 155)



# while True:
#
#      env.run_frame()
