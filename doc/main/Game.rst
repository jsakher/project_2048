2048 : The game
===============

Here are the playable versions of the game 2048.

Terminal version
----------------

To play this version of the game you just need a keyboard, and for greater comfort an *AZERTY* binded one.

Instructions
~~~~~~~~~~~~

You may type in a python shell the follwing line, after what the game will start:

.. code-block:: python

    Game_2048.Launch_2048()

The keys are the following :

    - z : up

    - q : left

    - d : right

    - s : down

To submit the direction, you must press enter after entering it.

.. autoclass:: Game2048.game.Main.Game_2048
    :members: display, down_movement, inverse, left_movement, main, maxcell_find, merge_left,
        newcell, newcell_start, possible_action, right_movement, stack, stop_game, sup_2048, transpose, up_movement


Graphic interface version
-------------------------

A graphical version looking like the classic game is also playable.

Instructions
~~~~~~~~~~~~

The graphical game follows the same instructions as the terminal version; The only difference stands in the python command:

.. code-block:: python

    Game_2048.Launch_2048_visual()


.. image:: ../_images/Human_playing.gif


6561 : An alternative game
==========================

Unlike the 2048 game, this one consists of a 3x3 grid.

Instructions
------------

Type the following code lines :

.. code-block:: python

    Game_2048.Launch_6561()

And play as you do with 2048.

.. autoclass:: Game2048.game.Main.Game_6561

