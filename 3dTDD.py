import matplotlib.pyplot as plt

step = 1
small_step = 0.5

ax = plt.figure().add_subplot(projection='3d')

# ax.legend()
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel('Tests')
ax.set_ylabel('Features')
ax.set_zlabel('Complexity')


def apply_delta(point, delta):
    return (point[0] + delta[0],
            point[1] + delta[1],
            point[2] + delta[2])


def plot_line(current_point, new_point, colour):
    plt.plot([current_point[0], new_point[0]],
             [current_point[1], new_point[1]],
             [current_point[2], new_point[2]], 'o' + colour + '-')


def red(current_point):
    # Red/Test
    new_point = apply_delta(current_point, (step, 0.0, 0.0))
    plot_line(current_point, new_point, 'r')
    return new_point


def green(current_point):
    # Green/Feature + Complexity
    new_point = apply_delta(current_point, (0.0, step, step))
    plot_line(current_point, new_point, 'g')
    return new_point


def refactor(current_point):
    # Refactor/Reduce Complexity
    new_point = apply_delta(current_point, (0.0, 0.0, -small_step))
    plot_line(current_point, new_point, 'b')
    return new_point

def backfill_test(current_point):
    # Green/Feature + Complexity
    new_point = apply_delta(current_point, (step, 0.0, 0.0))
    plot_line(current_point, new_point, 'g')
    return new_point



current_point = (0.0, 0.0, 0.0)

current_point = red(current_point)
current_point = green(current_point)

current_point = red(current_point)
current_point = green(current_point)

current_point = red(current_point)
current_point = green(current_point)

current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)

current_point = red(current_point)
current_point = green(current_point)

current_point = red(current_point)
current_point = green(current_point)

current_point = red(current_point)
current_point = green(current_point)

current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)


current_point = (0.0, 9.0, 9.0)

current_point = backfill_test(current_point)
current_point = backfill_test(current_point)
current_point = backfill_test(current_point)
current_point = backfill_test(current_point)
current_point = backfill_test(current_point)
current_point = backfill_test(current_point)
current_point = backfill_test(current_point)

current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)
current_point = refactor(current_point)


plt.show()

# Interaction with scene (rotation)
# Gradually reveal plot (using spacebar?)
# Other plots (Gilded Rose)
# Plot from a git repo? Commits need to start with Red, Green or Refactor?