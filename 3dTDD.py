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


class TDDPlot:
    def __init__(self, initial_point) -> None:
        super().__init__()
        self.current_point = initial_point

    def apply_delta(self, point, delta):
        return (point[0] + delta[0],
                point[1] + delta[1],
                point[2] + delta[2])

    def plot_line(self, from_point, to_point, colour):
        plt.plot([from_point[0], to_point[0]],
                 [from_point[1], to_point[1]],
                 [from_point[2], to_point[2]], 'o' + colour + '-')

    def plot_step(self, delta, colour):
        new_point = self.apply_delta(self.current_point, delta)
        self.plot_line(self.current_point, new_point, colour)
        self.current_point = new_point
        return self

    def red(self):
        # Add red Test
        return self.plot_step((step, 0.0, 0.0), 'r')

    def green(self):
        # Add Feature + Complexity
        return self.plot_step((0.0, step, step), 'g')

    def refactor(self):
        # Reduce Complexity
        return self.plot_step((0.0, 0.0, -small_step), 'b')

    def backfill_test(self):
        # Add green Test
        return self.plot_step((step, 0.0, 0.0), 'g')


simple_tdd_plot = TDDPlot((0.0, 0.0, 0.0))

simple_tdd_plot.\
    red().green().\
    red().green().\
    red().green().\
    refactor().\
    refactor().\
    refactor().\
    red().green().\
    red().green().\
    red().green().\
    refactor().\
    refactor().\
    refactor()

legacy_rescue_plot = TDDPlot((0.0, 9.0, 9.0)).\
    backfill_test().\
    backfill_test().\
    backfill_test().\
    backfill_test().\
    backfill_test().\
    backfill_test().\
    backfill_test().\
    refactor().\
    refactor().\
    refactor().\
    refactor().\
    refactor().\
    refactor().\
    refactor().\
    refactor().\
    refactor().\
    refactor()

plt.show()

# Interaction with scene (rotation) - command line ok, not PyCharm not... need to work out why
# Gradually reveal plot (using spacebar?)
# Plot from a git repo? Commits need to start with Red, Green or Refactor?