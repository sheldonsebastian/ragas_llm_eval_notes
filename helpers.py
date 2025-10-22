from ragas.metrics import (
    LLMContextPrecisionWithoutReference,
    LLMContextRecall,
    ResponseRelevancy,
    Faithfulness,
    FactualCorrectness,
)
from ragas import SingleTurnSample


async def compute_context_precision_score(
    llm_as_judge, user_query, retrieved_context_arr, generated_response
):
    # generate sample data
    sample = SingleTurnSample(
        user_input=user_query,
        retrieved_contexts=retrieved_context_arr,
        response=generated_response,
    )

    # initialize metric using LLM
    precision_metric = LLMContextPrecisionWithoutReference(llm=llm_as_judge)

    # compute precision score
    precision_score = await precision_metric.single_turn_ascore(sample)

    return precision_score


async def compute_context_recall_score(
    llm_as_judge, user_query, reference_ground_truth, retrieved_context_arr
):
    # generate sample data
    sample = SingleTurnSample(
        user_input=user_query,
        reference=reference_ground_truth,
        retrieved_contexts=retrieved_context_arr,
    )

    # initialize metric using LLM
    recall_metric = LLMContextRecall(llm=llm_as_judge)

    # compute recall score
    recall_score = await recall_metric.single_turn_ascore(sample)

    return recall_score


async def compute_response_relevance_score(
    llm_as_judge, embedding_model, user_query, generated_response
):
    sample = SingleTurnSample(
        user_input=user_query,
        response=generated_response,
    )

    # initialize metric using LLM
    response_relevance_metric = ResponseRelevancy(
        llm=llm_as_judge, embeddings=embedding_model
    )

    # compute relevance score
    response_relevance_score = await response_relevance_metric.single_turn_ascore(
        sample
    )

    return response_relevance_score


async def compute_faithfulness_score(
    llm_as_judge, user_query, retrieved_context_arr, generated_response
):
    sample = SingleTurnSample(
        user_input=user_query,
        retrieved_contexts=retrieved_context_arr,
        response=generated_response,
    )

    # initialize metric using LLM
    faithfulness_metric = Faithfulness(llm=llm_as_judge)

    # compute faithfulness score
    faithfulness_score = await faithfulness_metric.single_turn_ascore(sample)

    return faithfulness_score


async def compute_factual_correctness_score(
    llm_as_judge, generated_response, reference_ground_truth
):
    sample = SingleTurnSample(
        response=generated_response, reference=reference_ground_truth
    )

    # initialize metric using LLM
    factual_correctness_metric = FactualCorrectness(llm=llm_as_judge)

    # compute factual correctness score
    factual_correctness_score = await factual_correctness_metric.single_turn_ascore(
        sample
    )

    return factual_correctness_score
