Strategies battle
=================

It 's possible to launch two games with given strategies. To see them compete in a terminal, 
write the following line in a python shell : 

.. code-block:: python

    Game2048.versus(strategy1='random', strategy2='random', skip=False, speed=0.5)

.. autofunction:: Game2048.AI_versus.versus

New data comparison
===================

You can generate a new data set of strategies mean score and max cell, and compare them with the original one.
To do so, execute this command (you can change parameters, see the documentation below) : 

.. code-block:: python

    Game2048.Stats.Makedata(n)

.. autofunction:: Game2048.Stats.Makedata.Makedata