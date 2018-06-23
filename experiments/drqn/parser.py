import argparse

parser = argparse.ArgumentParser(description='Parser for vizdoom AI')
parser.add_argument('cfgfile', metavar='<filename-cfg>', type=str,
                    help='file name for cfg file')

# parser.add_argument('train', metavar='trainable', type=bool,
#                     help='true for train, false for evaluate, default true', default=True, nargs='?')

parser.add_argument('savepath', metavar='<dir-savepath>', type=str,
                    help='<dir> for save models and weights')

parser.add_argument('statfile', metavar='<filename-statfile>', type=str,
                    help='filename for the saved stats')

parser.add_argument('--test', dest='train', action='store_false')
parser.set_defaults(train=True)

parser.add_argument('--visible', dest='visible', action='store_true')
parser.set_defaults(visible=False)

parser.add_argument('--sound', dest='sound', action='store_true')
parser.set_defaults(sound=False)

