from datby001_assignment2 import BoostRobot, FocusRobot, GamerRobot

robot1 = BoostRobot("Speedy", "Elite", 7.5, 8.0)
robot1.calculate_performance()
print(robot1.model, robot1.tier, robot1.performance)

robot2 = FocusRobot("CalmEye", "Advanced", 6.0, True)
robot2.calculate_performance()
print(robot2.model, robot2.tier, robot2.performance)

robot3 = GamerRobot("GameMaster", "Basic", ["Chess", "Pac-Man", "Chess", "Tetris"])
robot3.calculate_performance()
print(robot3.model, robot3.tier, robot3.performance)
