Prompt Engineering: a methodology for optimizing interactions with
        AI-Language Models in the field of engineering•

                  Juan David Velásquez-Henao, Carlos Jaime Franco-Cardona & Lorena Cadavid-Higuita
        Universidad Nacional de Colombia, sede Medellín, Facultad de Minas, Medellín, Colombia. jdvelasq@unal.edu.co, cjfranco@unal.edu.co,
                                                               dlcadavi@unal.edu.co


Abstract
ChatGPT is a versatile conversational Artificial Intelligence model that responds to user input prompts, with applications in academia and various
sectors. However, crafting effective prompts can be challenging, leading to potentially inaccurate or contextually inappropriate responses,
emphasizing the importance of prompt engineering in achieving accurate outcomes across different domains. This study aims to address this void by
introducing a methodology for optimizing interactions with Artificial Intelligence language models, like ChatGPT, through prompts in the field of
engineering. The approach is called GPEI and relies on the latest advancements in this area; and consists of four steps: define the objective, design
the prompt, evaluate the response, and iterate. Our proposal involves two key aspects: data inclusion in prompt design for engineering applications
and the integration of Explainable Artificial Intelligence principles to assess responses, enhancing transparency. It combines insights from various
methodologies to address issues like hallucinations, emphasizing iterative prompt refinement techniques like posing opposing questions and using
specific patterns for improvement. This methodology could improve prompt precision and utility in engineering.

Keywords: ChatGPT; prompt engineering; large language models; prompt design.



       Ingeniería de instrucciones: una metodología para optimizar
 interacciones con Modelos de Lenguaje de IA en el campo de ingeniería
Resumen
ChatGPT es un modelo de Inteligencia Artificial conversacional versátil que responde a las indicaciones de entrada del usuario, con aplicaciones en el
mundo académico y diversos sectores. Sin embargo, elaborar indicaciones efectivas puede ser un desafío, lo que lleva a respuestas potencialmente
inexactas o contextualmente inapropiadas, lo que enfatiza la importancia de la ingeniería de instrucciones para lograr resultados precisos en diferentes
dominios. Este estudio pretende abordar este vacío introduciendo una metodología para optimizar las interacciones con modelos de lenguaje de
Inteligencia Artificial, como ChatGPT, a través de instrucciones en el campo de la ingeniería. El enfoque es llamado GPEI, y se basa en los últimos
avances en esta área, el cual consta de cuatro pasos: definir el objetivo, diseñar el mensaje, evaluar la respuesta e iterar. Nuestra propuesta involucra dos
aspectos clave: la inclusión de datos en el diseño rápido para aplicaciones de ingeniería y la integración de principios de Inteligencia Artificial Explicable
para evaluar las respuestas, mejorando la transparencia. Combina conocimientos de varias metodologías para abordar problemas como las alucinaciones,
enfatizando técnicas iterativas de refinamiento rápido, como plantear preguntas opuestas y usar patrones específicos para mejorar. Esta metodología
podría mejorar la precisión y la utilidad rápidas en ingeniería.

Palabras clave: ChatGPT; ingeniería de instrucciones; grandes modelos de lenguaje; diseño de instrucciones.




1      Introduction                                                                  model (LLM), ChatGPT has seen extensive applications
                                                                                     across various sectors, including academia, and it can
   ChatGPT is the acronym for Chat Generative Pre-Trained                            produce text that is often indistinguishable from that authored
Transformer, which can respond based on user requests using                          by humans [2,3]. ChatGPT is a generative AI platform that
input text prompts [1]. As a conversational large language                           allows users to input text prompts, which generate responses

How to cite: Velásquez-Henao, J.D., Franco-Cardona, C.J. and Cadavid-Higuita, L., Prompt Engineering: a methodology for optimizing interactions with AI-Language Models
in the field of engineering. DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.
                                              © The author; licensee Universidad Nacional de Colombia.
                         Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023, ISSN 0012-7353
                                                 DOI: https://doi.org/10.15446/dyna.v90n230.111700
                 Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


based on the knowledge accumulated during the training                   rate their performance and express their opinions. This
phase [4]. Typical applications include text generation,                 evaluation allows for continuous improvement of these
summarization, and translation [5].                                      systems. However, there are also profound ethical
    A prompt is a text describing a set of instructions that             implications to its use, given its potential for disseminating
customize, refine, or enhance the capabilities of a GPT model            biased or erroneous data and its implications for plagiarism
[6]. Effective prompts are characterized by the following                and copyright [14,15]. In essence, generative language
fundamental principles [7]: clarity and precision, contextual            models offer substantial opportunities in various fields but
information, desired format, and verbosity control. However,             require careful implementation, ethical oversight, and
writing effective prompts seems complicated for non-                     responsive adaptation to ensure their positive impact and
technical users, requiring creativity, intuition, and iterative          reliability [16-19].
refinement [7]. The problem becomes more significant when
it is necessary to incorporate precise information to solve              2.1    Discussion about ChatGPT
tasks in specific contexts.
    Consequently, the answers can be vague, imprecise,                       The current academic discussion about ChatGPT and
factually incorrect, or contextually inappropriate [5] when an           LLM revolves around three axes: Generative Artificial
inadequate prompt is used. In this context, prompt                       Intelligence, Education, and Ethics.
engineering emerges as a discipline to design prompts by                     Generative artificial intelligence (Generative AI), based
which users can program a Large Language Model, such as                  on transformer architectures, is rapidly advancing in the
ChatGPT, to produce accurate answers [8,9].                              domain of artificial intelligence [20,21]. These models can
    During the last year, much gray literature has been                  generate content in various formats, such as text, images, and
