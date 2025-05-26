"""
File: datby001_assignment2.py 
Description: <>
Author:Bhavya Datta
ID:1104088071
username: dayby001
This is my own work as defined by University's Academic Misconduct Policy.
"""

class Robot:
    def __init__(self, model, tier):
        self.model = model #"WALL-E"
        self.tier = tier #Elite
        self.performance = 0.0

class BoostRobot(Robot):
    def __init__(self, model, tier, acceleration_rate, battery_efficiency):
        super().__init__(model, tier)
        self.acceleration_rate = acceleration_rate
        self.battery_efficiency = battery_efficiency

    def calculate_performance(self):
        performance_score = self.acceleration_rate + self.battery_efficiency
        
        if self.tier == "Basic":
            performance_score *= 1.5
        elif self.tier == "Advanced":
            performance_score *= 2.8
        elif self.tier == "Elite":
            performance_score *= 4.6
        
        self.performance = performance_score
        return self.performance



    