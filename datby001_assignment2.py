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
        self.performance = 5.0
    
    def __str__(self):
        return f"{self.model} ({self.tier}) - Performance: {self.performance}"


class BoostRobot(Robot): #Robot A
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
    
    def __str__(self):
        return f"{self.model} ({self.tier}) - Accel: {self.acceleration_rate}, Battery: {self.battery_efficiency}, Perf: {self.performance}"

    
class FocusRobot(Robot): #ROBOT B
    def __init__(self, model, tier, calm_factor, stays_alert):
        super().__init__(model, tier)
        self.calm_factor = calm_factor      
        self.stays_alert = stays_alert      

    def calculate_performance(self):
        result = self.calm_factor

        if self.tier == "Basic":
            result *= 1.5
        elif self.tier == "Advanced":
            result *= 2.8
        elif self.tier == "Elite":
            result *= 4.6

        if self.stays_alert:
            result *= 1.2
        else:
            result *= 0.85

        self.performance = result
        return self.performance
    
    def __str__(self):
        return f"{self.model} ({self.tier}) - Calm: {self.calm_factor}, Alert: {self.stays_alert}, Perf: {self.performance}"


class GamerRobot(Robot): #Robot C
    def __init__(self, model, tier, games):
        super().__init__(model, tier)
        self.games = games  # list of game titles

    def calculate_performance(self):
        score = 0.0

        if isinstance(self.games, list):
            game_set = set(self.games)
            score += len(game_set) * 0.5

        if self.tier == "Basic":
            score *= 1.5
        elif self.tier == "Advanced":
            score *= 2.8
        elif self.tier == "Elite":
            score *= 4.6

        self.performance = score
        return self.performance
    
    def __str__(self):
        return f"{self.model} ({self.tier}) - Games: {len(self.games)}, Perf: {self.performance}"


    