class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs = sorted(pairs, key=lambda x:x[0], reverse=True)
        stack = []

        for p, s in pairs:
            # time it takes to get to the target
            current_arrival = float(target - p) / s
            stack.append(current_arrival)
            if len(stack) >= 2:
                car_ahead_arrival = stack[-2]
                if current_arrival <= car_ahead_arrival:
                    stack.pop()
        return len(stack)