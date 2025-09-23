![](data/code-stable.png)

# 07b: VSCode Tutorial
In this tutorial we will explore using an integrated development environment (IDE) for python programming. IDEs offer many advantages over Jupyter Notebooks, particularly for developing production code that will be reused many times and shared with others. The advantages of IDEs include:  
* *Linting* to catch errors, dead code, and other code quality issues
* automatic docstring generation and other auto completion
* code navigation (jumping to function definitions, etc.)
* interactive debugging (including plotting)
* support for automated testing and version control
* unlike Notebooks, code is always executed from start to finish (as it would be by another user), thereby increasing the chances for reproducibility.

VSCode offers the above advantages, and many other features through Extensions (plugins) that can be created by anyone. VSCode is also free and works well with large files (GB in size). The Live Share plugin allows for real-time code collaboration and debugging with multiple people.

## Getting started
If you haven't yet, install VS Code [here](https://code.visualstudio.com/download).

### Converting the Theis exercise notebook to a Python script
Once VSCode is installed, 
* Open ``notebooks/part0_python_intro/solutions/07a_Theis-exercise-solution.ipynb`` in Jupyter 
* From the ``File`` menu, select ``Save and Export Notebook as`` and then ``Executable Script``. This will create a python script version of the notebook (``07a_Theis-exercise-solution.py``)
* Rename this file to ``my_07a_Theis-exercise-solution.py``
* Save ``my_07a_Theis-exercise-solution.py`` to the ``notebooks/part0_python_intro`` folder (or copy it there from your Downloads folder).

### Launching VSCode
* Open a fresh Miniforge prompt from the Start menu and navigate to the root folder for the class (containing the ``AGENDA.md`` file).
* Activate the class python environment (``conda activate pyclass``) if needed. 
* Then type ``code .``
* If prompted, click "Yes, I trust the authors"

