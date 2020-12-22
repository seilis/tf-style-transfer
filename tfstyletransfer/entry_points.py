import argparse

DESCRIPTION = """
Simple CLI wrapper for the Tensorflow Neural Style Transfer Tutorial.

Not much more than a set of CLI arguments around the tutorial at:
https://www.tensorflow.org/tutorials/generative/style_transfer#visualize_the_input.

If you are interested in Neural Style Transfer or Tensorflow or both then the
link above is highly recommended.
"""

def main():
    """Main entry point to the CLI interface"""

    parser = argparse.ArgumentParser(description=DESCRIPTION)
    parser.add_argument('-o', '--output', default='output.jpg',
        help="Filename to use for the output image")
    parser.add_argument('INPUT_IMAGE', type=str,
        help="Filename for the input content image")
    parser.add_argument('STYLE_IMAGE', type=str,
        help="Filename to for the input style image")
    parser.add_argument('-s', '--style-weight', default=1e-2, type=float,
        help="Weight to apply for the loss associated with the style image. "
             "Making this bigger results in a final image more like the style image")
    parser.add_argument('-c', '--content-weight', default=1e4, type=float,
        help="Weight to apply for the loss associated with the content image. "
              "Making this bigger results in a final image more like the content image")
    parser.add_argument('-t', '--total-variation-loss', default=30, type=float,
        help="Weight for the total variation loss.")

    args = parser.parse_args()

    print(args)
