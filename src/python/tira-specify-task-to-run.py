#!/usr/bin/env python3

from glob import glob
from os.path import exists
from pathlib import Path

def find_job_to_execute():
     ret = list(glob('*/*/*/job-to-execute.txt'))
     return None if len(ret) == 0 else ret[0]

def config(job_file):
    ret = {}
    with open(job_file, 'r') as f:
        for l in f:
            l = l.split('=')
            if len(l) == 2:
                ret[l[0].strip()] = ret[l[1].strip()]
    
    return ret

def identify_environment_variables(job_file):
    if job_file is None or not exists(job_file) or not Path(job_file).is_file():
        return ['TIRA_IMAGE_TO_EXECUTE=ubuntu:16.04']
    
    job_dir = job_file.split('/job-to-execute')[0]
    
    tira_dataset_id = job_dir.split('/')[-3]
    tira_vm_id = job_dir.split('/')[-2]
    tira_run_id = job_dir.split('/')[-1]

    input_dataset = config(job_file)['TIRA_DATASET_TYPE'] + '-datasets/' + config(job_file)['TIRA_TASK_ID'] + '/' + tira_dataset_id + '/'
    absolute_input_dataset = '/mnt/ceph/tira/data/datasets/' + input_dataset
    input_dataset_truth = config(job_file)['TIRA_DATASET_TYPE'] + '-datasets-truth/' + config(job_file)['TIRA_TASK_ID'] + '/' + tira_dataset_id + '/'
    
    ret = [
        'TIRA_INPUT_RUN=' + absolute_input_dataset,
        'TIRA_DATASET_ID=' + tira_dataset_id,
        'TIRA_INPUT_DATASET=' + input_dataset,
        'inputDataset=' + input_dataset,
        'TIRA_EVALUATION_GROUND_TRUTH=' + input_dataset_truth,
        'TIRA_VM_ID=' + tira_vm_id,
        'TIRA_RUN_ID=' + tira_run_id,
        'TIRA_OUTPUT_DIR=' + job_dir + '/output',
    ]
    
    with open(job_file, 'r') as f:
        for l in f:
            if '=' in l:
                ret += [l.strip()]
    
    for i in ['TIRA_TASK_ID', 'TIRA_IMAGE_TO_EXECUTE', 'TIRA_COMMAND_TO_EXECUTE']:
        if len([j for j in ret if i in j]) != 1:
            raise ValueError('I expected the variable "' + i + '" to be defined by the job, but it is missing.')

    if exists(absolute_input_dataset) and not exists(input_dataset):
        print(f'Copy input data from {absolute_input_dataset} to {os.path.abspath(Path(input_dataset) / "..")}')
        shutil.copytree(absolute_input_dataset, os.path.abspath(Path(input_dataset) / '..'))
    
    if not exists(input_dataset):
        print(f'Make input-directory: "{input_dataset}"')
        Path(input_dataset).mkdir(parents=True, exist_ok=True)
    
    return ret

if __name__ == '__main__':
    job_to_execute = find_job_to_execute()
    for i in identify_environment_variables(job_to_execute):
        print(i.strip())

