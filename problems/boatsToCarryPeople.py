# Trying to add people in safety boats
# People array : consists of people's weights
# Every person has a weigh lower than or equal to limit
# Each boat can carry at most limit
# Each boat carries at most 2 people at the same time.
# Their weight sum is at most limit.
# Return the minimum number of boats to carry people


class BoatProblem:

    def carryPeopleUpToLimit(self, people_arr, limit):
        boat_num = 0
        left = 0
        right = len(people_arr) - 1
        people_arr.sort()
        while left <= right:
            if left == right:
                boat_num += 1
                break
            if (people_arr[left] + people_arr[right]) <= limit:
                left += 1
                right -= 1
                boat_num += 1
            else:
                right -= 1
                boat_num += 1
        print(boat_num)
        return boat_num


people = [3, 2, 2, 1]
lim = 3
b = BoatProblem()
b.carryPeopleUpToLimit(people, lim)

print("*****")
people2 = [1, 2]
lim2 = 3
b.carryPeopleUpToLimit(people2, 3)

print("*****")
b.carryPeopleUpToLimit([5, 2, 7, 1, 4], 8)

print("*****")
b.carryPeopleUpToLimit([5, 5, 7, 1, 4], 8)

print("*****")