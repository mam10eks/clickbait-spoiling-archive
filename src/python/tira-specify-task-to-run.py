#!/usr/bin/env python3

from glob import glob
from os.path import exists
from pathlib import Path

def find_job_to_execute():
     ret = list(glob('*/*/*/job-to-execute.txt'))
     return None if len(ret) == 0 else ret[0]

def identify_environment_variables(job_file):
    if job_file is None or not exists(job_file) or not Path(job_file).is_file():
        return ['TIRA_IMAGE_TO_EXECUTE=ubuntu:16.04']
    
    job_dir = job_file.split('/job-to-execute')[0]
    
    tira_dataset_id = job_dir.split('/')[-3]
    tira_vm_id = job_dir.split('/')[-2]
    tira_run_id = job_dir.split('/')[-1]
    
    ret = [
        'TIRA_INPUT_RUN=/mnt/ceph/tira/data/datasets/' + tira_dataset_id,
        'TIRA_DATASET_ID=' + tira_dataset_id,
        'TIRA_VM_ID=' + tira_vm_id,
        'TIRA_RUN_ID=' + tira_run_id,
        'TIRA_OUTPUT_DIR=' + job_dir + '/output',
    ]
    
    with open(job_file, 'r') as f:
        for l in f:
            if '=' in l:
                ret += [l.strip()]
    
    for i in ['TIRA_TASK_ID', 'TIRA_IMAGE_TO_EXECUTE', 'TIRA_COMMAND_TO_EXECUTE']:
        if len([j for j in ret if i in j] != 1:
            raise ValueError('I expected the variable "' + i + '" to be defined by the job, but it is missing.')
    
    return ret

if __name__ == '__main__':
    job_to_execute = find_job_to_execute()
    for i in identify_environment_variables(job_to_execute):
        print(i.strip())

