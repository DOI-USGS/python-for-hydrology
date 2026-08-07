![](data/code-stable.png)

# 07: VSCode Tutorial
In this tutorial we will briefly explore using an integrated development environment (IDE) for python programming. For a more extensive look at VSCode, see the [full demo](bonus_examples/full_VSCode_demo.md) in the bonus examples. IDEs offer many advantages over Jupyter Notebooks, particularly for developing production code that will be reused many times and shared with others. The advantages of IDEs include:  
* *Linting* to catch errors, dead code, and other code quality issues
* automatic docstring generation and other auto completion
* code navigation (jumping to function definitions, etc.)
* interactive debugging (including plotting)
* support for automated testing and version control
* unlike Notebooks, code is always executed from start to finish (as it would be by another user), thereby increasing the chances for reproducibility.

VSCode offers the above advantages, and many other features through Extensions (plugins) that can be created by anyone. VSCode is also free and works well with large files (GB in size). The Live Share plugin allows for real-time code collaboration and debugging with multiple people.

## Getting started
If you haven't yet, install VS Code [here](https://code.visualstudio.com/download).

### Launching VSCode
* Open a fresh Miniforge prompt from the Start menu and navigate to the root folder for the class (containing the ``AGENDA.md`` file).
* Activate the class python environment (``conda activate pyclass``) if needed. 
* Then type ``code .``
* If prompted, click "Yes, I trust the authors"

*Alternatively*

* Launch VSCode and from the initial screen or File menu choose Open. Navigate to the root folder for the class and select it


