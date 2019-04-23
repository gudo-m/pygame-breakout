

def get_action(paddle_x, ball_x, ball_y, ball_speed):
    act = -1
    offset = abs(paddle_x - ball_x)
    if offset > 25:
        if paddle_x < ball_x:
            act = 1
        elif paddle_x > ball_x:
            act = 0
    elif offset <= 25 and ball_y > 330:
        if abs(ball_speed[0]) > 3:
            if ball_speed[0] <= 0:
                act = 1
            else:
                act = 0
        else:
            if ball_speed[0] <= 0:
                act = 0
            else:
                act = 1
    return act
