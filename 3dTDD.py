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

    def plot_line(self, current_point, new_point, colour):
        plt.plot([current_point[0], new_point[0]],
                 [current_point[1], new_point[1]],
                 [current_point[2], new_point[2]], 'o' + colour + '-')

    def red(self):
        # Red/Test
        new_point = self.apply_delta(self.current_point, (step, 0.0, 0.0))
        self.plot_line(self.current_point, new_point, 'r')
        self.current_point = new_point
        return self

    def green(self):
        # Green/Feature + Complexity
        new_point = self.apply_delta(self.current_point, (0.0, step, step))
        self.plot_line(self.current_point, new_point, 'g')
        self.current_point = new_point
        return self

    def refactor(self):
        # Refactor/Reduce Complexity
        new_point = self.apply_delta(self.current_point, (0.0, 0.0, -small_step))
        self.plot_line(self.current_point, new_point, 'b')
        self.current_point = new_point
        return self

    def backfill_test(self):
        # Green/Feature + Complexity
        new_point = self.apply_delta(self.current_point, (step, 0.0, 0.0))
        self.plot_line(self.current_point, new_point, 'g')
        self.current_point = new_point
        return self


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