generated that mainly presents prompt templates for specific             more, that closely resemble what humans produce [20,21].
workflows and tasks in marketing, advertising, SEO, and text             These elements profoundly impact professional practice and
translation. There are also many prompt templates for using              education [3,22]. Many concerns relate to academic and
these technologies in everyday tasks such as travel                      professional integrity and student evaluation [22,23]. The
preparation. A quick analysis of this material allows us to              dual nature of technology (enabling academic dishonesty
conclude that the considerations made tend to be repetitive              while potentially enriching pedagogical approaches) forces
and need more depth to use these technologies as assistants              institutions to critically evaluate their assessment
in professional practice and engineering education. On the               methodologies to ensure content accuracy and authenticity
other hand, in the most relevant literature, efforts have been           [22,23]. The foray of generative AI into the educational space
made to formalize the construction of prompts, as will be                has motivated academics to rethink traditional educational
discussed later. However, research has concentrated mainly               frameworks, generating opportunities and challenges
on practice, research, teaching, and scientific publication in           [24,25]. In summary, the integration of generative artificial
health. Consequently, there is a gap when considering the                intelligence at the professional and academic levels requires
opportunities of using GPT and conversational assistants in              rigorous evaluation, continuous research, and adaptation
engineering; a similar conclusion is achieved in [10] by                 strategies to take advantage of its advantages and address the
analyzing the potential uses of LLM in business process                  associated challenges [22-25].
management.                                                                  Education is one of the areas most impacted by the
    This work seeks to fill this gap. We propose a                       popularization of GPTs, mainly by conversational agents
methodology for developing prompts in engineering based                  powered by AI [26]. There are already many publications on
on an iterative process based on the main developments that              this aspect in the most relevant literature, particularly for
have been presented to date on this topic.                               medical education. Since conversational models can generate
    The rest of this work is organized as follows: Section 2             human-like text, they can be used in curriculum design, as
overviews the current discourse on GPT and prompt                        part of teaching methodologies, and to create personalized
engineering. Section 3 presents the methodology employed                 learning resources [26]. These capabilities facilitate the
to propose a framework for engineering prompts, elaborating              teaching of complex concepts and help educators monitor
and illustrating it further in Section 4. Finally, the paper is          and refine their pedagogical approaches [26]. Beyond the
concluded in Section 5.                                                  educational field, conversational agents can offer relevant
                                                                         and accurate information to individuals and communities,
2    Literature review                                                   thus demonstrating their usefulness as a complementary
                                                                         information resource that improves access to information and
    Generative language models are part of the broader                   decision-making [14]. As in other cases discussed, there are
category of pre-trained Generative Transformers (GPT) and                essential concerns about possible bias, security, and ethical
are part of deep learning models [11]. Their competence in               implications associated with using these tools [17,15]. For
interpreting and producing human language is based on the                this reason, it is imperative to guarantee the accurate,
principles and techniques of natural language processing                 transparent, and ethically sound deployment of these tools,
(NLP) [12]. The GPT approach is based on the principles of               especially for public consultation in general [16].
deep learning and NLP. Prompt engineering is essential to                    Models, such as ChatGPT, have generated immense
use generative language models effectively [13].                         interest due to their transformative potential in different
    To evaluate generative language models, sentiment                    sectors, such as administration, finance, health, and education
analysis and opinion mining are usually used, where users                [27]. However, their integration has raised complex


                                                                    10
                 Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


questions, particularly around authorship, plagiarism, and the           prompts start with a verb that specifies the action to be
distinction between human- and AI-generated content [27-                 performed by the system. System prompts provide the system
29]. One of the fundamental issues is whether AI systems                 with a starting point or context to develop content. Question-
should be credited as authors in academic writings                       answer prompts formulate a wh* type question. Mixed
[27,28,30]. The distinction between human-written content                prompts blend two or more techniques mentioned above [8].
and AI-generated content becomes more blurred,                               According to the number of examples provided,
emphasizing concerns about plagiarism [27,28,31]. AI                     instructions are classified as zero-shot and few-shot prompts,
models can generate seemingly genuine but potentially                    where "shot" is equivalent to an example [36]. Zero-shot
misleading scientific texts [32]. In response, there is an               prompts are used in situations where it is not necessary to
emphasis on greater scrutiny, transparency, and ethical                  train the LLM or present sample outputs [37]. Examples of
standards in using AI in research [31,32]. In this way, it is            zero-shot prompts include prompts used to translate or
necessary to achieve a balance between the advantages of AI              summarize texts; other examples of zero-shot prompts are
and      ethical    considerations     becomes      paramount            simple questions that are answered with the internal
[27,29,30,33], which requires an emphasis on transparency,               knowledge of the LLM, such as, for example, "define prompt
fairness, and initiatives of open source [32,33].                        engineering." Few-shot prompts cover prompts with more
                                                                         detailed information.
2.2    Discussion about prompt engineering                                   Reproducibility is a desired characteristic, but LLM
                                                                         produces an inherent random response due to its intrinsic
    Prompt engineering is a set of techniques and methods to             design [7].
design, write, and optimize instructions for LLM, called                     Many sources recognize that the development of prompts
prompts, such that the model answers will be precise,                    is an iterative process. Also, it is desired that the prompt text
concrete, accurate, replicable, and factually correct [8,9,18].          must be clear, concise, and to the point, avoiding unnecessary
Prompts are understood as a form of programming because                  complexity [38].
they can customize the outputs and interactions with an LLM                  Following the discussion, poorly designed prompts
[9]. They involve adapting instructions in natural language,             generate vague, biased, misleading, or ambiguous responses.
obtaining the desired responses, guaranteeing contextually               Another major problem is hallucinations [5,9]. Many
accurate results, and increasing the usefulness of generative            researchers highlight the necessity of verifying facts
language models in various applications [13]. Its applications           presented in the response of conversational LLMs, such as
include fields such as medical education, radiology, and                 academic citations.
science education [11,12,34]. These systems can be used, for
example, as virtual assistants for student care or report                3     Methodology
writing, transforming complex information into a coherent
narrative [11,26,34].                                                    We conducted a comprehensive literature search using
    Efforts are underway to standardize the terminology and              the Scopus database to identify scientific papers on
concepts within prompt engineering, with various
classifications of prompts emerging based on different                   prompt engineering. Scopus is renowned as one of the
criteria.                                                                largest repositories of peer-reviewed scientific
    According to the structure, prompts can be formulated                literature, and it encompasses a broad spectrum of
using open-ended or closed-ended questions. Open-ended                   disciplines, including science, technology, medicine,
questions do not have a specific or limited answer and allow             and social sciences [39].
for a more extensive and detailed response from the model.               We designed and used the following search equation,
They are helpful, for example, for critical reading tasks [35].
                                                                         which retrieved 184 documents.
