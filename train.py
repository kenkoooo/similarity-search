import argparse
import numpy as np
from train_utils import run_train


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--train",
                        help="Path to the root directory of the training dataset")

    parser.add_argument("--batch_size", type=int, default=64,
                        help="The size of batch")

    parser.add_argument("--epoch", type=int, default=20,
                        help="Number of epochs to train")

    parser.add_argument("--mean", default="mean.npy",
                        help="Mean file (computed by compute_mean.py)")

    parser.add_argument("--gpu", type=int, default=0,
                        help="GPU ID")

    parser.add_argument("--out", default="result",
                        help="The directory in which logs are saved")

    parser.add_argument("--val_iteration", type=int, default=10000,
                        help="The number of iterations between every validation")

    parser.add_argument("--loaderjob", type=int, default=4,
                        help="The number of processes to launch for MultiprocessIterator")

    parser.add_argument("--log_iteration", type=int, default=100,
                        help="The number of iterations between every logging")

    parser.add_argument("--resume",
                        help="The path to the trainer snapshot to resume from."
                             "If unseprcified, no shapshot will be resumed")

    args = parser.parse_args()
    mean = np.load(args.mean)

    print("Training strats")
    run_train(
        train_data=args.train, mean=mean,
        epoch=args.epoch,  batchsize=args.batchsize,
        gpu=args.gpu, out=args.out, val_iteration=args.val_iteration,
        log_iteration=args.log_iteration, loaderjob=args.loaderjob,
        resume=args.resume, pre_trainedmodel=True
    )

if __name__ == '__main__':
    main()