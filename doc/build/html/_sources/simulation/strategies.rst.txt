Simulations
===========

Stats
~~~~~

Four strategies are implemented (available in :py:class:`Game2048.game.Main.Game_2048`).

For each one we simulate n=300.000 games and plot the score obtained over this number of simulation. 

Let :math:`s` the score fonction of a given strategy game. Using the following functions : 

.. math:: 

    \mu = \mathbb{E}(s(strategy)) = \frac{1}{300000} * \sum_{i=1}^{300000} s_{i}(strategy)

.. math:: 

    \sigma^{2} = \mathbb{V}(strategy) = \frac{1}{300000} * \sum_{i=1}^{300000}(s_{i}(strategy) - \mathbb{E}(s(strategy)))^{2},

a 95% confidence interval of the mean score, given by, 

.. math:: 

    [\mu - 1.96 * \sqrt{\frac{\sigma^{2}}{n}} \; , \; \mu + 1.96 * \sqrt{\frac{\sigma^{2}}{n}}] \; ,

is also provided on the graphs.

Note
~~~~

Python scripts of confidence intervals builder and their plot are available for consultation 
in the submodule *Stats* of *Game2048* in the github repository.
