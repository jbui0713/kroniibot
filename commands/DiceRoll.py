import random

class DiceRoll():
    def __init__(self, input: str):
        self.nums = self.num_check(input)
        
        if self.nums[0] > 0:
            self.roll_dice()

    def roll_dice(self):
        results = []
        for i in range(self.nums[0]):
            roll = random.randint(1, self.nums[1])
            results.append(roll)
        self.message = 'Results: ' + str(results)

    def num_check(self, die_list):
        dice_num = []
        side_num = []
        left_com = False
        parser = list(die_list)
        for char in parser:
            try:
                int(char)
                if left_com is False:
                    dice_num.append(char)
                else:
                    side_num.append(char)
            except:
                if char.lower() == 'd' and left_com is False:
                    left_com = True
                else:
                    self.message = '`{0}` is not a valid input. Format Ex: `?roll 1d20`'.format(die_list)
                    return (-1, -1)
        dice = int(''.join(dice_num))
        side = int(''.join(side_num))
        return (dice, side)
