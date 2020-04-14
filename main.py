from building import Building

eight_hundred_eighth = Building("800 8th Street", 12)
one_hundred_one = Building("101 1st st", 2)
two_hundred_one = Building("201 2nd st", 3)
three_hundred_three = Building("303 3rd st", 4)
six_hundred_six = Building("606 12th st", 14)

eight_hundred_eighth.purchase("Trinity")
one_hundred_one.purchase("Keaton")
two_hundred_one.purchase("Roxanne")
three_hundred_three.purchase("Michael")
six_hundred_six.purchase("Alyssa")

eight_hundred_eighth.construct()
one_hundred_one.construct()
two_hundred_one.construct()
three_hundred_three.construct()
six_hundred_six.construct()

print(f"{eight_hundred_eighth.address} was purchased by {eight_hundred_eighth.owner} on {eight_hundred_eighth.date_constructed} and has {eight_hundred_eighth.stories} stories")

print(f"{one_hundred_one.address} was purchased by {one_hundred_one.owner} on {one_hundred_one.date_constructed} and has {one_hundred_one.stories}")

print(f"{two_hundred_one.address} was purchased by {two_hundred_one.owner} on {two_hundred_one.date_constructed} and has {two_hundred_one.stories}")

print(f"{three_hundred_three.address} was purchased by {three_hundred_three.owner} on {three_hundred_three.date_constructed} and has {three_hundred_three.stories}")

print(f"{six_hundred_six.address} was purchased by {six_hundred_six.owner} on {six_hundred_six.date_constructed} and has {six_hundred_six.stories}")
