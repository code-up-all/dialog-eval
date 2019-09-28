# These can also be set as arguments via the command line.
class Config:
  bleu_smoothing = 4  # Smoothing method for bleu calculation.
  t = 1.97  # t value for confidence level calculation
  train_source = 'data/DailyDlog/baseline/trainSource.txt'
  test_source = 'data/DailyDialog/baseline/testSource.txt'
  test_target = 'data/DailyDialog/baseline/testTarget.txt'
  text_vocab = 'data/DailyDialog/vocab.txt'
  vector_vocab = 'data/DailyDialog/vocab.npy'
  test_responses = 'data/DailyDialog/baseline/test/testTarget.txt'
  metrics = {
    'length': 1,
    'per-unigram-entropy': 1,
    'per-bigram-entropy': 1,
    'utterance-unigram-entropy': 1,
    'utterance-bigram-entropy': 1,
    'unigram-kl-div': 0,
    'bigram-kl-div': 0,
    'embedding-average': 0,
    'embedding-extrema': 0,
    'embedding-greedy': 0,
    'coherence': 0,
    'distinct-1': 0,
    'distinct-2': 0,
    'bleu-1': 0,
    'bleu-2': 0,
    'bleu-3': 0,
    'bleu-4': 0
  }
