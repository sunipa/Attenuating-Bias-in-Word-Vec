# Attenuating-Bias-in-Word-Vec

The projection code returns for every vector u, its orthogonal projection from the direction of bias v.
Here, we assume that the bias direction v is 1 dimensional, for more dimensions, it is just an extension of the dot product.

The 2means code finds for two lists of names or words, the direction between them. Enter a data file in the numpy format for the vectors and the corresponding wordlist in the indicated lines to test it.

More details and explanations available in our paper, Attenuating Bias in Word Vectors (https://arxiv.org/pdf/1901.07656.pdf).
For questions, please email sunipad@cs.utah.edu


For citing this work :
@article{DBLP:journals/corr/abs-1901-07656,
  author    = {Sunipa Dev and
               Jeff M. Phillips},
  title     = {Attenuating Bias in Word Vectors},
  journal   = {CoRR},
  volume    = {abs/1901.07656},
  year      = {2019},
  url       = {http://arxiv.org/abs/1901.07656},
  archivePrefix = {arXiv},
  eprint    = {1901.07656},
  timestamp = {Sat, 02 Feb 2019 16:56:00 +0100},
  biburl    = {https://dblp.org/rec/bib/journals/corr/abs-1901-07656},
  bibsource = {dblp computer science bibliography, https://dblp.org}
}
