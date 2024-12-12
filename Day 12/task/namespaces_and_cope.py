# Local Scope
# Variables (or functions) declared inside functions have
# local scope (also called function scope).
# They are only seen by other code within the same block of code.
#
# e.g.
# def my_function():
#     my_local_var = 2
#
# # This will cause a NameError
# print(my_local_var)
#
# Global Scope
# Variables or functions declared at the top level (unindented)
# of a code file have global scope. It is accessible anywhere
# in the code file.
#
# e.g.
# my_global_var = 3
#
# def my_function():
#     # This works no problems
#     print(my_global_var)

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")

increase_enemies()
print(f"enemies outside function: {enemies}")

# Local Scope
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
#
# drink_potion()
# Can't access this potion_strength outside of its scope
# print(potion_strength)

# Global Scope
player_health = 10

def game():
    def drink_potion():
        potion_strength = 2
        print(player_health)

    drink_potion()

print(player_health)

