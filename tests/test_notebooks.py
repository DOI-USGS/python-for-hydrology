import os
from pathlib import Path
import shutil
import glob
import pytest


# Notebooks that we don't expect to execute successfully
# Notebook: reason
xfail_notebooks = {
    '00_python_basics_review.ipynb': 'intentional error',
    '01_functions_scripts.ipynb': 'intentional error',
    '00_python_basics_review__solutions.ipynb': 'intentional error',
    '01_functions_script__solution.ipynb': 'intentional error',
    
}
def included_notebooks():
    include = ['notebooks/part0_python_intro',
               'notebooks/part0_python_intro/solutions',
               'notebooks/part1_flopy/',
               'notebooks/part1_flopy/solutions'
               ]
    files = []
    for folder in include:
        files += sorted(list(Path(folder).glob('*.ipynb')))
    files_with_xfails = []
    for f in files:
        if f.name in xfail_notebooks:
            param_input = pytest.param(
                f, marks=pytest.mark.xfail(reason=xfail_notebooks[f.name]))
        else:
            param_input = f
        files_with_xfails.append(param_input)
    return files_with_xfails


@pytest.fixture(params=included_notebooks(), scope='module')
def notebook(request):
    return request.param


@pytest.fixture(scope='module')
def testdir(request):
    outdir = os.path.join('tests/temp')
    if os.path.isdir(outdir):
        shutil.rmtree(outdir)
    os.mkdir(outdir)

    def teardown():
        if os.path.isdir(outdir):
            shutil.rmtree(outdir)
    request.addfinalizer(teardown)
    return outdir


def test_notebook(notebook, testdir):
    # run autotest on each notebook
    path, fname = os.path.split(notebook)
    cmd = ('jupyter ' + 'nbconvert '
           '--ExecutePreprocessor.timeout=600 '
           '--ExecutePreprocessor.kernel_name=python3 '
           '--to ' + 'notebook '
           f'--execute {notebook} '
           f'--output-dir {testdir} '
           f'--output {fname}')
    ival = os.system(cmd)
    assert ival == 0, f'could not run {fname}'
