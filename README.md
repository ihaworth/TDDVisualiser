TDD Visualiser
--
This is an early prototype of a TDD Visualiser.
It plots Number of Tests vs Number of Features vs Complexity.
There's a simple DSL to simulate various testing processes.

Installation
-
I'd recommend using a virtual environment for the python setup:

`python3 -m venv venv`

`source venv/bin/activate`

Then get the required dependencies:

`python3 -m pip install -r requirements.txt`

Run the simulation
-
`python3 3dTDD.py`

Future Ideas
-

* Interaction with scene (rotation) - command line ok, not PyCharm not... need to work out why
* Gradually reveal plot (using space-bar?)
* Address z-order issue with matplotlib?
  * Consider mayavi
* Plot from a git repo?
  * Possible ways to detect different types of commits:
    * Commits could start with Red, Green or Refactor?
    * Maybe we could detect changes only in the `test` directory for 'red'
      * Maybe the next commit after a test commit in the `src` directory is a 'green' commit?
      * All others are refactor commits?
    * Maybe we can run the tests to know if they succeed or fail?
      * Failure indicates a 'red' test being added?
      * Passing immediately after failure indicates 'green'
      * Passing after Passing indicates 'refactoring'
    * Maybe run some kind of complexity metric on each revision?
      * Without this, we're simply guessing at complexity
      * Complexity might go up as we refactor, to then go down much more later