In contrast, closed-ended questions typically have specific
and limited answers, often yes or no, multiple-choice, or a              TITLE ( ( prompt AND ChatGPT ) OR ( prompt AND
short and defined response. For example, instead of asking               engineering ) ) OR KEY ( ( prompt AND ChatGPT ) OR (
“What is the capital of Italy?” (close-ended question), an               prompt AND engineering ) )
open-ended question might be, “Tell me about the history and
culture of Rome.”                                                            The analysis of the documents and the valuable findings
    According to the information provided, prompts can be                for a prompt design methodology are presented below.
categorized into levels 1 to 4. The first level consists of
straightforward questions, while the second level introduces             4     Results
additional context about the writer and the language model.
The third level includes provided examples for the language              4.1    Analysis
model to reference, and the fourth level allows the language
model to break down the request into individual components                   The majority of the literature found can be categorized
(much like requesting a step-by-step solution to a mathematical          into two groups: specific applications (particularly in the
problem, offering the language model a more structured way to            field of medicine) and guidelines and recommendations for
handle the prompt for improved accuracy) [36].                           prompt design [36] [38]. Only seven papers go beyond
    Comparably, prompts have also been classified as                     prompt design to propose a methodology for interacting with
instructive, system, question-answer, and mixed. Instructive


                                                                    11
                   Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.



Table 1.
Components of methodologies.
                                                                                                             Evaluation
                Authors                        Application          Guidelines              Data                                Iteration
                                                                                                              Criteria
Chang (2023) [35]                            Critical Reading           X                                        X                 X
Eager and Brunton, 2023 [18]                    Education               X                     X                  X                 X
Giray, 2023 [8]                             Academic Writing            X                     X
Jha et al., 2023 [5]                              General                                                         X                X
Lo, 2023 [19]                                     General               X                                         X                X
Shieh, 2023 [40]                                  General                                                                          X
Source: The authors



chatGPT using prompts. This situation can be attributed to                 methodology for interacting with ChatGPT through prompts
the large number of documents and gray literature offering                 for the engineering field.
compilations of prompt examples and templates for specific                     The methodology is called GPEI, which stands for Goal
tasks such as marketing, advertising, or text translation.                 Prompt Evaluation Iteration. GPEI consists of 4 steps: (1)
These guides are designed for the non-technical user, and                  define a goal, (1) design the prompt, (3) evaluate the answer,
they play an essential role in popularizing ChatGPT and                    and (4) iterate, as Figure 1 shows. The methodology is
LLM, although they may not be part of the scientific                       explained below.
literature. Table 1 presents the components of these
methodologies and other pertinent sources within the gray                  4.2.1. Step 1: Define a goal
literature.
    Several methodologies have been developed for general                      The process begins by defining the goal to be achieved by
applications (though they are typically published in medical               the AI model. The goal will determine the structure of the
field journals), while some have been proposed for specific                prompt to be designed in the following step and assist in
domains. We did not find any methodologies proposed for                    evaluating the quality of the system’s response before further
the field of engineering.                                                  iterations. Despite its significance, this activity is explicitly
Most of the methodologies provide guidelines for prompt                    outlined only in one of the analyzed methodologies [18]; in
design and incorporate interactiveness. However, given the                 the remaining methodologies, the objective is disaggregated
nature of the application field, some methodologies are based              within the prompt design.
on specific prompt designs, such as open-ended questions for
critical reading [35] or persona design for academic writers               4.2.2. Step 2: Prompt designing
[8]. Only two methodologies include providing data within
the prompt for the system's response retrieval.                                The first step consists of the design of the prompt. In [9],
    While some methodologies involve evaluating the                        a catalog of prompt patterns is presented and discussed. The
response before iterating on the prompt [5,18,19,35], not all              authors describe 12 patterns for prompt designing; also, they
of them provide components for conducting this assessment                  identify for each pattern the intent, motivation, key ideas, and
[5,18].                                                                    consequences of the approach. Five of these patterns are
    Even though some methodologies hold promise, they are                  oriented toward customizing the output obtained from the
not currently directly applicable to prompt design. For                    system: output Automater, persona, visualization generator,
instance, in [5,41], a methodology is proposed that may be                 recipe, and template.
useful for the internal programming of LLMs but not for
human-user interaction with such systems. Furthermore, in
[42], a hermeneutic exercise is conducted without a proposed
methodology that can be applied to other domains.
    As of the publication date of this paper, we have not found
official documentation from Google on recommendations for
interacting with Bard (the Artificial Intelligence system
developed by the company [43]). Similarly, we have not
come across official documentation from Microsoft
regarding recommendations for interacting with 12hatGPT
through their Bing browser [44].

4.1     Proposal

    We collected the guidelines, recommendations, and
common elements from the various methodologies for
prompt design that were analyzed earlier. Furthermore, we
also considered issues related to hallucinations and low-                  Figure 1. GPEI Methodology
                                                                           Source: The authors.
quality responses and integrated those elements into a


                                                                      12
                    Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


                                                                                  the system output. At this point, it is imperative to preserve the
                                                                                  history of the process design to realize ex-post evaluations of the
                                                                                  performance of the designed prompts.

                                                                                  4.2.3. Step 3: Evaluate the answer.

                                                                                      Realize a formal verification of the answer provided by
                                                                                  ChatGPT in terms of the design criteria specified in Step 1.
                                                                                  Evaluating the obtained response is not trivial since it can
Figure 2. Example of a prompt template for including specific information.        potentially reduce system hallucination.
Source: The authors.                                                                  The following questions could be helpful in this purpose [19]:
                                                                                      Is the answer as complete as expected?
                                                                                      Is the answer as accurate as expected?
    According to the established goal, the user should use the                        Is the answer as relevant as expected?
pattern that best suits their purpose. For example, if the                            Were the specified limits met?
persona pattern is chosen, the prompt should have the                                 Does the answer have elements that may be factually
following elements [36]:                                                          incorrect (hallucinations)?
• The definition of the role of the person who is asking the                          Does the answer have elements that may be contextually
     question.                                                                    inappropriate?
• The definition of a role or a context: "you are …", "you                            The available literature offers various methods for
     act as …"                                                                    assessing ChatGPT's responses. For instance, one approach
• The definition of what is required: Your task is … / Write                      involves rephrasing a question to elicit different responses,
     … / Rephase … /                                                              which can help identify inconsistencies among multiple
• A description of the output format (for example, a                              answers. Additionally, requesting additional evidence, such
     paragraph, a bulleted list, a table, JSON data, etc).                        as querying top-k information sources and having the