### Getting started
See [here](https://code.visualstudio.com/docs/getstarted/userinterface) for an overview of the VSCode user interface.

Once VSCode is launched, click on [the Extensions icon](https://code.visualstudio.com/docs/editor/extension-marketplace) on the Activity Bar on the left. Install the following extensions:  
* Python
* Python indent
* Pylance
* Partial Diff
* Jupyter
* Code spell checker
* autoDocstring
* Rainbow CSV

You may find other cool extensions that you want too. A key indicator of an extension's quality is the number of downloads.

### Linting
Now let's open the script we copied earlier (``notebooks/part0_python_intro/my_07a_Theis-exercise-solution.py``). You can do this from the File Explorer on the left side of the screen.

* as you scroll down through the script, note that "ts" is grayed out in the statement ``for ts in t:`` near line 213. This is the linter telling us that this variable is declared but never used. This is "dead code" that we want remove by refactoring.
* similarly, note further down that the variables ``x`` and ``y`` are underlined near lines 253 and 254. The linter is warning us that these variables were never declared. This is because their declarations were wrapped in the ``get_ipython().run_cell_magic`` statement near line 232, in translation of the notebook to a script.

### Cleaning up the script
Let's clean up the script so that  
* the initial background information is within a docstring (bracketed by triple quotes), instead of commented line by line. We can quickly do this with [column selection](https://code.visualstudio.com/docs/editor/codebasics#_column-box-selection).
* all imports are at the top (below the initial docstring)
* all functions are next below the imports, each surrounded by [two blank lines](https://peps.python.org/pep-0008/#blank-lines).
* two lines below the last function, add the statement: ``"if __name__ == "__main__":``, which [denotes the main body of the script (that gets executed when the script is called)](https://stackoverflow.com/questions/419163/what-does-if-name-main-do). 

To make the script easier to work with, you may want to also turn on Word Wrap (from the ``View`` menu) and [fold all of the code](https://code.visualstudio.com/docs/editor/codebasics#_folding) (control + k + 0).

### Using the Partial Diff plugin to compare two pieces of code
Let's use Partial Diff to compare our script to the class solution. Assuming the Partial Diff Extension was installed earlier,
* open the class solution (``notebooks/part0_python_intro/solutions/07a_Theis-exercise-solution.py``)
* within the solution, highlight any body of code; then right click and ``Select Text for Compare``
* then within your script, highlight the body of code to compare; right click and ``Compare Text with Previous Solution``.
* Partial Diff will open up a third window showing the differences

### Debugging  
* Place a break point anywhere below the first ``theis()`` call in the ``__main__`` part of the script, by clicking to the left of a line number (you should see a red dot).
* If needed, select the ``pyclass` environment as the Python interpreter. Go to ``View --> Command Palette``, then type ``Python: Select Interpreter``. Choose the option with ``(pyclass)`` from the dropdown menu.
* With the Python script (e.g.``07a_Theis-exercise-solution.py``) tab selected, you should see some version numbers followed by ``(pyclass)`` in the bottom right of the VS Code window. Note that you can also click here to change the Python environment.
* Then go to either ``Run --> Start Debugging`` or click on the debug icon in the Activity Bar and choose ``Run and Debug``. Choose ``Python File`` if prompted for a configuration. The debugger should run to the break point.

Often it is prudent to include internal checks in code, regardless of the context. There are a number of ways to do this; a simple one is an ``assert`` statement that checks a condition.

* Add an ``s = `` in front of the first ``theis()`` call to assign the results to a variable, and then in the line below, the following ``assert`` statement:
    ```
    assert np.allclose(s, 1.40636669)
    ```
    This checks that the resulting drawdown is equal to the number on the right within a certain tolerance. 

* try pasting the above assert statement into the debug console at the bottom of your screen. You can also highlight it, right click and ``Evaluate in Debug Console``.

#### The debug working directory
Import ``pathlib`` and type ``pathlib.Path.cwd()`` in the debug console. Note that the current directory is the root folder for the class (where we launched VSCode). VSCode is structured around projects, which include everything in a folder that was opened (and any subfolders). By default, the working directory for debugging is set at the root level for the project. We can change this (and other debugging settings), by creating a configuration file called ``launch.json``, which lives inside of a ``.vscode/`` folder at the root level of the project.

* After stopping the debugging session, make a default ``launch.json`` by clicking on the debug icon in the Activity Bar and then ``create a launch.json file``. Choose ``Python Debugger`` and then ``Python File`` if prompted for a configuration. A new tab will open up with ``launch.json``. Add ``"cwd": "${fileDirname}"`` at the bottom (don't forget the preceding comma!) so that the file looks like this:

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

* run the debugger again. ``Path.cwd()`` should show the ``part0_python_intro`` folder.

#### The Run and Debug view
The Run and Debug view on the left (available via the Activity Bar) shows the current variables in the namespace, and an additional "Watch" panel where we can add specific variables that we want to observe as the script executes. 
* Add a watch for the ``s`` variable by clicking the ``+`` sign on the upper right part of the panel. 
* Now put a breakpoint at the ``return`` statement of the ``theis_xy`` function.
* continue with the debugger (via the ``Run`` menu or debugging toolbar). Execution should stop again at the return statement where we just placed the breakpoint. Notice that ``s`` has changed in the Watch panel. There are also now two layers in the "Call Stack" box below-- one for the ``theis_xy()`` function that we are in, and one for the enclosing the main script.
* step out to the main script by clicking the second item in the call stack (labeled ``<module>``). Notice that ``s`` has changed again, reflecting the current state of ``s`` in that namespace. Notice also that the time-drawdown plot from Step 3 in the original notebook has popped up. 

### Plotting
During a debug session, as long as matplotlib has been imported, one can make plots via the Debug Console or by putting plotting code in the script.

### Automatic docstring generation
Right click at the beginning of the first line *below* the ``def`` statement for any of the functions and choose ``Generate docstring``. The autoDocstring extension should make a new template for a docstring that includes all of the parameters listed in the function signature. 

Note the format of the docstring, which may be different than the [Numpy-style docstrings](https://numpydoc.readthedocs.io/en/latest/format.html) in the class solution (the most widely-used format for scientific Python). To generate Numpy-style docstrings by default, click on [the Extensions icon](https://code.visualstudio.com/docs/editor/extension-marketplace) on the Activity Bar on the left. Find the autoDocstring extension, right click and select ``Settings``. In the ``Auto Docstring: Docstring Format`` drop-down, select ``numpy``.

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

### Liveshare
We will demo the Live Share extension during the class. In the meantime, you can learn more about it [here](https://code.visualstudio.com/learn/collaboration/live-share).