### Getting started
See [here](https://code.visualstudio.com/docs/getstarted/userinterface) for an overview of the VSCode user interface.

Once VSCode is launched, click on [the Extensions icon](https://code.visualstudio.com/docs/editor/extension-marketplace) on the Activity Bar on the left. Install the following extensions:  
* Python
* Python indent
* Pylance
* Jupyter
* Code spell checker
* autoDocstring
* Rainbow CSV

You may find other cool extensions that you want too. A key indicator of an extension's quality is the number of downloads.


### Linting
Now let's open the script ``notebooks/part0_python_intro/bonus_examples/solutions/Theis-exercise-solution.py``.
* On the left toolbar, select the Explorer icon (that looks like a stack of papers). In the file tree below, navigate to the script and select it.
* This script looks pretty clean, with no obvious issues except a lot of comments
* Try adding `import pandas as pd` to the imports. Notice how the `pd` is grayed out. The linter is flagging this as "dead code" that is declared but never used.
* Below the imports, type `pd.DataFrame(stuff)`. The `pd` above is no longer grayed out, because now it is used, but there is a yellow squiggly line beneath stuff, because this variable is being used but wasn't declared.
* Linters are valuable tools that make it easy to write clean code!


To make the script easier to work with, you may want to also turn on Word Wrap (from the ``View`` menu) and [fold all of the code](https://code.visualstudio.com/docs/editor/codebasics#_folding) (control + k + 0).



### Debugging  
* Place a break point on line 99, by `return s` in the `theis()` function, by clicking to the left of a line number (you should see a red dot).
* If needed, select the ``pyclass` environment as the Python interpreter. Go to ``View --> Command Palette``, then type ``Python: Select Interpreter``. Choose the option with ``(pyclass)`` from the dropdown menu.
* With the Python script (e.g.``Theis-exercise-solution.py``) tab selected, you should see some version numbers followed by ``(pyclass)`` in the bottom right of the VS Code window. Note that you can also click here to change the Python environment.
* Then go to either ``Run --> Start Debugging`` or click on the debug icon in the Activity Bar and choose ``Run and Debug``. Choose ``Python File`` if prompted for a configuration. The debugger should run to the break point.

#### The debug working directory
Import ``pathlib`` and type ``pathlib.Path.cwd()`` in the debug console. Note that the current directory is the root folder for the class (where we launched VSCode). VSCode is structured around projects, which include everything in a folder that was opened (and any subfolders). By default, the working directory for debugging is set at the root level for the project. We can change this (and other debugging settings), by creating a configuration file called ``launch.json``, which lives inside of a ``.vscode/`` folder at the root level of the project.

* After stopping the debugging session, make a default ``launch.json`` by 
  * clicking on the debug icon in the Activity Bar and then 
  * ``create a launch.json file``. 
  * Choose ``Python Debugger`` and then ``Python File`` if prompted for a configuration. 
  * A new tab will open up with ``launch.json``. 
  * Add ``"cwd": "${fileDirname}"`` at the bottom (don't forget the preceding comma!) so that the file looks like this:

    ```json
    {
        // Use IntelliSense to learn about possible attributes.
        // Hover to view descriptions of existing attributes.
        // For more information, visit: https://go.microsoft.com/fwlink/?linkid=830387
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: Current File",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "integratedTerminal",
                "cwd": "${fileDirname}"
            }
        ]
    }
* simply making a new file at `.vscode/launch.json` (within the root folder for the class), and pasting in the above text also works.
* run the debugger again. ``Path.cwd()`` should show the ``part0_python_intro`` folder.

#### The Run and Debug view
The Run and Debug view on the left (available via the Activity Bar) shows the current variables in the namespace, and an additional "Watch" panel where we can add specific variables that we want to observe as the script executes. 
* Add a watch for the ``s`` variable by clicking the ``+`` sign on the upper right part of the panel. 
* Now put a breakpoint at the ``return`` statement of the ``theis_xy`` function.
* continue with the debugger (via the ``Run`` menu or debugging toolbar). Execution should stop again at the return statement where we just placed the breakpoint. Notice that ``s`` has changed in the Watch panel. There are also now two layers in the "Call Stack" box below-- one for the ``theis_xy()`` function that we are in, and one for the enclosing main script.
* step out to the main script by clicking the second item in the call stack (labeled ``<module>``). Notice that ``s`` has changed again, reflecting the current state of ``s`` in that namespace. Notice also that the time-drawdown plot from Step 3 in the original notebook has popped up. 

### Plotting
During a debug session, as long as matplotlib has been imported, one can make plots via the Debug Console or by putting plotting code in the script.

**If the plot isn't showing up**
* Try making the plot by starting with `fig, ax = plt.subplots()` syntax (instead of `plt.plot()`)
* Then in the debug console enter `fig.show()` or `plt.draw()`
* Alternativey, try `plt.pause(1)`
* On Windows, look in the task bar for a matplotlib icon  <img src="https://upload.wikimedia.org/wikipedia/commons/8/84/Matplotlib_icon.svg" alt="drawing" width="40"/> (or press Alt + Tab to show the open windows)

### [Code navigation](https://code.visualstudio.com/docs/editor/editingevolved)
In the main part of the script, right click on one of the function calls (e.g. ``theis``) and choose ``Go to Definition``. VSCode should take you to where the function is defined. Right clicking on ``theis`` after the ``def`` and then ``Go to References`` opens a "peek" window with a list of all of the times ``theis()`` is called. Clicking on one of them takes you to that location in the script.

Navigation works across modules and packages too. If you right click on ``np.meshgrid`` in the main part of the script and ``Go to Definition``, VSCode takes you to the relevant code in ``numpy``.

### Code search
VS Code's powerful search capabilities are another key feature. 
* To search for text within a script (for example, the ``theis_xy`` function name), select ``Edit --> Find`` or press ``Ctrl+F``. 
* You can also highlight text and press ``Ctrl+F`` to auto-fill the search bar. 
* ``Edit --> Find in Files`` will quickly search across all files in a project (i.e., everything within the root folder for the class, which we launched VS Code from earlier). 
* ``Edit --> Replace in Files`` can be used to quickly refactor variable names across multiple code modules.
* In complex scripts or workflows, **ease of search is a key reason to choose meaningful and unique variable names!**