• A description of limits for the expected results.                               language model rate the credibility of each source, is another
    In an engineering context, we advise that the prompt                          strategy. Also, one can seek opposing viewpoints from the
includes the necessary data for the system to generate                            language model, including their sources and credibility, to
responses. An example is presented in Fig. 2.                                     evaluate the strength of a different perspective [35]. It is also
    The literature provides some recommendations for                              possible.
prompt design.                                                                        In [5], formal methods are integrated into the design of
• Extending prompts with phrases such as "within the scope"                       prompts for critical and autonomous systems with the aim of
     and "Let's think step by step … to reach conclusions" could                  self-monitoring and automatic detection of errors and
     improve the response of the system.                                          hallucinations. Among the recommendations, the authors
• A strategy for complex responses involves asking LLM to                         suggest that one could consider providing counterexamples
     break the result into small chunks [45].                                     in the prompt to prevent hallucinations [5].
                                                                                      Furthermore, it is possible to design other prompts to
• Think that prompts are instructions in the context of
                                                                                  evaluate a response. For instance, prompts falling under the
     computer programming, such that it is unnecessary to be                      error identification category in [9] involve generating a list
     polite; avoid phrases such as "Please, give me …" [45].                      of facts the output depends on that should be fact-checked
• Strategies, such as the Tree of Thoughts [41], can be used to                   and then introspecting on its output to identify any errors.
     structure prompts for complex problems.                                          A potentially useful strategy to evaluate the answer of an
• Frameworks, such as CLEAR, propose a Concise, Logical,                          LLM is to incorporate elements commonly used to design
     Explicit, Adaptive, and Reflective process to optimize                       Explainable AI systems (XAI) [46]. We propose the
     interactions with AI language models like ChatGPT through                    following guidelines to incorporate these principles to
     prompts.                                                                     evaluate the answer's quality:
• OpenAI suggests separating instructions from the context
     through a break in the prompt or using quotation marks to
     reference textual elements from the context [40].
• Adding examples to articulate the desired output could also
     be useful [40].

     Moreover, the prompt can be used as a template for
solving similar problems or generating new prompts for
similar problems (template pattern [9]). Disambiguation can
be avoided by providing a detailed description or scope of the
problem or the data, as exemplified in Fig. 3.
     A more comprehensive guide for developing template
                                                                                  Figure 3. Prompt example for including specific information.
prompts can be found in [35]. A very important recommendation                     Source: The authors.
is to use the designed prompt in the chat and then collect and save


                                                                             13
                  Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


•     Ask for the reasoning behind a particular answer.                   Table 2.
•     Verify that the prompt asking the LLM provides a                    First iteration for the application case.
                                                                             Role                                     Dialogue
      simple, direct, and unambiguous response.
                                                                                         Given the items below, choose the set of items that has the
•     Verify the prompt requires the LLM to justify the answer.                          highest total value, as long as the sum of the weights of
•     Ask the LLM to break down the answer in bullets, steps,                            those items does not exceed 10 kilograms: Item 1: Value -
      or stages for complex answers.                                                     8, Weight - 3 kg; Item 2: Value - 6, Weight - 2 kg; Item 3:
•     Inquire about the data sources or training data.                     Prompt        Value - 10, Weight - 5 kg; Item 4: Value - 3, Weight - 1 kg;
                                                                                         Item 5: Value - 7, Weight - 4 kg; Item 6: Value - 9, Weight
                                                                                         - 3 kg; Item 7: Value - 5, Weight - 2 kg; Item 8: Value - 4,
4.2.4. Step 4: Iterate                                                                   Weight - 1 kg; Item 9: Value - 2, Weight - 6 kg; Item 10:
                                                                                         Value - 10, weight - 10 kg
    If the answer fails to meet the evaluation criteria, prompt                          Given the items provided, the optimal selection to achieve the
modification is required, which entails adjusting the design                             highest total value without exceeding 10 kilograms would be:
obtaining and assessing a new answer. This iterative                                     * Item 1: Value - 8, Weight - 3 kg
                                                                           GPT
                                                                                         * Item 2: Value - 6, Weight - 2 kg
refinement process continues until the system's response is                              * Item 3: Value - 10, Weight - 5 kg
deemed adequate.                                                                         * Total value: 24; Total weight: 10 kg
    As suggested in [35], the iterative process could be as simple        Source: The authors.
as posing the same question from an opposing perspective.
However, other strategies that use specific prompt patterns can
also be helpful, like the patterns within the improvement group           Table 3.
focus on enhancing the quality of both input and output. Patterns         Second iteration for the application case.
                                                                             Role                                  Dialogue
in this category involve suggesting alternative ways for the
                                                                                       Given the items below, give me three sets with the highest total
Language Model (LLM) to accomplish a user-specified task,                              value. The sets can have any number of elements as long as they
instructing the LLM to automatically propose a series of                               are not repeated, and the sum of the weights of those items does
subquestions for users to answer before combining these                                not exceed 10 kilograms. Show only sets that do not exceed 10
subquestion answers to produce a response to the overarching                           kilograms: Item 1: Value - 8, Weight - 3 kg; Item 2: Value - 6,
question (similar to [41]) and mandating the LLM to                                    Weight - 2 kg; Item 3: Value - 10, Weight - 5 kg; Item 4: Value -
                                                                           Prompt
                                                                                       3, Weight - 1 kg; Item 5: Value - 7, Weight - 4 kg; Item 6: Value -
automatically rephrase user queries when it declines to provide                        9, Weight - 3 kg; Item 7: Value - 5, Weight - 2 kg; Item 8: Value -
an answer.                                                                             4, Weight - 1 kg; Item 9: Value - 2, Weight - 6 kg; Item 10: Value
    Moreover, the utilization of particular prompt patterns                            - 10, weight - 10 kg; Your best answer has been: Item 1: Value -
can prove advantageous. For example, patterns found within                             8, Weight - 3 kg; Item 2: Value - 6, Weight - 2 kg; Item 3: Value -
the Improvement category in [9] focus on enhancing input                               10, weight - 5 kg
                                                                                       Given the items provided and the constraint that the total
and output quality. These patterns suggest alternative                                 weight cannot exceed 10 kilograms, here are three sets with
methods for the LLM to execute a task specified by the user,                           the highest total value that do not exceed the weight limit:
directing the LLM to autonomously present a sequence of
subquestions for users to address before amalgamating these                             Set 1:
subquestion responses to formulate a comprehensive answer                               * Item 3: Value - 10, Weight - 5 kg
                                                                                        * Item 6: Value - 9, Weight - 3 kg.
