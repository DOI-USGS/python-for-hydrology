import json
import os
from pathlib import Path
import shutil
import sys
sys.path.append('notebooks')
import pytest
from clear_all_notebooks import skip_notebooks as leave_output_in


def included_notebooks():
    include = ['notebooks/part0_python_intro',
               'notebooks/part1_flopy/',
               ]
    included_notebooks = []
    for folder in include:
        included_notebooks += sorted(list(Path(folder).glob('*.ipynb')))
    return included_notebooks


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


def test_notebook_output(notebook):
    # run autotest on each notebook
    if notebook.name not in leave_output_in:
        with open(notebook) as src:
            data = src.read()
            data = json.loads(data)
            for item in data['cells']:
                for k, v in item.items():
                    if item['cell_type'] == 'code':
                        assert not any (item['outputs']),\
                            (f"{notebook} has output "
                                "but is not listed in notebooks/clean_all_notebooks.py "
                                "as excepted!")
    else:
        with open(notebook) as src:
            data = src.read()
            data = json.loads(data)
            outputs = []
            for item in data['cells']:
                for k, v in item.items():
                    if item['cell_type'] == 'code' and item['outputs']:
                        outputs.append(item['outputs'])
            assert outputs,\
                (f"{notebook} is expected to have outputs but has none!\n"
                 "Re-run this notebook and save with the outputs.")