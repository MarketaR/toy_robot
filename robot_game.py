from robot import Robot


if __name__ == '__main__':
    robot = Robot(placed=False, x=None, y=None, facing=None)
    commands = input(" ")
    commands_list = commands.split(" ")
    for index, command in enumerate(commands_list):
        if command == 'PLACE':
            value = commands_list[index + 1]
            x, y, f = value.split(",")
            robot.place(x, y, f)
        elif command == 'REPORT':
            robot.report()
        else:
            if robot.placed:
                if command == 'MOVE':
                    robot.move()
                elif command == 'LEFT':
                    robot.left()
                elif command == 'RIGHT':
                    robot.right()
                else:
                    pass