to the primary inquiry. Additionally, they instruct the LLM
                                                                                        * Item 1: Value - 8, Weight - 3 kg.
to automatically rephrase user queries in cases where it                                Total Value: 27
refuses to produce a solution.                                                          Total Weight: 11 kg (exceeds weight limit)

4.2     Application                                                                     Set 2:
                                                                                        * Item 3: Value - 10, Weight - 5 kg
                                                                           GPT          * Item 2: Value - 6, Weight - 2 kg
    For this example, we will seek the solution to a well-                              * Item 1: Value - 8, Weight - 3 kg
known engineering problem: the knapsack problem [47]. In                                Total Value: 24
this problem, one must decide which items to take on a trip                             Total Weight: 10 kg (within weight limit);
based on the utility value of each item, the weight of each
                                                                                        Set 3:
item, and a limit on the total weight that can be carried.                              * Item 3: Value - 10, Weight - 5 kg
                                                                                        * Item 6: Value - 9, Weight - 3 kg
4.3.1. Step 1: Define a goal.                                                           * Item 2: Value - 6, Weight - 2 kg
                                                                                        Total Value: 25
   From a given list of items, one should find the                                      Total Weight: 10 kg (within weight limit).
combination that has the highest total benefit without                                These sets provide the highest total value without exceeding
exceeding a total weight of 10 kg.                                                    the 10 kilograms weight limit.
                                                                          Source: The authors.
4.3.2. Step 2: Design the prompt.
                                                                          4.3.3. Step 3: Evaluate the answer.
   The designed prompt and the corresponding response are
presented in Table 2.                                                         The items meet the imposed restriction; however, when
                                                                          independently verified using an optimization tool, the
                                                                          following is the optimal solution:


                                                                     14
                     Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


•   Item 1: Value - 8, Weight - 3 kg.                                            Table 5.
•   Item 2: Value - 6, Weight - 2 kg.                                            Iteration 4 for the application case.
                                                                                   Role                                  Dialogue
•   Item 4: Value - 3, Weight - 1 kg.
                                                                                               Generate a code to solve this problem for Google Colab, Use
•   Item 6: Value - 9, Weight - 3 kg.                                                          the following items for the code: Item 1: Value - 8, Weight -
•   Item 8: Value - 4, Weight - 1 kg.                                                          3 kg; Item 2: Value - 6, Weight - 2 kg; Item 3: Value - 10,
•   Total value: 30.                                                               Prompt
                                                                                               Weight - 5 kg; Item 4: Value - 3, Weight - 1 kg; Item 5:
•   Total weight: 10 kg                                                                        Value - 7, Weight - 4 kg; Item 6: Value - 9, Weight - 3 kg;
   Let's see if we can find a better solution than the one                                     Item 7: Value - 5, Weight - 2 kg; Item 8: Value - 4, Weight -
                                                                                               1 kg; Item 9: Value - 2, Weight - 6 kg; Item 10: Value - 10,
found in iteration 1 using ChatGPT.                                                            weight - 10 kg
                                                                                             # Import PuLP library
4.3.4. Step 4: Iterate                                                                       !pip install pulp

                                                                                             from pulp import (
    A new designed prompt, presented int Table 3, is used for                                    LpMaximize, LpProblem, lpSum, LpVariable
the second iteration. Although a better answer was achieved                                  )
                                                                                             prob = LpProblem("Maximize_Value", LpMaximize)
in this iteration than the previous one, ChatGPT still does not                              items = {
find the system's optimum. Other strategies will be employed                                     1: {"value": 8, "weight": 3},
in iterations 3 and 4 to aid in solving this problem.                                            2: {"value": 6, "weight": 2},
                                                                                                 3: {"value": 10, "weight": 5},
    For the iteration 3, the strategy is changed from asking for                                 4: {"value": 3, "weight": 1},
the solution to requesting the formulation of the problem (See                                   5: {"value": 7, "weight": 4},
Table 4). In the iteration 4, we designed a prompt to request                                    6: {"value": 9, "weight": 3},
                                                                                                 7: {"value": 5, "weight": 2},
the generation of the code necessary for Google                                                  8: {"value": 4, "weight": 1},
Collaboratory [48] to solve the previous problem. The                                            9: {"value": 2, "weight": 6},
dialogue is presented in Table 5.                                                                10: {"value": 10, "weight": 10}
                                                                                             }
                                                                                             item_vars = LpVariable.dicts(
Table 4.                                                                                         "Item", items.keys(), 0, 1, LpVariable
Iteration 3 for the application case.                                                        )
                                                                                             prob += lpSum(
     Role                                     Dialogue                                           item_vars[i] * items[i]["value"]
              Formulate the objective function and the correspondent                             for i in items
              constraints for the following problem:                                         )
                                                                                             prob += lpSum(
                                                                                   GPT
              Given a number of items, each characterized by a value and                        item_vars[i] * items[i]["weight"]
    Prompt    a weight in kilograms, find the set of items where the sum                        for i in items
              of their values is maximum, and the sum of their weights is                    ) <= 10
              less than or equal to 10 kilograms. The sets can have any
                                                                                             prob.solve()
              number of elements, as long as they are not repeated.
                                                                                             selected_items = [
              This is a classic Knapsack problem.
                                                                                                 i
              Objective function:                                                                for i in items
                                                                                                 if item_vars[i].value() == 1
              Maximize 𝑍𝑍 where:                                                             ]
                                                                                             total_value = sum(
                                               𝑛𝑛
                                                                                                 items[i]["value"] for i in selected_items
                                   𝑍𝑍 = � 𝑤𝑤𝑖𝑖 𝑥𝑥𝑖𝑖 ≤ 10                                     )
                                              𝑖𝑖=1                                           total_weight = sum(
                                                                                                 items[i]["weight"]
              This objective function represents the total value of the                          for i in selected_items
              selected items.                                                                )
                                                                                             print("Selected items:")
              Constraints:                                                                   for i in selected_items:
                                                                                                 print(
              1. The total weight of the selected items should not exceed                           f"Item {i}: "
    GPT       10 kg:                                                                                f"Value - {items[i]['value']}, "
                                         𝑛𝑛
                                                                                                    f"Weight - {items[i]['weight']} kg"
                                                                                             )
                                        � 𝑤𝑤𝑖𝑖 𝑥𝑥𝑖𝑖 ≤ 10                                     print(f"Total Value: {total_value}")
                                        𝑖𝑖=1                                                 print(f"Total Weight: {total_weight} kg")
                                                                                 Source: The authors.
              2. Decision variable constraints:
                                         0 ≤ 𝑥𝑥𝑖𝑖 ≤ 1                                When we ran the code in Google Colab, we obtained this
              and 𝑥𝑥𝑖𝑖 must be an integer (binary)                               response:
              The objective function aims to maximize the total value of         Requirement      already      satisfied:       pulp                       in
              selected items, subject to the constraints that the total          /usr/local/lib/python3.10/dist-packages (2.7.0)
              weight does not exceed 10 kilograms and each item is either        Selected items:
              selected or not and not repeated.                                  Item 1: Value - 8, Weight - 3 kg;
                                                                                 Item 2: Value - 6, Weight - 2 kg;
