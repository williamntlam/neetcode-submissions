class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # iterate backwards.
        # if the previous car hits the next car, that becomes a fleet.
        # sort first.
        # use a monotonic stack.
        # positions = [0,1,4,7]
        # speed = [1,2,2,1]

        # do i simulate it or can i determine this at the end?
        # I think I can simulate it only? unless there's some intelligent way
        # do solve this.

        # The simulation is O(n^2) I believe. Since the # of steps could be
        # n + n - 1 + n - 2 + ... + 1 = O(n^2)
        # Maybe think it in terms of steps, I can I do need to simulate since I Don't know
        # when fleets will form
        # maybe the key is to find an optimization to the actual simulation.
        
        # process # of turns needed to reach the end for each car.
        # sort first.
        car_info = []
        for index in range(len(position)):
            car_info.append([position[index], speed[index]])

        car_info.sort(key=lambda x: x[0])
        
        turns_to_finish = []
        for current_position, current_speed in car_info:
            num_turns = (target - current_position) / current_speed 
            turns_to_finish.append(num_turns)

        monotonic_stack = []
        for index in range(len(turns_to_finish) - 1, -1, -1):
            num_turn = turns_to_finish[index]
            if not monotonic_stack or num_turn > monotonic_stack[-1]:
                monotonic_stack.append(num_turn)

        # deal with edge case where we reach the last element
        # runtime complexity: O(nlogn) due to the sort.
        # spacetime is O(n)
        return len(monotonic_stack)
