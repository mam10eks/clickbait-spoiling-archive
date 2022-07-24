#!/usr/bin/env python3

from git import Repo

def ensure_repo_is_fresh():
    repo = Repo('.')
    repo.remote().pull(repo.active_branch)
    
    print(repo.remote)
    print(repo.active_branch)

if __name__ == '__main__':
    ensure_repo_is_fresh()
#    db = TiraGitFileDatabase()
#
#    dataset_id = 'clickbait-spoiling-task-01-validation-dataset-2022-08-01'
#    vm_id = 'princess-knight'
#    run_id = '2022-07-20-12-54-28'
#    
#    input_run = db.RUNS_DIR_PATH / dataset_id / vm_id / run_id / 'output'
#    output_run = Path(dt.now().strftime('%Y-%m-%d-%H-%M-%S')) / 'output'
#    print(db._load_run(dataset_id, vm_id, run_id))
#    
#    task_id = 'clickbait-spoiling'
#
#    print(db.get_evaluator(dataset_id, task_id))