Source: The authors.                                                             Item 4: Value - 3, Weight - 1 kg;
                                                                                 Item 6: Value - 9, Weight - 3 kg;



                                                                            15
                    Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


Item 8: Value - 4, weight - 1 kg;                                                           6(1),            pp.           342-363,           2023.             DOI:
Total Value: 30;                                                                            https://doi.org/10.37074/jalt.2023.6.1.9.
Total Weight: 10 kg                                                                  [4]    Pavlik, J.V., Collaborating with ChatGPT: considering the
                                                                                            implications of generative artificial intelligence for journalism and
    Which is the correct solution to the problem. So here, we                               media education, Journal. Mass Commun. Educ., 78(1), pp. 84-93,
halted the process.                                                                         2023. DOI: https://doi.org/10.1177/10776958221149577.
                                                                                     [5]    Jha, S., Jha, S.K., Lincoln, P., Bastian, N.D., Velasquez, A., and
                                                                                            Neema, S., Dehallucinating large language models using formal
5     Conclusions                                                                           methods guided iterative prompting, in: 2023 IEEE International
                                                                                            Conference on Assured Autonomy (ICAA), IEEE, 2023. pp. 149-152.
    Prompt engineering plays a pivotal role in optimizing the                        [6]    Liu, P., Yuan, W., Fu, J., Jiang, Z., Hayashi, H., and Neubig, G., Pre-
performance of LLM by crafting instructions or prompts that                                 train, prompt, and predict: a systematic survey of prompting methods
                                                                                            in natural language processing, ACM Comput. Surv., 55(9), pp. 1-35,
elicit precise, accurate, and contextually appropriate                                      2023.
responses. Designing effective prompts is iterative and                              [7]    Lo, L.S., The art and science of prompt engineering: a new literacy in
requires clear and concise language to avoid generating                                     the information age, Internet Ref. Serv. Q., 2023. DOI:
vague or biased responses.                                                                  https://doi.org/10.1080/10875301.2023.2227621.
    A literature analysis found that multiple methodologies                          [8]    Giray, L., Prompt engineering with ChatGPT: a guide for academic
                                                                                            writers,       Ann.        Biomed.         Eng.,       2023.        DOI:
for prompt engineering have been developed. Notably, no                                     https://doi.org/10.1007/s10439-023-03272-4.
methodologies were found specifically designed for                                   [9]    White, J. et al., A prompt pattern catalog to enhance prompt
engineering. Most of these methodologies offer guidance for                                 engineering with chatgpt, ArXiv Prepr. ArXiv230211382, 2023.
prompt design and emphasize iterative processes. Only two                            [10]   Busch, K., Rochlitzer, A., Sola, D., and Leopold, H., Just tell me:
methodologies include data within the prompt to facilitate                                  prompt engineering in business process management, in: International
                                                                                            Conference on Business Process Modeling, Development and
system response retrieval. While some methodologies                                         Support, Springer, 2023, pp. 3-11.
involve response evaluation before iterating on the prompt,                          [11]   Lecler, A., Duron, L., and Soander, P., Revolutionizing radiologand
not all of them provide components for this assessment.                                     with GPT-based models: current applications, future possibilities and
    We propose an iterative methodology for optimizing                                      limitations of ChatGPT, Diagn. Interv. Imaging, 104(6), pp. 269-274,
interactions with AI language models in engineering through                                 2023. DOI: https://doi.org/10.1016/j.diii.2023.02.003.
                                                                                     [12]   Eandsenbach, G., The role of ChatGPT, generative language models,
prompts named GPEI. It is a four-step process, including defining                           and artificial intelligence in medical education: a conversation with
a goal, designing the prompt, evaluating the answer, and iterating                          ChatGPT and a call for papers, JMIR Med. Educ., 9, 2023. DOI:
to achieve an adequate response. GPEI has two key elements: the                             https://doi.org/10.2196/46885.
inclusion of data in prompt design, making it suitable for                           [13]   Wu, T., Terrand, M., and Cai, C.J., AI chains: transparent and
applications in the field of engineering, and the inclusion of                              controllable Human-AI interaction band chaining large language
                                                                                            model prompts, in: Conference on Human Factors in Computing
principles from Explainable AI (XAI) systems to evaluate                                    Sandstems            -         Proceedings,         2022.           DOI:
answers is proposed, promoting transparency and justifiability in                           https://doi.org/10.1145/3491102.3517582.
the responses generated by LLM.                                                      [14]   Raand P.P., and Majumder, P., Assessing the Accuracand of
    Our methodology integrates guidelines, recommendations, and                             responses band the language model ChatGPT to questions regarding
common elements from various methodologies to address issues like                           bariatric surgerand: a critical appraisal, Obes. Surg., 33(8), pp. 2588-
                                                                                            2589, 2023. DOI: https://doi.org/10.1007/s11695-023-06664-6.
hallucinations and low-quality responses. The iterative nature of                    [15]   Gupta, R., Herzog, I., Weisberger, J., Chao, J., Chaiandasate, K., and
prompt refinement is emphasized, with suggestions such as asking                            Lee, E.S., Utilization of ChatGPT for plastic surgerand research:
opposing questions and using specific prompt patterns for                                   friend or foe?, J. Plast. Reconstr. Aesthet. Surg., 80, pp. 145-147,
improvement. This methodology is a valuable tool for designing                              2023. DOI: https://doi.org/10.1016/j.bjps.2023.03.004.
prompts in engineering.                                                              [16]   Deiana, G., Dettori, M., Arghittu, A., Azara, A., Gabutti, G., and
                                                                                            Castiglia, P., Artificial intelligence and public health: evaluating
    The application example showcased the capabilities of                                   ChatGPT responses to vaccination mandths and misconceptions,
