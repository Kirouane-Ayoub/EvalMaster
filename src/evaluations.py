from llama_index.core.evaluation import (
    CorrectnessEvaluator,
    FaithfulnessEvaluator,
    PairwiseComparisonEvaluator,
    RelevancyEvaluator,
)
from models import prometheus_llm
from prompts import (
    ABS_SYSTEM_PROMPT,
    REL_SYSTEM_PROMPT,
    prometheus_correctness_eval_prompt_template,
    prometheus_faithfulness_eval_prompt_template,
    prometheus_faithfulness_refine_prompt_template,
    prometheus_pairwise_eval_prompt_template,
    prometheus_relevancy_eval_prompt_template,
    prometheus_relevancy_refine_prompt_template,
)
from utils import correctness_parser_function, pairwise_parser_function


def create_evaluator(
    evaluator_class, parser_function=None, eval_template=None, refine_template=None
):
    kwargs = {
        "llm": prometheus_llm,
        "eval_template": f"{ABS_SYSTEM_PROMPT}\n\n{eval_template}",
    }
    if parser_function:
        kwargs["parser_function"] = parser_function
    if refine_template:
        kwargs["refine_template"] = f"{ABS_SYSTEM_PROMPT}\n\n{refine_template}"
    return evaluator_class(**kwargs)


def evaluate_response(evaluator, query, response, reference=None, second_response=None):
    kwargs = {"query": query, "response": response}
    if reference:
        kwargs["reference"] = reference
    if second_response:
        kwargs["second_response"] = second_response
    result = evaluator.evaluate(**kwargs)
    return {
        "score": result.score,
        "feedback": getattr(result, "feedback", None),
        "passing": result.passing,
    }


def pairwise_evaluate(response1, response2, query):
    evaluator = create_evaluator(
        PairwiseComparisonEvaluator,
        parser_function=pairwise_parser_function,
        eval_template=f"{REL_SYSTEM_PROMPT}\n\n{prometheus_pairwise_eval_prompt_template}",
    )
    return evaluate_response(evaluator, query, response1, second_response=response2)


def correctness_evaluate(response1, response2, reference, query):
    evaluator = create_evaluator(
        CorrectnessEvaluator,
        parser_function=correctness_parser_function,
        eval_template=prometheus_correctness_eval_prompt_template,
    )
    return {
        "Result1": evaluate_response(evaluator, query, response1, reference),
        "Result2": evaluate_response(evaluator, query, response2, reference),
    }


def faithfulness_evaluate(response1, response2):
    evaluator = create_evaluator(
        FaithfulnessEvaluator,
        eval_template=prometheus_faithfulness_eval_prompt_template,
        refine_template=prometheus_faithfulness_refine_prompt_template,
    )
    return {
        "Result1": evaluate_response(evaluator, None, response1),
        "Result2": evaluate_response(evaluator, None, response2),
    }


def relevancy_evaluate(response1, response2, query):
    evaluator = create_evaluator(
        RelevancyEvaluator,
        eval_template=prometheus_relevancy_eval_prompt_template,
        refine_template=prometheus_relevancy_refine_prompt_template,
    )
    return {
        "Result1": evaluate_response(evaluator, query, response1),
        "Result2": evaluate_response(evaluator, query, response2),
    }
