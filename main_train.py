import argparse
from dataset.train import train


def main(args):
    train(args)
    return

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--epochs", type=int, help="Number of training epochs", default=100)
    args = parser.parse_args()
    main(args)