chatGPT in addressing engineering problems when integrated                                  Vaccines,        11(7),      art.      11071217,        2023.       DOI:
with other calculation tools. Future work stemming from this                                https://doi.org/10.3390/vaccines11071217.
research is related to applying the methodology in various                           [17]   Corsello, A. and Santangelo, A., Maand artificial intelligence
engineering applications to incorporate the necessary                                       influence future pediatric research?—The case of ChatGPT, children,
                                                                                            10(4), 2023. DOI: https://doi.org/10.3390/children10040757.
enhancements for improving its utility.                                              [18]   Eager, B., and Brunton, R., Prompting higher education towards AI-
                                                                                            Augmented teaching and learning practice, J. Univ. Teach. Learn.
                                                                                            Pract., 20(5), 2023. DOI: https://doi.org/10.53761/1.20.5.02.
References                                                                           [19]   Lo, L.S., The CLEAR path: a framework for enhancing information
                                                                                            literacand through prompt engineering, J. Acad. Librariansh., 49(4),
[1]   Lund, B.D., Wang, T., Mannuru, N.R., Nie, B., Shimray, S., and                        2023. DOI: https://doi.org/10.1016/j.acalib.2023.102720.
      Wang, Z., ChatGPT and a new academic reality: Artificial                       [20]   DK. Dwivedi, et al., So what if ChatGPT wrote it?
      Intelligence-written research papers and the ethics of the large                      Multidisciplinarand perspectives on opportunities, challenges and
      language models in scholarly publishing, J. Assoc. Inf. Sci. Technol.,                implications of generative conversational AI for research, practice
      74(5), pp. 570-581, 2023. DOI: https://doi.org/10.1002/asi.24750.                     and policand, Int. J. Inf. Manag., 71, 2023. DOI:
[2]   Macdonald, C., Adeloye, D., Sheikh, A., and Rudan, I., Can ChatGPT                    https://doi.org/10.1016/j.ijinfomgt.2023.102642.
      draft a research article? An example of population-level vaccine               [21]   Harrer, S., Attention is not all andou need: the complicated case of
      effectiveness analysis, J. Glob. Health, 13, 2023. DOI:                               ethicalland using large language models in healthcare and medicine,
      https://doi.org/10.7189/JOGH.13.01003.                                                eBioMedicine,                 90,              2023.                DOI:
[3]   Rudolph, J., Tan, S., and Tan, S., ChatGPT: bullshit spewer or the end                https://doi.org/10.1016/j.ebiom.2023.104512.
      of traditional assessments in higher education? J. Appl. Learn. Teach.,        [22]   Crawford, J., Cowling, M., and Allen, K.-A., Leadership is needed for
                                                                                            ethical ChatGPT: character, assessment, and learning using artificial


                                                                                16
                     Velásquez-Henao et al / Revista DYNA, 90 (230), Especial Conmemoración 90 años, pp. 9-17, Noviembre, 2023.


       intelligence (AI), J. Univ. Teach. Learn. Pract., 20(3), 2023. DOI:                   Available at: https://help.openai.com/en/articles/6654000-best-
       https://doi.org/10.53761/1.20.3.02.                                                   practices-for-prompt-engineering-with-openai-api
[23]   Alexander, K., Savvidou, C., and Alexander, C., Who wrote this                 [41]   Yao, S. et al., Tree of thoughts: deliberate problem solving with large
       essaand? Detecting ai-generated writing in second language education                  language models, ArXiv Prepr. ArXiv230510601, 2023.
       in higher education, Teach. Engl. Technol., 23(2), pp. 25-43, 2023.            [42]   Henrickson, L., and Meroño-Peñuela, A., Prompting meaning: a
       DOI: https://doi.org/10.56297/BUKA4060/XHLD5365.                                      hermeneutic approach to optimising prompt engineering with
[24]   Lim, W.M., Gunasekara, A., Pallant, J.L., Pallant, J.I., and                          ChatGPT, AI Soc., 2023, DOI: https://doi.org/10.1007/s00146-023-
       Pechenkina, E., Generative AI and the future of education: Ragnarök                   01752-8.
       or reformation? A paradoxical perspective from management                      [43]   Google, Bard - Chat based AI tool from Google, powered band PaLM
       educators, Int. J. Manag. Educ., 21(2), 2023, DOI:                                    2. [online]. Accessed: October 4th of 2023. Available at:
       https://doi.org/10.1016/j.ijme.2023.100790.                                           https://bard.google.com
[25]   Bilal, M., Jamil, Y., Rana, D., and Shah, H.H., Enhancing awareness            [44]   Microsoft, Your AI-Powered Copilot for the Web | Microsoft Bing.
       and Self-diagnosis of obstructive sleep apnea using AI-Powered                        [online]. Accessed: October 4th of 2023. Available at:
       chatbots: the role of ChatGPT in revolutionizing healthcare, Ann.                     https://www.microsoft.com/en-us/bing
       Biomed. Eng., 2023. DOI: https://doi.org/10.1007/s10439-023-                   [45]   Spasic, A.J., and Jankovic, D.S., Using ChatGPT standard prompt
       03298-8.                                                                              engineering techniques in lesson preparation: role, instructions and
[26]   Epstein, R.H., and Dexter, F., Variabilitand in large language Models'                seed-word prompts, in: 2023 58th International Scientific Conference
       responses to medical licensing and certification examinations.                        on Information, Communication and Energand Sandstems and
       comment on "How Does ChatGPT Perform on the United States                             Technologies, ICEST 2023 - Proceedings, 2023, pp. 47-50. DOI:
       Medical Licensing Examination? The Implications of Large                              https://doi.org/10.1109/ICEST58410.2023.10187269.
       Language Models for Medical Education and Knowledge                            [46]   Rudin, C., and Radin, J., Whand are we using black box models in AI
       Assessment",        JMIR     Med.      Educ.,     9,     2023.   DOI:                 when we don't need to? A lesson from an explainable AI competition,
       https://doi.org/10.2196/48305.                                                        Harv.     Data      Sci.    Rev.,    1.2,     p.   9,   2019.     DOI:
