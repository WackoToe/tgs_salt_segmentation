import argparse
from train.train import train


def main(args):
    train(args)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    main(args)