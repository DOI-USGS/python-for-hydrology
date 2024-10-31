Contributing
=======================================

Contributions are welcome from the community. Questions can be asked on the
[issues page][1]. Before creating a new issue, please take a moment to search
and make sure a similar issue does not already exist. If one does exist, you
can comment (most simply even with just a `:+1:`) to show your support for that
issue.

If you have direct contributions you would like considered for incorporation
into the project you can [fork this repository][2] and
[submit a pull request][3] for review.


[1]: https://github.com/DOI-USGS/python-for-hyrology/issues
[2]: https://help.github.com/articles/fork-a-repo/
[3]: https://help.github.com/articles/about-pull-requests/


Adding a Notebook
--------------------
1) Fork the repository
2) Install the `docs/docs-environment.yml` python environment, which has a few extra packages for building the HTML documentation.
3) See the existing `notebooks/` for examples.
4) When developing the notebook, pay attention to the markdown header levels:
    * `#` for the title, which will appear in the Table of Contents tree on the left, and as the caption for the thumbnail.
    * `##` for subheaders, which will also appear in the Table of Contents tree.
    * `###` and `####` between subheaders, as needed.
5) For now, each notebook title begins with the number (e.g. "01: Title").
6) Including output or not:

    * Currently, output in the exercise notebooks (not in the `solutions/` subfolders) should be cleared prior to submitting a PR, unless the notebook is listed as excepted in `notebooks/clear_all_notebooks.py`. The `.github/workflows/notebook-output.yaml` workflow will check for output in non-solution notebooks.

7) Notebook execution

    * Notebooks that don't have saved output will be executed by `nbsphinx`, so that the output is rendered in the HTML docs.
    * Excessive errors can be quieted by importing `warnings` at the top, and then including `warnings.filterwarnings("ignore")` within the offending cell.
    * Alternatively, screen output for a given cell can be turned off by including `%%capture` at the top.

8) Testing

    * The `.github/workflows/test.yaml` workflow will check for successful notebook execution.
    * If your notebook has intentional errors, consider just showing the error in a markdown block (wrapped in python`````` so that the syntax gets highlighted).
    * Otherwise, include the notebook in the `xfail_notebooks` list in `tests/test_notebooks.py`, so that the notebook gets marked as expected to fail (and doesn't fail the test workflow).


9) Adding the notebook to the example gallery
    
    * Edit the `copy_notebooks` list in `docs/conf.py` to add the notebook. This will copy the notebook to the `docs/notebooks` folder so that it can be rendered in the documentation.
    * Edit `part0.rst`, `part1.rst` or `bonus_examples.rst` to add the notebook to the appropriate example gallery. 
    * At the command line run `make -C docs html`
    * Check the results by entering `file:///<path to your notebook>` into a web browser
    * By default, the thumbnail icon is made from the last plot (if one exists). Otherwise, see the [nbsphinx instructions on thumbnails](https://nbsphinx.readthedocs.io/en/0.9.3/subdir/gallery.html#) to use another plot or include a static thumbnail.