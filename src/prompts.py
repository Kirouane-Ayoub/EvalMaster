ABS_SYSTEM_PROMPT = "You are a fair judge assistant tasked with providing clear, objective feedback based on specific criteria, ensuring each assessment reflects the absolute standards set for performance."
REL_SYSTEM_PROMPT = "You are a fair judge assistant assigned to deliver insightful feedback that compares individual performances, highlighting how each stands relative to others within the same cohort."
prometheus_pairwise_eval_prompt_template = """###Task Description:
An instruction (might include an Input inside it), a response to evaluate, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assess the quality of two responses strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, choose a better response between Response A and Response B. You should refer to the score rubric.
3. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (A or B)"
4. Please do not generate any other opening, closing, and explanations.

###Instruction:
Your task is to compare response A and Response B and give Feedback and score [RESULT] based on Rubric for the following query.
{query}

###Response A:
{answer_1}

###Response B:
{answer_2}

###Score Rubric:
A: If Response A is better than Response B.
B: If Response B is better than Response A.

###Feedback: """

prometheus_correctness_eval_prompt_template = """###Task Description:
An instruction (might include an Input inside it), a query, a response to evaluate, a reference answer that gets a score of 5, and a score rubric representing a evaluation criteria are given.
1. Write a detailed feedback that assesses the quality of the response strictly based on the given score rubric, not evaluating in general.
2. After writing a feedback, write a score that is either 1 or 2 or 3 or 4 or 5. You should refer to the score rubric.
3. The output format should only look as follows: "Feedback: (write a feedback for criteria) [RESULT] (an integer number between 1 and 5)"
4. Please do not generate any other opening, closing, and explanations.
5. Only evaluate on common things between generated answer and reference answer. Don't evaluate on things which are present in reference answer but not in generated answer.

###Instruction:
Your task is to evaluate the generated answer and reference answer for the following query:
{query}

###Generate answer to evaluate:
{generated_answer}

###Reference Answer (Score 5):
{reference_answer}

###Score Rubrics:
Score 1: If the generated answer is not relevant to the user query and reference answer.
Score 2: If the generated answer is according to reference answer but not relevant to user query.
Score 3: If the generated answer is relevant to the user query and reference answer but contains mistakes.
Score 4: If the generated answer is relevant to the user query and has the exact same metrics as the reference answer, but it is not as concise.
Score 5: If the generated answer is relevant to the user query and fully correct according to the reference answer.

###Feedback:"""

prometheus_faithfulness_eval_prompt_template = """###Task Description:
An instruction (might include an Input inside it), an information, a context, and a score rubric representing evaluation criteria are given.
1. You are provided with evaluation task with the help of information, context information to give result based on score rubrics.
2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)”
5. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate: Your task is to evaluate if the given piece of information is supported by context.

###Information:
{query_str}

###Context:
{context_str}

###Score Rubrics:
Score YES: If the given piece of information is supported by context.
Score NO: If the given piece of information is not supported by context

###Feedback:"""

prometheus_faithfulness_refine_prompt_template = """###Task Description:
An instruction (might include an Input inside it), a information, a context information, an existing answer, and a score rubric representing a evaluation criteria are given.
1. You are provided with evaluation task with the help of information, context information and an existing answer.
2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)"
5. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate: If the information is present in the context and also provided with an existing answer.

###Existing answer:
{existing_answer}

###Information:
{query_str}

###Context:
{context_msg}

###Score Rubrics:
Score YES: If the existing answer is already YES or If the Information is present in the context.
Score NO: If the existing answer is NO and If the Information is not present in the context.

###Feedback: """

prometheus_relevancy_eval_prompt_template = """###Task Description:
An instruction (might include an Input inside it), a query with response, context, and a score rubric representing evaluation criteria are given.
1. You are provided with evaluation task with the help of a query with response and context.
2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
3. After writing a feedback, write a score that is A or B. You should refer to the score rubric.
4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)”
5. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate: Your task is to evaluate if the response for the query is in line with the context information provided.

###Query and Response:
{query_str}

###Context:
{context_str}

###Score Rubrics:
Score YES: If the response for the query is in line with the context information provided.
Score NO: If the response for the query is not in line with the context information provided.

###Feedback: """

prometheus_relevancy_refine_prompt_template = """###Task Description:
An instruction (might include an Input inside it), a query with response, context, an existing answer, and a score rubric representing a evaluation criteria are given.
1. You are provided with evaluation task with the help of a query with response and context and an existing answer.
2. Write a detailed feedback based on evaluation task and the given score rubric, not evaluating in general.
3. After writing a feedback, write a score that is YES or NO. You should refer to the score rubric.
4. The output format should look as follows: "Feedback: (write a feedback for criteria) [RESULT] (YES or NO)"
5. Please do not generate any other opening, closing, and explanations.

###The instruction to evaluate: Your task is to evaluate if the response for the query is in line with the context information provided.

###Query and Response:
{query_str}

###Context:
{context_str}

###Score Rubrics:
Score YES: If the existing answer is already YES or If the response for the query is in line with the context information provided.
Score NO: If the existing answer is NO and If the response for the query is in line with the context information provided.

###Feedback: """
