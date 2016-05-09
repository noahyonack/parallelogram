# This is Parallelogram.

Parallelogram is a parallelization package that distributes computationally intensive programs across machines in a distributed system using a distribution model similar to that of the ride-sharing service Uber.

## Documentation:

Before you begin reading the README, please note that extensive documentation of the code itself can be found in documentation/pydoc. There you will find autogenerated HTML files corresponding to our code and dependencies. To view these files, simply open them in your web browser of choice.

## To begin using:

Clone and `cd` into the repository. Simply run `sudo python setup.py install` to install the package. Running this command will install all the necessary external dependencies.

To use this library, execute:

`python parallelogram_server.py`

Then, in another window, navigate to the root directory and execute your program, via:

`python filename.py`

All `filename.py` needs to do is import Parallelogram (as with `from parallelogram import parallelogram`),
and call one of our methods like so:

`result = parallelogram.p_map(foo, range(10000), PORT, 30)`,

where `foo` is a function to map over `range(10000)`, and PORT is 1001. This port configuration variable can be changed in `/parallelogram/config.py` if needed.

## How exactly does distribution work?

Uber has a pool of users that can be classified as
either passengers or drivers. When a passenger Sarah requires a lift, she broadcasts a request, which alerts nearby drivers who can then decide to either accept or ignore the request. Drivers who are already carrying passengers oftentimes do not accept the request, and only those drivers who are completely available (and ideally nearby) consider picking up Sarah. Once an Uber driver confirms Sarah’s request, all other available drivers are notified that Sarah no longer needs a ride.

This ride­sharing system will serve as the foundation of our parallelization model. Our library will, on a single machine, partition pieces of the client’s program into parallelizable
chunks.

## What methods does this library expose?
* `p_map(foo, data)`
    * Map a function `foo()` over `data` (of type list). `p_map()` modifies `data` in place
and supplies `foo()` with both the current element of the list and its
respective index.
* `p_filter(foo, data)`
    * Filter `data` (of type list) via a predicate formatted as a function.
* `p_reduce(foo, data)`
    * Reduce `data` (of type list) by continually applying `foo()` to subsequent
	elements of `data`.

## Package Structure

`MANIFEEST.in`: Tells setuptools to include the README when generating source distributions. Otherwise, only Python files will be included.

## How can I run or write tests?

Nose is a Python package that makes running the tests themselves easy. It automatically gets installed when you run `python setup.py install`. To run tests, navigate to the root directory. Then:

`nosetests`

Test files live in `/tests/local` and `/tests/distributed` and can be runing `nosetests` from the root directory.