[27]   Marchandot, B., Matsushita, K., Carmona, A., Trimaille, A., and                       https://doi.org/10.1162/99608f92.5a8a3a3d.
       Morel, O., ChatGPT: the next frontier in academic writing for                  [47]   Salkin, H.M., and De Kluandver, C.A., The knapsack problem: a
       cardiologists or a pandora's box of ethical dilemmas, Eur. Heart J.                   surveand, Nav. Res. Logist. Q., 22(1), pp. 127-144, 1975. DOI:
       Open, 3(2), 2023. DOI: https://doi.org/10.1093/ehjopen/oead007.                       https://doi.org/10.1002/nav.3800220110.
[28]   Graf, A. and Bernardi, R.E., ChatGPT in research: balancing ethics,            [48]   Bisong, E., Google Colaboratorand, en Building Machine Learning
       transparencand and advancement, Neuroscience, 515, pp. 71-73,                         and Deep Learning Models on Google Cloud Platform: A
       2023. DOI: https://doi.org/10.1016/j.neuroscience.2023.02.008.                        Comprehensive Guide for Beginners, E. Bisong, Ed., Berkeleand,
[29]   Yan, D., Impact of ChatGPT on learners in a L2 writing practicum:                     CA: Apress, 2019, pp. 59-64. DOI: https://doi.org/10.1007/978-1-
       an exploratorand investigation, Educ. Inf. Technol., 2023. DOI:                       4842-4470-8_7.
       https://doi.org/10.1007/s10639-023-11742-4.
[30]   Ruksakulpiwat, S., Kumar, A., and Ajibade, A., Using ChatGPT in
       Medical research: current status and future directions, J. Multidiscip.        J.D. Velásquez-Henao earned his BSc. in Civil Engineering in 1994, an
       Healthc.,        16,      pp.       1513-1520,         2023.     DOI:          MSc. in Systems Engineering in 1997, and a PhD in Energy Systems in
       https://doi.org/10.2147/JMDH.S413470.                                          2009, all from the Universidad Nacional de Colombia in Medellin,
[31]   Májovský, M., Černý, M., Kasal, M., Komarc, M., and Netuka, D.,                Colombia. From 1994 to 1999, he worked in electricity utilities and
       Artificial intelligence can generate fraudulent but authentic-looking          consulting companies on the power sector. In 2000, he joined the
       scientific medical articles: pandora's box has been opened, J. Med.            Universidad Nacional de Colombia in Medellin and was appointed as a Full
       Internet Res., 25, 2023. DOI: https://doi.org/10.2196/46924.                   Professor of Computer Science by 2012. Between 2004 and 2006, he served
[32]   Spirling, A., Whand open-source generative AI models are an ethical            as an Associate Dean for Research, and from 2009 to 2018, he led the
       waand forward for science, nature, 616(7957), art. 413, 2023. DOI:             Computing and Decision Science Department at the Facultad de Minas,
       https://doi.org/10.1038/d41586-023-01295-4.                                    Universidad Nacional de Colombia, Medellin Campus. His research and
[33]   Wang, S.H., OpenAI — explain whand some countries are excluded                 publications span simulation, modeling, optimization, and forecasting in
       from ChatGPT, nature, 615(7950), art. 34, 2023. DOI:                           energy markets. He specializes in nonlinear time-series analysis and
       https://doi.org/10.1038/d41586-023-00553-9.                                    forecasting using statistical and computational intelligence techniques,
[34]   Cooper, G., Examining science education in ChatGPT: An                         numerical optimization with metaheuristics, and analytics and data science.
       exploratorand studand of generative artificial intelligence, J. Sci.           He currently instructs postgraduate courses in data science, machine
       Educ.      Technol.,     32(3),    pp.     444-452,      2023.   DOI:          learning, and big data in the Analytics program, emphasizing Python
       https://doi.org/10.1007/s10956-023-10039-and.                                  programming.
[35]   Chang, E.Y., Prompting large language models with the socratic                 ORCID: 0000-0003-3043-3037
       method, in: 2023 IEEE 13th Annual Computing and Communication
       Workshop and Conference, CCWC 2023, 2023. pp. 351-360. DOI:                    C. J. Franco is a Full Professor at the Universidad Nacional de Colombia,
       https://doi.org/10.1109/CCWC57344.2023.10099179.                               Medellín Campus, Medellín, Colombia. He earned his MSc. in 1996 and his
[36]   Heston, T.F., and Khun, C., Prompt engineering in medical education,           PhD in 2002, both from the Universidad Nacional de Colombia. Currently,
       Int. Med. Educ., 2(3), pp. 198-205, 2023.                                      his research interests include energy markets, system dynamics, and
[37]   Yong, G., Jeon, K., Gil, D., and Lee, G., Prompt engineering for zero-         complexity.
       shot and few-shot defect detection and classification using a visual-          ORCID: 0000-0002-7750-857X
       language pretrained model, Comput.-Aided Civ. Infrastruct. Eng.,
       38(11),           pp.          1536-1554,          2023.         DOI:          L. Cadavid earned a BSc. in Management Engineering in 2006, an MSc in
       https://doi.org/10.1111/mice.12954.                                            Systems Engineering in 2010, and a PhD in Systems Engineering in 2015,
[38]   Bozkurt, A., and Sharma, R.C., Generative AI and prompt                        all from the Universidad Nacional de Colombia, Medellín, Colombia. She
       engineering: the art of whispering to let the genie out of the                 currently serves as an Assistant Professor at the Universidad Nacional de
       algorithmic world, Asian J. Distance Educ., 2023.                              Colombia, Medellín Campus. Her primary research focuses and publications
[39]   Elsevier, Whand choose Scopus - Scopus benefits. [online].                     include the diffusion of innovations, agent-based modeling and simulation,
       Accessed:        July     31th     of     2020]       Available     at:        and clean energy.
       https://www.elsevier.com/solutions/scopus/whand-choose-scopus                  ORCID: 0000-0002-6025-5940
[40]   Shieh, J., Best practices for prompt engineering with OpenAI API,
       OpenIA, [online]. Sept. 2023. Accessed: October 3rd of 2023.




                                                                                 17
