#!/usr/bin/env python3

from datetime import datetime as dt
from pathlib import Path
from os.path import exists
import json
from tira.git_integration import get_tira_db
import os
from django.conf import settings
import shutil

def fail_if_environment_variables_are_missing():
    for v in ['TIRA_DATASET_ID', 'TIRA_VM_ID', 'TIRA_RUN_ID', 'TIRA_OUTPUT_DIR', 'TIRA_TASK_ID']:
        if v not in os.environ:
            raise ValueError('I expect that the environment variable "' + v + '" is set, but it was absent.')

def run_output_dir():
    return settings.TIRA_ROOT / 'data' / 'runs' / os.environ['TIRA_DATASET_ID'] / os.environ['TIRA_VM_ID'] / os.environ['TIRA_RUN_ID'] / 'output'

def eval_dir():
    return Path(os.environ['TIRA_OUTPUT_DIR']) / '..' / '..' / dt.now().strftime('%Y-%m-%d-%H-%M-%S')

def copy_resources():
    if exists(run_output_dir()):
        print(str(run_output_dir()) + " exists already. I do not overwrite.")
        return
    
    if not exists(os.environ['TIRA_OUTPUT_DIR']):
        Path(os.environ['TIRA_OUTPUT_DIR']).mkdir(parents=True, exist_ok=True)
    
    Path(run_output_dir()).mkdir(parents=True, exist_ok=True)
    
    shutil.copytree(os.environ['TIRA_OUTPUT_DIR'], str(run_output_dir()))

def extract_evaluation_commands(evaluator):
    try:
        evaluator = json.loads(evaluator['command'])
        
        return {'TIRA_EVALUATION_IMAGE_TO_EXECUTE': evaluator['image'], 'TIRA_EVALUATION_COMMAND_TO_EXECUTE': evaluator['command']}
    except:
        return {'TIRA_EVALUATION_IMAGE_TO_EXECUTE': 'ubuntu:16.04', 'TIRA_EVALUATION_COMMAND_TO_EXECUTE': 'echo "No evaluation specified..."'}

def identify_environment_variables():
    db = get_tira_db()
    ret = set()
    for (k,v) in os.environ.items() :
        if k.lower().startswith('tira'):
            ret.add((k + '=' + v).strip())
    evaluator = extract_evaluation_commands(db.get_evaluator(os.environ['TIRA_DATASET_ID'], os.environ['TIRA_TASK_ID']))
    ret.add('TIRA_EVALUATION_INPUT_DIR=' + str(run_output_dir()))
    ret.add('TIRA_EVALUATION_OUTPUT_DIR=' + str(eval_dir() / 'output'))
    ret.add('TIRA_EVALUATION_IMAGE_TO_EXECUTE=' + evaluator['TIRA_EVALUATION_IMAGE_TO_EXECUTE'])
    ret.add('TIRA_EVALUATION_COMMAND_TO_EXECUTE=' + evaluator['TIRA_EVALUATION_COMMAND_TO_EXECUTE'])
    
    return sorted(list(ret))

if __name__ == '__main__':
    fail_if_environment_variables_are_missing()
    copy_resources()

    with open('task.env', 'w') as f:
        for l in identify_environment_variables():
            f.write(l.strip() + '\n')

