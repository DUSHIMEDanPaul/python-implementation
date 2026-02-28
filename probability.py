dataset = [
    {"text": "One of the other reviewers has mentioned that after watching just 1 Oz episode you'll be hooked.", "label": "positive"},
    {"text": "A wonderful little production. The filming technique is very unassuming.", "label": "positive"},
    {"text": "I thought this was a wonderful way to spend time on a too hot summer weekend.", "label": "positive"},
    {"text": "Basically there's a family where a little boy (Jake) thinks there's a zombie in his closet... totally ruins... meaningless thriller spots.", "label": "negative"},
    {"text": "Petter Mattei's Love in the Time of Money is a visually stunning film to watch.", "label": "positive"}
]

keywords = ["wonderful", "meaningless", "film"]

total_docs = len(dataset)
pos_docs = sum(1 for d in dataset if d["label"] == "positive")
prior_pos = pos_docs / total_docs

print(f"Prior P(Positive): {prior_pos}\n")
print("-" * 50)

for word in keywords:
    word_in_pos = sum(1 for d in dataset if d["label"] == "positive" and word in d["text"].lower())
    word_in_all = sum(1 for d in dataset if word in d["text"].lower())

    likelihood = word_in_pos / pos_docs if pos_docs > 0 else 0
    marginal = word_in_all / total_docs if total_docs > 0 else 0
    posterior = (likelihood * prior_pos) / marginal if marginal > 0 else 0

    print(f"Keyword: '{word}'")
    print(f"Likelihood P('{word}'|Positive) = {likelihood}")
    print(f"Marginal P('{word}') = {marginal}")
    print(f"Posterior P(Positive|'{word}') = {posterior}")
    print("-" * 50)
