#PascalCase
class StarCookie:
    milk = 0.1
    def __init__(self, color, weight=0):
        # initialize attributes
        self.color = color
        self.weight = weight
        print(f"The  {self.color} cookie is ready.")


# snake_case
star_cookie1 = StarCookie("red")

print(star_cookie1.color)
print(star_cookie1.weight)

star_cookie2 =StarCookie('orange', 10)

print(star_cookie2.weight)
star_cookie2.user = 'yoyo'
print(star_cookie2.user)

# star_cookie1.milk = 0.2
StarCookie.milk = 0.5

print(star_cookie1.__dict__)
print(star_cookie2.__dict__)
print(StarCookie.__dict__)



print(star_cookie1.milk)
print(star_cookie2.milk)
print(StarCookie.milk)

