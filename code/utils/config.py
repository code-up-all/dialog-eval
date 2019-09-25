# These can also be set as arguments via the command line.
class Config:
  bleu_smoothing = 4  # Smoothing method for bleu calculation.
  t = 1.97  # t value for confidence level calculation
  train_source = 'data/DailyDlog/baseline/filtered_data/trainSource.txt'
  test_source = 'data/DailyDialog/baseline/filtered_data/testSource.txt'
  test_target = 'data/DailyDialog/baseline/filtered_data/testTarget.txt'
  text_vocab = 'data/DailyDialog/baseline/filtered_data/vocab.txt'
  vector_vocab = 'data/DailyDialog/filtered_data/vocab.npy'
  test_responses = 'data/DailyDialog/baseline/filtered_data/test/testTarget.txt'
  metrics = {
    'length': 1,
    'per-unigram-entropy': 1,
    'per-bigram-entropy': 1,
    'utterance-unigram-entropy': 1,
    'utterance-bigram-entropy': 1,
    'unigram-kl-div': 1,
    'bigram-kl-div': 1,
    'embedding-average': 1,
    'embedding-extrema': 1,
    'embedding-greedy': 1,
    'coherence': 1,
    'distinct-1': 1,
    'distinct-2': 1,
    'bleu-1': 1,
    'bleu-2': 1,
    'bleu-3': 1,
    'bleu-4': 1
  }
