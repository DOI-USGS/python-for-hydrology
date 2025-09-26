import json
import os
from pathlib import Path
import shutil
import sys
import pytest


skip_notebooks = [
    'notebooks/part0_python_intro/solutions/00_skills_test_on_basics__solution.ipynb'
]

error_instructions = (
    "Each notebook should begin (somewhere before the first code cell)\n"
    "with a title level header ('#' or header level 1), followed by a\n"
    "02d formatted number for the notebook. For example:\n"
    "'# 01: Introduction to Flopy'.\n"
    "There should only be one title level header."
    )

def get_included_notebooks():
    """Only test the notebooks that are included 
    in the parts 0 and 1 galleries."""
    included_notebooks = []
    for index_file in ['docs/source/part0.rst', 
                       'docs/source/part1.rst']:
        with open(index_file) as src:
            for line in src:
                line = line.strip()
                if line.startswith('notebooks/part'):
                    nb_path = Path(line)
                    assert nb_path.exists()
                    if not nb_path.suffix == '.md':
                        included_notebooks.append(nb_path)
    return included_notebooks


@pytest.fixture(params=get_included_notebooks(), scope='module')
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


def test_notebook_header(notebook):
    # run autotest on each notebook
    with open(notebook) as src:
        data = src.read()
        data = json.loads(data)
        in_header = True
        header_level = '#' * 10
        has_number = False
        for item in data['cells']:
            if item['cell_type'] == 'code' and in_header:
                assert len(header_level) > 0,\
                    (f"\n{notebook}\nno title text!\n"
                        f"{error_instructions}")
                assert has_number,\
                    (f"\n{notebook}\nno header number!\n"
                        f"{error_instructions}")
                in_header = False
            elif item['cell_type'] == 'markdown':
                if in_header:
                    in_code_cell = False
                    for line in item['source']:
                        line = line.strip()
                        if line.startswith('```'):
                            in_code_cell = not in_code_cell
                        if not in_code_cell:
                            if not has_number and line.startswith('#'):
                                current_level = line.split()[0]
                                assert current_level == '#',\
                                    (f"\n{notebook}\nheader line {line}:\n"
                                    f"{error_instructions}")
                                header_level = current_level
                                header_number = line.split()[1].strip()
                                assert header_number[:2].isdigit(),\
                                    (f"\n{notebook}\nheader line {line}:\n"
                                        f"{error_instructions}")
                                assert header_number[-1] == ':',\
                                    (f"\n{notebook}\nheader line {line}:\n"
                                        f"{error_instructions}")
                                has_number = True
                            elif line.strip().startswith('#'):
                                current_level = line.split()[0]
                                assert len(current_level) > 1,\
                                    (f"\n{notebook}\nline {line}:\n"
                                    f"{error_instructions}")
                else:
                    in_code_cell = False
                    for line in item['source']:
                        line = line.strip()
                        if line.startswith('```'):
                            in_code_cell = not in_code_cell
                        if not in_code_cell and line.strip().startswith('#'):
                            current_level = line.split()[0]
                            assert len(current_level) > 1,\
                                (f"\n{notebook}\nline {line}:\n"
                                f"{error_instructions}")

