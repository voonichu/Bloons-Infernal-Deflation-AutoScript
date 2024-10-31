from infernal import enterInfernal, placeMonkeys, goHome
completions = 0

print('Welcome to auto bloon farm 3.0.')
print('Now with image recognition!')
input('Press enter to start.')

try:
    while True:
        enterInfernal()
        placeMonkeys()
        goHome()
        completions += 1
except KeyboardInterrupt:
    print(f'Total completions: {completions}')