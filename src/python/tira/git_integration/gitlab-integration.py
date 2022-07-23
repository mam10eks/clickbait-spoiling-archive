#!/usr/bin/env python3
import gitlab
import os
import string

def read_creds(name):
    return open('/etc/tira-git-credentials/' + name).read().strip()


def gitlab_client():
    return gitlab.Gitlab('https://' + os.environ['CI_SERVER_HOST'], private_token=read_creds('GITCREDENTIALPRIVATETOKEN'))

def clean_job_suffix(ret):
    if "[32;1m$ env|grep 'TIRA' > task.env" in ret:
        ret = ret.split("[32;1m$ env|grep 'TIRA' > task.env")[0]
    if "section_end:" in ret:
        ret = ret.split("section_end:")[0]

    return ret.strip()

def clean_job_output(ret):
    ret = ''.join(filter(lambda x: x in string.printable, ret.strip()))
    if '$ eval "${TIRA_COMMAND_TO_EXECUTE}"[0;m' in ret:
        return clean_job_suffix(ret.split('$ eval "${TIRA_COMMAND_TO_EXECUTE}"[0;m')[1])
    elif '$ eval "${TIRA_EVALUATION_COMMAND_TO_EXECUTE}"[0;m' in ret:
        return clean_job_suffix(ret.split('$ eval "${TIRA_EVALUATION_COMMAND_TO_EXECUTE}"[0;m')[1])
    else:
        raise ValueError('The format of the output seems to be changed...\n\n' + ret)


def job_trace(name):
    gl = gitlab_client()
    gl_project = gl.projects.get(int(os.environ['CI_PROJECT_ID']))
    gl_pipeline = gl_project.pipelines.get(int(os.environ['CI_PIPELINE_ID']))
    
    for job in gl_pipeline.jobs.list():
        if job.name == name:
            job = gl_project.jobs.get(job.id)
            return clean_job_output(job.trace().decode('UTF-8'))
    
    raise ValueError('I could not find the job trace.')

if __name__ == '__main__':
    print(job_trace('run-user-software'))
    print('#####################################################################')
    print(job_trace('evaluate-software-result'))

