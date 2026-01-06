import argparse
import numpy as np
import sys
import tensorflow as tf
import re

def get_similarities(doc_vectors, query_vector):
    norm_docs = np.linalg.norm(doc_vectors, axis=1)
    norm_query = np.linalg.norm(query_vector, axis=1)
    
    dot_product = np.dot(doc_vectors, query_vector.T).flatten()
    denominator = (norm_docs * norm_query) + 1e-8
    return dot_product / denominator


def main():
    document_lines = [line.strip() for line in sys.stdin if line.strip()]
    if not document_lines:
        print("Error: No input data received from stdin.")
        sys.exit(1)
    pattern = re.compile(r'[-()]+')
    formatted_lines = [pattern.sub(' ', line) for line in document_lines]

    parser = argparse.ArgumentParser()
    parser.add_argument("--query", type=str, required=True, help="Text to search for")
    args = parser.parse_args()

    query = args.query.strip()
    if not query:
        print("Error: Query cannot be empty or only whitespace.")
        sys.exit(1)

    vector_model = tf.keras.layers.TextVectorization(max_tokens=1000, output_mode='tf_idf')
    vector_model.adapt(formatted_lines)

    doc_vecs = vector_model(formatted_lines).numpy()
    query_vec = vector_model([query]).numpy()

    scores = get_similarities(doc_vecs, query_vec)

    top_k = min(3, len(scores))
    partitioned_indices =  np.argpartition(scores, -top_k)[-top_k:]
    best_indices = partitioned_indices[np.argsort(scores[partitioned_indices])[::-1]]


    found_any = False
    for i, idx in enumerate(best_indices):
        score = scores[idx]
        if score < 0.5:
            continue

        found_any = True
        print(f"\n{i+1}. Score: {score:.4f}: {document_lines[idx]}")
        print("-" * 20)

        # Context Window
        start_idx = max(0, idx - 3)
        end_idx = min(len(document_lines), idx + 4)
        for j in range(start_idx, end_idx):
            prefix = "--> " if j == idx else "    "
            print(f"{prefix}{document_lines[j]}")

    if not found_any:
        print(f"No matches found with confidence > 0.5 (Best score was: {np.max(scores):.4f})")

    print("-" * 20)


if __name__ == "__main__":
    main()
