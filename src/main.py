import argparse

from evaluations import (
    correctness_evaluate,
    faithfulness_evaluate,
    pairwise_evaluate,
    relevancy_evaluate,
)
from query_engines import default_query_engine, hybrid_query_engine


def main(query, reference):
    # Query responses from both engines
    response1 = hybrid_query_engine.query(query)
    response2 = default_query_engine.query(query)

    # Example usage of evaluation functions
    pairwise_result = pairwise_evaluate(response1, response2, query)
    correctness_result = correctness_evaluate(response1, response2, reference, query)
    faithfulness_result = faithfulness_evaluate(response1, response2)
    relevancy_result = relevancy_evaluate(response1, response2, query)

    # Print or further process results as needed
    print("Pairwise Comparison Result:", pairwise_result)
    print("Correctness Evaluation Result:", correctness_result)
    print("Faithfulness Evaluation Result:", faithfulness_result)
    print("Relevancy Evaluation Result:", relevancy_result)


if __name__ == "__main__":
    # Initialize argparse
    parser = argparse.ArgumentParser(
        description="Run evaluations on query responses from different engines."
    )
    parser.add_argument("query", type=str, help="The query to be executed.")
    parser.add_argument(
        "reference", type=str, help="The reference data for correctness evaluation."
    )

    # Parse arguments from command line
    args = parser.parse_args()

    # Call main function with parsed arguments
    main(args.query, args.reference)
