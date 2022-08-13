def grpc_client(args):
    import sys
    sys.path.append('/tira-git/src/tira_host')
    from grpc_client import TiraHostClient

    return TiraHostClient(args.tira_application_host, args.tira_application_grpc_port)


def confirm_run_eval(args):
    client = grpc_client(args)
    
    print(client.confirm_run_eval(vm_id=args.input_run_vm_id, dataset_id=args.dataset_id, run_id=args.run_id, transaction_id=args.transaction_id))


def parse_args():
    import argparse

    parser = argparse.ArgumentParser(description='Make some grpc calls')
    parser.add_argument('--tira_application_host', type=str, default='betaweb001.medien.uni-weimar.de')
    parser.add_argument('--tira_application_grpc_port', type=str, default='31553')
    
    parser.add_argument('--input_run_vm_id', type=str, required=True)
    parser.add_argument('--dataset_id', type=str, required=True)
    parser.add_argument('--run_id', type=str, required=True)
    parser.add_argument('--transaction_id', type=str, required=True)

    return parser.parse_args()


if __name__ == '__main__':
    args = parse_args()
    confirm_run_eval(args)

    # example python3 /tira/application/src/tira/git_integration/grpc_wrapper.py

