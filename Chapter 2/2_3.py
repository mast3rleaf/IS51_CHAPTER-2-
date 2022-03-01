
# print("one", "two", "three", sep=",")
# print("Hello", end=" ")
# print("World!")
# print("a\tb\tc")
# print("a\tb\tc\nd\te\tf")
# print("\"Hello World!\"")
# str1 = "There is a {0}% probability that the stock market will crash tomorrow and {1}% probability it will rally!",format(10, 50)
# print(str1.format(10,50))

print("{0:^5s}{1:<20s}{2:>3s}".format("Rank", "Player", "HR"))
print("{0:^5n}{1:<20s}{2:>3n}".format(1, "Barry Bonds", 762))
print("{0:^5n}{1:<20s}{2:>3n}".format(2, "Hank Aaron", 755))
print("{0:^5n}{1:<20s}{2:>3n}".format(3, "Babe Ruth", 714))

str2 = "The population of {0:s} is {1:.2%} of the U.S. population."
print(str2.format("Texas", 26440000/309000000))
