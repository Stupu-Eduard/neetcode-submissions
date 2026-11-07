class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        ordered_fleet = dict()
        res = 0

        for p,s in zip(position,speed):
            ordered_fleet[p] = s
        ordered_fleet = dict(sorted(ordered_fleet.items()))

        if len(position) == 1:
            return 1

        k0,v0 = ordered_fleet.popitem()
        prev_steps_to_target = (target - k0) / v0

        while ordered_fleet:
            k,v = ordered_fleet.popitem()
            steps_to_target = (target - k) / v
            
            #print(f"{steps_to_target} {(target - k) / v} {prev_steps_to_target} {k}")
            if steps_to_target > prev_steps_to_target:
                res += 1
                prev_steps_to_target = steps_to_target

            

        return res + 1