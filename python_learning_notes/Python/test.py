class AC:
    def cold_wind(self):
        """制冷"""
        pass

    def hot_wind(self):
        """制热"""
        pass

    def swing_left_right(self):
        """左右摆风"""
        pass

class Midea_AC(AC):
    def cold_wind(self):
        """制冷"""
        print("美的空调制冷")

    def hot_wind(self):
        """制热"""
        print("美的空调制热")

    def swing_left_right(self):
        """左右摆风"""
        print("美的空调左右摆风")

class Gree_AC(AC):
    def cold_wind(self):
        """制冷"""
        print("格力空调制冷")

    def hot_wind(self):
        """制热"""
        print("格力空调制热")

    def swing_left_right(self):
        """左右摆风"""
        print("格力空调左右摆风")

def make_cool(ac: AC):
    ac.cold_wind()

midea_ac = Midea_AC()
gree_ac = Gree_AC()
make_cool(midea_ac)# 输出美的空调制冷
make_cool(gree_ac)# 输出格力空调制冷
