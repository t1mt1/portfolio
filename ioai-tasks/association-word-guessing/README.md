# Word Guessing from Associations Using Sentence Transformers

This NLP project was part of the at-home stage of the International Olympiad in Artificial Intelligence (IOAI). The task involved **guessing a hidden word** based on 3 associations (hint words), chosen from a small candidate list.

---

## Task Overview

Each example consisted of:
- 3 **hint words** (e.g. `['fire', 'alarm', 'smoke']`)
- A list of **candidate words** (e.g. `['fire', 'detector', 'flame', 'fog']`)
- A **correct target** (e.g. `'detector'`)

The goal was to train a model that, given the hints, could correctly identify the most semantically related target word among the candidates.

---

## Key Insight: Hard Negative Mining

After fine-tuning a pretrained **sentence transformer** on (hints, target) pairs using cosine similarity, I found that the model still struggled with certain ambiguous examples.

To improve generalization, I implemented a **"negative training" strategy** by:
1. Running the trained model on a validation set
2. Identifying **hard negatives** — incorrect guesses the model found highly similar
3. Adding those hard negatives to the training set with negative labels
4. Re-training the model on this augmented dataset

---

## Techniques Used

- Sentence transformers (`all-MiniLM-L6-v2`)
- Cosine similarity ranking over candidate choices
- Custom data pipeline using `InputExample` format from `sentence-transformers`
- Hard negative mining based on model's most confident wrong guesses
- TQDM for progress monitoring

---

## Files

association-word-guessing.ipynb: Full notebook with data loading, training loop, and evaluation

## Dataset
The dataset and task were part of a private stage of IOAI and are no longer publicly available.
