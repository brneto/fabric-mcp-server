                                           The Prompt Report: A Systematic Survey of Prompt Engineering
                                                                   Techniques
                            Sander Schulhoff1,2∗ Michael Ilie1∗ Nishant Balepur1 Konstantine Kahadze1
                    Amanda Liu1 Chenglei Si4 Yinheng Li5 Aayush Gupta1 HyoJung Han1 Sevien Schulhoff1
                   Pranav Sandeep Dulepet1 Saurav Vidyadhara1 Dayeon Ki1 Sweta Agrawal12 Chau Pham13
                 Gerson Kroiz Feileen Li1 Hudson Tao1 Ashay Srivastava1 Hevander Da Costa1 Saloni Gupta1
                             Megan L. Rogers8 Inna Goncearenco9 Giuseppe Sarli9,10 Igor Galynker11
               Denis Peskoff Marine Carpuat1 Jules White6 Shyamal Anadkat3 Alexander Hoyle1 Philip Resnik1
                             7
             1
               University of Maryland 2 Learn Prompting       3
                                                                OpenAI 4 Stanford 5 Microsoft 6 Vanderbilt 7 Princeton
                                8                          9
                                  Texas State University     Icahn School of Medicine 10 ASST Brianza
                  11
                     Mount Sinai Beth Israel 12 Instituto de Telecomunicações 13 University of Massachusetts Amherst
                                        sschulho@umd.edu milie@umd.edu resnik@umd.edu
                                                                 Abstract
arXiv:2406.06608v6 [cs.CL] 26 Feb 2025




                                         Generative Artificial Intelligence (GenAI) systems are increasingly being deployed across diverse industries
                                         and research domains. Developers and end-users interact with these systems through the use of prompting
                                         and prompt engineering. Although prompt engineering is a widely adopted and extensively researched area,
                                         it suffers from conflicting terminology and a fragmented ontological understanding of what constitutes
                                         an effective prompt due to its relatively recent emergence. We establish a structured understanding of
                                         prompt engineering by assembling a taxonomy of prompting techniques and analyzing their applications.
                                         We present a detailed vocabulary of 33 vocabulary terms, a taxonomy of 58 LLM prompting techniques,
                                         and 40 techniques for other modalities. Additionally, we provide best practices and guidelines for prompt
                                         engineering, including advice for prompting engineering ChatGPT and other state-of-the-art (SOTA) LLMs.
                                         We further present a meta-analysis of the entire literature on natural language prefix-prompting. As a
                                         culmination of these efforts, this paper presents the most comprehensive survey on prompt engineering to
                                         date.




                                                                                              1
Contents


1   Introduction                               4                  4.1.4   Retrieval Augmented Gen-
    1.1 What is a Prompt? . . . . . . . . .    5                          eration (RAG) . . . . . .      25
    1.2 Terminology . . . . . . . . . . . .    5            4.2   Evaluation . . . . . . . . . . . . .   26
         1.2.1 Components of a Prompt .        5                  4.2.1 Prompting Techniques . .         26
         1.2.2 Prompting Terms . . . . .       6                  4.2.2 Output Format . . . . . .        27
    1.3 A Short History of Prompts . . . .     7                  4.2.3 Prompting Frameworks . .         27
                                                                  4.2.4 Other Methodologies . . .        27
2 A Meta-Analysis of Prompting                  8
  2.1 Systematic Review Process . . . .         8       5   Prompting Issues                             29
      2.1.1 The Pipeline . . . . . . .          8           5.1 Security . . . . . . . . . . . . . .     29
  2.2 Text-Based Techniques . . . . . .         8               5.1.1 Types of Prompt Hacking .          29
                                                                5.1.2 Risks of Prompt Hacking .          29
      2.2.1 In-Context Learning (ICL)           8
                                                                5.1.3 Hardening Measures . . .           30
      2.2.2 Thought Generation . . .           12
                                                            5.2 Alignment . . . . . . . . . . . . .      31
      2.2.3 Decomposition . . . . . .          13
                                                                5.2.1 Prompt Sensitivity . . . .         31
      2.2.4 Ensembling . . . . . . . .         14
                                                                5.2.2 Overconfidence and Cali-
      2.2.5 Self-Criticism . . . . . . .       15
                                                                        bration . . . . . . . . . .      31
  2.3 Prompting Technique Usage . . .          16               5.2.3 Biases, Stereotypes, and
      2.3.1 Benchmarks . . . . . . . .         16                       Culture . . . . . . . . . .      32
  2.4 Prompt Engineering . . . . . . . .       16               5.2.4 Ambiguity . . . . . . . .          32
  2.5 Answer Engineering . . . . . . .         18
      2.5.1 Answer Shape . . . . . .           18       6   Benchmarking                                 33
      2.5.2 Answer Space . . . . . . .         18           6.1 Technique Benchmarking . . . . .         33
      2.5.3 Answer Extractor . . . . .         18               6.1.1 Comparing      Prompting
                                                                       Techniques . . . . . . . .        33
3   Beyond English Text Prompting              20               6.1.2 Question Formats . . . . .         33
    3.1 Multilingual . . . . . . . . . . . .   20               6.1.3 Self-Consistency . . . . .         33
        3.1.1 Chain-of-Thought (CoT) .         20               6.1.4 Evaluating Responses . .           34
        3.1.2 In-Context Learning . . .        20               6.1.5 Results . . . . . . . . . .        34
        3.1.3 Prompt Template Lan-                          6.2 Prompt Engineering Case Study .          34
                guage Selection . . . . . .    20               6.2.1 Problem . . . . . . . . . .        34
        3.1.4 Prompting for Machine                             6.2.2 The Dataset . . . . . . . .        35
                Translation . . . . . . . .    21               6.2.3 The Process . . . . . . . .        35
    3.2 Multimodal . . . . . . . . . . . .     22               6.2.4 Discussion . . . . . . . .         42
        3.2.1 Image Prompting . . . . .        22
                                                        7   Related Work                                 44
        3.2.2 Audio Prompting . . . . .        23
        3.2.3 Video Prompting . . . . .        23       8   Conclusions                                  45
        3.2.4 Segmentation Prompting .         23
        3.2.5 3D Prompting . . . . . . .       23       A Appendices                                     62
                                                          A.1 Definitions of Prompting . . . . .         62
4   Extensions of Prompting                    24         A.2 Extended Vocabulary . . . . . . .          64
    4.1 Agents . . . . . . . . . . . . . . .   24             A.2.1 Prompting Terms . . . . .            64
         4.1.1 Tool Use Agents . . . . .       24             A.2.2 Prompt Engineering Terms             64
         4.1.2 Code-Generation Agents .        24             A.2.3 Fine-Tuning Terms . . . .            64
         4.1.3 Observation-Based Agents        25             A.2.4 Orthogonal Prompt Types              64

                                                    2
A.3 Datasheet . . . . . . . . . . . . .   66       A.6 Evaluation Table . . . . . . . . .     71
    A.3.1 Motivation . . . . . . . .      66       A.7 Entrapment Prompting Process . .       72
    A.3.2 Composition . . . . . . .       66
                                                        A.7.1 Exploration . . . . . . . .     72
    A.3.3 Collection Process . . . .      67
    A.3.4 Preprocessing/ Cleaning/                      A.7.2 Getting a Label . . . . . .     72
           Labeling . . . . . . . . .     67            A.7.3 Varying Prompting Tech-
    A.3.5 Uses . . . . . . . . . . . .    67                  niques . . . . . . . . . . .    72
    A.3.6 Distribution . . . . . . . .    67
                                                   A.8 Formally Defining a Prompt . . .       75
    A.3.7 Maintenance . . . . . . .       67
A.4 Keywords . . . . . . . . . . . . .    68       A.9 In-Context Learning Definitions
A.5 Prompt for Systematic Literature                   Disambiguation . . . . . . . . . .     77
    Review . . . . . . . . . . . . . .    70       A.10 Contributions . . . . . . . . . . .   79




                                               3
1      Introduction

   Transformer-based LLMs are widely deployed                                         Core Prompting Techniques
in consumer-facing, internal, and research settings
(Bommasani et al., 2021). Typically, these models                                         Text based Techniques
rely on the user providing an input “prompt” to
                                                                                   MLT/MMTs are often derived from fundamental 

which the model produces an output in response.                                         text-based prompting techniques.

Such prompts may be textual—“Write a poem
                                                                Multilingual Techniques                          Multimodal Techniques
about trees.”—or take other forms: images, audio,                *Techniques on text data from                *Techniques for processing multimedia
                                                                      multiple languages                               (video, audio, etc)
videos, or a combination thereof. The ability to
prompt models, particularly prompting with natu-
ral language, makes them easy to interact with and
                                                                                                     Agents
use flexibly across a wide range of use cases.                                     Often make use of core prompting techniques

   Knowing how to effectively structure, evaluate,
and perform other tasks with prompts is essential                       Safety                     Evaluation                      Security
                                                                Safety needs throughout      Need to evaluate prompt/         Security concerns
to using these models. Empirically, better prompts                                                agent outputs                  throughout

lead to improved results across a wide range of
tasks (Wei et al., 2022b; Liu et al., 2023b; Schul-          Figure 1.1: Categories within the field of prompting are
hoff, 2022). A large body of literature has grown            interconnected. We discuss 7 core categories that are
around the use of prompting to improve results               well described by the papers within our scope.
and the number of prompting techniques is rapidly
increasing.                                                  in the model’s vocabulary, while soft prompts may
   However, as prompting is an emerging field, the           contain tokens that have no corresponding word in
use of prompts continues to be poorly understood,            the vocabulary.
with only a fraction of existing terminologies and              Finally, we only study task-agnostic techniques.
techniques being well-known among practitioners.             These decisions keep the work approachable to less
We perform a large-scale review of prompting tech-           technical readers and maintain a manageable scope.
niques to create a robust resource of terminology
and techniques in the field. We expect this to be            Sections Overview We conducted a machine-
the first iteration of terminologies that will develop       assisted systematic review grounded in the
over time. We maintain an up-to-date list of terms           PRISMA process (Page et al., 2021) (Section 2.1)
and techniques at LearnPrompting.org.                        to identify 58 different text-based prompting tech-
                                                             niques, from which we create a taxonomy with a
Scope of Study We create a broad directory of                robust terminology of prompting terms (Section
prompting techniques, that can be quickly under-             1.2).
stood and easily implemented for rapid experimen-               Our goal is to provide a roadmap for the com-
tation by developers and researchers. To this end,           munity when considering which prompting tech-
we limit our study to focus on prefix prompts (Shin          niques to use (Figure 1.1). While much literature
et al., 2020a) rather than cloze prompts (Petroni            on prompting focuses on English-only settings, we
et al., 2019; Cui et al., 2021), because modern              also discuss multilingual techniques (Section 3.1).
LLM transformer architectures widely employ pre-             Given the rapid growth in multimodal prompting,
fix prompts and provide robust support for both              where prompts may include media such as images,
developers and researchers (Brown et al., 2020;              we also expand our scope to multimodal techniques
Google, 2023; Touvron et al., 2023). Additionally,           (Section 3.2). Many multilingual and multimodal
we refined our focus to hard (discrete) prompts              prompting techniques are direct extensions of En-
rather than soft (continuous) prompts and leave out          glish text-only prompting techniques.
papers that make use of techniques using gradient-              As prompting techniques grow more complex,
based updates (i.e. fine-tuning). Hard prompts con-          they have begun to incorporate external tools, such
tain only tokens (vectors) that correspond to words          as Internet browsing and calculators. We use the

                                                         4
term "agents" to describe these types of prompting
                                                                 Write a poem about trees.
techniques (Section 4.1).
   It is important to understand how to evaluate
the outputs of agents and prompting techniques to             Write a poem about the following topic:
ensure accuracy and avoid hallucinations. Thus,               {USER_INPUT}
we discuss ways of evaluating these outputs (Sec-
tion 4.2). We also discuss security (Section 5.1)
and safety measures (Section 5.2) for designing            Figure 1.2: Prompts and prompt templates are distinct
prompts that reduce the risk of harm to companies          concepts; a prompt template becomes a prompt when
and users.                                                 input is inserted into it.
   Finally, we apply prompting techniques in two
case studies (Section 6.1). In the first, we test a           Each tweet in the dataset would be inserted into
range of prompting techniques against the com-             a separate instance of the template and the resulting
monly used benchmark MMLU (Hendrycks et al.,               prompt would be given to a LLM for inference.
2021). In the second, we explore in detail an exam-
ple of manual prompt engineering on a significant,         1.2     Terminology
real-world use case, identifying signals of frantic
hopelessness–a top indicator of suicidal crisis–in         1.2.1    Components of a Prompt
the text of individuals seeking support (Schuck            There are a variety of common components in-
et al., 2019a). We conclude with a discussion of           cluded in a prompt. We summarize the most com-
the nature of prompting and its recent development         monly used components and discuss how they fit
(Section 8).                                               into prompts (Figure 1.3).

1.1   What is a Prompt?                                    Directive Many prompts issue a directive in the
                                                           form of an instruction or question.1 This is the
A prompt is an input to a Generative AI model, that        core intent of the prompt, sometimes simply called
is used to guide its output (Meskó, 2023; White            the "intent". For example, here is an instance of a
et al., 2023; Heston and Khun, 2023; Hadi et al.,          prompt with a single instruction:
2023; Brown et al., 2020). Prompts may consist
of text, image, sound, or other media. Some ex-
                                                                 Tell me five good books to read.
amples of prompts include the text, “write a three
paragraph email for a marketing campaign for an
                                                              Directives can also be implicit, as in this one-
accounting firm”, a photograph of a piece of paper
                                                           shot case, where the directive is to perform English
with the words “what is 10*179” written on it, or
                                                           to Spanish translation:
a recording of an online meeting, with the instruc-
tions “summarize this”. Prompts usually have some
text component, but this may change as non-text                  Night: Noche
modalities become more common.                                   Morning:

Prompt Template Prompts are often constructed              Examples Examples, also known as exemplars or
via a prompt template (Shin et al., 2020b). A              shots, act as demonstrations that guide the GenAI
prompt template is a function that contains one or         to accomplish a task. The above prompt is a One-
more variables which will be replaced by some me-          Shot (i.e. one example) prompt.
dia (usually text) to create a prompt. This prompt
can then be considered to be an instance of the            Output Formatting It is often desirable for the
template.                                                  GenAI to output information in certain formats,
   Consider applying prompting to the task of bi-          for example, CSV, Markdown, XML, or even cus-
nary classification of tweets. Here is an initial          tom formats(Xia et al., 2024). Structuring outputs
prompt template that can be used to classify inputs.       may reduce performance on some tasks (Tam et al.,
                                                           2024). However, Kurt (2024) point out various
    Classify the tweet as positive or negative:               1
                                                               “Directives”, from Searle (1969), are a type of speech act
   {TWEET}                                                 intended to encourage an action, and have been invoked in
                                                           models of human-computer dialogue Morelli et al. (1991).


                                                       5
                                              Context 1.2.1
                                              Context Window A.2.1
                                              Priming A.2.1                                               Few-Shot Prompt 2.2.1
                                                                               In-Context Learning
                                              Prompting Technique              2.2.1                      Exemplar 1.2.2
                                              1.2.2
                                                                               Zero-Shot Prompt 2.2.1.3   Continuous Prompt
                   Prompting 1.2.2
                                                                                                          A.2.4.2
                                                                               Density A.2.4.2
                                                                                                          Discrete Prompt A.2.4.2
                                                                                                          User Prompt A.2.4.1
                                              Orthogonal Prompt Types
                                              A.2.4                            Originator A.2.4.1         System Prompt A.2.4.1

                                              Prompt Chain 1.2.2                                          Assistant Prompt A.2.4.1

                                              Prompt Engineering                                          Prefix A.2.4.3
                                                                               Prediction Style A.2.4.3
      Prompt 1.1                              Technique 1.2.2                                             Cloze A.2.4.3
                   Prompt Template 1.1        Meta-Prompting 2.4
                                                                               Verbalizer 2.5.3
                   Prompt Engineering 1.2.2   Answer Engineering
                                                                               Extractor 2.5.3
                                              2.5
                                                                               Answer Trigger 2.5.3
                                              Conversational Prompt
                                              Engineering A.2.2
                                              Prompt-Based
                                              Learning A.2.3
                   Fine-Tuning A.2.3
                                              Prompt Tuning A.2.3


Figure 1.3: A Terminology of prompting. Terms with links to the appendix are not sufficiently critical to describe in
the main paper, but are important to the field of prompting. Prompting techniques are shown in Figure 2.2
                                                                   .

flaws in Tam et al. (2024) and show that structuring                   position so the GenAI can properly sign the email.
outputs may actually improve performance. Here                         Additional Information is sometimes called ‘con-
is an example of how you might format a prompt                         text‘, though we discourage the use of this term as
to output information as a CSV:                                        it is overloaded with other meanings in the prompt-
                                                                       ing space2 .
   {PARAGRAPH}
   Summarize this into a CSV.                                          1.2.2      Prompting Terms
                                                                       Terminology within the prompting literature is
Style Instructions Style instructions are a type of                    rapidly developing. As it stands, there are many
output formatting used to modify the output stylisti-                  poorly understood definitions (e.g. prompt, prompt
cally rather than structurally (Section 2.2.1.3). For                  engineering) and conflicting ones (e.g. role prompt
example:                                                               vs persona prompt). The lack of a consistent vocab-
                                                                       ulary hampers the community’s ability to clearly
   Write a clear and curt paragraph about lla-                         describe the various prompting techniques in use.
   mas.                                                                We provide a robust vocabulary of terms used in the
                                                                       prompting community (Figure 1.3).3 Less frequent
Role A Role, also known as a persona (Schmidt                          terms are left to Appendix A.2. In order to accu-
et al., 2023; Wang et al., 2023l), is a frequently                     rately define frequently-used terms like prompt and
discussed component that can improve writing and                       prompt engineering, we integrate many definitions
style text (Section 2.2.1.3). For example:                             (Appendix A.1) to derive representative definitions.

    Pretend you are a shepherd and write a lim-                        Prompting Prompting is the process of provid-
    erick about llamas.                                                ing a prompt to a GenAI, which then generates a
                                                                       response. For example, the action of sending a
Additional Information It is often necessary to
                                                                          2
include additional information in the prompt. For                           e.g. the context is the tokens processed by the LLM in a
                                                                       forward pass
example, if the directive is to write an email, you                       3
                                                                            By robust, we mean that it covers most existing commonly
might include information such as your name and                        used terms in the field.


                                                                   6
 Dataset Inference (i.e. entries x₁ ... xₙ)                     Exemplar Exemplars are examples of a task be-
                                                                ing completed that are shown to a model in a
    x₁       x₂          xₙ
                                                                prompt (Brown et al., 2020).

                                                                1.3     A Short History of Prompts
     Prompt Template                                            The idea of using natural language prefixes, or
                                                                prompts, to elicit language model behaviors and
                                                                responses originated before the GPT-3 and Chat-
         Generative AI                                          GPT era. GPT-2 (Radford et al., 2019a) makes
                                   Modify Prompt
                                                                use of prompts and they appear to be first used in
                                   Template until
                                                                the context of Generative AI by Fan et al. (2018).
                                   Desiderata Met

            Extractor
                                                                However, the concept of prompts was preceded by
                                                                related concepts such as control codes (Pfaff, 1979;
                                                                Poplack, 1980; Keskar et al., 2019) and writing
                                                                prompts in literature.
         Utility Function
                                                                   The term Prompt Engineering appears to have
                                                                come into existence more recently from Radford
Figure 1.4: The Prompt Engineering Process consists of          et al. (2021) then slightly later from Reynolds and
three repeated steps 1) performing inference on a dataset
                                                                McDonell (2021).
2) evaluating performance and 3) modifying the prompt
template. Note that the extractor is used to extract a
                                                                   However, various papers perform prompt engi-
final response from the LLM output (e.g. "This phrase           neering without naming the term (Wallace et al.,
is positive" → "positive"). See more information on             2019; Shin et al., 2020a), including Schick and
extractors in Section 2.5.                                      Schütze (2020a,b); Gao et al. (2021) for non-
                                                                autoregressive language models.
                                                                   Some of the first works on prompting define a
chunk of text or uploading an image constitutes
                                                                prompt slightly differently to how it is currently
prompting.
                                                                used. For example, consider the following prompt
Prompt Chain A prompt chain (activity: prompt                   from Brown et al. (2020):
chaining) consists of two or more prompt templates
used in succession. The output of the prompt gen-                     Translate English to French:
erated by the first prompt template is used to pa-                    llama
rameterize the second template, continuing until all
templates are exhausted (Wu et al., 2022).                         Brown et al. (2020) consider the word "llama" to
                                                                be the prompt, while "Translate English to French:"
Prompting Technique A prompting technique
                                                                is the "task description". More recent papers, in-
is a blueprint that describes how to structure a
                                                                cluding this one, refer to the entire string passed to
prompt, prompts, or dynamic sequencing of multi-
                                                                the LLM as the prompt.
ple prompts. A prompting technique may incorpo-
rate conditional or branching logic, parallelism, or
other architectural considerations spanning multi-
ple prompts.
Prompt Engineering Prompt engineering is the
iterative process of developing a prompt by modify-
ing or changing the prompting technique that you
are using (Figure 1.4).
Prompt Engineering Technique A prompt engi-
neering technique is a strategy for iterating on a
prompt to improve it. In literature, this will often
be automated techniques (Deng et al., 2022), but in
consumer settings, users often perform prompt en-
gineering manually, without any assistive tooling.

                                                            7
2       A Meta-Analysis of Prompting

2.1     Systematic Review Process                                   3,677 from arXiv 2,087 from SS, 639 from ACL = 4797 Records




                                                                            -550

In order to robustly collect a dataset of sources
for this paper, we ran a systematic literature re-                 4,247 Records after Title
                                                                                                        1,661 papers human reviewed
                                                                        Deduplication

view grounded in the PRISMA process (Page et al.,
2021) (Figure 2.1). We host this dataset on Hug-                             -316                           316 papers excluded


gingFace 4 and present a datasheet (Gebru et al.,
2021) for the dataset in Appendix A.3. Our main                 3,931 Records after Human

                                                                           Review
                                                                                                         Check if paper contains the

                                                                                                                word “prompt”

data sources were arXiv, Semantic Scholar, and
ACL. We query these databases with a list of                                -1,579                         1,579 papers excluded


44 keywords narrowly related to prompting and
prompt engineering (Appendix A.4).                                   2,352 Records after

                                                                removing papers that don’t                1,071 papers AI reviewed

                                                                contain the word “prompt”



2.1.1    The Pipeline                                                                                       787 papers excluded
                                                                             -787


In this section, we introduce our data scraping
pipeline, which includes both human and LLM-                              After The PRISMA Review Process,


                                                                          1,565 records included in quantitative analysis.

assisted review.5 As an initial sample to estab-
lish filtering critera, we retrieve papers from arXiv
                                                             Figure 2.1: The PRISMA systematic literature review
based on a simple set of keywords and boolean                process. We accumulate 4,247 unique records from
rules (A.4). Then, human annotators label a sample           which we extract 1,565 relevant records.
of 1,661 articles from the arXiv set for the follow-
ing criteria:
                                                             2.2      Text-Based Techniques
  1. Include if the paper proposes a novel prompt-
                                                             We now present a comprehensive taxonomical on-
     ing technique.
                                                             tology of 58 text-based prompting techniques, bro-
                                                             ken into 6 major categories (Figure 2.2). Although
  2. Include if the paper strictly covers hard prefix
                                                             some of the techniques might fit into multiple cate-
     prompts.
                                                             gories, we place them in a single category of most
                                                             relevance.
  3. Exclude if the paper focuses on training by
     backpropagating gradients.                              2.2.1      In-Context Learning (ICL)

  4. Include if the paper uses a masked frame                  ICL refers to the ability of GenAIs to learn skills
     and/or window for non-text modalities.                    and tasks by providing them with exemplars and or
                                                               relevant instructions within the prompt, without the
A set of 300 articles are reviewed independently               need for weight updates/retraining (Brown et al.,
by two annotators, with 92% agreement (Krippen- 2020; Radford et al., 2019b). These skills can be
dorff’s α = Cohen’s κ = 81%). Next, we develop                 learned from exemplars (Figure 2.4) and/or instruc-
a prompt using gpt-4-1106-preview to classify the              tions (Figure 2.5). Note that the word "learn" is
remaining articles (Appendix A.5). We validate                 misleading. ICL can simply be task specification–
the prompt against 100 ground-truth annotations, the skills are not necessarily new, and can have
achieving 89% precision and 75% recall (for an F 1 already been included in the training data (Figure
of 81%). The combined human and LLM annota- 2.6). See Appendix A.9 for a discussion of the use
tions generate a final set of 1,565 papers.                    of this term. Significant work is currently being
                                                               done on optimizing (Bansal et al., 2023) and un-
   4                                                           derstanding (Si et al., 2023a; Štefánik and Kadlčík,
     https://huggingface.co/datasets/PromptSystematicReview/Prompt_Systematic_Review_Dataset
   5
     Using gpt-4-1106-preview                                  2023) ICL.

                                                         8
                                                     Emotion Prompting 2.2.1.3
                                                     Role Prompting 2.2.1.3
                                                     Style Prompting 2.2.1.3
                                                     S2A 2.2.1.3
                          Zero-Shot 2.2.1.3
                                                     SimToM 2.2.1.3
                                                     RaR 2.2.1.3
                                                     RE2 2.2.1.3
                                                     Self-Ask 2.2.1.3
                                                     Exemplar Generation             SG-ICL 2.2.1.2
                                                     Exemplar Ordering 2.2.1.1
                                                                                                             Analogical Prompting
                          Few-Shot 2.2.1             Exemplar Selection              KNN 2.2.1.2             2.2.2.1
                                                     2.2.1.2                         Vote-K 2.2.1.2          Step-Back Prompting
                                                     Instruction Selection 2.2.1.1                           2.2.2.1
                                                                                     Zero-Shot CoT 2.2.2.1
                                                                                                             Thread-of-Thought
                                                                                                             (ThoT) 2.2.2.1
                                                                                                             Tab-CoT 2.2.2.1

                                                     Chain-of-Thought                                        Active-Prompt 2.2.2.2
                          Thought Generation 2.2.2
                                                     (CoT) 2.2.2
                                                                                                             Auto-CoT 2.2.2.2
                                                     COSP 2.2.4
                                                                                                             Complexity-Based 2.2.2.2
                                                     DENSE 2.2.4
                                                                                                             Contrastive 2.2.2.2
                                                     DiVeRSe 2.2.4
                                                                                     Few-Shot CoT 2.2.2.2    Memory-of-Thought
                                                     Max Mutual                                              2.2.2.2
                                                     Information 2.2.4
Text-Base Prompt. Tech.                                                                                      Uncertainty-Routed
                                                     Meta-CoT 2.2.4                                          CoT 2.2.2.2
                          Ensembling 2.2.4
                                                     MoRE 2.2.4                                              Prompt Mining 2.2.1.2

                                                     Self-Consistency 2.2.4                                  AutoDiCoT 6.2.3.3

                                                     Universal
                                                     Self-Consistency 2.2.4
                                                     USP 2.2.4
                                                     Prompt Paraphrasing 2.2.4
                                                     Chain-of-Verification 2.2.5
                                                     Self-Calibration 2.2.5
                                                     Self-Refine 2.2.5
                          Self-Criticism 2.2.5
                                                     Self-Verification 2.2.5
                                                     ReverseCoT 2.2.5
                                                     Cumulative Reason. 2.2.5
                                                     DECOMP 2.2.3
                                                     Faithful CoT 2.2.3
                                                     Least-to-Most 2.2.3
                                                     Plan-and-Solve 2.2.3
                          Decomposition 2.2.3        Program-of-Thought 2.2.3
                                                     Recurs.-of-Thought 2.2.3
                                                     Skeleton-of-Thought 2.2.3
                                                     Tree-of-Thought 2.2.3
                                                     Metacognitive 2.2.3


                          Figure 2.2: All text-based prompting techniques from our dataset.




                                                                   9
   1. Exemplar Quantity                2. Exemplar Ordering
   Include as many exemplars as        Randomly order exemplars*              2+2: four
   possible*
                                                                              4+5: nine
       Trees are beautiful: Happy
      I am so mad: Angry

       I hate Pizza: Angry
             I love life: Happy
                   8+0:
       Squirrels are so cute: Happy
    I hate my boss: Angry

       YouTube Ads Suck: Angry
         Life is good: Happy

       I’m so excited:                  I’m so excited:
                                                                                     Figure 2.4: ICL exemplar prompt
                                        I love life: Happy

       Trees are beautiful: Happy
      Life is good: Happy

       I’m so excited:                  I am so mad: Angry

                                        I hate my boss: Angry

                                        I’m so excited:                       Extract all words that have 3 of the same
   3. Exemplar Label Distribution      4. Exemplar Label Quality              letter and at least 3 other letters from the
   Provide a balanced label            Ensure exemplars are labeled           following text: {TEXT}
   distribution*                       correctly*
       I am so mad: Angry
              I am so mad: Angry

       I love life: Happy
              I love life: Happy

       I hate my boss: Angry
           I hate my boss: Angry
                      Figure 2.5: ICL instruction prompt
       Life is good: Happy
             Life is good: Happy

       I’m so excited:                  I’m so excited:

       I am so mad: Angry
              I am so mad: Happy

       People are so dense: Angry
      I love life: Angry
                Exemplar Quantity Increasing the quantity of ex-
       I hate my boss: Angry
           I hate my boss: Angry

       Life is good: Happy
             Life is good: Happy
               emplars in the prompt generally improves model
       I’m so excited:                  I’m so excited:
                                                                           performance, particularly in larger models (Brown
   5. Exemplar Format                  6. Exemplars Similarity             et al., 2020). However, in some cases, the bene-
   Choose a common format*             Select similar exemplars to
                                       the test instance*                  fits may diminish beyond 20 exemplars (Liu et al.,
                                                                           2021). In the case of long context LLMs, addi-
       Im hyped!: Happy
                Im hyped!: Happy

       Im not very excited: Angry
      Im not very excited: Angry
        tional exemplars continue to increase performance,
       I’m so excited:                  I’m so excited:                    though efficiency varies depending on task and
                                                                           model (Agarwal et al., 2024; Bertsch et al., 2024;
       Trees are nice===Happy
          Trees are beautiful: Happy
        Jiang et al., 2024).
       YouTube Ads Suck===Angry
        YouTube Ads Suck: Angry

       I’m so excited===                I’m so excited:
                                                                           Exemplar Ordering The order of exemplars af-
                                                                           fects model behavior (Lu et al., 2021; Kumar and
Figure 2.3: We highlight six main design decisions
                                                                           Talukdar, 2021; Liu et al., 2021; Rubin et al., 2022).
when crafting few-shot prompts. ∗ Please note that rec-
ommendations here do not generalize to all tasks; in
                                                                           On some tasks, exemplar order can cause accuracy
some cases, each of them could hurt performance.                           to vary from sub-50% to 90%+ (Lu et al., 2021).

                                                                           Exemplar Label Distribution As in traditional
Few-Shot Prompting (Brown et al., 2020) is the                             supervised machine learning, the distribution of
paradigm seen in Figure 2.4, where the GenAI                               exemplar labels in the prompt affects behavior. For
learns to complete a task with only a few examples                         example, if 10 exemplars from one class and 2
(exemplars). Few-shot prompting is a special case                          exemplars of another class are included, this may
of Few-Shot Learning (FSL) (Fei-Fei et al., 2006;                          cause the model to be biased toward the first class.
Wang et al., 2019), but does not require updating
                                                                           Exemplar Label Quality Despite the general ben-
of model parameters
                                                                           efit of multiple exemplars, the necessity of strictly
                                                                           valid demonstrations is unclear. Some work (Min
2.2.1.1       Few-Shot Prompting Design Decisions
                                                                           et al., 2022) suggests that the accuracy of labels is
Selecting exemplars for a prompt is a difficult task–                      irrelevant—providing models with exemplars with
performance depends significantly on various fac-                          incorrect labels may not negatively diminish per-
tors of the exemplars (Dong et al., 2023), and only                        formance. However, under certain settings, there
a limited number of exemplars fit in the typical                           is a significant impact on performance (Yoo et al.,
LLM’s context window. We highlight six separate                            2022). Larger models are often better at handling
design decisions, including the selection and or-                          incorrect or unrelated labels (Wei et al., 2023c).
der of exemplars that critically influence the output                         It is important to discuss this factor, since if you
quality (Zhao et al., 2021a; Lu et al., 2021; Ye and                       are automatically constructing prompts from large
Durrett, 2023) (Figure 2.3).                                               datasets that may contain inaccuracies, it may be

                                                                      10
                                                              generated with respect to Dxtest
                                                                                            i  at test time. Here
   Translate the word "cheese" to French.
                                                              is the prompt template we will use for this section,
                                                              following the ‘input: output‘ format (Figure 2.4):
Figure 2.6: ICL from training data prompt. In this
version of ICL, the model is not learning a new skill,
but rather using knowledge likely in its training set.
                                                                 {Exemplars}
                                                                 Dxtest
                                                                    i :



necessary to study how label quality affects your
results.                                                            Figure 2.7: Few-Shot Prompting Template

Exemplar Format The formatting of exemplars
also affects performance. One of the most common              K-Nearest Neighbor (KNN) (Liu et al., 2021) is
formats is “Q: {input}, A: {label}”, but the optimal          part of a family of algorithms that selects exemplars
format may vary across tasks; it may be worth                 similar to Dxtest
                                                                            i   to boost performance. Although ef-
trying multiple formats to see which performs best.           fective, employing KNN during prompt generation
There is some evidence to suggest that formats that           may be time and resource intensive.
occur commonly in the training data will lead to
better performance (Jiang et al., 2020).                      Vote-K (Su et al., 2022) is another method to
                                                              select similar exemplars to the test sample. In one
Exemplar Similarity Selecting exemplars that                  stage, a model proposes useful unlabeled candidate
are similar to the test sample is generally bene-             exemplars for an annotator to label. In the sec-
ficial for performance (Liu et al., 2021; Min et al.,         ond stage, the labeled pool is used for Few-Shot
2022). However, in some cases, selecting more                 Prompting. Vote-K also ensures that newly added
diverse exemplars can improve performance (Su                 exemplars are sufficiently different than existing
et al., 2022; Min et al., 2022).                              ones to increase diversity and representativeness.
Instruction Selection While instructions are re-              Self-Generated In-Context Learning (SG-ICL)
quired to guide LLMs in zero-shot prompts (Wei                (Kim et al., 2022) leverages a GenAI to automati-
et al., 2022a), the benefits of adding instructions           cally generate exemplars. While better than zero-
before exemplars in few-shot prompts is less clear.           shot scenarios when training data is unavailable,
Ajith et al. (2024) show that generic, task-agnostic          the generated samples are not as effective as actual
instructions (i.e., no instruction or “Complete the           data.
following task:”) improve classification and ques-
tion answering accuracy over task-specific ones               Prompt Mining (Jiang et al., 2020) is the process
(e.g., What is the answer to this question?) conclud-         of discovering optimal "middle words" in prompts
ing instruction-following abilities can be achieved           through large corpus analysis. These middle words
via exemplars alone. While they may not improve               are effectively prompt templates. For example, in-
correctness, instructions in few-shot prompts can             stead of using the common "Q: A:" format for few-
still guide auxiliary output attributes like writing          shot prompts, there may exist something similar
style (Roy et al., 2023).                                     that occurs more frequently in the corpus. Formats
                                                              which occur more often in the corpus will likely
2.2.1.2 Few-Shot Prompting Techniques
                                                              lead to improved prompt performance.
Considering all of these factors, Few-Shot Prompt-
ing can be very difficult to implement effectively.           More Complicated Techniques such as LENS
We now examine techniques for Few-Shot Prompt-                (Li and Qiu, 2023a), UDR (Li et al., 2023f), and
ing in the supervised setting. Ensembling ap-                 Active Example Selection (Zhang et al., 2022a)
proaches can also benefit Few-Shot Prompting, but             leverage iterative filtering, embedding and retrieval,
we discuss them separately (Section 2.2.4).                   and reinforcement learning, respectively.
   Assume we have a training dataset, Dtrain ,
which contains multiple inputs Dxtrain
                                    i  and outputs            2.2.1.3   Zero-Shot Prompting Techniques
Dytrain
   i    , which can be  used  to few-shot prompt a            In contrast to Few-Shot Prompting, Zero-Shot
GenAI (rather than performing gradient-based up-              Prompting uses zero exemplars. There are a num-
dates). Assume that this prompt can be dynamically            ber of well-known standalone zero-shot techniques

                                                         11
as well as zero-shot techniques combined with an-
                                                                  Q: Jack has two baskets, each containing
other concept (e.g. Chain of Thought), which we
                                                                  three balls. How many balls does Jack have
discuss later (Section 2.2.2).
                                                                  in total?
Role Prompting (Wang et al., 2023j; Zheng                         A: One basket contains 3 balls, so two bas-
et al., 2023d) , also known as persona prompting                  kets contain 3 * 2 = 6 balls.
(Schmidt et al., 2023; Wang et al., 2023l), assigns a             Q: {QUESTION}
specific role to the GenAI in the prompt. For exam-               A:
ple, the user might prompt it to act like "Madonna"
or a "travel writer". This can create more desir-               Figure 2.8: A One-Shot Chain-of-Thought Prompt.
able outputs for open-ended tasks (Reynolds and
McDonell, 2021) and in some cases may improve
accuracy on benchmarks (Zheng et al., 2023d).                 in reasoning benchmarks, especially with complex
                                                              questions.
Style Prompting (Lu et al., 2023a) involves spec-
ifying the desired style, tone, or genre in the prompt        Self-Ask (Press et al., 2022) prompts LLMs to
to shape the output of a GenAI. A similar effect              first decide if they need to ask follow up questions
can be achieved using role prompting.                         for a given prompt. If so, the LLM generates these
                                                              questions, then answers them and finally answers
Emotion Prompting (Li et al., 2023a) incorpo-                 the original question.
rates phrases of psychological relevance to humans
(e.g., "This is important to my career") into the             2.2.2     Thought Generation
prompt, which may lead to improved LLM perfor-
                                                              Thought generation encompasses a range of tech-
mance on benchmarks and open-ended text genera-
                                                              niques that prompt the LLM to articulate its reason-
tion.
                                                              ing while solving a problem (Zhang et al., 2023c).
System 2 Attention (S2A) (Weston and                          Chain-of-Thought (CoT) Prompting (Wei et al.,
Sukhbaatar, 2023) first asks an LLM to rewrite                2022b) leverages few-shot prompting to encour-
the prompt and remove any information unrelated               age the LLM to express its thought process before
to the question therein. Then, it passes this new             delivering its final answer.6 This technique is occa-
prompt into an LLM to retrieve a final response.              sionally referred to as Chain-of-Thoughts (Tutunov
SimToM (Wilf et al., 2023) deals with compli-                 et al., 2023; Besta et al., 2024; Chen et al., 2023d).
cated questions which involve multiple people or              It has been demonstrated to significantly enhance
objects. Given the question, it attempts to establish         the LLM’s performance in mathematics and reason-
the set of facts one person knows, then answer the            ing tasks. In Wei et al. (2022b), the prompt includes
question based only on those facts. This is a two             an exemplar featuring a question, a reasoning path,
prompt process and can help eliminate the effect of           and the correct answer (Figure 2.8).
irrelevant information in the prompt.                         2.2.2.1    Zero-Shot-CoT
Rephrase and Respond (RaR) (Deng et al., 2023)                The most straightforward version of CoT contains
instructs the LLM to rephrase and expand the ques-            zero exemplars. It involves appending a thought
tion before generating the final answer. For ex-              inducing phrase like "Let’s think step by step."
ample, it might add the following phrase to the               (Kojima et al., 2022) to the prompt. Other sug-
question: "Rephrase and expand the question, and              gested thought-generating phrases include "First,
respond". This could all be done in a single pass             let’s think about this logically" (Kojima et al.,
or the new question could be passed to the LLM                2022). Zhou et al. (2022b) uses LLMs to generate
separately. RaR has demonstrated improvements                 "Let’s work this out in a step by step way to be
on multiple benchmarks.                                       sure we have the right answer". Yang et al. (2023a)
                                                              searches for an optimal thought inducer. Zero-Shot-
Re-reading (RE2) (Xu et al., 2023) adds the
                                                                  6
phrase "Read the question again:" to the prompt in                  We note that such techniques are often described using
                                                              words like "think" that anthropomorphize models. We attempt
addition to repeating the question. Although this is          not to use this language, but do use original authors’ language
such a simple technique, it has shown improvement             where appropriate.


                                                         12
CoT approaches are attractive as they don’t require          benchmark for both GPT-4 and Gemini Ultra mod-
exemplars and are generally task agnostic.                   els.
Step-Back Prompting (Zheng et al., 2023c) is a               Complexity-based Prompting (Fu et al., 2023b)
modification of CoT where the LLM is first asked             involves two major modifications to CoT. First, it
a generic, high-level question about relevant con-           selects complex examples for annotation and in-
cepts or facts before delving into reasoning. This           clusion in the prompt, based on factors like ques-
approach has improved performance significantly              tion length or reasoning steps required. Second,
on multiple reasoning benchmarks for both PaLM-              during inference, it samples multiple reasoning
2L and GPT-4.                                                chains (answers) and uses a majority vote among
Analogical Prompting (Yasunaga et al., 2023)                 chains exceeding a certain length threshold, under
is similar to SG-ICL, and automatically generates            the premise that longer reasoning indicates higher
exemplars that include CoTs. It has demonstrated             answer quality. This technique has shown improve-
improvements in mathematical reasoning and code              ments on three mathematical reasoning datasets.
generation tasks.                                            Active Prompting (Diao et al., 2023) starts with
Thread-of-Thought (ThoT) Prompting (Zhou                     some training questions/exemplars, asks the LLM
et al., 2023) consists of an improved thought in-            to solve them, then calculates uncertainty (disagree-
ducer for CoT reasoning. Instead of "Let’s think             ment in this case) and asks human annotators to
step by step," it uses "Walk me through this context         rewrite the exemplars with highest uncertainty.
in manageable parts step by step, summarizing and
analyzing as we go." This thought inducer works              Memory-of-Thought Prompting (Li and Qiu,
well in question-answering and retrieval settings,           2023b) leverage unlabeled training exemplars to
especially when dealing with large, complex con-             build Few-Shot CoT prompts at test time. Before
texts.                                                       test time, it performs inference on the unlabeled
                                                             training exemplars with CoT. At test time, it re-
Tabular Chain-of-Thought (Tab-CoT) (Jin and                  trieves similar instances to the test sample. This
Lu, 2023) consists of a Zero-Shot CoT prompt that            technique has shown substantial improvements in
makes the LLM output reasoning as a markdown                 benchmarks like Arithmetic, commonsense, and
table. This tabular design enables the LLM to im-            factual reasoning.
prove the structure and thus the reasoning of its
output.                                                      Automatic Chain-of-Thought (Auto-CoT) Prompt-
                                                             ing (Zhang et al., 2022b) uses Wei et al. (2022b)’s
2.2.2.2 Few-Shot CoT                                         Zero-Shot prompt to automatically generate chains
This set of techniques presents the LLM with mul-            of thought. These are then used to build a Few-Shot
tiple exemplars, which include chains-of-thought.            CoT prompt for a test sample.
This can significantly enhance performance. This
technique is occasionally referred to as Manual-             2.2.3   Decomposition
CoT (Zhang et al., 2022b) or Golden CoT (Del and             Significant research has focused on decomposing
Fishel, 2023).                                               complex problems into simpler sub-questions. This
Contrastive CoT Prompting (Chia et al., 2023)                is an effective problem-solving strategy for humans
adds both exemplars with incorrect and correct ex-           as well as GenAI (Patel et al., 2022). Some decom-
planations to the CoT prompt in order to show the            position techniques are similar to thought-inducing
LLM how not to reason. This method has shown                 techniques, such as CoT, which often naturally
significant improvement in areas like Arithmetic             breaks down problems into simpler components.
Reasoning and Factual QA.                                    However, explicitly breaking down problems can
                                                             further improve LLMs’ problem solving ability.
Uncertainty-Routed CoT Prompting (Google,
2023) samples multiple CoT reasoning paths, then             Least-to-Most Prompting (Zhou et al., 2022a)
selects the majority if it is above a certain thresh-        starts by prompting a LLM to break a given prob-
old (calculated based on validation data). If not, it        lem into sub-problems without solving them. Then,
samples greedily and selects that response. This             it solves them sequentially, appending model re-
method demonstrates improvement on the MMLU                  sponses to the prompt each time, until it arrives

                                                        13
at a final result. This method has shown signif-              mathematical and programming-related tasks but
icant improvements in tasks involving symbolic                is less effective for semantic reasoning tasks.
manipulation, compositional generalization, and
mathematical reasoning.                                       Faithful Chain-of-Thought (Lyu et al., 2023)
                                                              generates a CoT that has both natural language and
Decomposed Prompting (DECOMP) (Khot                           symbolic language (e.g. Python) reasoning, just
et al., 2022) Few-Shot prompts a LLM to show it               like Program-of-Thoughts. However, it also makes
how to use certain functions. These might include             use of different types of symbolic languages in a
things like string splitting or internet searching;           task-dependent fashion.
these are often implemented as separate LLM calls.
                                                              Skeleton-of-Thought (Ning et al., 2023) focuses
Given this, the LLM breaks down its original prob-
                                                              on accelerating answer speed through paralleliza-
lem into sub-problems which it sends to different
                                                              tion. Given a problem, it prompts an LLM to create
functions. It has shown improved performance over
                                                              a skeleton of the answer, in a sense, sub-problems
Least-to-Most prompting on some tasks.
                                                              to be solved. Then, in parallel, it sends these ques-
Plan-and-Solve Prompting (Wang et al., 2023f)                 tions to a LLM and concatenates all the outputs to
consists of an improved Zero-Shot CoT prompt,                 get a final response.
"Let’s first understand the problem and devise a              Metacognitive Prompting (Wang and Zhao,
plan to solve it. Then, let’s carry out the plan and          2024) attempts to make the LLM mirror human
solve the problem step by step". This method gener-           metacognitive processes with a five part prompt
ates more robust reasoning processes than standard            chain, with steps including clarifying the question,
Zero-Shot-CoT on multiple reasoning datasets.                 preliminary judgement, evaluation of response, de-
                                                              cision confirmation, and confidence assessment.
Tree-of-Thought (ToT) (Yao et al., 2023b), also
known as Tree of Thoughts, (Long, 2023), creates a            2.2.4   Ensembling
tree-like search problem by starting with an initial
problem then generating multiple possible steps in            In GenAI, ensembling is the process of using multi-
the form of thoughts (as from a CoT). It evaluates            ple prompts to solve the same problem, then aggre-
the progress each step makes towards solving the              gating these responses into a final output. In many
problem (through prompting) and decides which                 cases, a majority vote—selecting the most frequent
steps to continue with, then keeps creating more              response—is used to generate the final output. En-
thoughts. ToT is particularly effective for tasks that        sembling techniques reduce the variance of LLM
require search and planning.                                  outputs and often improving accuracy, but come
                                                              with the cost of increasing the number of model
Recursion-of-Thought (Lee and Kim, 2023) is                   calls needed to reach a final answer.
similar to regular CoT. However, every time it en-
                                                              Demonstration Ensembling (DENSE) (Khalifa
counters a complicated problem in the middle of its
                                                              et al., 2023) creates multiple few-shot prompts,
reasoning chain, it sends this problem into another
                                                              each containing a distinct subset of exemplars from
prompt/LLM call. After this is completed, the an-
                                                              the training set. Next, it aggregates over their out-
swer is inserted into the original prompt. In this
                                                              puts to generate a final response.
way, it can recursively solve complex problems, in-
cluding ones which might otherwise run over that              Mixture of Reasoning Experts (MoRE) (Si et al.,
maximum context length. This method has shown                 2023d) creates a set of diverse reasoning experts
improvements on arithmetic and algorithmic tasks.             by using different specialized prompts for different
Though implemented using fine-tuning to output a              reasoning types (such as retrieval augmentation
special token that sends sub-problem into another             prompts for factual reasoning, Chain-of-Thought
prompt, it could also be done only through prompt-            reasoning for multi-hop and math reasoning, and
ing.                                                          generated knowledge prompting for commonsense
                                                              reasoning). The best answer from all experts is
Program-of-Thoughts (Chen et al., 2023d) uses                 selected based on an agreement score.
LLMs like Codex to generate programming code
as reasoning steps. A code interpreter executes               Max Mutual Information Method (Sorensen
these steps to obtain the final answer. It excels in          et al., 2022) creates multiple prompt templates with

                                                         14
varied styles and exemplars, then selects the opti-         Prompt Paraphrasing (Jiang et al., 2020) trans-
mal template as the one that maximizes mutual               forms an original prompt by changing some of the
information between the prompt and the LLM’s                wording, while still maintaining the overall mean-
outputs.                                                    ing. It is effectively a data augmentation technique
                                                            that can be used to generate prompts for an ensem-
Self-Consistency (Wang et al., 2022) is based               ble.
on the intuition that multiple different reasoning
paths can lead to the same answer. This method              2.2.5   Self-Criticism
first prompts the LLM multiple times to perform
CoT, crucially with a non-zero temperature to elicit        When creating GenAI systems, it can be useful to
diverse reasoning paths. Next, it uses a majority           have LLMs criticize their own outputs (Huang et al.,
vote over all generated responses to select a final         2022). This could simply be a judgement (e.g., is
response. Self-Consistency has shown improve-               this output correct) or the LLM could be prompted
ments on arithmetic, commonsense, and symbolic              to provide feedback, which is then used to improve
reasoning tasks.                                            the answer. Many approaches to generating and
                                                            integrating self-criticism have been developed.
Universal Self-Consistency (Chen et al., 2023e)
is similar to Self-Consistency except that rather           Self-Calibration (Kadavath et al., 2022) first
than selecting the majority response by program-            prompts an LLM to answer a question. Then, it
matically counting how often it occurs, it inserts          builds a new prompt that includes the question, the
all outputs into a prompt template that selects the         LLM’s answer, and an additional instruction asking
majority answer. This is helpful for free-form text         whether the answer is correct. This can be useful
generation and cases where the same answer may              for gauging confidence levels when applying LLMs
be output slightly differently by different prompts.        when deciding when to accept or revise the original
                                                            answer.
Meta-Reasoning over Multiple CoTs (Yoran
et al., 2023) is similar to universal Self-                 Self-Refine (Madaan et al., 2023) is an iterative
Consistency; it first generates multiple reasoning          framework where, given an initial answer from the
chains (but not necessarily final answers) for a            LLM, it prompts the same LLM to provide feed-
given problem. Next, it inserts all of these chains         back on the answer, and then prompts the LLM to
in a single prompt template then generates a final          improve the answer based on the feedback. This
answer from them.                                           iterative process continues until a stopping condi-
                                                            tion is met (e.g., max number of steps reached).
DiVeRSe (Li et al., 2023i) creates multiple
                                                            Self-Refine has demonstrated improvement across
prompts for a given problem then performs Self-
                                                            a range of reasoning, coding, and generation tasks.
Consistency for each, generating multiple reason-
ing paths. They score reasoning paths based on
                                                            Reversing Chain-of-Thought (RCoT) (Xue
each step in them then select a final response.
                                                            et al., 2023) first prompts LLMs to reconstruct
Consistency-based Self-adaptive Prompting                   the problem based on generated answer. Then, it
(COSP) (Wan et al., 2023a) constructs Few-Shot              generates fine-grained comparisons between the
CoT prompts by running Zero-Shot CoT with                   original problem and the reconstructed problem
Self-Consistency on a set of examples then                  as a way to check for any inconsistencies. These
selecting a high agreement subset of the outputs            inconsistencies are then converted to feedback for
to be included in the final prompt as exemplars. It         the LLM to revise the generated answer.
again performs Self-Consistency with this final
prompt.                                                     Self-Verification (Weng et al., 2022) gener-
                                                            ates multiple candidate solutions with Chain-of-
Universal Self-Adaptive Prompting (USP) (Wan                Thought (CoT). It then scores each solution by
et al., 2023b) builds upon the success of COSP, aim-        masking certain parts of the original question and
ing to make it generalizable to all tasks. USP makes        asking an LLM to predict them based on the rest
use of unlabeled data to generate exemplars and a           of the question and the generated solution. This
more complicated scoring function to select them.           method has shown improvement on eight reasoning
Additionally, USP does not use Self-Consistency.            datasets.

                                                       15
Chain-of-Verification     (COVE) (Dhuliawala                   any mentioned dataset or model from the body of
et al., 2023) first uses an LLM to generate an                 papers in our dataset. After, we manually filtered
answer to a given question. Then, it creates a                 out results that were not models or datasets. The
list of related questions that would help verify               citation counts were acquired by searching items
the correctness of the answer. Each question is                from the finalized list on Semantic Scholar.
answered by the LLM, then all the information
is given to the LLM to produce the final revised               2.4     Prompt Engineering
answer. This method has shown improvements in                  In addition to surveying prompting techniques, we
various question-answering and text-generation                 also review prompt engineering techniques, which
tasks.                                                         are used to automatically optimize prompts. We
Cumulative Reasoning (Zhang et al., 2023b)                     discuss some techniques that use gradient updates,
first generates several potential steps in answering           since the set of prompt engineering techniques is
the question. It then has a LLM evaluate them, de-             much smaller than that of prompting techniques.
ciding to either accept or reject these steps. Finally,        Meta Prompting is the process of prompting a
it checks whether it has arrived at the final answer.          LLM to generate or improve a prompt or prompt
If so, it terminates the process, but otherwise it             template (Reynolds and McDonell, 2021; Zhou
repeats it. This method has demonstrated improve-              et al., 2022b; Ye et al., 2023). This is often done
ments in logical inference tasks and mathematical              without any scoring mechanism, using just a sim-
problem.                                                       ple template (Figure 2.12). However, other works
                                                               present more complex uses of meta-prompting,
2.3     Prompting Technique Usage
                                                               with multiple iterations and scoring mechanisms
As we have just seen, there exist many text-based              Yang et al. (2023a); Fernando et al. (2023).
prompting techniques. However, only a small sub-
set of them are commonly used in research and in                     Improve the following prompt: {PROMPT}
industry. We measure technique usage by proxy of
measuring the number of citations by other papers
in our dataset. We do so with the presumption that               Figure 2.12: A simple Meta Prompting template.
papers about prompting are more likely to actually
use or evaluate the cited technique. We graph the              AutoPrompt (Shin et al., 2020b) uses a frozen
top 25 papers cited in this way from our dataset and           LLM as well as a prompt template that includes
find that most of them propose new prompting tech-             some "trigger tokens", whose values are updated
niques (Figure 2.11). The prevalence of citations              via backpropogation at training time. This is a
for Few-Shot and Chain-of-Thought prompting is                 version of soft-prompting.
unsurprising and helps to establish a baseline for
understanding the prevalence of other techniques.              Automatic Prompt Engineer (APE) (Zhou et al.,
                                                               2022b) uses a set of exemplars to generate a Zero-
2.3.1    Benchmarks                                            Shot instruction prompt. It generates multiple pos-
In prompting research, when researchers propose                sible prompts, scores them, then creates variations
a new technique, they usually benchmark it across              of the best ones (e.g. by using prompt paraphras-
multiple models and datasets. This is important to             ing). It iterates on this process until some desider-
prove the utility of the technique and examine how             ata are reached.
it transfers across models.
                                                               Gradientfree Instructional Prompt Search
    In order to make it easier for researchers propos-
                                                               (GrIPS) (Prasad et al., 2023) is similar to APE,
ing new techniques to know how to benchmark
                                                               but uses a more complex set of operations includ-
them, we quantitatively examine which models
                                                               ing deletion, addition, swapping, and paraphrasing
(Figure 2.9) and what benchmark datasets (Fig-
                                                               in order to create variations of a starting prompt.
ure 2.10) are being used. Again, we measure usage
by how many times papers in our dataset cite the               Prompt Optimization with Textual Gradients (Pro-
benchmark datasets and models.                                 TeGi) (Pryzant et al., 2023) is a unique approach
    To find which datasets and models are being                to prompt engineering that improves a prompt tem-
used, we prompted GPT-4-1106-preview to extract                plate through a multi-step process. First, it passes

                                                          16
                                                          Citation Counts of Prompting Techniques




                                                                                                                                                                                                                                                                                       Figure 2.11: Citation Counts of Prompting Techniques.

                                                                                                                                                                                                                                                                                       they are cited by other papers in our dataset. Most pa-
                                                                                                                                                                                                                                                                                       The top 25 papers in our dataset, measured by how often

                                                                                                                                                                                                                                                                                       pers here are prompting techniques*, and the remaining
         103
         102
Counts




                                                                                                                                                                                                                                                                                       papers contains prompting advice.
         101
         100
                           * * s * y * al g * * * * * * * * * y * s * * * s * r* t* * * * n * * * * g t* *
                        ing ing ple ncy tivit ting iev tin CoT Ask hts hts ting fine ting tion ting rve hts izer ting ting CoT ple ting ve gh CoT tion ICL itio tion ing tion ting blin gh ond
                     arn on am te si p tr mp ic lf- ug ug p Re p ua p Su ug im p p ul am p rie ou e- ca ed os ca on ca p m ou sp
                   Le eas Ex sis en om Re ro at Se f Tho f Tho Prom Self- Prom Eval Prom ning f Tho Opt Prom Prom aithf rt Ex Prom Ret of-Th omat erifi erat omp erifi Reas erifi Prom Ense of-Th d Re
                ot t R xt Con er S t Pr pt el P tom              o o d                     f- c r o s e e F po NN mo ee- ut re V en Dec e V ive of-V ive on ry- an
             -Sh ho nte lf- rd os rom ev Au
                   S          e          M P         L        ee m se              osed Sel uti ea ph s a tiv lv
                                                                                                        L                 o     p k e r A       T          a     - G       t iv t - t i o se
                                                                                                                                                                                         n       t
                         o
          Few ro- -C S pt to-
                                   O
                                                an
                                                   -        Tr    gra -Ba       mp
                                                                                              i e     t
                                                                                          Ma ex Gr LL A d-
                                                                                                          a M     c     S   S u
                                                                                                                                           ed
                                                                                                                                              D               l f      n          a    i     p
                                                                                                                                                        -Aw Se tio duc ul ha -Ada nstr Mem phra
                                                                                                                                                                                               a
              Ze od In          m    st-      m                Pro lexity    co                   n t
                                                                                                                  n-a
                                                                                                                      n              i f i
                                                                                                                                                  Ste
                                                                                                                                                      p            e s   e    u m   C     lf o
                Go           Pro Lea       Hu                             De                  co
                                                                                                              Pla
                                                                                                                                  Un                          Qu D C                  Se Dem       Re
                                                                mp                        In-
                                                                  Co
                                                                                                            Prompting Techniques




                                                                                                                                                                                                                                                                                                                                                                                            17
                     Counts of Model Mentions in Dataset                                                                                                                                                             Dataset Mentions in Papers




                                                                                                                            Figure 2.9: Citation Counts of GenAI Models




                                                                                                                                                                                                                                                                                                                                                 Figure 2.10: Citation Counts of Datasets
         500                                                                                                                                                                                   800




                                                                                                                                                                          Number of Mentions
         400
                                                                                                                                                                                               600
Count




         300
                                                                                                                                                                                               400
         200
         100                                                                                                                                                                                   200
           0                                                                                                                                                                                     0
                 T-3 RT T-4 RTa LM MA RT ex PT PT OM AN LIP AM RT da go MZ Op er P-2 LP ma RT VA ron NO ion                                                                                            M8
                                                                                                                                                                                                          K     LU         H            A          ag          h
                                                                                                                                                                                                                                                             nc rand
                                                                                                                                                                                                                                                                     e     SC             AT     QA
               GP BE GP E Pa La BA od O tG O FL C S BE mb in O Co rm LI V lla BE LatorTg DI Fus
                         B      L     C        u c   L       i o   a       m   O   o      fo B       e  i n   L                                                                                      GS       MM       BB         seQ            Sw      -be             QA            A-R thful
                      Ro                    tr     B       B     L   F l a  B L  C    n s        o d   F       Gandinream                                                                                                      sen            lla                G                 U
                                        Ins                                       r a          C                                                                                                                            on              He        BIG Wino                  AQ           Tru
                                                                                nT                            ou D                                                                                                      mm
                                                                             io                             Gr
                                                                         Vis                                                                                                                                          Co
                                                           Model Name                                                                                                                                                                            Dataset Name
                                                                                 LLM Response
a batch of inputs through the template, then passes
the output, ground truth, and prompt into another                                   Likely Negative
prompt that criticizes the original prompt. It gener-
ates new prompts from these criticisms then uses
                                                              Answer Shape:

                                                             A span of tokens       This is negative
a bandit algorithm (Gabillon et al., 2011) to se-                                   NEGATIVE !
lect one. ProTeGi demonstrates improvements over
methods like APE and GRIPS.
                                                                              Answer Space:
           Answer Extraction:

                                                                       All possible spans of tokens   Select the proper label
RLPrompt (Deng et al., 2022) uses a frozen LLM
with an unfrozen module added. It uses this LLM to           Figure 2.13: An annotated output of a LLM output for a
                                                             labeling task, which shows the three design decisions of
generate prompt templates, scores the templates on
                                                             answer engineering: the choice of answer shape, space,
a dataset, and updates the unfrozen module using             and extractor. Since this is an output from a classifi-
Soft Q-Learning (Guo et al., 2022). Interestingly,           cation task, the answer shape could be restricted to a
the method often selects grammatically nonsensical           single token and the answer space to one of two tokens
text as the optimal prompt template.                         ("positive" or "negative"), though they are unrestricted
                                                             in this image.
Dialogue-comprised Policy-gradient-based Dis-
crete Prompt Optimization (DP2O) (Li et al.,
2023b) is perhaps the most complicated prompt en-            2.5.1    Answer Shape
gineering technique, involving reinforcement learn-          The shape of an answer is its physical format. For
ing, a custom prompt scoring function, and conver-           example, it could be a token, span of tokens, or
sations with an LLM to construct the prompt.                 even an image or video.7 It is sometimes useful to
                                                             restrict the output shape of a LLM to a single token
2.5   Answer Engineering                                     for tasks like binary classification.

Answer engineering is the iterative process of de-           2.5.2    Answer Space
veloping or selecting among algorithms that extract          The space of an answer is the domain of values
precise answers from LLM outputs. To understand              that its structure may contain. This may simply be
the need for answer engineering, consider a bi-              the space of all tokens, or in a binary labeling task,
nary classification task where the labels are "Hate          could just be two possible tokens.
Speech" and "Not Hate Speech". The prompt tem-
plate might look like this:                                  2.5.3    Answer Extractor
                                                             In cases where it is impossible to entirely control
   Is this "Hate Speech" or "Not Hate Speech":               the answer space (e.g. consumer-facing LLMs), or
   {TEXT}                                                    the expected answer may be located somewhere
                                                             within the model output, a rule can be defined to
   When a hate speech sample is put through the              extract the final answer. This rule is often a simple
template, it might have outputs such as "It’s hate           function (e.g. a regular expression), but can also
speech", "Hate Speech.", or even "Hate speech,               use a separate LLM to extract the answer.
because it uses negative language against a racial           Verbalizer Often used in labeling tasks, a verbal-
group". This variance in response formats is diffi-          izer maps a token, span, or other type of output
cult to parse consistently; improved prompting can           to a label and vice-versa (injective) (Schick and
help, but only to a certain extent.                          Schütze, 2021). For example, if we wish for a
   There are three design decisions in answer en-            model to predict whether a Tweet is positive or
gineering, the choice of answer space, answer                negative, we could prompt it to output either "+"
shape, and answer extractor (Figure 2.13). Liu               or "-" and a verbalizer would map these token se-
et al. (2023b) define the first two as necessary             quences to the appropriate labels. The selection
components of answer engineering and we append               of a verbalizer constitutes a component of answer
the third. We consider answer engineering to be              engineering.
distinct from prompt engineering, but extremely                 7
                                                                 We use a different definition than Liu et al. (2023b) with
closely related; the processes are often conducted           respect to granularity (e.g. token vs span), since the output
in tandem.                                                   could be of a different modality.


                                                        18
Regex As mentioned previously, Regexes are of-
ten used to extract answers. They are usually used
to search for the first instance of a label. However,
depending on the output format and whether CoTs
are generated, it may be better to search for the last
instance.
Separate LLM Sometimes outputs are so com-
plicated that regexes won’t work consistently. In
this case, it can be useful to have a separate LLM
evaluate the output and extract an answer. This
separate LLM will often use an answer trigger
(Kojima et al., 2022), e.g. "The answer (Yes or No)
is", to extract the answer.




                                                         19
3       Beyond English Text Prompting

Prompting GenAIs with English text currently                  X-InSTA Prompting (Tanwar et al., 2023) ex-
stands as the dominant method for interaction.                plores three distinct approaches for aligning in-
Prompting in other languages or through differ-               context examples with the input sentence for classi-
ent modalities often requires special techniques to           fication tasks: using semantically similar examples
achieve comparable performance. In this context,              to the input (semantic alignment), examples that
we discuss the domains of multilingual and multi-             share the same label as the input (task-based align-
modal prompting.                                              ment), and the combination of both semantic and
                                                              task-based alignments.
3.1     Multilingual
                                                              In-CLT (Cross-lingual Transfer) Prompting
State-of-the-art GenAIs have often been predom-               (Kim et al., 2023) leverages both the source and
inately trained with English dataset, leading to a            target languages to create in-context examples, di-
notable disparity in the output quality in languages          verging from the traditional method of using source
other than English, particularly low-resource lan-            language exemplars. This strategy helps stimulate
guages (Bang et al., 2023; Jiao et al., 2023; Hendy           the cross-lingual cognitive capabilities of multilin-
et al., 2023; Shi et al., 2022). As a result, various         gual LLMs, thus boosting performance on cross-
multilingual prompting techniques have emerged                lingual tasks.
in an attempt to improve model performance in                 3.1.2.1 In-Context Example Selection
non-English settings (Figure 3.1).
                                                              In-context example selection heavily influences the
                                                              multilingual performance of LLMs (Garcia et al.,
Translate First Prompting (Shi et al., 2022) is
                                                              2023; Agrawal et al., 2023). Finding in-context ex-
perhaps the simplest strategy and first translates
                                                              amples that are semantically similar to the source
non-English input examples into English. By trans-
                                                              text is very important (Winata et al., 2023; Moslem
lating the inputs into English, the model can utilize
                                                              et al., 2023; Sia and Duh, 2023). However, us-
its strengths in English to better understand the con-
                                                              ing semantically dissimilar (peculiar) exemplars
tent. Translation tools vary; Shi et al. (2022) use an
                                                              has also been shown to enhance performance (Kim
external MT system, Etxaniz et al. (2023) prompt
                                                              and Komachi, 2023). This same contrast exists in
multilingual LMs and Awasthi et al. (2023) prompt
                                                              the English-only setting. Additionally, when deal-
LLMs to translate non-English inputs.
                                                              ing with ambiguous sentences, selecting exemplars
3.1.1    Chain-of-Thought (CoT)                               with polysemous or rare word senses may boost
                                                              performance (Iyer et al., 2023).
CoT prompting (Wei et al., 2023a) has been ex-
tended to the multilingual setting in multiple ways.          PARC (Prompts Augmented by Retrieval Cross-
                                                              lingually) (Nie et al., 2023) introduce a frame-
XLT (Cross-Lingual Thought) Prompting                         work that retrieves relevant exemplars from a high
(Huang et al., 2023a) utilizes a prompt template              resource language. This framework is specifically
composed of six separate instructions, including              designed to enhance cross-lingual transfer perfor-
role assignment, cross-lingual thinking, and CoT.             mance, particularly for low-resource target lan-
                                                              guages. Li et al. (2023g) extend this work to
Cross-Lingual Self Consistent Prompting (CLSP)                Bangla.
(Qin et al., 2023a) introduces an ensemble tech-
nique that constructs reasoning paths in different            3.1.3   Prompt Template Language Selection
languages to answer the same question.                        In multilingual prompting, the selection of lan-
                                                              guage for the prompt template can markedly in-
3.1.2    In-Context Learning                                  fluence the model performance.
ICL has also been extended to multilingual settings           English Prompt Template Constructing the
in multiple ways.                                             prompt template in English is often more effec-

                                                         20
                                                                                    XLT 3.1.1
                                                 Chain-of-Thought 3.1.1
                                                                                    CLSP 3.1.1

                                                                                    X-InSTA 3.1.2
                                                 In-Context Learning 3.1.2
                                                                                    In-CLT 3.1.2

                                                                                    PARC 3.1.2.1

                                                 In-Context Ex. Selection 3.1.2.1   Semantically-Aligned 3.1.2.1

                                                                                    Semantically-Distant 3.1.2.1

                                                                                    Interactive Chain 3.1.4.1
                                                 Human-in-the-Loop 3.1.4.1
                                                                                    Iterative 3.1.4.1
                       Multilingual Techniques
                                                                                    Chain-of-Dictionary 3.1.4

                                                                                    DecoMT 3.1.4
                                                 Translation 3.1.4
                                                                                    DiPMT 3.1.4

                                                                                    MAPS 3.1.4

                                                                                    External MT Systems 3.1

                                                 Translate First Prompting 3.1      Standard LLMs 3.1

                                                                                    Multilingual LLMs 3.1

                                                                                    English 3.1.3
                                                 Prompt Language 3.1.3
                                                                                    Task Language 3.1.3


                                  Figure 3.1: All multilingual prompting techniques.


tive than in the task language for multilingual tasks.               3.1.4       Prompting for Machine Translation
This is likely due to the predominance of English
data during LLM pre-training (Lin et al., 2022;                      There is significant research into leveraging GenAI
Ahuja et al., 2023). Lin et al. (2022) suggest that                  to facilitate accurate and nuanced translation. Al-
this is likely due to a high overlap with pre-training               though this is a specific application of prompt-
data and vocabulary. Similarly, Ahuja et al. (2023)                  ing, many of these techniques are important more
highlight how translation errors when creating task                  broadly for multilingual prompting.
language templates propagate in the form of in-
correct syntax and semantics, adversely affecting                    Multi-Aspect Prompting and Selection (MAPS)
task performance. Further, Fu et al. (2022) com-                     (He et al., 2023b) mimics the human translation pro-
pare in-lingual (task language) prompts and cross-                   cess, which involves multiple preparatory steps to
lingual (mixed language) prompts and find the                        ensure high-quality output. This framework starts
cross-lingual approach to be more effective, likely                  with knowledge mining from the source sentence
because it uses more English in the prompt, thus                     (extracting keywords and topics, and generating
facilitating retrieving knowledge from the model.                    translation exemplars). It integrates this knowledge
                                                                     to generate multiple possible translations, then se-
                                                                     lects the best one.

                                                                     Chain-of-Dictionary (CoD) (Lu et al., 2023b)
Task Language Prompt Template In contrast,                           first extracts words from the source phrase, then
many multilingual prompting benchmarks such                          makes a list of their meanings in multiple lan-
as BUFFET (Asai et al., 2023) or LongBench                           guages, automatically via retrieval from a dictio-
(Bai et al., 2023a) use task language prompts                        nary (e.g. English: ‘apple’, Spanish: ‘manzana’).
for language-specific use cases. Muennighoff                         Then, they prepend these dictionary phrases to the
et al. (2023) specifically studies different transla-                prompt, where it asks a GenAI to use them during
tion methods when constructing native-language                       translation.
prompts. They demonstrate that human translated
prompts are superior to their machine-translated                     Dictionary-based Prompting for Machine Trans-
counterparts. Native or non-native template perfor-                  lation (DiPMT) (Ghazvininejad et al., 2023)
mance can differ across tasks and models (Li et al.,                 works similarly to CoD, but only gives definitions
2023h). As such, neither option will always be the                   in the source and target languages, and formats
best approach (Nambi et al., 2023).                                  them slightly differently.

                                                              21
                                                                                                          Chain-of-Images 3.2.1.2

                                                                                 MM. CoT 3.2.1.2          Duty Distinct CoT 3.2.1.2

                                                                                                          MM Graph-of-Thought 3.2.1.2

                                                                                                          Image-as-Text Prompt3.2.1.1
                                             Image 3.2.1
                                                                                 Multimodal ICL 3.2.1.1
                                                                                                          Paired-Image Prompt 3.2.1.1
                                                                                 Negative Prompt 3.2.1
             Multimodal (MM) Techniques      Segmentation Prompting 3.2.4        Prompt Modifiers 3.2.1

                                             Video 3.2.3                         Video Gen. 3.2.3.1

                                             3D Prompting 3.2.5


                                          Figure 3.2: All multimodal prompting techniques.


Decomposed Prompting for MT (DecoMT)                                             generation (Ding et al., 2021; Hinz et al., 2022;
(Puduppully et al., 2023) divides the source text                                Tao et al., 2022; Li et al., 2019a,b; Rombach et al.,
into several chunks and translates them indepen-                                 2022), caption generation (Li et al., 2020), image
dently using few-shot prompting. Then it uses these                              classification (Khalil et al., 2023), and image edit-
translations and contextual information between                                  ing (Crowson et al., 2022; Kwon and Ye, 2022;
chunks to generate a final translation.                                          Bar-Tal et al., 2022; Hertz et al., 2022). We now
                                                                                 describe various image prompting techniques used
3.1.4.1    Human-in-the-Loop                                                     for such applications.
Interactive-Chain-Prompting (ICP) (Pilault
et al., 2023) deals with potential ambiguities in                                Prompt Modifiers are simply words appended to
translation by first asking the GenAI to generate                                a prompt to change the resultant image (Oppenlaen-
sub-questions about any ambiguities in the phrase                                der, 2023). Components such as Medium (e.g. "on
to be translated. Humans later respond to these                                  canvas") or Lighting (e.g. "a well lit scene") are
questions and the system includes this information                               often used.
to generate a final translation.
Iterative Prompting (Yang et al., 2023d) also                                    Negative Prompting allows users to numerically
involves humans during translation. First, they                                  weight certain terms in the prompt so that the
prompt LLMs to create a draft translation. This                                  model considers them more/less heavily than oth-
initial version is further refined by integrating su-                            ers. For example, by negatively weighting the
pervision signals obtained from either automated                                 terms “bad hands” and “extra digits”, models may
retrieval systems or direct human feedback.                                      be more likely to generate anatomically accurate
                                                                                 hands (Schulhoff, 2022).
3.2     Multimodal
                                                                                 3.2.1.1         Multimodal In-Context Learning
As GenAI models evolve beyond text-based do-
mains, new prompting techniques emerge. These                                    The success of ICL in text-based settings has
multimodal prompting techniques are often not                                    prompted research into multimodal ICL (Wang
simply applications of text-based prompting tech-                                et al., 2023k; Dong et al., 2023).
niques, but entirely novel ideas made possible by
different modalities. We now extend our text-                                    Paired-Image Prompting shows the model two
based taxonomy to include a mixture of multimodal                                images: one before and one after some transforma-
analogs of text-based prompting techniques as well                               tion. Then, present the model with a new image for
as completely novel multimodal techniques (Figure                                which it will perform the demonstrated conversion.
3.2).                                                                            This can be done either with textual instructions
                                                                                 (Wang et al., 2023k) or without them (Liu et al.,
3.2.1     Image Prompting                                                        2023e).
The image modality encompasses data such as pho-
tographs, drawings, or even screenshots of text                                  Image-as-Text Prompting (Hakimov and
(Gong et al., 2023). Image prompting may refer                                   Schlangen, 2023) generates a textual description of
to prompts that either contain images or are used                                an image. This allows for the easy inclusion of the
to generate images. Common tasks include image                                   image (or multiple images) in a text-based prompt.

                                                                            22
3.2.1.2    Multimodal Chain-of-Thought                       and video-to-text generation (Yousaf et al., 2023;
CoT has been extended to the image domain in                 Mi et al., 2023; Ko et al., 2023a).
various ways (Zhang et al., 2023d; Huang et al.,             3.2.3.1 Video Generation Techniques
2023c; Zheng et al., 2023b; Yao et al., 2023c). A
                                                             When prompting a model to generate video, var-
simple example of this would be a prompt contain-
                                                             ious modalities of prompts can be used as input,
ing an image of a math problem accompanied by
                                                             and several prompt-related techniques are often em-
the textual instructions "Solve this step by step".
                                                             ployed to enhance video generation. Image related
Duty Distinct Chain-of-Thought (DDCoT)                       techniques, such as prompt modifiers can often be
(Zheng et al., 2023b) extends Least-to-Most                  used for video generation (Runway, 2023).
prompting (Zhou et al., 2022a) to the multimodal             3.2.4   Segmentation Prompting
setting, creating subquestions, then solving them
and combining the answers into a final response.             Prompting can also be used for segmentation (e.g.
                                                             semantic segmentation) (Tang et al., 2023; Liu
Multimodal Graph-of-Thought (Yao et al.,                     et al., 2023c).
2023c) extends Graph-of-Thought Zhang et al.
(2023d) to the multimodal setting. GoT-Input also            3.2.5   3D Prompting
uses a two step rationale then answer process. At            Prompting can also be used in 3D modalities, for
inference time, the the input prompt is used to con-         example in 3D object synthesis (Feng et al., 2023;
struct a thought graph, which is then used along             Li et al., 2023d,c; Lin et al., 2023; Chen et al.,
with the original prompt to generate a rationale to          2023f; Lorraine et al., 2023; Poole et al., 2022; Jain
answer the question. When an image is input along            et al., 2022), 3D surface texturing (Liu et al., 2023g;
with the question, an image captioning model is              Yang et al., 2023b; Le et al., 2023; Pajouheshgar
employed to generate a textual description of the            et al., 2023), and 4D scene generation (animating a
image, which is then appended to the prompt before           3D scene) (Singer et al., 2023; Zhao et al., 2023c),
the thought graph construction to provide visual             where input prompt modalities include text, image,
context.                                                     user annotation (bounding boxes, points, lines), and
                                                             3D objects.
Chain-of-Images (CoI) (Meng et al., 2023) is a
multimodal extension of Chain-of-Thought prompt-
ing, that generates images as part of its thought
process. They use the prompt “Let’s think image
by image” to generate SVGs, which the model can
then use to reason visually.

3.2.2     Audio Prompting
Prompting has also been extended to the audio
modality. Experiments with audio ICL have gener-
ated mixed results, with some open source audio
models failing to perform ICL (Hsu et al., 2023).
However, other results do show an ICL ability in
audio models (Wang et al., 2023g; Peng et al., 2023;
Chang et al., 2023). Audio prompting is currently
in early stages, but we expect to see various prompt-
ing techniques proposed in the future.

3.2.3     Video Prompting
Prompting has also been extended to the video
modality, for use in text-to-video generation
(Brooks et al., 2024; Lv et al., 2023; Liang et al.,
2023; Girdhar et al., 2023), video editing (Zuo
et al., 2023; Wu et al., 2023a; Cheng et al., 2023),

                                                        23
4        Extensions of Prompting

The techniques we have discussed thus far can be                     (Karpas et al., 2022), LLMs that can output strings
extremely complicated, incorporating many steps                      that cause actions to be taken in a gym-like (Brock-
and iterations. However, we can take prompting                       man et al., 2016; Towers et al., 2023) environment
further by adding access to external tools (agents)                  (Yao et al., 2022), and more broadly, LLMs which
and complex evaluation algorithms to judge the                       write and record plans, write and run code, search
validity of LLM outputs.                                             the internet, and more (Significant Gravitas, 2023;
                                                                     Yang et al., 2023c; Osika, 2023). OpenAI Assis-
4.1     Agents                                                       tants OpenAI (2023), LangChain Agents (Chase,
                                                                     2022), and LlamaIndex Agents (Liu, 2022) are ad-
As LLMs have improved rapidly in capabilities
                                                                     ditional examples.
(Zhang et al., 2023c), companies (Adept, 2023)
and researchers (Karpas et al., 2022) have explored                  4.1.1   Tool Use Agents
how to allow them to make use of external sys-
tems. This has been necessitated by shortcomings                     Tool use is a critical component for GenAI agents.
of LLMs in areas such as mathematical computa-                       Both symbolic (e.g. calculator, code interpreter)
tions, reasoning, and factuality. This has driven sig-               and neural (e.g. a separate LLM) external tools
nificant innovations in prompting techniques; these                  are commonly used. Tools may occasionally be
systems are often driven by prompts and prompt                       referred to as experts (Karpas et al., 2022) or mod-
chains, which are heavily engineered to allow for                    ules.
agent-like behaviour (Figure 4.1).                                   Modular Reasoning, Knowledge, and Language
Definition of Agent In the context of GenAI, we                      (MRKL) System (Karpas et al., 2022) is one of
define agents to be GenAI systems that serve a                       the simplest formulations of an agent. It contains
user’s goals via actions that engage with systems                    a LLM router providing access to multiple tools.
outside the GenAI itself.8 This GenAI is usually a                   The router can make multiple calls to get informa-
LLM. As a simple example, consider an LLM that                       tion such as weather or the current date. It then
is tasked with solving the following math problem:                   combines this information to generate a final re-
                                                                     sponse. Toolformer (Schick et al., 2023), Gorilla
                                                                     (Patil et al., 2023), Act-1 (Adept, 2023), and oth-
      If Annie has 4,939 grapes, and gives exactly
                                                                     ers (Shen et al., 2023; Qin et al., 2023b; Hao et al.,
      39% of them to Amy, how many does she
                                                                     2023) all propose similar techniques, most of which
      have left?
                                                                     involve some fine-tuning.
   If properly prompted, the LLM could output the                    Self-Correcting with Tool-Interactive Critiquing
string CALC(4,939*.39). This output could be                         (CRITIC) (Gou et al., 2024a) first generates a re-
extracted and put into a calculator to obtain the                    sponse to the prompt, with no external calls. Then,
final answer.                                                        the same LLM criticizes this response for possible
   This is an example of an agent: the LLM outputs                   errors. Finally, it uses tools (e.g. Internet search or
text which then uses a downstream tool. Agent                        a code interpreter) accordingly to verify or amend
LLMs may involve a single external system (as                        parts of the response.
above), or they may need to solve the problem
of routing, to choose which external system to                       4.1.2   Code-Generation Agents
use. Such systems also frequently involve memory                     Writing and executing code is another important
and planning in addition to actions (Zhang et al.,                   ability of many agents.9
2023c).
   Examples of agents include LLMs that can make                     Program-aided Language Model (PAL) (Gao
API calls to use external tools like a calculator                    et al., 2023b) translates a problem directly into
     8                                                                  9
       We do not cover the notion of independently-acting AI,             This ability may be considered a tool (i.e. code inter-
i.e. systems that in any sense have their own goals                  preter)


                                                                24
                                                                        CRITIC 4.1.1
                                  Tool Use Agents
                                                                        MRKL Sys. 4.1.1

                                                                        PAL 4.1.2

                                  Code-Based Agents 4.1.2               ToRA 4.1.2

                                                                        Task Weaver 4.1.2

             Agents                                                     ReAct 4.1.3

                                  Observation-Based Agents 4.1.3        Reflexion 4.1.3
                                                                                                         Voyager 4.1.3.1
                                                                        Lifelong Learn. Agents 4.1.3.1
                                                                                                         GITM 4.1.3.1
                                                                        IRCoT 4.1.4

                                                                        DSP 4.1.4
                                  Retrieval Aug. Generation 4.1.4
                                                                        Verify-and-Edit 4.1.4

                                                                        Iterative Retrieval Aug. 4.1.4


                             Figure 4.1: Agent techniques covered in this section.


code, which is sent to a Python interpreter to gen-                     open-world videogame. We view these agents
erate an answer.                                                        not merely as applications of agent techniques
                                                                        to Minecraft, but rather novel agent frameworks
Tool-Integrated Reasoning Agent (ToRA) (Gou                             which can be explored in real world tasks that re-
et al., 2024b) is similar to PAL, but instead of a                      quire lifelong learning.
single code generation step, it interleaves code and
reasoning steps for as long as necessary to solve                       Voyager (Wang et al., 2023a) is composed of
the problem.                                                            three parts. First, it proposes tasks for itself to
                                                                        complete in order to learn more about the world.
TaskWeaver (Qiao et al., 2023) is also similar to                       Second, it generates code to execute these actions.
PAL, transforming user requests into code, but can                      Finally, it saves these actions to be retrieved later
also make use of user-defined plugin.                                   when useful, as part of a long-term memory system.
                                                                        This system could be applied to real world tasks
4.1.3     Observation-Based Agents
                                                                        where an agent needs to explore and interact with
Some agents are designed to solve problems by                           a tool or website (e.g. penetration testing, usability
interacting with toy environments (Brockman et al.,                     testing).
2016; Towers et al., 2023). These observation-
based agents receive observations inserted into their                   Ghost in the Minecraft (GITM) (Zhu et al.,
prompts.                                                                2023) starts with an arbitrary goal, breaks it down
                                                                        into subgoals recursively, then iteratively plans and
Reasoning and Acting (ReAct) (Yao et al.                                executes actions by producing structured text (e.g.
(2022)) generates a thought, takes an action, and                       "equip(sword)") rather than writing code. GITM
receives an observation (and repeats this process)                      uses an external knowledge base of Minecraft items
when given a problem to solve. All of this informa-                     to assist with decomposition as well as a memory
tion is inserted into the prompt so it has a memory                     of past experience.
of past thoughts, actions, and observations.
                                                                        4.1.4 Retrieval Augmented Generation (RAG)
Reflexion (Shinn et al., 2023) builds on ReAct,                         In the context of GenAI agents, RAG is a paradigm
adding a layer of introspection. It obtains a trajec-                   in which information is retrieved from an external
tory of actions and observations, then is given an                      source and inserted into the prompt. This can en-
evaluation of success/failure. Then, it generates                       hance performance in knowledge intensive tasks
a reflection on what it did and what went wrong.                        (Lewis et al., 2021). When retrieval itself is used
This reflection is added to its prompt as a working                     as an external tool, RAG systems are considered to
memory, and the process repeats.                                        be agents.
4.1.3.1    Lifelong Learning Agents                                     Verify-and-Edit (Zhao et al., 2023a) improves on
Work on LLM-integrated Minecraft agents has gen-                        self-consistency by generating multiple chains-of-
erated impressive results, with agents able to ac-                      thought, then selecting some to be edited. They do
quire new skills as they navigate the world of this                     this by retrieving relevant (external) information to

                                                                   25
                                                                           Chain-Of-Thought 4.2.1

                                                                           In-Context Learning 4.2.1
                                            Prompting Techniques 4.2.1
                                                                           Model-Gen. Guidelines 4.2.1

                                                                           Role-Based Evaluation 4.2.1

                                                                           Binary Score 4.2.2

                                                                           Likert Scale 4.2.2
                                            Output Format
                                                                           Linear Scale 4.2.2
                      Evaluation
                                                                           Styling 4.2.2

                                                                           LLM-EVAL 4.2.3

                                            Prompting Frameworks 4.2.3     G-EVAL 4.2.3

                                                                           ChatEval 4.2.3

                                                                           Batch Prompting 4.2.4
                                            Other Methodologies 4.2.4
                                                                           Pairwise Evaluation 4.2.4


                                     Figure 4.2: Evaluation techniques.


the CoTs, and allowing the LLM to augment them               strong contenders as evaluators.10 For example, it
accordingly.                                                 is possible to prompt a LLM to evaluate the quality
                                                             of an essay or even a previous LLM output accord-
Demonstrate-Search-Predict (Khattab et al.,                  ing to some metrics defined in the prompt. We de-
2022) first decomposes a question into sub-                  scribe four components of evaluation frameworks
questions, then uses queries to solve them and               that are important in building robust evaluators: the
combine their responses in a final answer. It uses           prompting technique(s), as described in Section
few-shot prompting to decompose the problem and              2.2, the output format of the evaluation, the frame-
combine responses.                                           work of the evaluation pipeline, and some other
Interleaved Retrieval guided by Chain-of-                    methodological design decisions (Figure 4.2).
Thought (IRCoT) (Trivedi et al., 2023) is a
                                                             4.2.1       Prompting Techniques
technique for multi-hop question answering that
interleaves CoT and retrieval. IRCoT leverages               The prompting technique used in the evaluator
CoT to guide which documents to retrieve and                 prompt (e.g. simple instruction vs CoT) is in-
retrieval to help plan the reasoning steps of CoT.           strumental in building a robust evaluator. Evalua-
                                                             tion prompts often benefit from regular text-based
Iterative Retrieval Augmentation techniques,                 prompting techniques, including a role, instructions
like Forward-Looking Active REtrieval augmented              for the task, the definitions of the evaluation cri-
generation (FLARE) (Jiang et al., 2023) and Im-              teria, and in-context examples. Find a full list of
itate, Retrieve, Paraphrase (IRP) (Balepur et al.,           techniques in Appendix A.6.
2023), perform retrieval multiple times during long-
form generation. Such models generally perform               In-Context Learning is frequently used in evalu-
an iterative three-step process of: 1) generating            ation prompts, much in the same way it is used in
a temporary sentence to serve as a content plan              other applications (Dubois et al., 2023; Kocmi and
for the next output sentence; 2) retrieving exter-           Federmann, 2023a; Brown et al., 2020).
nal knowledge using the temporary sentence as a
query; and 3) injecting the retrieved knowledge              Role-based Evaluation is a useful technique for
into the temporary sentence to create the next out-          improving and diversifying evaluations (Wu et al.,
put sentence. These temporary sentences have been            2023b; Chan et al., 2024). By creating prompts
shown to be better search queries compared to the            with the same instructions for evaluation, but dif-
document titles provided in long-form generation             ferent roles, it is possible to effectively generate
tasks.                                                       diverse evaluations. Additionally, roles can be used
                                                             in a multiagent setting where LLMs debate the va-
4.2   Evaluation                                             lidity of the text to be evaluated (Chan et al., 2024).
The potential of LLMs to extract and reason about              10
                                                                  This section does not describe how to benchmark LLMs,
information and understand user intent makes them            but rather how to use them as evaluators.


                                                        26
Chain-of-Thought prompting can further im-
                                                               Score the following story according to the
prove evaluation performance (Lu et al., 2023c;
                                                               following scale:
Fernandes et al., 2023).
                                                               Poor
Model-Generated Guidelines (Liu et al.,                        Acceptable
2023d,h) prompt an LLM to generate guidelines                  Good
for evaluation. This reduces the insufficient                  Very Good
prompting problem arising from ill-defined scoring             Incredible
guidelines and output spaces, which can result in              {INPUT}
inconsistent and misaligned evaluations. Liu et al.
(2023d) generate a chain-of-thought of the detailed         4.2.3    Prompting Frameworks
evaluation steps that the model should perform
before generating a quality assessment. Liu et al.          LLM-EVAL (Lin and Chen, 2023) is one of the
(2023h) propose AUTO C ALIBRATE, which derives              simplest evaluation frameworks. It uses a single
scoring criteria based on expert human annotations          prompt that contains a schema of variables to eval-
and uses a refined subset of model-generated                uate (e.g. grammar, relevance, etc.), an instruction
criteria as a part of the evaluation prompt.                telling the model to output scores for each variable
                                                            within a certain range, and the content to evaluate.
4.2.2   Output Format
                                                            G-EVAL (Liu et al., 2023d) is similar to LLM-
The output format of the LLM can significantly
                                                            EVAL, but includes an AutoCoT steps in the
affect evaluation performance Gao et al. (2023c).
                                                            prompt itself. These steps are generated accord-
Styling Formatting the LLM’s response using                 ing to the evaluation instructions, and inserted into
XML or JSON styling has also been shown to im-              the final prompt. These weight answers according
prove the accuracy of the judgment generated by             to token probabilities.
the evaluator (Hada et al., 2024; Lin and Chen,
2023; Dubois et al., 2023).                                 ChatEval (Chan et al., 2024) uses a multi-agent
                                                            debate framework with each agent having a sepa-
Linear Scale A very simple output format is a               rate role.
linear scale (e.g. 1-5). Many works use ratings of
1-10 (Chan et al., 2024), 1-5 (Araújo and Aguiar,           4.2.4    Other Methodologies
2023), or even 0-1 (Liu et al., 2023f). The model
                                                            While most approaches directly prompt the LLM
can be prompted to output a discrete (Chan et al.,
                                                            to generate a quality assessment (explicit), some
2024) or continuous (Liu et al., 2023f) score be-
                                                            works also use implicit scoring where a quality
tween the bounds.
                                                            score is derived using the model’s confidence in
                                                            its prediction (Chen et al., 2023g) or the likelihood
   Score the following story on a scale of 1-5
                                                            of generating the output (Fu et al., 2023a) or via
   from well to poorly written:
                                                            the models’ explanation (e.g. count the number
   {INPUT}
                                                            of errors as in Fernandes et al. (2023); Kocmi and
                                                            Federmann (2023a)) or via evaluation on proxy
Binary Score Prompting the model to generate                tasks (factual inconsistency via entailment as in
binary responses like Yes or No (Chen et al., 2023c)        Luo et al. (2023)).
and True or False (Zhao et al., 2023b) is another
frequently used output format.                              Batch Prompting For improving compute and
                                                            cost efficiency, some works employ batch prompt-
   Is the following story well written at a high-           ing for evaluation where multiple instances are
   school level (yes/no)?:                                  evaluated at once11 (Lu et al., 2023c; Araújo and
   {INPUT}                                                  Aguiar, 2023; Dubois et al., 2023) or the same in-
                                                            stance is evaluated under different criteria or roles
Likert Scale Prompting the GenAI to make use                (Wu et al., 2023b; Lin and Chen, 2023). However,
of a Likert Scale (Bai et al., 2023b; Lin and Chen,           11
                                                                Disambiguation: there is no relation to making a forward
2023; Peskoff et al., 2023) can give it a better un-        pass with multiple prompts in parallel. We are referring to a
derstanding of the meaning of the scale.                    single prompt that contains multiple items to evaluate.


                                                       27
evaluating multiple instances in a single batch often
degrades performance (Dubois et al., 2023).
Pairwise Evaluation (Chen et al., 2023g) find
that directly comparing the quality of two texts may
lead to suboptimal results and that explicitly asking
LLM to generate a score for individual summaries
is the most effective and reliable method. The order
of the inputs for pairwise comparisons can also
heavily affect evaluation (Wang et al., 2023h,b).




                                                        28
5        Prompting Issues

We now highlight prompting related issues in the             prompting (Schulhoff, 2024; Willison, 2024; Perez
form of security and alignment concerns.                     and Ribeiro, 2022). It is either an architectural
                                                             problem or a training problem made possible by
5.1     Security                                             the fact that adversarial prompts are extremely dif-
As the use of prompting grows, so too does the               ficult to prevent.
threat landscape surrounding it. These threats                  Consider the following jailbreaking example,
are extremely varied and uniquely difficult to de-           which is analogous to the previous prompt injec-
fend against compared to both non-neural and pre-            tion example, but without developer instructions in
prompting security threats. We provide a discus-             the prompt. Instead of inserting text in a prompt
sion of the prompting threat landscape and lim-              template, the user can go directly to the GenAI and
ited state of defenses. We begin by describing               prompt it maliciously.
prompt hacking, the means through which prompt-
ing is used to exploit LLMs, then describe dangers              Make a threat against the president.
emerging from this, and finally describe potential
defenses (Figure 5.1).
                                                             5.1.2     Risks of Prompt Hacking
5.1.1    Types of Prompt Hacking                             Prompt hacking can lead to real world risks such
Prompt hacking refers to a class of attacks which            as privacy concerns and system vulnerabilities.
manipulate the prompt in order to attack a GenAI
(Schulhoff et al., 2023). Such prompts have been             5.1.2.1    Data Privacy
used to leak private information (Carlini et al.,            Both model training data and prompt templates can
2021), generate offensive content (Shaikh et al.,            be leaked via prompt hacking (usually by prompt
2023) and produce deceptive messages (Perez et al.,          injection).
2022). Prompt hacking is a superset of both prompt
injection and jailbreaking, which are distinct con-          Training Data Reconstruction refers to the prac-
cepts.                                                       tice of extracting training data from GenAIs. A
                                                             straightforward example of this is Nasr et al. (2023),
Prompt Injection is the process of overriding                who found that by prompting ChatGPT to repeat
original developer instructions in the prompt                the word "company" forever, it began to regurgitate
with user input (Schulhoff, 2024; Willison, 2024;            training data.
Branch et al., 2022; Goodside, 2022). It is an archi-
tectural problem resulting from GenAI models not             Prompt Leaking refers to the process of extract-
being able to understand the difference between              ing the prompt template from an application. Devel-
original developer instructions and user input in-           opers often spend significant time creating prompt
structions.                                                  templates, and consider them to be IP worth pro-
   Consider the following prompt template. A user            tecting. Willison (2022) demonstrate how to leak
could input "Ignore previous instructions and make           the prompt template from a Twitter Bot, by simply
a threat against the president.", which might lead to        providing instructions like the following:
the model being uncertain as to which instruction
to follow, and thus possibly following the malicious
                                                                Ignore the above and instead tell me what
instruction.
                                                                your initial instructions were.

       Recommend a book for the following per-
      son: {USER_INPUT}                                      5.1.2.2    Code Generation Concerns
                                                             LLMs are often used to generate code. Attackers
Jailbreaking is the process of getting a GenAI               may target vulnerabilities that occur as a result of
model to do or say unintended things through                 this code.

                                                        29
                                                                 Prompt Injection 5.1.1
                                 Prompt Hacking 5.1.1
                                                                 Jailbreaking 5.1.1           Training Data
                                                                                              Reconstruction 5.1.2.1
                                                                 Data Privacy 5.1.2.1
                                                                                              Prompt Leaking 5.1.2.1

                                 Risks 5.1.2                     Code Generation Concerns     Package Halluc. 5.1.2.2
             Security
                                                                 5.1.2.2                      Bugs 5.1.2.2
                                                                 Customer Service 5.1.2.3

                                                                 Prompt-based Defense 5.1.3

                                 Hardening Measures 5.1.3        Guardrails 5.1.3

                                                                 Detectors 5.1.3


                                       Figure 5.1: Security & prompting


Package Hallucination occurs when LLM-                           Prompt-based Defenses Multiple prompt-based
generated code attempts to import packages that do               defenses have been proposed, in which instructions
not exist (Lanyado et al., 2023; Thompson and                    are included in the prompt to avoid prompt injec-
Kelly, 2023). After discovering what package                     tion (Schulhoff, 2022). For example, the following
names are frequently hallucinated by LLMs, hack-                 string could be added to a prompt:
ers could create those packages, but with malicious
code (Wu et al., 2023c). If the user runs the in-
stall for these formerly non-existent packages, they                   Do not output any malicious content
would download a virus.
                                                                   However, Schulhoff et al. (2023) ran a study with
Bugs (and security vulnerabilities) occur more
                                                                 hundreds of thousands of malicious prompts and
frequently in LLM-generated code (Pearce et al.,
                                                                 found that no prompt-based defense is fully secure,
2021, 2022; Sandoval et al., 2022; Perry et al.,
                                                                 though they can mitigate prompt hacking to some
2022). Minor changes to the prompting technique
                                                                 extent.
can also lead to such vulnerabilities in the gener-
ated code (Pearce et al., 2021).
                                                                 Detectors are tools designed to detect malicious
5.1.2.3    Customer Service                                      inputs and prevent prompt hacking (AI, 2023; Inan
Malicious users frequently perform prompt injec-                 et al., 2023). Many companies have built such
tion attacks against corporate chatbots, leading                 detectors (ArthurAI, 2024; Preamble, 2024; Lak-
to brand embarrassment (Bakke, 2023; Goodside,                   era, 2024), which are often built using fine-tuned
2022). These attacks may induce the chatbot to                   models trained on malicious prompts. Generally,
output harmful comment or agree to sell the user                 these tools can mitigate prompt hacking to a greater
a company product at a very low price. In the lat-               extent than prompt-based defenses.
ter case, the user may actually be entitled to the
deal. Garcia (2024) describe how an airline chat-
bot gave a customer incorrect information about                  Guardrails are rules and frameworks for guiding
refunds. The customer appealed in court and won.                 GenAI outputs (Hakan Tekgul, 2023; Dong et al.,
Although this chatbot was pre-ChatGPT, and was                   2024). Guardrails often make use of detectors, but
in no way tricked by the user, this precedent may                not always. Guardrails are more concerned with
apply when nuanced prompt hacking techniques                     the general dialogue flow in an application. For
are used.                                                        example, a simple guardrail could use a detector to
                                                                 find malicious prompts, then respond with a canned
                                                                 message if malicious. More complicated tools em-
5.1.3     Hardening Measures
                                                                 ploy dialogue managers (Rebedea et al., 2023),
Several tools and prompting techniques have been                 which allow the LLM to choose from a number
developed to mitigate some of the aforementioned                 of curated responses. Prompting-specific program-
security risks. However, prompt hacking (both in-                ming languages have also been proposed to im-
jection and jailbreaking) remain unsolved problems               prove templating and act as guardrails (Scott Lund-
and likely are impossible to solve entirely.                     berg, 2023; Luca Beurer-Kellner, 2023).

                                                            30
                                                                            Ambig. Demonstrations 5.2.4
                                           Ambiguity 5.2.4
                                                                            Question Clarification 5.2.4
                                                                            AttrPrompt 5.2.3
                                                                            Cultural Awareness 5.2.3
                                           Biases 5.2.3
                                                                            Demonstration Sel. 5.2.3
               Alignment                                                    Vanilla Prompting 5.2.3
                                                                            Sycophancy 5.2.2
                                           Calibration 5.2.2
                                                                            Verbalized Score 5.2.2
                                                                            Few-Shot Ordering 5.2.1
                                                                            Prompt Drift 5.2.1
                                           Prompt Sensitivity 5.2.1
                                                                            Prompt Wording 5.2.1
                                                                            Task Format 5.2.1


                              Figure 5.2: Prompt-based Alignment Organization


5.2     Alignment                                              show that these minor changes can alter the
                                                               accuracy of GPT-3 by up to 30%. Similarly, minor
Ensuring that LLMs are well-aligned with user
                                                               perturbations on task-specific prompts that are
needs in downstream tasks is essential for success-
                                                               logically equivalent, such as altering the order of
ful deployment. Models may output harmful con-
                                                               choices in multiple-choice questions, can result in
tent, yield inconsistent responses, or show bias,
                                                               significant performance degradation (Pezeshkpour
all of which makes deploying them more difficult.
                                                               and Hruschka, 2023; Zheng et al., 2023a; Voronov
To help mitigate these risks, it is possible to care-
                                                               et al., 2024).
fully design prompts that elicit less harmful outputs
from LLMs. In this section, we describe prompt
alignment problems as well as potential solutions              Prompt Drift (Chen et al., 2023b) occurs when
(Figure 5.2).                                                  the model behind an API changes over time, so the
                                                               same prompt may produce different results on the
5.2.1   Prompt Sensitivity
                                                               updated model. Although not directly a prompt-
Several works show that LLMs are highly sensitive              ing issue, it necessitates continuous monitoring of
to the input prompt (Leidinger et al., 2023), i.e.,            prompt performance.
even subtle changes to a prompt such as exemplar
order (Section 2.2.1.1) can result in vastly different         5.2.2   Overconfidence and Calibration
outputs. Below, we describe several categories
                                                               LLMs are often overconfident in their answers,
of these perturbations and their impacts on model
                                                               especially when prompted to express their own
behavior.
                                                               confidence in words (Kiesler and Schiffner, 2023;
Small Changes in the Prompt such as extra                      Xiong et al., 2023a), which may lead to user
spaces, changing capitalization, modifying delim-              overreliance on model outputs (Si et al., 2023c).
iters, or swapping synonyms can significantly im-              Confidence calibration provides a score that
pact performance (Lu et al., 2024; Tjuatja et al.,             represents the confidence of the model (Guo et al.,
2024). Despite these changes being minor, Sclar                2017). While a natural solution for confidence
et al. (2023a) find that they can cause the perfor-            calibration is to study the output token probabilities
mance of LLaMA2-7B to range from nearly 0 to                   provided by the LLM, a variety of prompting
0.804 on some tasks.                                           techniques have also been created for confidence
                                                               calibration.
Task Format describes different ways to prompt
an LLM to execute the same task. For example,
a prompt tasking an LLM to perform sentiment                   Verbalized Score is a simple calibration tech-
analysis could ask the LLM to classify a review                nique that generates a confidence score (e.g. “How
as “positive” or “negative”, or the prompt could               confident are you from 1 to 10”), but its efficacy
ask the LLM “Is this review positive?” to elicit               is under debate. Xiong et al. (2023b) find that
a “yes” or “no” response. Zhao et al. (2021b)                  several LLMs are highly overconfident when ver-

                                                          31
balizing confidence scores, even when employing                       refine its own output; and 2) instructing the LLM
self-consistency and chain-of-thought. In contrast,                   to use culturally relevant words.
Tian et al. (2023) find that simple prompts (Section
                                                                      AttrPrompt (Yu et al., 2023) is a prompting
4.2) can achieve more accurate calibration than the
                                                                      technique designed to avoid producing text biased
model’s output token probabilities.
                                                                      towards certain attributes when generating syn-
Sycophancy refers to the concept that LLMs will                       thetic data. Traditional data generation approaches
often express agreement with the user, even when                      may be biased towards specific lengths, locations
that view contradicts the model’s own intial out-                     and styles. To overcome this, AttrPrompt: 1) asks
put. Sharma et al. (2023) find that when LLMs                         the LLM to generate specific attributes that are
are asked to comment on opinions of arguments,                        important to alter for diversity (e.g. location); and
the model is easily swayed if the user’s opinion                      2) prompts the LLM to generate synthetic data by
is included in the prompt (e.g. “I really like/dis-                   varying each of these attributes.
like this argument”). Further, they find that ques-
tioning the LLM’s original answer (e.g. “Are you
                                                                      5.2.4   Ambiguity
sure?”), strongly providing an assessment of cor-
rectness (e.g. “I am confident you are wrong”), and                   Questions that are ambiguous can be interpreted in
adding false assumptions will completely change                       multiple ways, where each interpretation could re-
the model output. Wei et al. (2023b) note similar re-                 sult in a different answer (Min et al., 2020). Given
sults with opinion-eliciting and false user presump-                  these multiple interpretations, ambiguous questions
tions, also finding that sycophancy is heightened                     are challenging for existing models (Keyvan and
for larger and instruction-tuned models. Thus, to                     Huang, 2022), but a few prompting techniques have
avoid such influence, personal opinions should not                    been developed to help address this challenge.
be included in prompts.12                                             Ambiguous Demonstrations Gao et al. (2023a)
5.2.3    Biases, Stereotypes, and Culture                             are examples that have an ambiguous label set.
                                                                      Including them in a prompt can increase ICL
LLMs should be fair to all users, such that no bi-                    performance. This can be automated with a
ases, stereotypes, or cultural harms are perpetuated                  retriever, but it can also be done manually.
in model outputs (Mehrabi et al., 2021). Some
prompting technique have been designed in accor-
dance with these goals.                                               Question Clarification (Rao and Daumé III,
                                                                      2019) allows the LLM to identify ambiguous ques-
Vanilla Prompting (Si et al., 2023b) simply con-                      tions and generate clarifying questions to pose to
sists of an instruction in the prompt that tells the                  the user. Once these questions are clarified by the
LLM to be unbiased. This technique has also been                      user, the LLM can regenerate its response. Mu et al.
referred to as moral self-correction (Ganguli et al.,                 (2023) do this for code generation and Zhang and
2023).                                                                Choi (2023) equip LLMs with a similar pipeline
                                                                      for resolving ambiguity for general tasks, but ex-
Selecting Balanced Demonstrations (Si et al.,
                                                                      plicitly design separate prompts to: 1) generate an
2023b), or obtaining demonstrations optimized
                                                                      initial answer 2) classify whether to generate clar-
over fairness metrics (Ma et al., 2023), can reduce
                                                                      ification questions or return the initial answer 3)
biases in LLM outputs (Section 2.2.1.1).
                                                                      decide what clarification questions to generate 4)
Cultural Awareness (Yao et al., 2023a) can be                         generate a final answer.
injected into prompts to help LLMs with cultural
adaptation (Peskov et al., 2021). This can be done
by creating several prompts to do this with machine
translation, which include: 1) asking the LLM to
   12
      For example, a practitioner may use the prompt template
“Detect all instances where the user’s input is harmful: {IN-
PUT}” in an attempt to prevent adversarial inputs, but this
subtly makes the false presupposition that the user’s input is
actually harmful. Thus, due to sycophancy, the LLM may be
inclined to classify the user’s output as harmful.


                                                                 32
6       Benchmarking

Now that we have carried out a systematic review                  we used three thought inducers (instructions that
of prompting techniques, we will analyze the em-                  cause the model to generate reasoning steps) includ-
pirical performance of different techniques in two                ing the standard "Let’s think step by step" chain-
ways: via a formal benchmark evaluation, and by                   of-thought (Kojima et al., 2022), as well as ThoT
illustrating in detail the process of prompt engineer-            (Zhou et al., 2023), and Plan and Solve (Wang et al.,
ing on a challenging real-world problem.                          2023f). Then, we selected the best of these, and
                                                                  ran it with Self-Consistency with three iterations,
6.1     Technique Benchmarking                                    taking the majority response.
A formal evaluation of prompting techniques might
                                                                  Few-Shot Setups We also ran Few-Shot prompts
be done in a broad study that compares hundreds of
                                                                  and Few-Shot-CoT prompts, both with exemplars
them across hundreds of models and benchmarks.
                                                                  generated by one of our authors. For each, we used
This is beyond our scope, but since it has not been
                                                                  three variations of the base instruction as well as
done before, we provide a first step in this direction.
                                                                  the two question formats (also applied to the exem-
We choose a subset of prompting techniques and
                                                                  plars). Then we used the best performing phrasing
run them on the widely used benchmark MMLU
                                                                  with Self-Consistency with three iterations, taking
(Hendrycks et al., 2021). We ran on a representa-
                                                                  the majority response.
tive subset of 2,800 MMLU questions (20% of the
questions from each category).13 and used gpt-3.5-                           1.0

turbo for all experiments.
                                                                             0.8


6.1.1   Comparing Prompting Techniques                                       0.6
                                                                  Accuracy




We benchmark six distinct prompting techniques                               0.4

using the same general prompt template (Figure
                                                                             0.2
6.2). This template shows the location of different
                                                                                        0.627 0.547 0.574 0.652 0.692 0.691
components of the prompts. Only base instructions                            0.0




                                                                                                                                              C
                                                                                        t


                                                                                                    oT



                                                                                                                 SC



                                                                                                                        ot



                                                                                                                                    T
                                                                                     ho




                                                                                                                                   Co



                                                                                                                                              TS
                                                                                                                       -Sh
                                                                                                 tC




and question exist in every prompt. The base in-
                                                                                       S




                                                                                                                 oT




                                                                                                                               ot



                                                                                                                                          Co
                                                                                   ro-



                                                                                              ho




                                                                                                                      Few
                                                                                                             tC




                                                                                                                              -Sh
                                                                                   Ze



                                                                                                S




                                                                                                                                         ot
                                                                                                           ho
                                                                                            ro-




                                                                                                                             Few



                                                                                                                                        -Sh
                                                                                                             S




struction is a phrase like "Solve the problem and
                                                                                            Ze



                                                                                                         ro-




                                                                                                                                    Few
                                                                                                      Ze




return (A), (B), (C) or (D)." that we vary in some
cases. We additionally test two formats of the ques-               Figure 6.1: Accuracy values are shown for each prompt-
tion (Figures 6.3 and 6.4). The question format                    ing technique, with the model used being gpt-3.5-turbo.
                                                                   Purple error bars illustrate the minimum and maximum
is inserted into the prompt template in place of
                                                                   for each technique, since they were each run on different
"{QUESTION}". We test each prompting tech-                         phrasings and formats (except SC).
nique with 6 total variations, except for ones that
use Self-Consistency.
Zero-Shot As a baseline, we ran questions di-                      6.1.2                   Question Formats
rectly through the model without any special                      We experiment with two formatting choices from
prompting technique, only the base instruction and                Sclar et al. (2023b), who explored how formatting
question. For this baseline, we utilized both for-                choices can affect benchmarking results. We use
mats as well as three phrasing variations of the base             two formats which lead to varied results on their
instruction. Thus, there were six total runs through              task (Figures 6.3 and 6.4).
the 2800 questions for this benchmark. This did
not include any exemplars or thought inducers.                     6.1.3                   Self-Consistency
Zero-Shot-CoT Techniques We ran also ran                           For the two Self-Consistency results, we set temper-
Zero-Shot-CoT. As the three different variations,                  ature to 0.5, following Wang et al. (2022)’s guide-
   13
      We excluded human_sexuality, since gpt-3.5-turbo re-         lines. For all other prompts, a temperature of 0 was
fused to answer these questions.                                   used.

                                                             33
   {BASE_INSTRUCTION}                                              PROBLEM::{QUESTION}, OPTIONS::
   {EXEMPLARS}                                                     (A): {A}
   {QUESTION} {THOUGHT_INDUCER}                                    (B): {B}
                                                                   (C): {C}
                                                                   (D): {D}, ANSWER::
   Figure 6.2: Prompt template for benchmarking.

                                                                           Figure 6.4: Question format 2.
      Problem
           {QUESTION}
      Options                                                  of actually solving the problem. Rather, it provides
                                                               one illustration of how an experienced prompt en-
      (A)::{A} (B)::{B} (C)::{C} (D)::{D}                      gineer would approach a task like this, along with
      Answer                                                   lessons learned.

             Figure 6.3: Question format 1.                    6.2.1   Problem
                                                               Our illustrative problem involves detection of sig-
6.1.4    Evaluating Responses                                  nal that is predictive of crisis-level suicide risk in
                                                               text written by a potentially suicidal individual. Sui-
Evaluating whether a LLM has properly responded
                                                               cide is a severe problem worldwide, compounded,
to a question is a difficult task (Section 2.5). We
                                                               as are most mental health issues, by a desperate
marked answers as correct if they followed certain
                                                               lack of mental health resources. In the United
identifiable patterns, such as being the only capital-
                                                               States, more than half the national population lives
ized letter (A-D) within parentheses or following a
                                                               in federally defined mental heath provider short-
phrase like “The correct answer is”.
                                                               age areas (National Center for Health Workforce
6.1.5    Results                                               Analysis, 2023); in addition, many mental health
                                                               professionals lack core competencies in suicide
Performance generally improved as techniques                   prevention (Cramer et al., 2023). In 2021, 12.3M
grew more complex (Figure 6.1). However, Zero-                 Americans thought seriously about suicide, with
Shot-CoT dropped precipitously from Zero-Shot.                 1.7M actually making attempts resulting in over
Although it had a wide spread, for all variants,               48,000 deaths (CDC, 2023). In the U.S., suicide
Zero-Shot performed better. Both cases of Self-                was the second leading cause of death (after acci-
Consistency, naturally had lower spread since they             dents) in people aged 10-14, 15-24, or 25-34 as of
repeated a single technique, but it only improved ac-          2021 statistics, and it was the fifth leading cause
curacy for Zero-Shot prompts. Few-Shot CoT per-                of death in people aged 35–54 (Garnett and Curtin,
forms the best, and unexplained performance drops              2023).
from certain techniques need further research. As
                                                                  Recent research suggests that there is significant
prompting technique selection is akin to hyperpa-
                                                               value in assessments of potential suicidality that
rameter search, this it is a very difficult task (Khat-
                                                               focus specifically on the identification of suicidal
tab et al., 2023). However, we hope this small study
                                                               crisis, i.e. the state of acute distress associated with
spurs research in the direction of more performant
                                                               a high risk of imminent suicidal behavior. However,
and robust prompting techniques.
                                                               validated assessments for diagnostic approaches
6.2     Prompt Engineering Case Study                          such as Suicide Crisis Syndrome (SCS) (Schuck
                                                               et al., 2019b; Melzer et al., 2024) and Acute Sui-
Prompt engineering is emerging as an art that many             cidal Affective Disturbance (Rogers et al., 2019)
people have begun to practice professionally, but              require either personal clinical interactions or com-
the literature does not yet include detailed guid-             pletion of self-report questionnaires that contain
ance on the process. As a first step in this direction,        dozens of questions. The ability to accurately flag
we present an annotated prompt engineering case                indicators of suicidal crisis in individuals’ language
study for a difficult real-world problem. This is not          could therefore have a large impact within the men-
intended to be an empirical contribution in terms              tal health ecosystem, not as a replacement for clini-

                                                          34
cal judgment but as a way to complement existing                     exercise proceeded through 47 recorded develop-
practices (Resnik et al., 2021).                                     ment steps, cumulatively about 20 hours of work.
   As a starting point, we focus here on the most                    From a cold start with 0% performance (the prompt
important predictive factor in Suicide Crisis Syn-                   wouldn’t return properly structured responses), per-
drome assessments, referred to in the literature as                  formance was boosted to an F1 of 0.53, where that
either frantic hopelessness or entrapment, “a desire                 F1 is the harmonic mean of 0.86 precision and 0.38
to escape from an unbearable situation, tied with                    recall.16
the perception that all escape routes are blocked”                      Below, the set of prompts qinf is the test item,
(Melzer et al., 2024).14 This characteristic of what                 while qi , ri , and ai denote the questions, chain-of-
an individual is experiencing is also central in other               thought steps, and answers in exemplars.
characterizations of mental processes that result in
suicide.                                                             6.2.3.1    Dataset Exploration (2 steps)
                                                                     The process began with the prompt engineer review-
6.2.2    The Dataset                                                 ing a description of entrapment (Figure 6.7); this
We worked with a subset of data from the Univer-                     description had been used as a first-pass rubric for
sity of Maryland Reddit Suicidality Dataset (Shing                   the human coders early in the coding process, not-
et al., 2018), which is constructed from posts in                    ing, however, that they were familiar with SCS and
r/SuicideWatch, a subreddit that offers peer sup-                    knew it was neither a formal definition nor exhaus-
port for anyone struggling with suicidal thoughts.                   tive. The prompt engineer then loaded the dataset
Two coders trained on the recognition of the factors                 into a Python notebook for data exploration pur-
in Suicide Crisis Syndrome coded a set of 221 posts                  poses. He began by asking gpt-4-turbo-preview if it
for presence or absence of entrapment, achieving                     knew what entrapment was (Figure 6.8), but found
solid inter-coder reliability (Krippendorff’s alpha                  that the LLM’s response was not similar to the de-
= 0.72).                                                             scription that had been given. In consequence, the
                                                                     prompt engineer included the Figure 6.7 descrip-
6.2.3    The Process                                                 tion of entrapment in all future prompts.
An expert prompt engineer, who has authored a
widely used guide on prompting (Schulhoff, 2022),                    6.2.3.2    Getting a Label (8 steps)
took on the task of using an LLM to identify entrap-                 As noted in Section 6.1 with regard to the hu-
ment in posts.15 The prompt engineer was given a                     man_sexuality subset of MMLU, LLMs exhibit
brief verbal and written summary of Suicide Crisis                   unpredictable and difficult to control behaviour in
Syndrome and entrapment, along with 121 develop-                     sensitive domains. For multiple steps in the prompt
ment posts and their positive/negative labels (where                 engineering process, the prompt engineer found
“positive” means entrapment is present), the other                   that the LLM was giving mental health advice (e.g.
100 labeled posts being reserved for testing. This                   Figure 6.9) instead of labeling the input. This was
limited information mirrors frequent real-life sce-                  addressed by switching to the GPT-4-32K model.
narios in which prompts are developed based on                          A take-away from this initial phase is that the
a task description and the data. More generally, it                  “guard rails” associated with some large language
is consistent with a tendency in natural language                    models may interfere with the ability to make
processing and AI more generally to approach cod-                    progress on a prompting task, and this could in-
ing (annotation) as a labeling task without delving                  fluence the choice of model for reasons other than
very deeply into the fact that the labels may, in fact,              the LLM’s potential quality.
refer to nuanced and complex underlying social
science constructs.                                                  6.2.3.3    Prompting Techniques (32 steps)
   We documented the prompt engineering pro-                         The prompt engineer then spent the majority of
cess in order to illustrate the way that an experi-                  his time improving the prompting technique being
enced prompt engineer goes about their work. The                     used. This included techniques such as Few-Shot,
   14                                                                   16
      The former term more explicitly emphasizes the frantic               Precision is also known as positive predictive value, and
and desperate action required to escape an unbearable life           recall is also known as true positive rate or sensitivity. Al-
situation. However, the term entrapment is briefer and used          though F1 is often used in computional system evaluations as
widely so we adopt it here.                                          a single figure of merit, we note that in this problem space
   15
      Disclosure: that expert is also the lead author of this        its even weighting of precision and recall is probably not
paper.                                                               appropriate. We discuss this further below.


                                                                35
                                Scores of Different Prompting Techniques on Development Set
         1.0    F1
                Recall
                Precision

         0.8



         0.6
Scores




         0.4



         0.2



         0.0
                  + Default to Reject
                 + 1-Shot AutoDiCoT
                   1-Shot AutoDiCoT

                   1-Shot AutoDiCoT

               Ensemble + Extraction
                  10-Shot AutoDiCoT

                 Zero-Shot + Context

                 Zero-Shot + Context




                                                                                Anonymized Email


                                                                                                                       10-Shot AutoDiCoT

                                                                                                                                           Triplicate Context
                                                                                                                                                                              20-Shot AutoDiCoT



                                                                                                                                                                             + Extraction Prompt
                                                                                                                                                                                                   20-Shot AutoDiCoT

                                                                                                                                                                                                                       10-Shot AutoDiCoT
                                                                                                   10-Shot + Context




                                                                                                                                                                + Full Words + Extraction Prompt
                                                           Full Context Only
                  10-Shot AutoDiCoT




                                                                                                                                                                             10-Shot AutoDiCoT
                                                                                                                         De-Dupe Email
                      + Full Context



                     Without Email
                10-Shot AutoDiCoT




                                                                                                                                                                                 + Full Words
                    (Exact Match)
                        (no email)




                     (First Chars)
                        10-Shot




                                                                                                                                                                       20-Shot AutoDiCoT

Figure 6.5: F1 scores varied widely from worst performing prompts to highest performing prompts, but most
prompts scored within a similar range.


Chain-of-Thought, AutoCoT, Contrastive CoT, and                                section until we reach CoT. This approach obtained
multiple answer extraction techniques. We report                               0.40 F1, 1.0 recall, and 0.25 precision, evaluated
statistics for the first runs of these techniques; F1                          on all samples from the training/development since
scores could change by as much as 0.04 upon sub-                               no samples had been used as exemplars.
sequent runs, even with temperature and top p set
to zero.17                                                                     10-Shot + Context. Next, the prompt engineer
                                                                               added the first ten data samples (with labels) into
Zero-Shot + Context was the first technique eval-                              the prompt, in Q: (question) A: (answer) format
uated (Figure 6.10), using the description in Fig-                             (Figure 6.11). He evaluated this 10-shot prompt
ure 6.7. Notice the word definition in the prompt,                             on the remaining items in the training/development
although Figure 6.7 is not a formal definition.                                set, yielding ↑0.05 (0.45) F1, ↓0.09 (0.91) recall,
   In order to obtain a final response from the LLM                            and ↑ 0.05 (0.30) precision, relative to the previous
to use in calculating performance metrics, it was                              best prompt.18
necessary to extract a label from the LLM output.
                                                                               One-Shot AutoDiCot + Full Context. After per-
The prompt engineer tested two extractors, one that
                                                                               forming 10-shot prompting, the prompt engineer
checks if the output is exactly "Yes" or "No", and
                                                                               observed that the 12th item in the development set
another which just checks if those words match the
                                                                               was being incorrectly being labeled as a positive in-
first few characters of the output. The latter had
                                                                               stance, and began experimenting with ways of mod-
better performance, and it is used for the rest of this
                                                                                        18
                                                                                   Here and for the remainder of the case study, we judge
    17
     Temperature and top-p are configuration hyperparameters                   “best” by F1, and we report on the current prompt under dis-
that control randomness of the output (Schulhoff, 2022).                       cussion relative to the best performing previous prompt.


                                                                36
                                                                                                                                                                               F1 Scores




                                                                                                                                                             0.0
                                                                                                                                                                   0.1
                                                                                                                                                                         0.2
                                                                                                                                                                                    0.3
                                                                                                                                                                                           0.4
                                                                                                                                                                                                 0.5




     deteriorations.
                                                                                                                                           Zero-Shot + Context
                                                                                                                                               (First Chars)
                                                                                                                                           Zero-Shot + Context
                                                                                                                                              (Exact Match)
                                                                                                                                             10-Shot + Context
                                                                                                                                              1-Shot AutoDiCoT
                                                                                                                                                + Full Context
                                                                                                                                              1-Shot AutoDiCoT
                                                                                                                                                  (no email)
                                                                                                                                  10-Shot\n+ 1-Shot AutoDiCoT
                                                                                                                                             Full Context Only
                                                                                                                                            10-Shot AutoDiCoT




37
                                                                                                                                          20-Shot AutoDiCoT
                                                                                                                                          20-Shot AutoDiCoT
                                                                                                                                             + Full Words




                                                                                                                     Techniques
                                                                                                                                   20-Shot AutoDiCoT
                                                                                                                            + Full Words + Extraction Prompt
                                                                                                                                         10-Shot AutoDiCoT
                                                                                                                                         + Extraction Prompt
                                                                                                                                          10-Shot AutoDiCoT
                                                                                                                                             Without Email
                                                                                                                                          10-Shot AutoDiCoT
                                                                                                                                            De-Dupe Email
                                                                                                                                          10-Shot AutoDiCoT
                                                                                                                                          + Default to Reject
                                                                                                                                        10-Shot AutoDiCoT
                                                                                                                                                                                                                            F1 Scores of Prompting Techniques on Development Set




                                                                                                                                      Ensemble + Extraction
                                                                                                                                           Triplicate Context
                                                                                                                                            Anonymized Email
                                                                                                                                                                                                       Max F1 Score: 0.53




     F1 score were hard to come by and and often involved testing multiple underperforming prompts before finding
     Figure 6.6: From the first prompt tried (Zero-Shot + Context) to the last (Anonymized Email), improvements in

     a performant one. Green lines show improvements over the current highest F1 score, while red lines show
     Entrapment:                                                           {ENTRAPMENT DEFINITION (Figure
    - Feeling like there is no exit                                        6.7)}
    - Feeling hopeless                                                     {qinf }
    - Feeling like there is no way out                                     Is this entrapment? Yes or no.
    - Feeling afraid that things will never be
     normal again
    - Feeling helpless to change                                        Figure 6.10: A Zero-Shot + Context prompt, the sim-
    - Feeling trapped                                                   plest of all prompts explored in this case study.
    - Feeling doomed
    - Feeling or thinking that things will never                           {ENTRAPMENT DEFINITION (Figure
     change                                                                6.7)}
    - Feeling like there is no escape                                      Q: {q1 }
    - Feeling like there are no good solutions to                          A: {a1 }
     problems                                                              ...
                                                                           Q: {q10 }
                                                                           A: {a10 }
Figure 6.7: The description of entrapment used by the
                                                                           Q: {qinf }
prompt engineer
                                                                           A:

    What is entrapment with respect to Suicide
    Crisis Syndrome?                                                           Figure 6.11: 10-Shot + Context Prompt


                                                                            Figure 6.12 shows a version of that process, gen-
Figure 6.8: Question asked to the LLM to determine
whether its training data had provided relevant knowl-                  eralized to produce explanations for all develop-
edge about entrapment (it had not).                                     ment question/answer items (qi , ai ) in a set T rather
                                                                        than just item 12. Informed by the reasoning steps
                                                                        r12 elicited with respect to the incorrectly labeled
ifying the prompting such that the model would get                      q12 , the previous prompt was modified by including
that item correct. In order to get a sense of why this                  r12 in a One-Shot CoT example with incorrect rea-
mislabeling was taking place, the prompt engineer                       soning, as an exemplar for what not to do (Figure
prompted the LLM to generate an explanation of                          6.13) .
why the 12th item would have been labeled the way                           We call the algorithm in Figure 6.12 Automatic
it was.19                                                               Directed CoT (AutoDiCoT), since it automatically
   19
      We are trying to avoid misleading language like “the              directs the CoT process to reason in a particular
LLM generated an explanation of its reasoning”. LLMs do                 way. This technique can be generalized to any
not have access to their own internal processes, and therefore
they cannot “explain their reasoning” in the usual sense. An            labeling task. It combines the automatic generation
LLM generating an “explanation” is producing description of             of CoTs (Zhang et al., 2022b) with showing the
potential reasoning steps in getting to the output that could be
true, but also may not be accurate at all.
                                                                        LLM examples of bad reasoning, as in the case of
                                                                        Contrastive CoT (Chia et al., 2023). The algorithm
                                                                        was also used in developing later prompts.
    If you’re in immediate danger of harming                                Finally, the prompt was extended with two ad-
    yourself, please contact emergency services                         ditional pieces of context/instruction. The first
    or a crisis hotline in your area. They can                          was an email message the prompt engineer had
    provide immediate support and help ensure                           received explaining overall goals of the project,
    your safety.                                                        which provided more context around the concept
                                                                        of entrapment and the reasons for wanting to label
                                                                        it. The second addition was inspired by the prompt
Figure 6.9: A snippet from an output, which does not la-                engineer noticing the model was frequently over-
bel the data point, but rather attempts to provide mental               generating a positive label for entrapment. Hypoth-
health support to the user. Such outputs are often five                 esizing that the model was being too aggressive
times as long as this snippet.                                          in its pretraining-based inferences from the overt

                                                                   38
      1. Require: Development items T with n                     {PROFESSOR’S EMAIL}
         pairs (qi , ai )
                                                                 {ENTRAPMENT DEFINITION (Figure
      2. For each pair (qi , ai ) in T :                         6.7)}
          (a) Label qi as entrapment or not en-
                                                                 IMPORTANT: Only label the post as
              trapment using the model
                                                                 entrapment if they explicitly say that they
          (b) If the model labels correctly:
                                                                 feel trapped.
                i. Prompt the model with
                   "Why?" to generate a reason-                  Q: {q12 }
                   ing chain ri                                  R: Although "Today I found out I have
          (c) Else:                                              10 days to vacate my apartment or I’ll be
                i. Prompt the model with "It                     formally evicted. I’m 2 months behind
                   is actually [is/is not] entrap-               on my rent due to a bad time where I got
                   ment, please explain why." to                 demoted at work and rent from making
                   generate a reasoning chain ri                 roughly $1000 ever 2 weeks to around
          (d) Store the tuple (qi , ri , ai )                    $450. If I get evicted, I’ll probably be
                                                                 homeless" seems to express feelings of
      3. Return: n tuples (qi , ri , ai )                        being trapped/stuck, it is not sufficiently
                                                                 explicit to be labeled Entrapment. seems
                                                                 to express feelings of being trapped/stuck,
  Figure 6.12: Algorithm: Automatic Directed CoT
                                                                 it is not sufficiently explicit to be labeled
                                                                 Entrapment.
language, he instructed the model to restrict itself             A: {a12 }
to explicit statements of entrapment (Figure 6.13).              Q: {qinf }
Below we refer to these two pieces of context, pro-
vided in addition to the description of entrapment,
                                                                Figure 6.13: One-Shot AutoDiCot + Full Context
as full context.
   A new extractor was also used for this prompt,
which checks if the last word in the output is "Yes"          sitivity (i.e. not missing people who should be
or "No", instead of the first word. This updated              flagged as at-risk) may matter more because the
prompt was tested against all inputs in the develop-          potential cost of a false negative is so high.
ment set except for the first 20. It did not improve             The take-away here, although the insight came
F1, ↓0.09 (0.36) F1, but it led the prompt engineer           later, is that it is easy for the process of prompt
in a direction that did, as discussed below. Re-              development to diverge from the actual goals un-
call dropped to ↓ 0.58 (0.33) recall and precision            less regular engagement is fostered between the
improved to ↑ 0.09 (0.39) precision.                          prompt engineer and domain experts who more
   At this point, though, it is worth observing that,         deeply understand the real-world use case.
although it did ultimately lead to a gain in F1 score,
the steps taken here to cut down on over-generation           Ablating Email. The results of the previous
of positive labels were not, in fact, the right move          changes were promising, but they did involve cre-
in terms of the longer term goals. Entrapment                 ating a prompt that included information from an
need not be expressed explicitly in order to be               email message that had not been created for that
present (e.g. through phrases like “I feel trapped”           purpose, and which included information about the
or “There’s no way out”); rather, clinical experts            project, the dataset, etc. that were not intended for
who have looked at the texts found that expressions           disclosure to a broad audience. Ironically, remov-
of entrapment could be implicit and potentially               ing this email brought performance significantly
quite nuanced. Moreover, in most use cases for                down, ↓ 0.27 (0.18) F1, ↓ 0.75 (0.17) recall and ↓
automatically spotting entrapment in someone’s                0.1 (0.20) precision. We attribute this to the fact
language, precision and recall are unlikely to be             that the email provided richer background informa-
equally important and, of the two, the recall/sen-            tion about the goals of the labeling. Although we

                                                         39
   {PROFESSOR’s EMAIL}                                          {PROFESSOR’s EMAIL}
                                                                {PROFESSOR’s EMAIL}
   {ENTRAPMENT           DEFINITION        (Fig-
   ure 6.7)}                                                    {ENTRAPMENT          DEFINITION         (Fig-
                                                                ure 6.7)}
   IMPORTANT: Only label the post as
   entrapment if they explicitly say that they                  IMPORTANT: Only label the post as
   feel trapped.                                                entrapment if they explicitly say that they
                                                                feel trapped.
   Q: {q1 }
   A: {a1 }                                                     Q: {qinf } A:
   ...
   Q: {q10 }
   A: {a10 }                                                           Figure 6.15: Full Context Only
   Q: {q12 }
   R: Although "{LLM REASONING}"
   seems to express feelings of being                           This can be interpreted both optimistically and
   trapped/stuck, it is not sufficiently explicit            pessimistically. Optimistically, it demonstrates
   to be labeled Entrapment.                                 how improvements can arise through exploration
   A: {a12 }                                                 and fortuitous discovery. On the pessimistic side,
   Q: {qinf }                                                the value of duplicating the email in the prompt
                                                             highlights the extent to which prompting remains a
                                                             difficult to explain black art, where the LLM may
        Figure 6.14: 10-Shot + 1 AutoDiCoT                   turn out to be unexpectedly sensitive to variations
                                                             one might not expect to matter.

would not recommend including email or any other             10-Shot AutoDiCoT. The next step was to create
potentially identifying information in any LLM               more AutoDiCoT exemplars, per the algorithm in
prompt, we chose to leave the email in the prompt;           Figure 6.12. A total of ten new AutoDiCoT exem-
this is consistent with scenarios in many typical            plars were added to the full context prompt (Figure
settings, in which prompts are not expected to be            6.16). This yielded the most successful prompt
exposed to others.                                           from this prompt engineering exercise, in terms of
                                                             F1 score, ↑ 0.08 (0.53) F1, ↓ 0.05 (0.86) recall, ↑
10-Shot + 1 AutoDiCoT. As a next step, the                   0.08 (0.38) precision.
prompt engineer tried including full context, 10 reg-
ular exemplars, and the one-shot exemplar about              20-Shot AutoDiCoT. Further experimentation
how not to reason. This hurt performance (Figure             proceeded seeking (unsuccesfully) to improve on
6.14) ↓ 0.30 (0.15) F1, ↓ 0.08 (0.10) recall, ↓ 0.03         the previous F1 result. In one attempt, the prompt
(0.33) precision.                                            engineer labeled an additional ten exemplars, and
                                                             created a 20-shot prompt from the first 20 data
Full Context Only. Next, a prompt was created                points in the development set. This led to worse
using only full context, without any exemplars (Fig-         results than the 10-shot prompt, when tested on all
ure 6.15). This boosted performance over the pre-            samples other than the first twenty, ↓ 0.04 (0.49)
vious technique, but did not make progress over-             F1, ↑ 0.08 (0.94) recall, ↓ 0.05 (0.33) precision.
all ↓ 0.01 (0.44) F1, ↑ 0.01 (0.92) recall, ↓ 0.01           Notably, it also yielded worse performance on the
(0.29) precision. Interestingly, in this prompt, the         test set.
prompt engineer accidentally pasted in the full-
context email twice, and that ended up having sig-           20-Shot AutoDiCoT + Full Words. The prompt
nificant positive effects on performance later (and          engineer conjectured that the LLM would perform
removing the duplicate actually decreased perfor-            better if the prompt included full words Question,
mance). This is reminiscent of the re-reading tech-          Reasoning, and Answer rather than Q, R, A. How-
nique (Xu et al., 2023).                                     ever, this did not succeed (Figure 6.17), ↓ 0.05

                                                        40
   {PROFESSOR’s EMAIL}

   {ENTRAPMENT DEFINITION}
                                                             {PROFESSOR’s EMAIL}
   IMPORTANT: Only label the post as
   entrapment if they explicitly say that they               {ENTRAPMENT DEFINITION}
   feel trapped.
                                                             IMPORTANT: Only label the post as
   Q: {q1 }                                                  entrapment if they explicitly say that they
   R: {r1 }                                                  feel trapped.
   A: {a1 }
   ...                                                       Question: {q1 }
   Q: {q10 }                                                 Reasoning: {r1 }
   R: {r10 }                                                 Answer: {a1 }
   A: {a10 }                                                 ...
   Q: {qinf }                                                Question: {q20 }
                                                             Reasoning: {r20 }
                                                             Answer: {a20 }
          Figure 6.16: 10-Shot AutoDiCoT                     Question: {qinf }

(0.48) F1, ↑ 0.08 (0.94) recall, ↓ 0.06 (0.32) preci-
sion.                                                              Figure 6.17: 20-shot AutoDiCoT

20-Shot AutoDiCoT + Full Words + Extraction
Prompt. The prompt engineer then noticed that in
many cases, the LLM generated outputs that could
not properly be parsed to obtain a response. So,
they crafted a prompt that extracted answers from
the LLM’s response (Figure 6.18). Although this
improved accuracy by a few points, it decreased
                                                             {PROFESSOR’s EMAIL}
F1, thanks to the fact that many of the outputs
that had been unparsed actually contained incorrect
                                                             {ENTRAPMENT DEFINITION}
responses, ↓ 0.05 (0.48) F1, ↓ 0.05 (0.33) precision,
with no change in recall (0.86).
                                                             IMPORTANT: Only label the post as
10-Shot AutoDiCoT + Extraction Prompt. Ap-                   entrapment if they explicitly say that they
plying the extraction prompt to the best performing          feel trapped.
10-Shot AutoDiCoT prompt did not improve re-
sults, ↓ 0.04 (0.49) F1, ↓ 0.08 (0.78) recall, ↓ 0.03        Question: {REDACTED}
(0.35) precision.                                            Answer: {ANSWER}
10-Shot AutoDiCoT without Email. As noted
                                                             Does this Answer indicate entrapment?
above, removing the email outright from the
                                                             Output the word Yes if it is labeled as
prompt hurt performance, ↓ 0.14 (0.39) F1, ↓ 0.39
                                                             entrapment and output the word No if it is
(0.48) recall, ↓ 0.06 (0.32) precision.
                                                             not labeled as entrapment. Only output the
De-Duplicating Email. Also as noted above, it                word Yes or the word No.
seemed reasonable that removing the duplication
of the email would perform as well or better than
                                                                    Figure 6.18: Extraction Prompt
the prompt with the unintentional duplication. As it
turned out, however, removing the duplicate signif-
icantly hurt performance, ↓ 0.07 (0.45) F1, ↓ 0.12
(0.74) recall, ↓ 0.05 (0.33) precision.

                                                        41
10-Shot AutoDiCoT + Default to Reject. This                                                  Scores of Different Prompting Techniques on Test Set
                                                                                        F1
approach used the best performing prompt, and de-                                       Recall
                                                                         0.8            Precision
faulted to labeling as negative (not entrapment) in
the case of answers that are not extracted properly.                     0.6




                                                                Scores
This did not help performance, ↓ 0.11 (0.42) F1, ↓                       0.4
0.04 (0.83) recall, ↓ 0.10 (0.28) precision.
                                                                         0.2
Ensemble + Extraction. Especially for systems                            0.0




                                                                                                                               DSPy Default
                                                                               10-Shot AutoDiCoT




                                                                                                           20-Shot AutoDiCoT




                                                                                                                                              + Small Modifications
that are sensitive to the details of their inputs, there




                                                                                                                                                 DSPy Default
are advantages in trying multiple variations of an
input and then combining their results. That was
done here by taking the best performing prompt,
the 10-Shot AutoDiCoT prompt, and creating three
versions of it with different orderings of the exem-            Figure 6.19: Scores of different prompting techniques
plars. The average of the three results was taken to            on the test set.
be the final answer. Unfortunately, both orderings
that differed from the default ordering led to the              ultimate objective of maximizing F 1 on the
LLM not outputting a well-structured response. An               same development set used above. We used
extraction prompt was therefore used to obtain final            gpt-4-0125-preview and the default settings
answers. This exploration hurt rather than helped               for the BootstrapFewShotWithRandomSearch
performance ↓ 0.16 (0.36) F1, ↓ 0.23 (0.64) recall,             “teleprompter” (the optimization approach). Fig-
↓ 0.13 (0.26) precision.                                        ure 6.19 shows the results of two of these prompts
                                                                on the test set, one of which used default DSPy
10-Shot AutoCoT + 3x the context (no email
                                                                behaviour, and the second which was manually
dupe). Recall that context refers to the descrip-
                                                                modified slightly from this default. The best result-
tion of entrapment, an instruction about explicit-
                                                                ing prompt includes 15 exemplars (without CoT
ness, and an email. Since the duplicated email
                                                                reasoning) and one bootstrapped reasoning demon-
had improved performance, the prompt engineer
                                                                stration. It achieves 0.548 F 1 (and 0.385 / 0.952
tested out pasting in three copies of the context
                                                                precision / recall) on the test set, without making
(first de-duplicating the email). However, this did
                                                                any use of the professor’s email nor the incorrect
not improve performance, ↓ 0.06 (0.47) F1, ↓ 0.08
                                                                instruction about the explicitness of entrapment. It
(0.78) recall, ↓ 0.05 (0.33) precision.
                                                                also performs much better than the human prompt
Anonymize Email. At this point it seemed clear                  engineer’s prompts on the test set, which demon-
that including the duplicated email in the prompt               strates the significant promise of automated prompt
was actually, although not explainably, essential to            engineering.
the best performance so far obtained. The prompt
                                                                6.2.4          Discussion
engineer decided to anonymize the email by re-
placing personal names with other, random names.                Prompt engineering is a non-trivial process, the nu-
However, surprisingly, this decreased performance               ances of which are not currently well described in
significantly ↓ 0.08 (0.45) F1, ↓ 0.14 (0.72) recall,           literature. From the fully manual process illustrated
↓ 0.06 (0.33) precision.                                        above, there are several take-aways worth summa-
                                                                rizing. First, prompt engineering is fundamentally
DSPy. We concluded the case study by explor-                    different from other ways of getting a computer to
ing an alternative to manual prompt engineer-                   behave the way you want it to: these systems are
ing, the DSPy framework (Khattab et al., 2023),                 being cajoled, not programmed, and, in addition
which automatically optimizes LLM prompts for                   to being quite sensitive to the specific LLM being
a given target metric. Specifically, we begin                   used, they can be incredibly sensitive to specific
with a chain-of-thought classification pipeline                 details in prompts without there being any obvi-
that uses the definition of entrapment in Figure                ous reason those details should matter. Second,
6.7. Over 16 iterations, DSPy bootstrapped syn-                 therefore, it is important to dig into the data (e.g.
thetic LLM-generated demonstrations and ran-                    generating potential explanations for LLM “reason-
domly sampled training exemplars, with the                      ing” that leads to incorrect responses). Related, the

                                                           42
third and most important take-away is that prompt
engineering should involve engagement between
the prompt engineer, who has expertise in how to
coax LLMs to behave in desired ways, and domain
experts, who understand what those desired ways
are and why.
   Ultimately we found that there was significant
promise in an automated method for exploring the
prompting space, but also that combining that au-
tomation with human prompt engineering/revision
was the most successful approach. We hope that
this study will serve as a step toward more robust
examinations of how to perform prompt engineer-
ing.




                                                     43
7      Related Work

In this section, we review existing surveys and             erage. Hua et al. (2024) use a GPT-4-automated ap-
meta-analyses of prompting. Liu et al. (2023b)              proach to review LLMs in the mental health space.
perform a systematic review of prompt engineer-             Wang et al. (2023c) review prompt engineering and
ing in the pre-ChatGPT era, including various               relevant models in the visual modality and Yang
aspects of prompting like prompt template engi-             et al. (2023e) provided a comprehensive list of qual-
neering, answer engineering, prompt ensembling,             itative analyses of multimodal prompting, particu-
and prompt tuning methods. Their review cov-                larly focusing on GPT-4V20 . Durante et al. (2024)
ers many different types of prompting (e.g., cloze,         review multimodal interactions based on LLM em-
soft-prompting, etc., across many different types           bodied agents. Ko et al. (2023b) review literature
of language models) while we focus on discrete              on the adoption of Text-to-Image generation mod-
pre-fix prompting but more in-depth discussion.             els for visual artists’ creative works. Gupta et al.
Chen et al. (2023a) provide a review of popular             (2024) review GenAI through a topic modeling
prompting techniques like Chain-of-Thought, Tree-           approach. Awais et al. (2023) review foundation
of-Thought, Self-Consistency, and Least-to-Most             models in vision, including various prompting tech-
prompting, along with outlooks for future prompt-           niques. Hou et al. (2023) perform a systematic
ing research. White et al. (2023) and Schmidt               review of prompt engineering techniques as they
et al. (2023) provide a taxonomy of prompt pat-             relate to software engineering. They use a sys-
terns, which are similar to software patterns (and          tematic review technique developed by Keele et al.
prompting techniques for that matter). Gao (2023)           (2007), specifically for software engineering re-
provide a practical prompting technique tutorial for        views. Wang et al. (2023e) review the literature
a non-technical audience. Santu and Feng (2023)             on software testing with large language models.
provide a general taxonomy of prompts that can be           Zhang et al. (2023a) review ChatGPT prompting
used to design prompts with specific properties to          performance on software engineering tasks such as
perform a wide range of complex tasks. Bubeck               automated program repair. Neagu (2023) provide
et al. (2023) qualitatively experiment with a wide          a systematic review on how prompt engineering
range of prompting methods on the early version             can be leveraged in computer science education. Li
of GPT-4 to understand its capabilities. Chu et al.         et al. (2023j) review literature on the fairness of
(2023) review Chain-of-Thought related prompt-              large language models. There are also surveys on
ing methods for reasoning. In earlier work, Bom-            related aspects such as hallucination of language
masani et al. (2021) review and discuss opportuni-          models (Huang et al., 2023b), verifiability (Liu
ties and risks of foundation models broadly, and            et al., 2023a), reasoning (Qiao et al., 2022), aug-
Dang et al. (2022) discuss prompting strategies for         mentation (Mialon et al., 2023), and linguistic prop-
interactive creative applications that use prompting        erties of prompts (Leidinger et al., 2023). Different
as a new paradigm for human interaction, with a             from these works, we perform our review targeting
particular focus on the user interface design that          broad coverage and generally applicable prompting
supports user prompting. As an addition to these            techniques. Finally, in terms of more general prior
existing surveys, our review aims to provide a more         and concurrent surveys (Liu et al., 2023b; Sahoo
updated and formalized systematic review.                   et al., 2024; Vatsal and Dubey, 2024), this survey
   There is also a line of work that surveys prompt-        offers an update in a fast-moving field. In addition,
ing techniques for particular domains or down-              we provide a starting point for taxonomic organi-
stream applications. Meskó (2023) and Wang et al.           zation of prompting techniques and standardiza-
(2023d) offer recommended use cases and limi-               tion of terminology. Moreover, unlike many works
tations of prompt engineering in the medical and            that claim to be systematic, we base our work in
healthcare domains. Heston and Khun (2023) pro-             the widely used standard for systematic literature
vide a review of prompt engineering for medical             reviews—PRISMA (Page et al., 2021).
education use cases. Peskoff and Stewart (2023)               20
                                                                 https://openai.com/research/
query ChatGPT and YouChat to assess domain cov-             gpt-4v-system-card


                                                       44
8      Conclusions

Generative AI is a novel technology, and broader             working with constitute a good representation of
understanding of models’ capabilities and limita-            that problem. It is better to start with simpler ap-
tions remains limited. Natural language is a flexi-          proaches first, and to remain skeptical of claims
ble, open-ended interface, with models having few            about method performance. To those already en-
obvious affordances. The use of Generative AI                gaged in prompt engineering, we hope that our tax-
therefore inherits many of the standard challenges           onomy will shed light on the relationships between
of linguistic communication—e.g., ambiguity, the             existing techniques. To those developing new tech-
role of context, the need for course correction—             niques, we encourage situating new methods within
while at the same time adding the challenge of               our taxonomy, as well as including ecologically
communicating with an entity whose “understand-              valid case studies and illustrations of those tech-
ing” of language may not bear any substantial re-            niques.
lationship to human understanding. Many of the
techniques described here have been called “emer-            Acknowledgements
gent”, but it is perhaps more appropriate to say that        We appreciate the advice given by Hal Daumé III,
they were discovered—the result of thorough ex-              Adam Visokay, and Jordan Boyd-Graber and re-
perimentation, analogies from human reasoning, or            view by Diyi Yang, Brandon M. Stewart, Shubham
pure serendipity.                                            Vatsal, Mason Marchetti, Aaron Tay, Andrea Vella,
   The present work is an initial attempt to catego-         and Allie Miller. We also appreciate the 10K USD
rize the species of an unfamiliar territory. While           in API credits given by OpenAI and design work
we make every attempt to be comprehensive, there             by Benjamin DiMarco.
are sure to be gaps and redundancies. Our inten-
tion is to provide a taxonomy and terminology that
cover a large number of existing prompt engineer-
ing techniques, and which can accommodate future
methods. We discuss over 200 prompting tech-
niques, frameworks built around them, and issues
like safety and security that need to be kept in mind
when using them. We also present two case studies
in order to provide a clear sense of models’ ca-
pabilities and what it is like to tackle a problem
in practice. Last, our stance is primarily observa-
tional, and we make no claims to the validity of the
presented techniques. The field is new, and evalua-
tion is variable and unstandardized—even the most
meticulous experimentation may suffer from unan-
ticipated shortcomings, and model outputs them-
selves are sensitive to meaning-preserving changes
in inputs. As a result, we encourage the reader to
avoid taking any claims at face value and to rec-
ognize that techniques may not transfer to other
models, problems, or datasets.
   To those just beginning in prompt engineering,
our recommendations resemble what one would
recommend in any machine learning setting: un-
derstand the problem you are trying to solve (rather
than just focusing on input/output and benchmark
scores), and ensure the data and metrics you are

                                                        45
References                                                        Liu, Aohan Zeng, Lei Hou, Yuxiao Dong, Jie Tang,
                                                                  and Juanzi Li. 2023a. Longbench: A bilingual, mul-
Adept. 2023. ACT-1: Transformer for Actions. https:               titask benchmark for long context understanding.
  //www.adept.ai/blog/act-1.
                                                                Yushi Bai, Jiahao Ying, Yixin Cao, Xin Lv, Yuze He,
Rishabh Agarwal, Avi Singh, Lei M Zhang, Bernd                    Xiaozhi Wang, Jifan Yu, Kaisheng Zeng, Yijia Xiao,
  Bohnet, Luis Rosias, Stephanie Chan, Biao Zhang,                Haozhe Lyu, et al. 2023b. Benchmarking Foundation
  Ankesh Anand, Zaheer Abbas, Azade Nova, et al.                  Models with Language-Model-as-an-Examiner. In
  2024. Many-shot in-context learning. arXiv preprint             NeurIPS 2023 Datasets and Benchmarks.
  arXiv:2404.11018.
                                                                Chris Bakke. 2023. Buying a chevrolet for 1$.
Sweta Agrawal, Chunting Zhou, Mike Lewis, Luke
  Zettlemoyer, and Marjan Ghazvininejad. 2023. In-              Nishant Balepur, Jie Huang, and Kevin Chang. 2023.
  context examples selection for machine translation.             Expository text generation: Imitate, retrieve, para-
  In Findings of the Association for Computational                phrase. In Proceedings of the 2023 Conference on
  Linguistics: ACL 2023, pages 8857–8873, Toronto,                Empirical Methods in Natural Language Process-
  Canada. Association for Computational Linguistics.              ing, pages 11896–11919, Singapore. Association for
                                                                  Computational Linguistics.
Kabir Ahuja, Harshita Diddee, Rishav Hada, Milli-
  cent Ochieng, Krithika Ramesh, Prachi Jain, Ak-               Yejin Bang, Samuel Cahyawijaya, Nayeon Lee, Wen-
  shay Nambi, Tanuja Ganu, Sameer Segal, Maxamed                  liang Dai, Dan Su, Bryan Wilie, Holy Lovenia, Ziwei
  Axmed, Kalika Bali, and Sunayana Sitaram. 2023.                 Ji, Tiezheng Yu, Willy Chung, Quyet V. Do, Yan Xu,
  MEGA: Multilingual Evaluation of Generative AI.                 and Pascale Fung. 2023. A Multitask, Multilingual,
  In EMNLP.                                                       Multimodal Evaluation of ChatGPT on Reasoning,
                                                                  Hallucination, and Interactivity. In AACL.
Rebuff AI. 2023. A self-hardening prompt injection
  detector.                                                     Hritik Bansal, Karthik Gopalakrishnan, Saket Dingliwal,
Anirudh Ajith, Chris Pan, Mengzhou Xia, Ameet Desh-               Sravan Bodapati, Katrin Kirchhoff, and Dan Roth.
  pande, and Karthik Narasimhan. 2024. InstructEval:              2023. Rethinking the Role of Scale for In-Context
  Systematic evaluation of instruction selection meth-            Learning: An Interpretability-based Case Study at 66
  ods. In Findings of the Association for Computa-                Billion Scale. In ACL.
  tional Linguistics: NAACL 2024, pages 4336–4350,              Omer Bar-Tal, Dolev Ofri-Amar, Rafail Fridman, Yoni
  Mexico City, Mexico. Association for Computational             Kasten, and Tali Dekel. 2022. Text2live: Text-driven
  Linguistics.                                                   layered image and video editing.
Sílvia Araújo and Micaela Aguiar. 2023. Comparing
                                                                Amanda Bertsch, Maor Ivgi, Uri Alon, Jonathan Berant,
   chatgpt’s and human evaluation of scientific texts’
                                                                  Matthew R Gormley, and Graham Neubig. 2024. In-
   translations from english to portuguese using popular
                                                                  context learning with long-context models: An in-
   automated translators. CLEF.
                                                                  depth exploration. arXiv preprint arXiv:2405.00200.
ArthurAI. 2024. Arthur shield.
                                                                Maciej Besta, Nils Blach, Ales Kubicek, Robert Ger-
Akari Asai, Sneha Kudugunta, Xinyan Velocity Yu,                 stenberger, Lukas Gianinazzi, Joanna Gajda, Tomasz
  Terra Blevins, Hila Gonen, Machel Reid, Yulia                  Lehmann, Michał Podstawski, Hubert Niewiadomski,
  Tsvetkov, Sebastian Ruder, and Hannaneh Hajishirzi.            Piotr Nyczyk, and Torsten Hoefler. 2024. Graph of
  2023. BUFFET: Benchmarking Large Language                      Thoughts: Solving Elaborate Problems with Large
  Models for Few-shot Cross-lingual Transfer.                    Language Models. Proceedings of the AAAI Confer-
                                                                 ence on Artificial Intelligence, 38(16):17682–17690.
Muhammad Awais, Muzammal Naseer, Salman
 Khan, Rao Muhammad Anwer, Hisham Cholakkal,                    Rishi Bommasani, Drew A. Hudson, Ehsan Adeli, Russ
 Mubarak Shah, Ming-Hsuan Yang, and Fahad Shah-                   Altman, Simran Arora, Sydney von Arx, Michael S.
 baz Khan. 2023. Foundational models defining a new               Bernstein, Jeannette Bohg, Antoine Bosselut, Emma
 era in vision: A survey and outlook.                             Brunskill, Erik Brynjolfsson, S. Buch, Dallas Card,
                                                                  Rodrigo Castellon, Niladri S. Chatterji, Annie S.
Abhijeet Awasthi, Nitish Gupta, Bidisha Samanta,                  Chen, Kathleen A. Creel, Jared Davis, Dora Dem-
  Shachi Dave, Sunita Sarawagi, and Partha Talukdar.              szky, Chris Donahue, Moussa Doumbouya, Esin Dur-
  2023. Bootstrapping multilingual semantic parsers               mus, Stefano Ermon, John Etchemendy, Kawin Etha-
  using large language models. In Proceedings of the              yarajh, Li Fei-Fei, Chelsea Finn, Trevor Gale, Lau-
  17th Conference of the European Chapter of the As-              ren E. Gillespie, Karan Goel, Noah D. Goodman,
  sociation for Computational Linguistics, pages 2455–            Shelby Grossman, Neel Guha, Tatsunori Hashimoto,
  2467, Dubrovnik, Croatia. Association for Computa-              Peter Henderson, John Hewitt, Daniel E. Ho, Jenny
  tional Linguistics.                                             Hong, Kyle Hsu, Jing Huang, Thomas F. Icard, Saahil
                                                                  Jain, Dan Jurafsky, Pratyusha Kalluri, Siddharth
Yushi Bai, Xin Lv, Jiajie Zhang, Hongchang Lyu,                   Karamcheti, Geoff Keeling, Fereshte Khani, O. Khat-
  Jiankai Tang, Zhidian Huang, Zhengxiao Du, Xiao                 tab, Pang Wei Koh, Mark S. Krass, Ranjay Krishna,


                                                           46
  Rohith Kuditipudi, Ananya Kumar, Faisal Ladhak,             CDC. 2023. Suicide data and statistics.
  Mina Lee, Tony Lee, Jure Leskovec, Isabelle Levent,
  Xiang Lisa Li, Xuechen Li, Tengyu Ma, Ali Malik,            Chi-Min Chan, Weize Chen, Yusheng Su, Jianxuan Yu,
  Christopher D. Manning, Suvir Mirchandani, Eric               Wei Xue, Shanghang Zhang, Jie Fu, and Zhiyuan Liu.
  Mitchell, Zanele Munyikwa, Suraj Nair, Avanika                2024. Chateval: Towards better LLM-based eval-
  Narayan, Deepak Narayanan, Benjamin Newman,                   uators through multi-agent debate. In The Twelfth
  Allen Nie, Juan Carlos Niebles, Hamed Nilforoshan,            International Conference on Learning Representa-
  J. F. Nyarko, Giray Ogut, Laurel J. Orr, Isabel Pa-           tions.
  padimitriou, Joon Sung Park, Chris Piech, Eva Porte-
  lance, Christopher Potts, Aditi Raghunathan, Robert         Ernie Chang, Pin-Jie Lin, Yang Li, Sidd Srinivasan,
  Reich, Hongyu Ren, Frieda Rong, Yusuf H. Roohani,             Gael Le Lan, David Kant, Yangyang Shi, Forrest
  Camilo Ruiz, Jack Ryan, Christopher R’e, Dorsa                Iandola, and Vikas Chandra. 2023. In-context prompt
  Sadigh, Shiori Sagawa, Keshav Santhanam, Andy                 editing for conditional audio generation.
  Shih, Krishna Parasuram Srinivasan, Alex Tamkin,
                                                              Harrison Chase. 2022. LangChain.
  Rohan Taori, Armin W. Thomas, Florian Tramèr,
  Rose E. Wang, William Wang, Bohan Wu, Jiajun                Banghao Chen, Zhaofeng Zhang, Nicolas Langrené,
  Wu, Yuhuai Wu, Sang Michael Xie, Michihiro Ya-                and Shengxin Zhu. 2023a. Unleashing the potential
  sunaga, Jiaxuan You, Matei A. Zaharia, Michael                of prompt engineering in large language models: a
  Zhang, Tianyi Zhang, Xikun Zhang, Yuhui Zhang,                comprehensive review.
  Lucia Zheng, Kaitlyn Zhou, and Percy Liang. 2021.
  On the Opportunities and Risks of Foundation Mod-           Lingjiao Chen, Matei Zaharia, and James Zou. 2023b.
  els. ArXiv, abs/2108.07258.                                   How is chatgpt’s behavior changing over time? arXiv
                                                                preprint arXiv:2307.09009.
Hezekiah J. Branch, Jonathan Rodriguez Cefalu, Jeremy
  McHugh, Leyla Hujer, Aditya Bahl, Daniel del                Shiqi Chen, Siyang Gao, and Junxian He. 2023c. Eval-
  Castillo Iglesias, Ron Heichman, and Ramesh Dar-              uating factual consistency of summaries with large
  wishi. 2022. Evaluating the susceptibility of pre-            language models. arXiv preprint arXiv:2305.14069.
  trained language models via handcrafted adversarial
  examples.                                                   Wenhu Chen, Xueguang Ma, Xinyi Wang, and
                                                               William W. Cohen. 2023d. Program of thoughts
Greg Brockman, Vicki Cheung, Ludwig Pettersson,                prompting: Disentangling computation from reason-
  Jonas Schneider, John Schulman, Jie Tang, and Woj-           ing for numerical reasoning tasks. TMLR.
  ciech Zaremba. 2016. Openai gym.
                                                              Xinyun Chen, Renat Aksitov, Uri Alon, Jie Ren, Ke-
Tim Brooks, Bill Peebles, Connor Homes, Will DePue,             fan Xiao, Pengcheng Yin, Sushant Prakash, Charles
  Yufei Guo, Li Jing, David Schnurr, Joe Taylor, Troy           Sutton, Xuezhi Wang, and Denny Zhou. 2023e. Uni-
  Luhman, Eric Luhman, Clarence Wing Yin Ng, Ricky              versal self-consistency for large language model gen-
  Wang, and Aditya Ramesh. 2024. Video generation               eration.
  models as world simulators. OpenAI.
                                                              Yang Chen, Yingwei Pan, Yehao Li, Ting Yao, and Tao
Tom B. Brown, Benjamin Mann, Nick Ryder, Melanie                Mei. 2023f. Control3d: Towards controllable text-to-
  Subbiah, Jared Kaplan, Prafulla Dhariwal, Arvind              3d generation.
  Neelakantan, Pranav Shyam, Girish Sastry, Amanda
  Askell, Sandhini Agarwal, Ariel Herbert-Voss,               Yi Chen, Rui Wang, Haiyun Jiang, Shuming Shi, and
  Gretchen Krueger, Tom Henighan, Rewon Child,                  Ruifeng Xu. 2023g. Exploring the use of large lan-
  Aditya Ramesh, Daniel M. Ziegler, Jeffrey Wu,                 guage models for reference-free text quality evalua-
  Clemens Winter, Christopher Hesse, Mark Chen, Eric            tion: An empirical study. In Findings of the Associa-
  Sigler, Mateusz Litwin, Scott Gray, Benjamin Chess,           tion for Computational Linguistics: IJCNLP-AACL
  Jack Clark, Christopher Berner, Sam McCandlish,               2023 (Findings), pages 361–374, Nusa Dua, Bali.
  Alec Radford, Ilya Sutskever, and Dario Amodei.               Association for Computational Linguistics.
  2020. Language models are few-shot learners.
                                                              Jiaxin Cheng, Tianjun Xiao, and Tong He. 2023. Con-
Sébastien Bubeck, Varun Chandrasekaran, Ronen El-                sistent video-to-video transfer using synthetic dataset.
  dan, John A. Gehrke, Eric Horvitz, Ece Kamar, Peter            ArXiv, abs/2311.00213.
  Lee, Yin Tat Lee, Yuan-Fang Li, Scott M. Lundberg,
  Harsha Nori, Hamid Palangi, Marco Tulio Ribeiro,            Yew Ken Chia, Guizhen Chen, Luu Anh Tuan, Soujanya
  and Yi Zhang. 2023. Sparks of artificial general              Poria, and Lidong Bing. 2023. Contrastive chain-of-
  intelligence: Early experiments with gpt-4. ArXiv,            thought prompting.
  abs/2303.12712.
                                                              Jiqun Chu and Zuoquan Lin. 2023. Entangled repre-
Nicholas Carlini, Florian Tramer, Eric Wallace,                  sentation learning: A bidirectional encoder decoder
  Matthew Jagielski, Ariel Herbert-Voss, Katherine               model. In Proceedings of the 2022 5th International
  Lee, Adam Roberts, Tom Brown, Dawn Song, Ul-                   Conference on Algorithms, Computing and Artificial
  far Erlingsson, Alina Oprea, and Colin Raffel. 2021.           Intelligence, ACAI ’22, New York, NY, USA. Asso-
  Extracting training data from large language models.           ciation for Computing Machinery.


                                                         47
Zheng Chu, Jingchang Chen, Qianglong Chen, Weijiang           Yi Dong, Ronghui Mu, Gaojie Jin, Yi Qi, Jinwei Hu,
  Yu, Tao He, Haotian Wang, Weihua Peng, Ming Liu,              Xingyu Zhao, Jie Meng, Wenjie Ruan, and Xiaowei
  Bing Qin, and Ting Liu. 2023. A survey of chain of            Huang. 2024. Building guardrails for large language
  thought reasoning: Advances, frontiers and future.            models.
Robert J Cramer, Jacinta Hawgood, Andréa R Kaniuka,           Yann Dubois, Xuechen Li, Rohan Taori, Tianyi Zhang,
  Byron Brooks, and Justin C Baker. 2023. Updated               Ishaan Gulrajani, Jimmy Ba, Carlos Guestrin, Percy
  suicide prevention core competencies for mental               Liang, and Tatsunori B Hashimoto. 2023. Alpaca-
  health professionals: Implications for training, re-          farm: A simulation framework for methods that learn
  search, and practice. Clinical Psychology: Science            from human feedback. In NeurIPS.
  and Practice.
                                                              Zane Durante, Qiuyuan Huang, Naoki Wake, Ran Gong,
Katherine Crowson, Stella Biderman, Daniel Kornis,              Jae Sung Park, Bidipta Sarkar, Rohan Taori, Yusuke
  Dashiell Stander, Eric Hallahan, Louis Castricato,            Noda, Demetri Terzopoulos, Yejin Choi, Katsushi
  and Edward Raff. 2022. Vqgan-clip: Open domain                Ikeuchi, Hoi Vo, Fei-Fei Li, and Jianfeng Gao. 2024.
  image generation and editing with natural language            Agent ai: Surveying the horizons of multimodal in-
  guidance.                                                     teraction.
Leyang Cui, Yu Wu, Jian Liu, Sen Yang, and Yue Zhang.         Julen Etxaniz, Gorka Azkune, Aitor Soroa, Oier Lopez
  2021. Template-based named entity recognition us-              de Lacalle, and Mikel Artetxe. 2023. Do multilingual
  ing bart. Findings of the Association for Computa-             language models think better in english?
  tional Linguistics: ACL-IJCNLP 2021.
                                                              Angela Fan, Mike Lewis, and Yann Dauphin. 2018.
Hai Dang, Lukas Mecke, Florian Lehmann, Sven Goller,            Hierarchical neural story generation. In Proceedings
  and Daniel Buschek. 2022. How to prompt? opportu-             of the 56th Annual Meeting of the Association for
  nities and challenges of zero- and few-shot learning          Computational Linguistics (Volume 1: Long Papers).
  for human-ai interaction in creative applications of          Association for Computational Linguistics.
  generative models.
                                                              Li Fei-Fei, Rob Fergus, and Pietro Perona. 2006. One-
Maksym Del and Mark Fishel. 2023. True detective: A              shot learning of object categories. IEEE Transac-
 deep abductive reasoning benchmark undoable for                 tions on Pattern Analysis and Machine Intelligence,
 gpt-3 and challenging for gpt-4. In Proceedings of              28:594–611.
 the 12th Joint Conference on Lexical and Computa-
 tional Semantics (*SEM 2023). Association for Com-           Lincong Feng, Muyu Wang, Maoyu Wang, Kuo Xu, and
 putational Linguistics.                                        Xiaoli Liu. 2023. Metadreamer: Efficient text-to-3d
                                                                creation with disentangling geometry and texture.
Mingkai Deng, Jianyu Wang, Cheng-Ping Hsieh, Yihan
  Wang, Han Guo, Tianmin Shu, Meng Song, Eric P.              Patrick Fernandes, Daniel Deutsch, Mara Finkel-
  Xing, and Zhiting Hu. 2022. RLPrompt: Optimizing              stein, Parker Riley, André Martins, Graham Neubig,
  Discrete Text Prompts with Reinforcement Learning.            Ankush Garg, Jonathan Clark, Markus Freitag, and
  In RLPrompt: Optimizing Discrete Text Prompts with            Orhan Firat. 2023. The devil is in the errors: Leverag-
  Reinforcement Learning.                                       ing large language models for fine-grained machine
                                                                translation evaluation. In Proceedings of the Eighth
Yihe Deng, Weitong Zhang, Zixiang Chen, and Quan-               Conference on Machine Translation, pages 1066–
  quan Gu. 2023. Rephrase and respond: Let large                1083, Singapore. Association for Computational Lin-
  language models ask better questions for themselves.          guistics.
Shehzaad Dhuliawala, Mojtaba Komeili, Jing Xu,                Chrisantha Fernando, Dylan Banarse, Henryk
  Roberta Raileanu, Xian Li, Asli Celikyilmaz, and              Michalewski, Simon Osindero, and Tim Rock-
  Jason Weston. 2023. Chain-of-verification reduces             täschel. 2023. Promptbreeder: Self-referential
  hallucination in large language models.                       self-improvement via prompt evolution.
Shizhe Diao, Pengcheng Wang, Yong Lin, and Tong               Jinlan Fu, See-Kiong Ng, Zhengbao Jiang, and Pengfei
  Zhang. 2023. Active prompting with chain-of-                   Liu. 2023a. Gptscore: Evaluate as you desire. arXiv
  thought for large language models.                             preprint arXiv:2302.04166.
Ming Ding, Zhuoyi Yang, Wenyi Hong, Wendi Zheng,              Jinlan Fu, See-Kiong Ng, and Pengfei Liu. 2022. Poly-
  Chang Zhou, Da Yin, Junyang Lin, Xu Zou, Zhou                  glot prompt: Multilingual multitask prompt training.
  Shao, Hongxia Yang, and Jie Tang. 2021. Cogview:               In Proceedings of the 2022 Conference on Empiri-
  Mastering text-to-image generation via transform-              cal Methods in Natural Language Processing, pages
  ers. In Advances in Neural Information Processing              9919–9935, Abu Dhabi, United Arab Emirates. As-
  Systems, volume 34, pages 19822–19835. Curran As-              sociation for Computational Linguistics.
  sociates, Inc.
                                                              Yao Fu, Hao Peng, Ashish Sabharwal, Peter Clark, and
Qingxiu Dong, Lei Li, Damai Dai, Ce Zheng, Zhiyong              Tushar Khot. 2023b. Complexity-based prompting
  Wu, Baobao Chang, Xu Sun, Jingjing Xu, Lei Li, and            for multi-step reasoning. In The Eleventh Interna-
  Zhifang Sui. 2023. A survey on in-context learning.           tional Conference on Learning Representations.


                                                         48
Victor Gabillon, Mohammad Ghavamzadeh, Alessandro              Rohit Girdhar, Mannat Singh, Andrew Brown, Quentin
  Lazaric, and Sébastien Bubeck. 2011. Multi-bandit              Duval, Samaneh Azadi, Sai Saketh Rambhatla, Akbar
  best arm identification. In Advances in Neural In-             Shah, Xi Yin, Devi Parikh, and Ishan Misra. 2023.
  formation Processing Systems, volume 24. Curran                Emu video: Factorizing text-to-video generation by
  Associates, Inc.                                               explicit image conditioning.
Deep Ganguli, Amanda Askell, Nicholas Schiefer,                Yichen Gong, Delong Ran, Jinyuan Liu, Conglei Wang,
  Thomas Liao, Kamilė Lukošiūtė, Anna Chen, Anna              Tianshuo Cong, Anyu Wang, Sisi Duan, and Xiaoyun
  Goldie, Azalia Mirhoseini, Catherine Olsson, Danny             Wang. 2023. Figstep: Jailbreaking large vision-
  Hernandez, et al. 2023. The capacity for moral self-           language models via typographic visual prompts.
  correction in large language models. arXiv preprint
  arXiv:2302.07459.                                            Riley Goodside. 2022. Exploiting gpt-3 prompts with
                                                                 malicious inputs that order the model to ignore its
Andrew Gao. 2023. Prompt engineering for large lan-
  guage models. SSRN.                                            previous directions.

Lingyu Gao, Aditi Chaudhary, Krishna Srinivasan,               Google. 2023. Gemini: A family of highly capable
  Kazuma Hashimoto, Karthik Raman, and Michael                   multimodal models.
  Bendersky. 2023a. Ambiguity-aware in-context
  learning with large language models. arXiv preprint          Zhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen,
  arXiv:2309.07900.                                              Yujiu Yang, Nan Duan, and Weizhu Chen. 2024a.
                                                                 CRITIC: Large language models can self-correct
Luyu Gao, Aman Madaan, Shuyan Zhou, Uri Alon,                    with tool-interactive critiquing. In The Twelfth Inter-
  Pengfei Liu, Yiming Yang, Jamie Callan, and Gra-               national Conference on Learning Representations.
  ham Neubig. 2023b. Pal: program-aided lan-
  guage models. In Proceedings of the 40th Interna-            Zhibin Gou, Zhihong Shao, Yeyun Gong, yelong shen,
  tional Conference on Machine Learning, ICML’23.                Yujiu Yang, Minlie Huang, Nan Duan, and Weizhu
  JMLR.org.                                                      Chen. 2024b. ToRA: A tool-integrated reasoning
                                                                 agent for mathematical problem solving. In The
Mingqi Gao, Jie Ruan, Renliang Sun, Xunjian Yin, Ship-           Twelfth International Conference on Learning Repre-
  ing Yang, and Xiaojun Wan. 2023c. Human-like sum-              sentations.
  marization evaluation with chatgpt. arXiv preprint
  arXiv:2304.02554.                                            Chuan Guo, Geoff Pleiss, Yu Sun, and Kilian Q Wein-
Tianyu Gao, Adam Fisch, and Danqi Chen. 2021.                    berger. 2017. On calibration of modern neural net-
  Making pre-trained language models better few-shot             works. In International conference on machine learn-
  learners. In Proceedings of the 59th Annual Meet-              ing, pages 1321–1330. PMLR.
  ing of the Association for Computational Linguistics
  and the 11th International Joint Conference on Natu-         Han Guo, Bowen Tan, Zhengzhong Liu, Eric P. Xing,
  ral Language Processing (Volume 1: Long Papers),               and Zhiting Hu. 2022. Efficient (soft) q-learning for
  pages 3816–3830, Online. Association for Computa-              text generation with limited good data.
  tional Linguistics.
                                                               Priyanka Gupta, Bosheng Ding, Chong Guan, and Ding
Marisa Garcia. 2024. What air canada lost in ‘remark-             Ding. 2024. Generative ai: A systematic review
 able’ lying ai chatbot case. Forbes.                             using topic modelling techniques. Data and Informa-
                                                                  tion Management, page 100066.
Xavier Garcia, Yamini Bansal, Colin Cherry, George
  Foster, Maxim Krikun, Melvin Johnson, and Orhan              Rishav Hada, Varun Gumma, Adrian Wynter, Harshita
  Firat. 2023. The unreasonable effectiveness of few-            Diddee, Mohamed Ahmed, Monojit Choudhury, Ka-
  shot learning for machine translation. In Proceedings          lika Bali, and Sunayana Sitaram. 2024. Are large
  of the 40th International Conference on Machine                language model-based evaluators the solution to scal-
  Learning, ICML’23. JMLR.org.                                   ing up multilingual evaluation? In Findings of the
                                                                 Association for Computational Linguistics: EACL
MF Garnett and SC Curtin. 2023. Suicide mortality
                                                                 2024, pages 1051–1070, St. Julian’s, Malta. Associa-
 in the united states, 2001–2021. NCHS Data Brief,
                                                                 tion for Computational Linguistics.
 464:1–8.
Timnit Gebru, Jamie Morgenstern, Briana Vec-                   Muhammad Usman Hadi, Qasem Al Tashi, Rizwan
  chione, Jennifer Wortman Vaughan, Hanna Wal-                  Qureshi, Abbas Shah, Amgad Muneer, Muhammad
  lach, Hal Daumé III, and Kate Crawford. 2021.                 Irfan, and et al. 2023. Large language models: A
  Datasheets for datasets. Communications of the                comprehensive survey of its applications, challenges,
  ACM, 64(12):86–92.                                            limitations, and future prospects. TechRxiv.

Marjan Ghazvininejad, Hila Gonen, and Luke Zettle-             Aparna Dhinakaran Hakan Tekgul. 2023. Guardrails:
 moyer. 2023. Dictionary-based phrase-level prompt-              What are they and how can you use nemo and
 ing of large language models for machine translation.           guardrails ai to safeguard llms? Online.


                                                          49
Sherzod Hakimov and David Schlangen. 2023. Images               Jiaxin Huang, Shixiang Shane Gu, Le Hou, Yuexin Wu,
  in language space: Exploring the suitability of large            Xuezhi Wang, Hongkun Yu, and Jiawei Han. 2022.
  language models for vision & language tasks. In                  Large language models can self-improve. arXiv
  Findings of the Association for Computational Lin-               preprint arXiv:2210.11610.
  guistics: ACL 2023, pages 14196–14210, Toronto,
  Canada. Association for Computational Linguistics.            Lei Huang, Weijiang Yu, Weitao Ma, Weihong Zhong,
                                                                  Zhangyin Feng, Haotian Wang, Qianglong Chen,
Shibo Hao, Tianyang Liu, Zhen Wang, and Zhiting Hu.               Weihua Peng, Xiaocheng Feng, Bing Qin, and Ting
  2023. ToolkenGPT: Augmenting Frozen Language                    Liu. 2023b. A survey on hallucination in large lan-
  Models with Massive Tools via Tool Embeddings. In               guage models: Principles, taxonomy, challenges, and
  NeurIPS.                                                        open questions.
Hangfeng He, Hongming Zhang, and Dan Roth. 2023a.               Shaohan Huang, Li Dong, Wenhui Wang, Yaru Hao,
  Socreval: Large language models with the so-                    Saksham Singhal, Shuming Ma, Tengchao Lv, Lei
  cratic method for reference-free reasoning evaluation.          Cui, Owais Khan Mohammed, Barun Patra, Qiang
  arXiv preprint arXiv:2310.00074.                                Liu, Kriti Aggarwal, Zewen Chi, Johan Bjorck,
                                                                  Vishrav Chaudhary, Subhojit Som, Xia Song, and
Zhiwei He, Tian Liang, Wenxiang Jiao, Zhuosheng
                                                                  Furu Wei. 2023c. Language is not all you need:
  Zhang, Yujiu Yang, Rui Wang, Zhaopeng Tu, Shum-
                                                                  Aligning perception with language models.
  ing Shi, and Xing Wang. 2023b. Exploring human-
  like translation strategy with large language models.
                                                                Hakan Inan, Kartikeya Upasani, Jianfeng Chi, Rashi
Dan Hendrycks, Collin Burns, Steven Basart, Andy Zou,             Rungta, Krithika Iyer, Yuning Mao, Michael
  Mantas Mazeika, Dawn Song, and Jacob Steinhardt.                Tontchev, Qing Hu, Brian Fuller, Davide Testuggine,
  2021. Measuring Massive Multitask Language Un-                  and Madian Khabsa. 2023. Llama guard: Llm-based
  derstanding. In ICLR.                                           input-output safeguard for human-ai conversations.

Amr Hendy, Mohamed Gomaa Abdelrehim, Amr                        Vivek Iyer, Pinzhen Chen, and Alexandra Birch. 2023.
 Sharaf, Vikas Raunak, Mohamed Gabr, Hitokazu                     Towards effective disambiguation for machine trans-
 Matsushita, Young Jin Kim, Mohamed Afify, and                    lation with large language models.
 Hany Hassan Awadalla. 2023. How good are gpt
 models at machine translation? a comprehensive                 Ajay Jain, Ben Mildenhall, Jonathan T. Barron, Pieter
 evaluation. ArXiv, abs/2302.09210.                               Abbeel, and Ben Poole. 2022. Zero-shot text-guided
                                                                  object generation with dream fields.
Amir Hertz, Ron Mokady, Jay Tenenbaum, Kfir Aber-
 man, Yael Pritch, and Daniel Cohen-Or. 2022.                   Qi Jia, Siyu Ren, Yizhu Liu, and Kenny Q Zhu. 2023.
 Prompt-to-prompt image editing with cross attention              Zero-shot faithfulness evaluation for text summariza-
 control.                                                         tion with foundation language model. arXiv preprint
                                                                  arXiv:2310.11648.
T.F. Heston and C. Khun. 2023. Prompt engineering in
   medical education. Int. Med. Educ., 2:198–205.               Yixing Jiang, Jeremy Irvin, Ji Hun Wang, Muham-
                                                                  mad Ahmed Chaudhry, Jonathan H Chen, and An-
Tobias Hinz, Stefan Heinrich, and Stefan Wermter. 2022.           drew Y Ng. 2024. Many-shot in-context learning
  Semantic object accuracy for generative text-to-                in multimodal foundation models. arXiv preprint
  image synthesis. IEEE Transactions on Pattern Anal-             arXiv:2405.09798.
  ysis and Machine Intelligence, 44(3):1552–1565.
                                                                Zhengbao Jiang, Frank Xu, Luyu Gao, Zhiqing Sun,
Xinyi Hou, Yanjie Zhao, Yue Liu, Zhou Yang, Kailong
                                                                  Qian Liu, Jane Dwivedi-Yu, Yiming Yang, Jamie
  Wang, Li Li, Xiapu Luo, David Lo, John Grundy,
                                                                  Callan, and Graham Neubig. 2023. Active retrieval
  and Haoyu Wang. 2023. Large language models for
                                                                  augmented generation. In Proceedings of the 2023
  software engineering: A systematic literature review.
                                                                  Conference on Empirical Methods in Natural Lan-
Ming-Hao Hsu, Kai-Wei Chang, Shang-Wen Li, and                    guage Processing, pages 7969–7992, Singapore. As-
  Hung yi Lee. 2023. An exploration of in-context                 sociation for Computational Linguistics.
  learning for speech language model.
                                                                Zhengbao Jiang, Frank F. Xu, Jun Araki, and Graham
Yining Hua, Fenglin Liu, Kailai Yang, Zehan Li, Yi han            Neubig. 2020. How can we know what language
  Sheu, Peilin Zhou, Lauren V. Moran, Sophia Ana-                 models know? Transactions of the Association for
  niadou, and Andrew Beam. 2024. Large language                   Computational Linguistics, 8:423–438.
  models in mental health care: a scoping review.
                                                                Wenxiang Jiao, Wenxuan Wang, Jen tse Huang, Xing
Haoyang Huang, Tianyi Tang, Dongdong Zhang,                      Wang, Shuming Shi, and Zhaopeng Tu. 2023. Is chat-
  Wayne Xin Zhao, Ting Song, Yan Xia, and Furu Wei.              gpt a good translator? yes with gpt-4 as the engine.
  2023a. Not all languages are created equal in llms:
  Improving multilingual capability by cross-lingual-           Ziqi Jin and Wei Lu. 2023. Tab-cot: Zero-shot tabular
  thought prompting.                                              chain of thought.


                                                           50
Saurav Kadavath, Tom Conerly, Amanda Askell, Tom                 Natalie Kiesler and Daniel Schiffner. 2023. Large lan-
  Henighan, Dawn Drain, Ethan Perez, Nicholas                      guage models in introductory programming educa-
  Schiefer, Zac Hatfield-Dodds, Nova DasSarma, Eli                 tion: Chatgpt’s performance and implications for
  Tran-Johnson, Scott Johnston, Sheer El-Showk,                    assessments. arXiv preprint arXiv:2308.08572.
  Andy Jones, Nelson Elhage, Tristan Hume, Anna
  Chen, Yuntao Bai, Sam Bowman, Stanislav Fort,                  Hwichan Kim and Mamoru Komachi. 2023. Enhancing
  Deep Ganguli, Danny Hernandez, Josh Jacobson,                    few-shot cross-lingual transfer with target language
  Jackson Kernion, Shauna Kravec, Liane Lovitt, Ka-                peculiar examples. In Findings of the Association for
  mal Ndousse, Catherine Olsson, Sam Ringer, Dario                Computational Linguistics: ACL 2023, pages 747–
  Amodei, Tom Brown, Jack Clark, Nicholas Joseph,                  767, Toronto, Canada. Association for Computational
  Ben Mann, Sam McCandlish, Chris Olah, and Jared                  Linguistics.
  Kaplan. 2022. Language models (mostly) know what
  they know.                                                     Hyuhng Joon Kim, Hyunsoo Cho, Junyeob Kim, Taeuk
                                                                   Kim, Kang Min Yoo, and Sang goo Lee. 2022.
Ehud Karpas, Omri Abend, Yonatan Belinkov, Barak                   Self-generated in-context learning: Leveraging auto-
  Lenz, Opher Lieber, Nir Ratner, Yoav Shoham, Hofit               regressive language models as a demonstration gen-
  Bata, Yoav Levine, Kevin Leyton-Brown, Dor Muhl-                 erator.
  gay, Noam Rozen, Erez Schwartz, Gal Shachaf,
  Shai Shalev-Shwartz, Amnon Shashua, and Moshe                  Sunkyoung Kim, Dayeon Ki, Yireun Kim, and Jinsik
  Tenenholtz. 2022. Mrkl systems: A modular, neuro-                Lee. 2023. Boosting cross-lingual transferability in
  symbolic architecture that combines large language               multilingual models via in-context learning.
  models, external knowledge sources and discrete rea-           Dayoon Ko, Sangho Lee, and Gunhee Kim. 2023a. Can
  soning.                                                          language models laugh at youtube short-form videos?
Staffs Keele et al. 2007. Guidelines for performing              Hyung-Kwon Ko, Gwanmo Park, Hyeon Jeon, Jaemin
   systematic literature reviews in software engineering.          Jo, Juho Kim, and Jinwook Seo. 2023b. Large-scale
                                                                   text-to-image generation models for visual artists’
Nitish Shirish Keskar, Bryan McCann, Lav R. Varshney,              creative works. Proceedings of the 28th International
  Caiming Xiong, and Richard Socher. 2019. Ctrl: A                 Conference on Intelligent User Interfaces.
  conditional transformer language model for control-
  lable generation.                                              Tom Kocmi and Christian Federmann. 2023a. Gemba-
                                                                   mqm: Detecting translation quality error spans with
Kimiya Keyvan and Jimmy Xiangji Huang. 2022. How                   gpt-4. arXiv preprint arXiv:2310.13988.
  to approach ambiguous queries in conversational
  search: A survey of techniques, approaches, tools,             Tom Kocmi and Christian Federmann. 2023b. Large
  and challenges. ACM Computing Surveys, 55(6):1–                  language models are state-of-the-art evaluators of
  40.                                                              translation quality. In Proceedings of the 24th An-
                                                                   nual Conference of the European Association for Ma-
Muhammad Khalifa, Lajanugen Logeswaran, Moontae                    chine Translation, pages 193–203, Tampere, Finland.
 Lee, Honglak Lee, and Lu Wang. 2023. Exploring                    European Association for Machine Translation.
 demonstration ensembling for in-context learning.
                                                                 Takeshi Kojima, Shixiang Shane Gu, Machel Reid, Yu-
Mahmoud Khalil, Ahmad Khalil, and Alioune Ngom.                    taka Matsuo, and Yusuke Iwasawa. 2022. Large lan-
 2023. A comprehensive study of vision transformers                guage models are zero-shot reasoners.
 in image classification tasks.
                                                                 Sawan Kumar and Partha Talukdar. 2021. Reordering
Omar Khattab, Keshav Santhanam, Xiang Lisa Li,                     examples helps during priming-based few-shot learn-
 David Hall, Percy Liang, Christopher Potts, and                   ing.
 Matei Zaharia. 2022. Demonstrate-search-predict:
 Composing retrieval and language models for                     Will Kurt. 2024. Say what you mean: A response to
 knowledge-intensive nlp.                                         ’let me speak freely’. https://blog.dottxt.co/
                                                                   say-what-you-mean.html.
Omar Khattab, Arnav Singhvi, Paridhi Maheshwari,                 Gihyun Kwon and Jong Chul Ye. 2022. Clipstyler:
 Zhiyuan Zhang, Keshav Santhanam, Sri Vard-                        Image style transfer with a single text condition.
 hamanan, Saiful Haq, Ashutosh Sharma, Thomas T.
 Joshi, Hanna Moazam, Heather Miller, Matei Za-                  Lakera. 2024. Lakera guard.
 haria, and Christopher Potts. 2023. Dspy: Compiling
 declarative language model calls into self-improving            Bar Lanyado, Ortal Keizman, and Yair Divinsky. 2023.
 pipelines. arXiv preprint arXiv:2310.03714.                       Can you trust chatgpt’s package recommendations?
                                                                   Vulcan Cyber Blog.
Tushar Khot, Harsh Trivedi, Matthew Finlayson, Yao Fu,
  Kyle Richardson, Peter Clark, and Ashish Sabharwal.            Cindy Le, Congrui Hetang, Ang Cao, and Yihui He.
  2022. Decomposed prompting: A modular approach                   2023. Euclidreamer: Fast and high-quality texturing
  for solving complex tasks.                                       for 3d models with stable diffusion depth.


                                                            51
Soochan Lee and Gunhee Kim. 2023. Recursion of                  Xiaoqian Li, Ercong Nie, and Sheng Liang. 2023g.
  thought: A divide-and-conquer approach to multi-                Crosslingual retrieval augmented in-context learning
  context reasoning with language models.                         for bangla.

Alina Leidinger, Robert van Rooij, and Ekaterina                Xiujun Li, Xi Yin, Chunyuan Li, Pengchuan Zhang,
  Shutova. 2023. The language of prompting: What                  Xiaowei Hu, Lei Zhang, Lijuan Wang, Houdong Hu,
  linguistic properties make a prompt successful?                 Li Dong, Furu Wei, Yejin Choi, and Jianfeng Gao.
                                                                  2020. Oscar: Object-semantics aligned pre-training
Brian Lester, Rami Al-Rfou, and Noah Constant. 2021.              for vision-language tasks.
  The power of scale for parameter-efficient prompt
  tuning. In Proceedings of the 2021 Conference on              Yaoyiran Li, Anna Korhonen, and Ivan Vulić. 2023h.
  Empirical Methods in Natural Language Processing.               On bilingual lexicon induction with large language
  Association for Computational Linguistics.                      models.
Patrick Lewis, Ethan Perez, Aleksandra Piktus, Fabio
                                                                Yifei Li, Zeqi Lin, Shizhuo Zhang, Qiang Fu, Bei Chen,
  Petroni, Vladimir Karpukhin, Naman Goyal, Hein-
                                                                  Jian-Guang Lou, and Weizhu Chen. 2023i. Making
  rich Küttler, Mike Lewis, Wen tau Yih, Tim Rock-
                                                                   language models better reasoners with step-aware
  täschel, Sebastian Riedel, and Douwe Kiela. 2021.
                                                                  verifier. In Proceedings of the 61st Annual Meeting
  Retrieval-augmented generation for knowledge-
                                                                   of the Association for Computational Linguistics (Vol-
  intensive nlp tasks.
                                                                   ume 1: Long Papers). Association for Computational
Bowen Li, Xiaojuan Qi, Thomas Lukasiewicz, and                     Linguistics.
  Philip H. S. Torr. 2019a. Controllable text-to-image
  generation.                                                   Yingji Li, Mengnan Du, Rui Song, Xin Wang, and Ying
                                                                  Wang. 2023j. A survey on fairness in large language
Cheng Li, Jindong Wang, Yixuan Zhang, Kaijie Zhu,                 models.
  Wenxin Hou, Jianxun Lian, Fang Luo, Qiang Yang,
  and Xing Xie. 2023a. Large language models under-             Jingyun Liang, Yuchen Fan, Kai Zhang, Radu Timofte,
  stand and can be enhanced by emotional stimuli.                  Luc Van Gool, and Rakesh Ranjan. 2023. Movideo:
                                                                   Motion-aware video generation with diffusion mod-
Chengzhengxu Li, Xiaoming Liu, Yichen Wang, Duyi                   els.
  Li, Yu Lan, and Chao Shen. 2023b. Dialogue for
  prompting: a policy-gradient-based discrete prompt            Chen-Hsuan Lin, Jun Gao, Luming Tang, Towaki
  optimization for few-shot learning.                             Takikawa, Xiaohui Zeng, Xun Huang, Karsten Kreis,
                                                                  Sanja Fidler, Ming-Yu Liu, and Tsung-Yi Lin. 2023.
Jiahao Li, Hao Tan, Kai Zhang, Zexiang Xu, Fujun                  Magic3d: High-resolution text-to-3d content cre-
   Luan, Yinghao Xu, Yicong Hong, Kalyan Sunkavalli,              ation.
   Greg Shakhnarovich, and Sai Bi. 2023c. Instant3d:
   Fast text-to-3d with sparse-view generation and large        Xi Victoria Lin, Todor Mihaylov, Mikel Artetxe, Tianlu
   reconstruction model.                                          Wang, Shuohui Chen, Daniel Simig, Myle Ott, Na-
                                                                  man Goyal, Shruti Bhosale, Jingfei Du, Ramakanth
Ming Li, Pan Zhou, Jia-Wei Liu, Jussi Keppo, Min Lin,             Pasunuru, Sam Shleifer, Punit Singh Koura, Vishrav
  Shuicheng Yan, and Xiangyu Xu. 2023d. Instant3d:                Chaudhary, Brian O’Horo, Jeff Wang, Luke Zettle-
  Instant text-to-3d generation.                                  moyer, Zornitsa Kozareva, Mona Diab, Veselin Stoy-
                                                                  anov, and Xian Li. 2022. Few-shot learning with
Ruosen Li, Teerth Patel, and Xinya Du. 2023e.                     multilingual generative language models. In Proceed-
  Prd: Peer rank and discussion improve large lan-                ings of the 2022 Conference on Empirical Methods
  guage model based evaluations. arXiv preprint                   in Natural Language Processing, pages 9019–9052,
  arXiv:2307.02762.                                               Abu Dhabi, United Arab Emirates. Association for
                                                                  Computational Linguistics.
Wenbo Li, Pengchuan Zhang, Lei Zhang, Qiuyuan
 Huang, Xiaodong He, Siwei Lyu, and Jianfeng Gao.
 2019b. Object-driven text-to-image synthesis via               Yen-Ting Lin and Yun-Nung Chen. 2023. Llm-eval:
 adversarial training.                                            Unified multi-dimensional automatic evaluation for
                                                                  open-domain conversations with large language mod-
Xiaonan Li, Kai Lv, Hang Yan, Tianyang Lin, Wei Zhu,              els. arXiv preprint arXiv:2305.13711.
  Yuan Ni, Guotong Xie, Xiaoling Wang, and Xipeng
  Qiu. 2023f. Unified demonstration retriever for in-           Jerry Liu. 2022. LlamaIndex.
  context learning.
                                                                Jiachang Liu, Dinghan Shen, Yizhe Zhang, Bill Dolan,
Xiaonan Li and Xipeng Qiu. 2023a. Finding support                  Lawrence Carin, and Weizhu Chen. 2021. What
  examples for in-context learning.                                makes good in-context examples for GPT-3? In
                                                                   Workshop on Knowledge Extraction and Integration
Xiaonan Li and Xipeng Qiu. 2023b. Mot: Memory-of-                  for Deep Learning Architectures; Deep Learning In-
  thought enables chatgpt to self-improve.                         side Out.


                                                           52
Nelson F Liu, Tianyi Zhang, and Percy Liang. 2023a.             Yao Lu, Max Bartolo, Alastair Moore, Sebastian Riedel,
  Evaluating verifiability in generative search engines.          and Pontus Stenetorp. 2021. Fantastically ordered
  In Proceedings of the 2023 Conference on Empirical              prompts and where to find them: Overcoming few-
  Methods in Natural Language Processing.                         shot prompt order sensitivity.

Pengfei Liu, Weizhe Yuan, Jinlan Fu, Zhengbao Jiang,            Yao Lu, Jiayi Wang, Raphael Tang, Sebastian Riedel,
  Hiroaki Hayashi, and Graham Neubig. 2023b. Pre-                 and Pontus Stenetorp. 2024. Strings from the library
  train, prompt, and predict: A systematic survey of              of babel: Random sampling as a strong baseline for
  prompting methods in natural language processing.               prompt optimisation.
  ACM Computing Surveys, 55(9):1–35.
                                                                Charles Duffy Luca Beurer-Kellner, Marc Fischer. 2023.
Weihuang Liu, Xi Shen, Chi-Man Pun, and Xiaodong                  lmql. GitHub repository.
 Cun. 2023c. Explicit visual prompting for low-level
                                                                Zheheng Luo, Qianqian Xie, and Sophia Ananiadou.
 structure segmentations. In 2023 IEEE/CVF Confer-
                                                                  2023. Chatgpt as a factual inconsistency evaluator
 ence on Computer Vision and Pattern Recognition
                                                                  for abstractive text summarization. arXiv preprint
 (CVPR). IEEE.
                                                                  arXiv:2303.15621.
Yang Liu, Dan Iter, Yichong Xu, Shuohang Wang,                  Jiaxi Lv, Yi Huang, Mingfu Yan, Jiancheng Huang,
  Ruochen Xu, and Chenguang Zhu. 2023d. Gpte-                      Jianzhuang Liu, Yifan Liu, Yafei Wen, Xiaoxin
  val: Nlg evaluation using gpt-4 with better human                Chen, and Shifeng Chen. 2023. Gpt4motion: Script-
  alignment. arXiv preprint arXiv:2303.16634.                      ing physical motions in text-to-video generation via
                                                                   blender-oriented gpt planning.
Yihao Liu, Xiangyu Chen, Xianzheng Ma, Xintao Wang,
  Jiantao Zhou, Yu Qiao, and Chao Dong. 2023e. Uni-             Qing Lyu, Shreya Havaldar, Adam Stein, Li Zhang,
  fying image processing as visual prompting question             Delip Rao, Eric Wong, Marianna Apidianaki, and
  answering.                                                      Chris Callison-Burch. 2023. Faithful chain-of-
                                                                  thought reasoning.
Yongkang Liu, Shi Feng, Daling Wang, Yifei Zhang,
  and Hinrich Schütze. 2023f. Evaluate what you can’t           Huan Ma, Changqing Zhang, Yatao Bian, Lemao Liu,
  evaluate: Unassessable generated responses quality.             Zhirui Zhang, Peilin Zhao, Shu Zhang, Huazhu Fu,
  arXiv preprint arXiv:2305.14658.                                Qinghua Hu, and Bingzhe Wu. 2023. Fairness-
                                                                  guided few-shot prompting for large language mod-
Yuxin Liu, Minshan Xie, Hanyuan Liu, and Tien-Tsin                els. arXiv preprint arXiv:2303.13217.
  Wong. 2023g. Text-guided texturing by synchronized
  multi-view diffusion.                                         Aman Madaan, Niket Tandon, Prakhar Gupta, Skyler
                                                                 Hallinan, Luyu Gao, Sarah Wiegreffe, Uri Alon,
Yuxuan Liu, Tianchi Yang, Shaohan Huang, Zihan                   Nouha Dziri, Shrimai Prabhumoye, Yiming Yang,
  Zhang, Haizhen Huang, Furu Wei, Weiwei Deng,                   Shashank Gupta, Bodhisattwa Prasad Majumder,
  Feng Sun, and Qi Zhang. 2023h. Calibrating llm-                Katherine Hermann, Sean Welleck, Amir Yazdan-
  based evaluator. arXiv preprint arXiv:2309.13308.              bakhsh, and Peter Clark. 2023. Self-refine: Iterative
                                                                 refinement with self-feedback.
Jieyi Long. 2023. Large language model guided tree-of-
   thought.                                                     Ninareh Mehrabi, Fred Morstatter, Nripsuta Saxena,
                                                                  Kristina Lerman, and Aram Galstyan. 2021. A sur-
Jonathan Lorraine, Kevin Xie, Xiaohui Zeng, Chen-                 vey on bias and fairness in machine learning. ACM
  Hsuan Lin, Towaki Takikawa, Nicholas Sharp, Tsung-              computing surveys (CSUR), 54(6):1–35.
  Yi Lin, Ming-Yu Liu, Sanja Fidler, and James Lucas.
                                                                Laura Melzer, Thomas Forkmann, and Tobias Teismann.
  2023. Att3d: Amortized text-to-3d object synthesis.
                                                                  2024. Suicide crisis syndrome: A systematic review.
                                                                  Suicide and Life-Threatening Behavior. February 27,
Albert Lu, Hongxin Zhang, Yanzhe Zhang, Xuezhi
                                                                  online ahead of print.
  Wang, and Diyi Yang. 2023a. Bounding the capabili-
  ties of large language models in open text generation         Fanxu Meng, Haotong Yang, Yiding Wang, and Muhan
  with prompt constraints.                                        Zhang. 2023. Chain of images for intuitively reason-
                                                                  ing.
Hongyuan Lu, Haoyang Huang, Dongdong Zhang, Hao-
  ran Yang, Wai Lam, and Furu Wei. 2023b. Chain-                B. Meskó. 2023. Prompt engineering as an impor-
  of-dictionary prompting elicits translation in large            tant emerging skill for medical professionals: Tuto-
  language models.                                                rial. Journal of Medical Internet Research, 25(Suppl
                                                                  1):e50638.
Qingyu Lu, Baopu Qiu, Liang Ding, Liping Xie, and
  Dacheng Tao. 2023c. Error analysis prompting en-              Yachun Mi, Yu Li, Yan Shu, Chen Hui, Puchao Zhou,
  ables human-like translation evaluation in large lan-           and Shaohui Liu. 2023. Clif-vqa: Enhancing video
  guage models: A case study on chatgpt. arXiv                    quality assessment by incorporating high-level se-
  preprint arXiv:2303.13809.                                      mantic information related to human feelings.


                                                           53
Grégoire Mialon, Roberto Dessì, Maria Lomeli, Christo-        Alexandra Neagu. 2023. How can large language mod-
  foros Nalmpantis, Ram Pasunuru, Roberta Raileanu,             els and prompt engineering be leveraged in Com-
  Baptiste Rozière, Timo Schick, Jane Dwivedi-Yu,               puter Science education?: Systematic literature re-
  Asli Celikyilmaz, Edouard Grave, Yann LeCun, and              view. Master’s thesis, Delft University of Technol-
  Thomas Scialom. 2023. Augmented language mod-                 ogy, 6.
  els: a survey.
                                                              Ercong Nie, Sheng Liang, Helmut Schmid, and Hinrich
Sewon Min, Xinxi Lyu, Ari Holtzman, Mikel Artetxe,              Schütze. 2023. Cross-lingual retrieval augmented
  Mike Lewis, Hannaneh Hajishirzi, and Luke Zettle-             prompt for low-resource languages. In Findings of
  moyer. 2022. Rethinking the role of demonstrations:           the Association for Computational Linguistics: ACL
  What makes in-context learning work?                          2023, pages 8320–8340, Toronto, Canada. Associa-
                                                                tion for Computational Linguistics.
Sewon Min, Julian Michael, Hannaneh Hajishirzi, and
  Luke Zettlemoyer. 2020. Ambigqa: Answering                  Xuefei Ning, Zinan Lin, Zixuan Zhou, Zifu Wang,
  ambiguous open-domain questions. arXiv preprint               Huazhong Yang, and Yu Wang. 2023. Skeleton-of-
  arXiv:2004.10645.                                             thought: Large language models can do parallel de-
                                                                coding.
R.A. Morelli, J.D. Bronzino, and J.W. Goethe. 1991. A
  computational speech-act model of human-computer            OpenAI. 2023. OpenAI Assistants.
  conversations. In Proceedings of the 1991 IEEE
  Seventeenth Annual Northeast Bioengineering Con-            Jonas Oppenlaender. 2023. A taxonomy of prompt
  ference, pages 263–264.                                       modifiers for text-to-image generation.

Yasmin Moslem, Rejwanul Haque, John D. Kelleher,              Anton Osika. 2023. gpt-engineer.
  and Andy Way. 2023. Adaptive machine translation
  with large language models. In Proceedings of the           Matthew J Page, Joanne E McKenzie, Patrick M
  24th Annual Conference of the European Association           Bossuyt, Isabelle Boutron, Tammy C Hoffmann,
  for Machine Translation, pages 227–237, Tampere,             Cynthia D Mulrow, Larissa Shamseer, Jennifer M
  Finland. European Association for Machine Transla-           Tetzlaff, Elie A Akl, Sue E Brennan, Roger Chou,
  tion.                                                        Julie Glanville, Jeremy M Grimshaw, Asbjørn Hrób-
                                                               jartsson, Manoj M Lalu, Tianjing Li, Elizabeth W
                                                               Loder, Evan Mayo-Wilson, Steve McDonald, Luke A
Fangwen Mu, Lin Shi, Song Wang, Zhuohao Yu, Bin-               McGuinness, Lesley A Stewart, James Thomas, An-
  quan Zhang, Chenxue Wang, Shichao Liu, and Qing              drea C Tricco, Vivian A Welch, Penny Whiting, and
  Wang. 2023. Clarifygpt: Empowering llm-based                 David Moher. 2021. The prisma 2020 statement: an
  code generation with intention clarification.                updated guideline for reporting systematic reviews.
                                                               BMJ, 372.
Niklas Muennighoff, Thomas Wang, Lintang Sutawika,
  Adam Roberts, Stella Biderman, Teven Le Scao,               Ehsan Pajouheshgar, Yitao Xu, Alexander Mordvint-
  M Saiful Bari, Sheng Shen, Zheng Xin Yong, Hai-               sev, Eyvind Niklasson, Tong Zhang, and Sabine
  ley Schoelkopf, Xiangru Tang, Dragomir Radev,                 Süsstrunk. 2023. Mesh neural cellular automata.
  Alham Fikri Aji, Khalid Almubarak, Samuel Al-
  banie, Zaid Alyafeai, Albert Webson, Edward Raff,           Pruthvi Patel, Swaroop Mishra, Mihir Parmar, and
  and Colin Raffel. 2023. Crosslingual generaliza-              Chitta Baral. 2022. Is a question decomposition unit
  tion through multitask finetuning. In Proceedings             all we need?
  of the 61st Annual Meeting of the Association for
  Computational Linguistics (Volume 1: Long Papers),          Shishir G. Patil, Tianjun Zhang, Xin Wang, and
  pages 15991–16111, Toronto, Canada. Association               Joseph E. Gonzalez. 2023. Gorilla: Large lan-
  for Computational Linguistics.                                guage model connected with massive apis. ArXiv,
                                                                abs/2305.15334.
Akshay Nambi, Vaibhav Balloli, Mercy Ranjit, Tanuja
  Ganu, Kabir Ahuja, Sunayana Sitaram, and Kalika             Hammond Pearce, Baleegh Ahmad, Benjamin Tan,
  Bali. 2023. Breaking language barriers with a leap:           Brendan Dolan-Gavitt, and Ramesh Karri. 2021.
  Learning strategies for polyglot llms.                        Asleep at the keyboard? assessing the security of
                                                                github copilot’s code contributions.
Milad Nasr, Nicholas Carlini, Jonathan Hayase,
  Matthew Jagielski, A. Feder Cooper, Daphne Ip-              Hammond Pearce, Benjamin Tan, Baleegh Ahmad,
  polito, Christopher A. Choquette-Choo, Eric Wal-              Ramesh Karri, and Brendan Dolan-Gavitt. 2022. Ex-
  lace, Florian Tramèr, and Katherine Lee. 2023. Scal-          amining zero-shot vulnerability repair with large lan-
  able extraction of training data from (production)            guage models.
  language models.
                                                              Puyuan Peng, Brian Yan, Shinji Watanabe, and David
National Center for Health Workforce Analysis. 2023.            Harwath. 2023. Prompting the hidden talent of web-
  Behavioral health workforce, 2023.                            scale speech models for zero-shot task generalization.


                                                         54
Ethan Perez, Saffron Huang, Francis Song, Trevor Cai,           Preamble. 2024. Our product.
  Roman Ring, John Aslanides, Amelia Glaese, Nat
  McAleese, and Geoffrey Irving. 2022. Red teaming              Ofir Press, Muru Zhang, Sewon Min, Ludwig Schmidt,
  language models with language models.                           Noah A. Smith, and Mike Lewis. 2022. Measuring
                                                                  and narrowing the compositionality gap in language
Fábio Perez and Ian Ribeiro. 2022. Ignore previous                models.
  prompt: Attack techniques for language models.
                                                                Reid Pryzant, Dan Iter, Jerry Li, Yin Tat Lee, Chen-
Neil Perry, Megha Srivastava, Deepak Kumar, and Dan               guang Zhu, and Michael Zeng. 2023. Automatic
  Boneh. 2022. Do users write more insecure code                  prompt optimization with "gradient descent" and
  with ai assistants?                                             beam search.
Denis Peskoff and Brandon M Stewart. 2023. Credi-               Ratish Puduppully, Anoop Kunchukuttan, Raj Dabre,
  ble without credit: Domain experts assess generative            Ai Ti Aw, and Nancy F. Chen. 2023. Decomposed
  language models. In Proceedings of the 61st Annual              prompting for machine translation between related
  Meeting of the Association for Computational Lin-               languages using large language models.
  guistics (Volume 2: Short Papers), pages 427–438.
                                                                Bo Qiao, Liqun Li, Xu Zhang, Shilin He, Yu Kang,
Denis Peskoff, Adam Visokay, Sander Schulhoff, Ben-               Chaoyun Zhang, Fangkai Yang, Hang Dong, Jue
  jamin Wachspress, Alan Blinder, and Brandon M                   Zhang, Lu Wang, Ming-Jie Ma, Pu Zhao, Si Qin, Xi-
  Stewart. 2023. Gpt deciphering fedspeak: Quantify-              aoting Qin, Chao Du, Yong Xu, Qingwei Lin, S. Raj-
  ing dissent among hawks and doves. In Findings                  mohan, and Dongmei Zhang. 2023. Taskweaver: A
  of the Association for Computational Linguistics:               code-first agent framework. ArXiv, abs/2311.17541.
  EMNLP 2023, pages 6529–6539.
                                                                Shuofei Qiao, Yixin Ou, Ningyu Zhang, Xiang Chen,
Denis Peskov, Viktor Hangya, Jordan Boyd-Graber, and              Yunzhi Yao, Shumin Deng, Chuanqi Tan, Fei Huang,
  Alexander Fraser. 2021. Adapting entities across                and Huajun Chen. 2022. Reasoning with language
  languages and cultures. Findings of the Association             model prompting: A survey.
  for Computational Linguistics: EMNLP 2021.
                                                                Libo Qin, Qiguang Chen, Fuxuan Wei, Shijue Huang,
Fabio Petroni, Tim Rocktäschel, Sebastian Riedel,                 and Wanxiang Che. 2023a. Cross-lingual prompt-
  Patrick Lewis, Anton Bakhtin, Yuxiang Wu, and                   ing: Improving zero-shot chain-of-thought reasoning
  Alexander Miller. 2019. Language models as knowl-               across languages.
  edge bases? Proceedings of the 2019 Conference
  on Empirical Methods in Natural Language Process-             Yujia Qin, Shengding Hu, Yankai Lin, Weize Chen,
  ing and the 9th International Joint Conference on               Ning Ding, Ganqu Cui, Zheni Zeng, Yufei Huang,
  Natural Language Processing (EMNLP-IJCNLP).                     Chaojun Xiao, Chi Han, Yi Ren Fung, Yusheng Su,
                                                                  Huadong Wang, Cheng Qian, Runchu Tian, Kunlun
Pouya Pezeshkpour and Estevam Hruschka. 2023.                     Zhu, Shi Liang, Xingyu Shen, Bokai Xu, Zhen Zhang,
  Large language models sensitivity to the order of               Yining Ye, Bo Li, Ziwei Tang, Jing Yi, Yu Zhu, Zhen-
  options in multiple-choice questions. arXiv preprint            ning Dai, Lan Yan, Xin Cong, Ya-Ting Lu, Weilin
  arXiv:2308.11483.                                               Zhao, Yuxiang Huang, Jun-Han Yan, Xu Han, Xian
                                                                  Sun, Dahai Li, Jason Phang, Cheng Yang, Tong-
Carol W. Pfaff. 1979. Constraints on language mix-                shuang Wu, Heng Ji, Zhiyuan Liu, and Maosong
  ing: Intrasentential code-switching and borrowing in            Sun. 2023b. Tool learning with foundation models.
  spanish/english. Language, pages 291–318.                       ArXiv, abs/2304.08354.
Jonathan Pilault, Xavier Garcia, Arthur Bražinskas, and         Alec Radford, Jong Wook Kim, Chris Hallacy, Aditya
  Orhan Firat. 2023. Interactive-chain-prompting: Am-             Ramesh, Gabriel Goh, Sandhini Agarwal, Girish Sas-
  biguity resolution for crosslingual conditional gener-          try, Amanda Askell, Pamela Mishkin, Jack Clark,
  ation with interaction.                                         et al. 2021. Learning transferable visual models from
                                                                  natural language supervision. In International confer-
Ben Poole, Ajay Jain, Jonathan T. Barron, and Ben                 ence on machine learning, pages 8748–8763. PMLR.
  Mildenhall. 2022. Dreamfusion: Text-to-3d using 2d
  diffusion.                                                    Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
                                                                  Dario Amodei, Ilya Sutskever, et al. 2019a. Lan-
Shana Poplack. 1980. Sometimes i’ll start a sentence in           guage models are unsupervised multitask learners.
  spanish y termino en español: Toward a typology of              OpenAI blog, 1(8):9.
  code-switching. Linguistics, 18(7-8):581–618.
                                                                Alec Radford, Jeffrey Wu, Rewon Child, David Luan,
Archiki Prasad, Peter Hase, Xiang Zhou, and Mohit                 Dario Amodei, Ilya Sutskever, et al. 2019b. Lan-
  Bansal. 2023. GrIPS: Gradient-free, edit-based in-              guage models are unsupervised multitask learners.
  struction search for prompting large language models.           OpenAI blog, 1(8):9.
  In Proceedings of the 17th Conference of the Euro-
  pean Chapter of the Association for Computational             Sudha Rao and Hal Daumé III. 2019. Answer-based
  Linguistics, pages 3845–3864, Dubrovnik, Croatia.               adversarial training for generating clarification ques-
  Association for Computational Linguistics.                      tions. arXiv preprint arXiv:1904.02281.


                                                           55
Traian Rebedea, Razvan Dinu, Makesh Sreedhar,                      Timo Schick and Hinrich Schütze. 2020a. Exploiting
  Christopher Parisien, and Jonathan Cohen. 2023.                    cloze-questions for few-shot text classification and
  Nemo guardrails: A toolkit for controllable and safe               natural language inference. In Conference of the Eu-
  llm applications with programmable rails. arXiv.                   ropean Chapter of the Association for Computational
                                                                     Linguistics.
Philip Resnik, April Foreman, Michelle Kuchuk, Kather-
  ine Musacchio Schafer, and Beau Pinkham. 2021.                   Timo Schick and Hinrich Schütze. 2020b. It’s not just
  Naturally occurring language as a source of evidence               size that matters: Small language models are also
  in suicide prevention. Suicide and Life-Threatening                few-shot learners. ArXiv, abs/2009.07118.
  Behavior, 51(1):88–96.
                                                                   Timo Schick and Hinrich Schütze. 2021. Exploiting
Laria Reynolds and Kyle McDonell. 2021. Prompt pro-                  cloze-questions for few-shot text classification and
  gramming for large language models: Beyond the                     natural language inference. In Proceedings of the
  few-shot paradigm. In Extended Abstracts of the                    16th Conference of the European Chapter of the Asso-
  2021 CHI Conference on Human Factors in Comput-                    ciation for Computational Linguistics: Main Volume.
  ing Systems, CHI ’21. ACM.                                         Association for Computational Linguistics.
Megan L Rogers, Carol Chu, and Thomas Joiner. 2019.                Douglas C. Schmidt, Jesse Spencer-Smith, Quchen Fu,
 The necessity, validity, and clinical utility of a new di-          and Jules White. 2023. Cataloging prompt patterns to
 agnostic entity: Acute suicidal affective disturbance               enhance the discipline of prompt engineering. Dept.
 (asad). Journal of Clinical Psychology, 75(6):999.                  of Computer Science, Vanderbilt University. Email:
                                                                     douglas.c.schmidt, jesse.spencer-smith, quchen.fu,
Robin Rombach, Andreas Blattmann, Dominik Lorenz,
                                                                     jules.white@vanderbilt.edu.
  Patrick Esser, and Björn Ommer. 2022. High-
  resolution image synthesis with latent diffusion mod-            Allison Schuck, Raffaella Calati, Shira Barzilay, Sarah
  els.                                                               Bloch-Elkouby, and Igor I. Galynker. 2019a. Suicide
Shamik Roy, Raphael Shu, Nikolaos Pappas, Elman                      crisis syndrome: A review of supporting evidence
  Mansimov, Yi Zhang, Saab Mansour, and Dan Roth.                    for a new suicide-specific diagnosis. Behavioral sci-
  2023. Conversation style transfer using few-shot                   ences & the law, 37 3:223–239.
  learning. In Proceedings of the 13th International               Allison Schuck, Raffaella Calati, Shira Barzilay, Sarah
  Joint Conference on Natural Language Processing                    Bloch-Elkouby, and Igor Galynker. 2019b. Suicide
  and the 3rd Conference of the Asia-Pacific Chapter of
                                                                     crisis syndrome: A review of supporting evidence
  the Association for Computational Linguistics (Vol-
                                                                     for a new suicide-specific diagnosis. Behavioral sci-
  ume 1: Long Papers), pages 119–143, Nusa Dua,
                                                                     ences and the law, 37(3):223–239.
  Bali. Association for Computational Linguistics.
Ohad Rubin, Jonathan Herzig, and Jonathan Berant.                  Sander Schulhoff. 2022. Learn Prompting.
  2022. Learning to retrieve prompts for in-context                Sander Schulhoff, Jeremy Pinto, Anaum Khan, Louis-
  learning. In Proceedings of the 2022 Conference of                 François Bouchard, Chenglei Si, Svetlina Anati,
  the North American Chapter of the Association for                  Valen Tagliabue, Anson Kost, Christopher Carnahan,
  Computational Linguistics: Human Language Tech-                    and Jordan Boyd-Graber. 2023. Ignore this title and
  nologies. Association for Computational Linguistics.               HackAPrompt: Exposing systemic vulnerabilities
Runway. 2023.    Gen-2 prompt tips.   https:                         of LLMs through a global prompt hacking compe-
  //help.runwayml.com/hc/en-us/articles/                             tition. In Proceedings of the 2023 Conference on
  17329337959699-Gen-2-Prompt-Tips.                                  Empirical Methods in Natural Language Processing,
                                                                     pages 4945–4977, Singapore. Association for Com-
Pranab Sahoo, Ayush Kumar Singh, Sriparna Saha,                      putational Linguistics.
  Vinija Jain, Samrat Mondal, and Aman Chadha. 2024.
  A systematic survey of prompt engineering in large               Sander V Schulhoff. 2024. Prompt injection vs jail-
  language models: Techniques and applications.                      breaking: What is the difference?

Gustavo Sandoval, Hammond Pearce, Teo Nys, Ramesh                  Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane
  Karri, Siddharth Garg, and Brendan Dolan-Gavitt.                  Suhr. 2023a. Quantifying language models’ sensi-
  2022. Lost at c: A user study on the security implica-            tivity to spurious features in prompt design or: How
  tions of large language model code assistants.                    i learned to start worrying about prompt formatting.
                                                                    arXiv preprint arXiv:2310.11324.
Shubhra Kanti Karmaker Santu and Dongji Feng. 2023.
  Teler: A general taxonomy of llm prompts for bench-              Melanie Sclar, Yejin Choi, Yulia Tsvetkov, and Alane
  marking complex tasks.                                            Suhr. 2023b. Quantifying language models’ sensitiv-
                                                                    ity to spurious features in prompt design or: How i
Timo Schick, Jane Dwivedi-Yu, Roberto Dessì, Roberta                learned to start worrying about prompt formatting.
  Raileanu, Maria Lomeli, Luke Zettlemoyer, Nicola
  Cancedda, and Thomas Scialom. 2023. Toolformer:                  Harsha-Nori Scott Lundberg, Marco Tulio Cor-
  Language models can teach themselves to use tools.                 reia Ribeiro. 2023. guidance. GitHub repository.


                                                              56
John R. Searle. 1969. Speech Acts: An Essay in the Phi-          Chenglei Si, Navita Goyal, Sherry Tongshuang Wu,
  losophy of Language. Cambridge University Press.                 Chen Zhao, Shi Feng, Hal Daumé III, and Jordan
                                                                   Boyd-Graber. 2023c. Large language models help
Omar Shaikh, Hongxin Zhang, William Held, Michael                  humans verify truthfulness–except when they are con-
 Bernstein, and Diyi Yang. 2023. On second thought,                vincingly wrong. arXiv preprint arXiv:2310.12558.
 let’s not think step by step! bias and toxicity in zero-
 shot reasoning.                                                 Chenglei Si, Weijia Shi, Chen Zhao, Luke Zettlemoyer,
                                                                   and Jordan Lee Boyd-Graber. 2023d. Getting MoRE
Mrinank Sharma, Meg Tong, Tomasz Korbak, David                     out of Mixture of language model Reasoning Experts.
  Duvenaud, Amanda Askell, Samuel R Bowman,                        Findings of Empirical Methods in Natural Language
  Newton Cheng, Esin Durmus, Zac Hatfield-Dodds,                   Processing.
  Scott R Johnston, et al. 2023. Towards understand-
  ing sycophancy in language models. arXiv preprint              Suzanna Sia and Kevin Duh. 2023. In-context learn-
  arXiv:2310.13548.                                                ing as maintaining coherency: A study of on-the-fly
                                                                   machine translation using large language models.
Yongliang Shen, Kaitao Song, Xu Tan, Dong Sheng Li,              Significant Gravitas. 2023. AutoGPT.
  Weiming Lu, and Yue Ting Zhuang. 2023. Hugging-
  gpt: Solving ai tasks with chatgpt and its friends in          Uriel Singer, Shelly Sheynin, Adam Polyak, Oron
  hugging face. ArXiv, abs/2303.17580.                             Ashual, Iurii Makarov, Filippos Kokkinos, Naman
                                                                   Goyal, Andrea Vedaldi, Devi Parikh, Justin Johnson,
Freda Shi, Mirac Suzgun, Markus Freitag, Xuezhi Wang,              and Yaniv Taigman. 2023. Text-to-4d dynamic scene
   Suraj Srivats, Soroush Vosoughi, Hyung Won Chung,               generation.
  Yi Tay, Sebastian Ruder, Denny Zhou, Dipanjan Das,
   and Jason Wei. 2022. Language models are multilin-            Taylor Sorensen, Joshua Robinson, Christopher Ryt-
   gual chain-of-thought reasoners.                                ting, Alexander Shaw, Kyle Rogers, Alexia Delorey,
                                                                   Mahmoud Khalil, Nancy Fulda, and David Wingate.
Taylor Shin, Yasaman Razeghi, Robert L Logan IV,                   2022. An information-theoretic approach to prompt
  Eric Wallace, and Sameer Singh. 2020a. Eliciting                 engineering without ground truth labels. In Proceed-
  knowledge from language models using automati-                   ings of the 60th Annual Meeting of the Association
  cally generated prompts. ArXiv, abs/2010.15980.                  for Computational Linguistics (Volume 1: Long Pa-
                                                                   pers), pages 819–862, Dublin, Ireland. Association
Taylor Shin, Yasaman Razeghi, Robert L. Logan IV, Eric             for Computational Linguistics.
  Wallace, and Sameer Singh. 2020b. Autoprompt:
  Eliciting knowledge from language models with au-              Andrea Sottana, Bin Liang, Kai Zou, and Zheng Yuan.
  tomatically generated prompts. Proceedings of the                2023. Evaluation metrics in the era of gpt-4: Reli-
  2020 Conference on Empirical Methods in Natural                  ably evaluating large language models on sequence
  Language Processing (EMNLP).                                     to sequence tasks. arXiv preprint arXiv:2310.13800.

Han-Chin Shing, Suraj Nair, Ayah Zirikly, Meir Frieden-          Michal Štefánik and Marek Kadlčík. 2023. Can in-
  berg, Hal Daumé III, and Philip Resnik. 2018. Expert,            context learners learn a reasoning concept from
  crowdsourced, and machine assessment of suicide                  demonstrations? In Proceedings of the 1st Work-
  risk via online postings. In Proceedings of the Fifth            shop on Natural Language Reasoning and Structured
  Workshop on Computational Linguistics and Clinical               Explanations (NLRSE), pages 107–115, Toronto,
  Psychology: From Keyboard to Clinic, pages 25–36,                Canada. Association for Computational Linguistics.
  New Orleans, LA. Association for Computational
  Linguistics.                                                   Hongjin Su, Jungo Kasai, Chen Henry Wu, Weijia Shi,
                                                                   Tianlu Wang, Jiayi Xin, Rui Zhang, Mari Ostendorf,
                                                                   Luke Zettlemoyer, Noah A. Smith, and Tao Yu. 2022.
Noah Shinn, Federico Cassano, Edward Berman, Ash-
                                                                   Selective annotation makes language models better
  win Gopinath, Karthik Narasimhan, and Shunyu Yao.
                                                                   few-shot learners.
  2023. Reflexion: Language agents with verbal rein-
  forcement learning.                                            Zhi Rui Tam, Cheng-Kuang Wu, Yi-Lin Tsai, Chieh-
                                                                   Yen Lin, Hung yi Lee, and Yun-Nung Chen. 2024.
Chenglei Si, Dan Friedman, Nitish Joshi, Shi Feng,                 Let me speak freely? a study on the impact of format
  Danqi Chen, and He He. 2023a. Measuring induc-                   restrictions on performance of large language models.
  tive biases of in-context learning with underspecified
  demonstrations. In Association for Computational               Lv Tang, Peng-Tao Jiang, Hao-Ke Xiao, and Bo Li.
  Linguistics (ACL).                                               2023. Towards training-free open-world segmenta-
                                                                   tion via image prompting foundation models.
Chenglei Si, Zhe Gan, Zhengyuan Yang, Shuohang
  Wang, Jianfeng Wang, Jordan Boyd-Graber, and Li-               Eshaan Tanwar, Subhabrata Dutta, Manish Borthakur,
  juan Wang. 2023b. Prompting gpt-3 to be reliable.                and Tanmoy Chakraborty. 2023. Multilingual LLMs
  In International Conference on Learning Representa-              are better cross-lingual in-context learners with align-
  tions (ICLR).                                                    ment. In Proceedings of the 61st Annual Meeting of


                                                            57
  the Association for Computational Linguistics (Vol-              the 61st Annual Meeting of the Association for Com-
  ume 1: Long Papers), pages 6292–6307, Toronto,                   putational Linguistics (Volume 1: Long Papers),
  Canada. Association for Computational Linguistics.               pages 10014–10037, Toronto, Canada. Association
                                                                   for Computational Linguistics.
Ming Tao, Hao Tang, Fei Wu, Xiao-Yuan Jing, Bing-
  Kun Bao, and Changsheng Xu. 2022. Df-gan: A                    Rasul Tutunov, Antoine Grosnit, Juliusz Ziomek, Jun
  simple and effective baseline for text-to-image syn-             Wang, and Haitham Bou-Ammar. 2023. Why can
  thesis.                                                          large language models generate correct chain-of-
                                                                   thoughts?
Charlotte Thompson and Tiana Kelly. 2023. When
  hallucinations become reality: An exploration of ai            Shubham Vatsal and Harsh Dubey. 2024. A survey
  package hallucination attacks. Darktrace Blog.                   of prompt engineering methods in large language
                                                                   models for different nlp tasks.
Katherine Tian, Eric Mitchell, Allan Zhou, Archit
  Sharma, Rafael Rafailov, Huaxiu Yao, Chelsea Finn,             Anton Voronov, Lena Wolf, and Max Ryabinin. 2024.
  and Christopher Manning. 2023. Just ask for cali-                Mind your format: Towards consistent evaluation of
  bration: Strategies for eliciting calibrated confidence          in-context learning improvements. arXiv preprint
  scores from language models fine-tuned with human                arXiv:2401.06766.
  feedback. In Proceedings of the 2023 Conference
  on Empirical Methods in Natural Language Process-              Eric Wallace, Shi Feng, Nikhil Kandpal, Matt Gardner,
  ing, pages 5433–5442, Singapore. Association for                  and Sameer Singh. 2019. Universal adversarial trig-
  Computational Linguistics.                                        gers for attacking and analyzing nlp. In Conference
                                                                    on Empirical Methods in Natural Language Process-
Lindia Tjuatja, Valerie Chen, Tongshuang Wu, Ameet                  ing.
  Talwalkwar, and Graham Neubig. 2024. Do llms
  exhibit human-like response biases? a case study in            Xingchen Wan, Ruoxi Sun, Hanjun Dai, Sercan O. Arik,
  survey design. Transactions of the Association for               and Tomas Pfister. 2023a. Better zero-shot reasoning
  Computational Linguistics, 12:1011–1026.                         with self-adaptive prompting.

Hugo Touvron, Louis Martin, Kevin Stone, Peter Al-               Xingchen Wan, Ruoxi Sun, Hootan Nakhost, Han-
  bert, Amjad Almahairi, Yasmine Babaei, Nikolay                   jun Dai, Julian Martin Eisenschlos, Sercan O. Arik,
  Bashlykov, Soumya Batra, Prajjwal Bhargava, Shruti               and Tomas Pfister. 2023b. Universal self-adaptive
  Bhosale, Dan Bikel, Lukas Blecher, Cristian Canton               prompting.
  Ferrer, Moya Chen, Guillem Cucurull, David Esiobu,
  Jude Fernandes, Jeremy Fu, Wenyin Fu, Brian Fuller,            Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Man-
  Cynthia Gao, Vedanuj Goswami, Naman Goyal, An-                   dlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, and An-
  thony Hartshorn, Saghar Hosseini, Rui Hou, Hakan                 ima Anandkumar. 2023a. Voyager: An open-ended
  Inan, Marcin Kardas, Viktor Kerkez, Madian Khabsa,               embodied agent with large language models.
  Isabel Kloumann, Artem Korenev, Punit Singh Koura,
  Marie-Anne Lachaux, Thibaut Lavril, Jenya Lee, Di-             Jiaan Wang, Yunlong Liang, Fandong Meng, Haoxiang
  ana Liskovich, Yinghai Lu, Yuning Mao, Xavier Mar-                Shi, Zhixu Li, Jinan Xu, Jianfeng Qu, and Jie Zhou.
  tinet, Todor Mihaylov, Pushkar Mishra, Igor Moly-                 2023b. Is chatgpt a good nlg evaluator? a preliminary
  bog, Yixin Nie, Andrew Poulton, Jeremy Reizen-                    study. arXiv preprint arXiv:2303.04048.
  stein, Rashi Rungta, Kalyan Saladi, Alan Schelten,
  Ruan Silva, Eric Michael Smith, Ranjan Subrama-                Jiaqi Wang, Zhengliang Liu, Lin Zhao, Zihao Wu,
  nian, Xiaoqing Ellen Tan, Binh Tang, Ross Tay-                    Chong Ma, Sigang Yu, Haixing Dai, Qiushi Yang,
  lor, Adina Williams, Jian Xiang Kuan, Puxin Xu,                   Yiheng Liu, Songyao Zhang, Enze Shi, Yi Pan, Tuo
  Zheng Yan, Iliyan Zarov, Yuchen Zhang, Angela Fan,                Zhang, Dajiang Zhu, Xiang Li, Xi Jiang, Bao Ge,
  Melanie Kambadur, Sharan Narang, Aurelien Ro-                     Yixuan Yuan, Dinggang Shen, Tianming Liu, and
  driguez, Robert Stojnic, Sergey Edunov, and Thomas                Shu Zhang. 2023c. Review of large vision models
  Scialom. 2023. Llama 2: Open foundation and fine-                 and visual prompt engineering.
  tuned chat models.
                                                                 Jiaqi Wang, Enze Shi, Sigang Yu, Zihao Wu, Chong
Mark Towers, Jordan K. Terry, Ariel Kwiatkowski,                    Ma, Haixing Dai, Qiushi Yang, Yanqing Kang, Jinru
 John U. Balis, Gianluca de Cola, Tristan Deleu,                    Wu, Huawen Hu, Chenxi Yue, Haiyang Zhang, Yi-
 Manuel Goulão, Andreas Kallinteris, Arjun KG,                      heng Liu, Xiang Li, Bao Ge, Dajiang Zhu, Yixuan
 Markus Krimmel, Rodrigo Perez-Vicente, Andrea                      Yuan, Dinggang Shen, Tianming Liu, and Shu Zhang.
 Pierré, Sander Schulhoff, Jun Jet Tai, Andrew Tan Jin              2023d. Prompt engineering for healthcare: Method-
 Shen, and Omar G. Younis. 2023. Gymnasium.                         ologies and applications.

Harsh Trivedi, Niranjan Balasubramanian, Tushar Khot,            Junjie Wang, Yuchao Huang, Chunyang Chen, Zhe Liu,
  and Ashish Sabharwal. 2023. Interleaving retrieval               Song Wang, and Qing Wang. 2023e. Software testing
  with chain-of-thought reasoning for knowledge-                   with large language model: Survey, landscape, and
  intensive multi-step questions. In Proceedings of                vision.


                                                            58
Lei Wang, Wanyu Xu, Yihuai Lan, Zhiqiang Hu,                   Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
  Yunshi Lan, Roy Ka-Wei Lee, and Ee-Peng Lim.                    Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and
  2023f. Plan-and-solve prompting: Improving zero-                Denny Zhou. 2023a. Chain-of-thought prompting
  shot chain-of-thought reasoning by large language               elicits reasoning in large language models.
  models.
                                                               Jerry Wei, Da Huang, Yifeng Lu, Denny Zhou, and
Siyin Wang, Chao-Han Huck Yang, Ji Wu, and Chao                   Quoc V Le. 2023b. Simple synthetic data reduces
  Zhang. 2023g. Can whisper perform speech-based                  sycophancy in large language models. arXiv preprint
  in-context learning.                                            arXiv:2308.03958.

Xinyi Wang, Wanrong Zhu, Michael Saxon, Mark                   Jerry Wei, Jason Wei, Yi Tay, Dustin Tran, Albert
  Steyvers, and William Yang Wang. 2023h. Large                   Webson, Yifeng Lu, Xinyun Chen, Hanxiao Liu,
  language models are latent variable models: Explain-            Da Huang, Denny Zhou, et al. 2023c. Larger
  ing and finding good demonstrations for in-context              language models do in-context learning differently.
  learning.                                                       arXiv preprint arXiv:2303.03846.

                                                               Yixuan Weng, Minjun Zhu, Fei Xia, Bin Li, Shizhu He,
Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le,
                                                                 Shengping Liu, Bin Sun, Kang Liu, and Jun Zhao.
  Ed Chi, Sharan Narang, Aakanksha Chowdhery, and
                                                                 2022. Large language models are better reasoners
  Denny Zhou. 2022. Self-consistency improves chain
                                                                 with self-verification.
  of thought reasoning in language models.
                                                               Jason Weston and Sainbayar Sukhbaatar. 2023. System
Yaqing Wang, Jiepu Jiang, Mingyang Zhang, Cheng                   2 attention (is something you might need too).
  Li, Yi Liang, Qiaozhu Mei, and Michael Bender-
  sky. 2023i. Automated evaluation of personalized             Jules White, Quchen Fu, Sam Hays, Michael Sandborn,
  text generation using large language models. arXiv              Carlos Olea, Henry Gilbert, Ashraf Elnashar, Jesse
  preprint arXiv:2310.11593.                                      Spencer-Smith, and Douglas C. Schmidt. 2023. A
                                                                  prompt pattern catalog to enhance prompt engineer-
Yaqing Wang, Quanming Yao, James Kwok, and Li-                    ing with chatgpt.
  onel M. Ni. 2019. Generalizing from a few examples:
  A survey on few-shot learning.                               Alex Wilf, Sihyun Shawn Lee, Paul Pu Liang, and Louis-
                                                                 Philippe Morency. 2023. Think twice: Perspective-
Yuqing Wang and Yun Zhao. 2024. Metacognitive                    taking improves large language models’ theory-of-
  prompting improves understanding in large language             mind capabilities.
  models.
                                                               Simon Willison. 2022. Prompt injection attacks against
Zekun Moore Wang, Zhongyuan Peng, Haoran Que,                    gpt-3.
  Jiaheng Liu, Wangchunshu Zhou, Yuhan Wu,
  Hongcheng Guo, Ruitong Gan, Zehao Ni, Man                    Simon Willison. 2024. Prompt injection and jailbreak-
  Zhang, Zhaoxiang Zhang, Wanli Ouyang, Ke Xu,                   ing are not the same thing.
  Wenhu Chen, Jie Fu, and Junran Peng. 2023j.
  Rolellm: Benchmarking, eliciting, and enhancing              Genta Indra Winata, Liang-Kang Huang, Soumya Vad-
  role-playing abilities of large language models.               lamannati, and Yash Chandarana. 2023. Multilingual
                                                                 few-shot learning via language model retrieval.
Zhendong Wang, Yifan Jiang, Yadong Lu, Yelong Shen,
                                                               Jay Zhangjie Wu, Yixiao Ge, Xintao Wang, Weixian
  Pengcheng He, Weizhu Chen, Zhangyang Wang, and
                                                                 Lei, Yuchao Gu, Yufei Shi, Wynne Hsu, Ying Shan,
  Mingyuan Zhou. 2023k. In-context learning un-
                                                                 Xiaohu Qie, and Mike Zheng Shou. 2023a. Tune-a-
  locked for diffusion models.
                                                                 video: One-shot tuning of image diffusion models
                                                                 for text-to-video generation.
Zhenhailong Wang, Shaoguang Mao, Wenshan Wu, Tao
  Ge, Furu Wei, and Heng Ji. 2023l. Unleashing cogni-          Ning Wu, Ming Gong, Linjun Shou, Shining Liang,
  tive synergy in large language models: A task-solving          and Daxin Jiang. 2023b. Large language models are
  agent through multi-persona self-collaboration.                diverse role-players for summarization evaluation.
                                                                 arXiv preprint arXiv:2303.15078.
Jason Wei, Maarten Bosma, Vincent Zhao, Kelvin Guu,
   Adams Wei Yu, Brian Lester, Nan Du, Andrew M.               Tongshuang Wu, Michael Terry, and Carrie Jun Cai.
   Dai, and Quoc V Le. 2022a. Finetuned language                 2022. Ai chains: Transparent and controllable
   models are zero-shot learners. In International Con-          human-ai interaction by chaining large language
   ference on Learning Representations.                          model prompts. CHI Conference on Human Factors
                                                                 in Computing Systems.
Jason Wei, Xuezhi Wang, Dale Schuurmans, Maarten
   Bosma, Brian Ichter, Fei Xia, Ed Chi, Quoc Le, and          Xiaodong Wu, Ran Duan, and Jianbing Ni. 2023c. Un-
   Denny Zhou. 2022b. Chain-of-thought prompting                 veiling security, privacy, and ethical concerns of chat-
   elicits reasoning in large language models.                   gpt. Journal of Information and Intelligence.


                                                          59
Congying Xia, Chen Xing, Jiangshu Du, Xinyi Yang,              Yao Yao, Zuchao Li, and Hai Zhao. 2023c. Beyond
  Yihao Feng, Ran Xu, Wenpeng Yin, and Caiming                   chain-of-thought, effective graph-of-thought reason-
  Xiong. 2024. Fofo: A benchmark to evaluate llms’               ing in large language models.
  format-following capability.
                                                               Michihiro Yasunaga, Xinyun Chen, Yujia Li, Panupong
Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie                Pasupat, Jure Leskovec, Percy Liang, Ed H. Chi,
  Fu, Junxian He, and Bryan Hooi. 2023a. Can llms                and Denny Zhou. 2023. Large language models as
  express their uncertainty? an empirical evaluation             analogical reasoners.
  of confidence elicitation in llms. arXiv preprint
  arXiv:2306.13063.                                            Qinyuan Ye, Maxamed Axmed, Reid Pryzant, and
                                                                 Fereshte Khani. 2023. Prompt engineering a prompt
Miao Xiong, Zhiyuan Hu, Xinyang Lu, Yifei Li, Jie                engineer.
  Fu, Junxian He, and Bryan Hooi. 2023b. Can llms
  express their uncertainty? an empirical evaluation           Xi Ye and Greg Durrett. 2023. Explanation selection
  of confidence elicitation in llms. arXiv preprint              using unlabeled data for chain-of-thought prompting.
  arXiv:2306.13063.

Xiaohan Xu, Chongyang Tao, Tao Shen, Can Xu,                   Kang Min Yoo, Junyeob Kim, Hyuhng Joon Kim, Hyun-
  Hongbo Xu, Guodong Long, and Jian guang Lou.                   soo Cho, Hwiyeol Jo, Sang-Woo Lee, Sang goo Lee,
  2023. Re-reading improves reasoning in language                and Taeuk Kim. 2022. Ground-truth labels matter: A
  models.                                                        deeper look into input-label demonstrations.

Tianci Xue, Ziqi Wang, Zhenhailong Wang, Chi Han,              Ori Yoran, Tomer Wolfson, Ben Bogin, Uri Katz, Daniel
  Pengfei Yu, and Heng Ji. 2023. Rcot: Detecting                 Deutch, and Jonathan Berant. 2023. Answering
  and rectifying factual inconsistency in reasoning by           questions by meta-reasoning over multiple chains
  reversing chain-of-thought.                                    of thought.

Chengrun Yang, Xuezhi Wang, Yifeng Lu, Hanxiao Liu,            Adeel Yousaf, Muzammal Naseer, Salman Khan, Fa-
  Quoc V. Le, Denny Zhou, and Xinyun Chen. 2023a.                had Shahbaz Khan, and Mubarak Shah. 2023. Video-
  Large language models as optimizers.                           prompter: an ensemble of foundational models for
                                                                 zero-shot video understanding.
Haibo Yang, Yang Chen, Yingwei Pan, Ting Yao, Zhi-
  neng Chen, and Tao Mei. 2023b. 3dstyle-diffusion:            Yue Yu, Yuchen Zhuang, Jieyu Zhang, Yu Meng,
  Pursuing fine-grained text-driven 3d stylization with          Alexander Ratner, Ranjay Krishna, Jiaming Shen,
  2d diffusion models.                                           and Chao Zhang. 2023. Large language model as
                                                                 attributed training data generator: A tale of diversity
Hui Yang, Sifu Yue, and Yunzhong He. 2023c. Auto-                and bias. arXiv preprint arXiv:2306.15895.
  gpt for online decision making: Benchmarks and
  additional opinions.                                         Xiang Yue, Boshi Wang, Kai Zhang, Ziru Chen, Yu Su,
                                                                 and Huan Sun. 2023. Automatic evaluation of at-
Xinyi Yang, Runzhe Zhan, Derek F. Wong, Junchao                  tribution by large language models. arXiv preprint
  Wu, and Lidia S. Chao. 2023d. Human-in-the-loop                arXiv:2305.06311.
  machine translation with large language model. In
  Proceedings of Machine Translation Summit XIX Vol.           Zhiyuan Zeng, Jiatong Yu, Tianyu Gao, Yu Meng, Tanya
  2: Users Track, pages 88–98, Macau SAR, China.                 Goyal, and Danqi Chen. 2023. Evaluating large
  Machine Translation Summit.                                    language models at evaluating instruction following.
                                                                 arXiv preprint arXiv:2310.07641.
Zhengyuan Yang, Linjie Li, Kevin Lin, Jianfeng Wang,
  Chung-Ching Lin, Zicheng Liu, and Lijuan Wang.
                                                               Michael JQ Zhang and Eunsol Choi. 2023. Clarify when
  2023e. The dawn of lmms: Preliminary explorations
                                                                 necessary: Resolving ambiguity through interaction
  with gpt-4v(ision). ArXiv, abs/2309.17421.
                                                                 with lms. arXiv preprint arXiv:2311.09469.
Binwei Yao, Ming Jiang, Diyi Yang, and Junjie Hu.
  2023a. Empowering llm-based machine translation              Quanjun Zhang, Tongke Zhang, Juan Zhai, Chunrong
  with cultural awareness.                                       Fang, Bowen Yu, Weisong Sun, and Zhenyu Chen.
                                                                 2023a. A critical review of large language model on
Shunyu Yao, Dian Yu, Jeffrey Zhao, Izhak Shafran,                software engineering: An example from chatgpt and
  Thomas L. Griffiths, Yuan Cao, and Karthik                     automated program repair.
  Narasimhan. 2023b. Tree of thoughts: Deliberate
  problem solving with large language models.                  Yifan Zhang, Jingqin Yang, Yang Yuan, and Andrew
                                                                 Chi-Chih Yao. 2023b. Cumulative reasoning with
Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak                 large language models.
  Shafran, Karthik Narasimhan, and Yuan Cao. 2022.
  React: Synergizing reasoning and acting in language          Yiming Zhang, Shi Feng, and Chenhao Tan. 2022a. Ac-
  models.                                                        tive example selection for in-context learning.


                                                          60
Zhuosheng Zhang, Yao Yao, Aston Zhang, Xiangru                     Denny Zhou, Nathanael Schärli, Le Hou, Jason Wei,
  Tang, Xinbei Ma, Zhiwei He, Yiming Wang, Mark                      Nathan Scales, Xuezhi Wang, Dale Schuurmans,
  Gerstein, Rui Wang, Gongshen Liu, and Hai Zhao.                    Claire Cui, Olivier Bousquet, Quoc Le, et al. 2022a.
  2023c. Igniting language intelligence: The hitch-                  Least-to-most prompting enables complex reason-
  hiker’s guide from chain-of-thought reasoning to lan-              ing in large language models. arXiv preprint
  guage agents.                                                      arXiv:2205.10625.

Zhuosheng Zhang, Aston Zhang, Mu Li, and Alex                      Yongchao Zhou, Andrei Ioan Muresanu, Ziwen Han,
  Smola. 2022b. Automatic chain of thought prompt-                   Keiran Paster, Silviu Pitis, Harris Chan, and Jimmy
  ing in large language models.                                      Ba. 2022b. Large language models are human-level
                                                                     prompt engineers.
Zhuosheng Zhang, Aston Zhang, Mu Li, Hai Zhao,
                                                                   Yucheng Zhou, Xiubo Geng, Tao Shen, Chongyang Tao,
  George Karypis, and Alex Smola. 2023d. Multi-
                                                                     Guodong Long, Jian-Guang Lou, and Jianbing Shen.
  modal chain-of-thought reasoning in language mod-
                                                                     2023. Thread of thought unraveling chaotic contexts.
  els.
                                                                   Xizhou Zhu, Yuntao Chen, Hao Tian, Chenxin Tao, Wei-
Ruochen Zhao, Xingxuan Li, Shafiq Joty, Chengwei                     jie Su, Chenyu Yang, Gao Huang, Bin Li, Lewei Lu,
  Qin, and Lidong Bing. 2023a. Verify-and-edit: A                    Xiaogang Wang, Yu Qiao, Zhaoxiang Zhang, and
  knowledge-enhanced chain-of-thought framework.                     Jifeng Dai. 2023. Ghost in the minecraft: Gener-
  In Proceedings of the 61st Annual Meeting of the                   ally capable agents for open-world environments via
  Association for Computational Linguistics (Volume                  large language models with text-based knowledge
  1: Long Papers), pages 5823–5840, Toronto, Canada.                 and memory.
  Association for Computational Linguistics.
                                                                   Zhichao Zuo, Zhao Zhang, Yan Luo, Yang Zhao, Haijun
Tony Z. Zhao, Eric Wallace, Shi Feng, Dan Klein, and                 Zhang, Yi Yang, and Meng Wang. 2023. Cut-and-
  Sameer Singh. 2021a. Calibrate before use: Improv-                 paste: Subject-driven video editing with attention
  ing few-shot performance of language models.                       control.

Yilun Zhao, Haowei Zhang, Shengyun Si, Linyong Nan,
  Xiangru Tang, and Arman Cohan. 2023b. Large lan-
   guage models are effective table-to-text generators,
   evaluators, and feedback providers. arXiv preprint
   arXiv:2305.14987.

Yuyang Zhao, Zhiwen Yan, Enze Xie, Lanqing Hong,
  Zhenguo Li, and Gim Hee Lee. 2023c. Animate124:
  Animating one image to 4d dynamic scene.

Zihao Zhao, Eric Wallace, Shi Feng, Dan Klein, and
  Sameer Singh. 2021b. Calibrate before use: Im-
  proving few-shot performance of language models.
  In International Conference on Machine Learning,
  pages 12697–12706. PMLR.

Chujie Zheng, Hao Zhou, Fandong Meng, Jie Zhou, and
  Minlie Huang. 2023a. On large language models’ se-
  lection bias in multi-choice questions. arXiv preprint
  arXiv:2309.03882.

Ge Zheng, Bin Yang, Jiajin Tang, Hong-Yu Zhou, and
  Sibei Yang. 2023b. Ddcot: Duty-distinct chain-of-
  thought prompting for multimodal reasoning in lan-
  guage models.

Huaixiu Steven Zheng, Swaroop Mishra, Xinyun Chen,
  Heng-Tze Cheng, Ed H. Chi, Quoc V Le, and Denny
  Zhou. 2023c. Take a step back: Evoking reasoning
  via abstraction in large language models.

Mingqian Zheng, Jiaxin Pei, and David Jurgens. 2023d.
  Is "a helpful assistant" the best role for large language
  models? a systematic evaluation of social roles in
  system prompts.


                                                              61
A       Appendices

A.1   Definitions of Prompting

 Reference        Prompt                                        Prompt Engineering
 (Meskó,                                                        The practice of designing, refining, and
 2023)                                                          implementing prompts or instructions that
                                                                guide the output of LLMs to help in vari-
                                                                ous tasks. It is essentially the practice of
                                                                effectively interacting with AI systems to
                                                                optimize their benefits.
 (Chen et al.,    the input of the model                        the process of structuring input text for
 2023a)                                                         LLMs and is a technique integral to opti-
                                                                mizing the efficacy of LLMs
 (Santu and       refers to a textual input provided to the involves crafting and revising the query
 Feng, 2023)      LLMs with the intention of guiding its or context in such a way that it elicits the
                  output toward a specific task                 desired response or behavior from LLMs
 (Wang et al.,                                                  involves designing effective prompts to
 2023d)                                                         guide the pre-trained language model in
                                                                downstream tasks.
 (Wang et al.,                                                  the process of designing prompts that en-
 2023c)                                                         able the model to adapt and generalize to
                                                                different tasks. downstream tasks.
 (Hou et al.,     manually predefined natural language in- the careful design of specialized prompts
 2023)            structions
 (Wang et al.,    input of the LLMs                             communicate with LLMs to steer its be-
 2023e)                                                         havior for desired outcomes
 (White et al.,   Instructions given to an LLM to enforce an increasingly important skill set needed
 2023)            rules, automate processes, and ensure spe- to converse effectively with large lan-
                  cific qualities (and quantities) of generated guage models (LLMs), such as ChatGPT
                  output. Prompts are also a form of pro- the means by which LLMs are pro-
                  gramming that can customize the outputs grammed via prompts
                  and interactions with an LLM.
              A prompt is a set of instructions provided
              to an LLM that programs the LLM by cus-
              tomizing it and/or en- hancing or refining
              its capabilities
 (Heston and the input                                   structuring the input in a specialized man-
 Khun, 2023)                                             ner
 (Liu et al.,                                            choosing a proper prompt
 2023b)                                                  the process of creating a prompting func-
                                                                tion fprompt (x) that results in the most
                                                                effective performance on the downstream
                                                                task.




                                                     62
(Hadi et al.,     the instructions provided to an LLM to refers to the designing and wording of
2023)             make it follow specified rules, automation prompts given to LLMs so as to get a de-
                  of processes and to ensure that the out- sired response from them.
                  put generated is of a specific quality or
                  quantity
(Neagu,                                                      entails various strate- gies, including ex-
2023)                                                        plicit instruction, and implicit context [21].
                                                             Explicit instruction involves providing ex-
                                                             plicit guidance or constraints to the model
                                                             through instructions, examples, or speci-
                                                             fications. Implicit context leverages the
                                                             model’s under- standing of the preceding
                                                             context to influence its response
(Dang et al.,                                                the systematic practice of constructing
2022)                                                        prompts to improve the generated output
                                                             of a generative model

                Table A.1: Definitions of Prompt and Prompt Engineering from different papers.




                                                      63
A.2     Extended Vocabulary
A.2.1   Prompting Terms
Context Window The context window is the space of tokens (for LLMs) which the model can process.
It has a maximal length (the context length).
Priming (Schulhoff, 2022) refers to giving a model an initial prompt that lays out certain instructions
for the rest of a conversation. This priming prompt might contains a role or other instructions on how to
interact with the user. Priming can either be done in the system or user prompt (see below).

A.2.2   Prompt Engineering Terms
Conversational Prompt Engineering is Prompt Engineering in colloquio. That is, during the course of a
conversation with a GenAI, a user may ask the GenAI to refine its output. In contrast, prompt engineering
is often done by sending the GenAI a completely new prompt rather than continuing a conversation.

A.2.3   Fine-Tuning Terms
Prompt-Based Learning (Liu et al., 2023b), also known as Prompt Learning (Liu et al., 2023b; Wang
et al., 2023d) refers to the process of using prompting-related techniques. It often is used in the context of
fine-tuning, especially fine-tuning prompts. Due to conflicting usage, we do not use this term.
Prompt Tuning (Lester et al., 2021) refers to directly optimizing the weights of the prompt itself,
usually through some form of gradient-based updates. It has also been referred to has Prompt Fine-Tuning.
It should not be used to refer to discrete prompt engineering.

A.2.4   Orthogonal Prompt Types
We now discuss terminology for high-level ways of classifying prompts.
A.2.4.1 Originator
User Prompt This is the type of prompt that comes from the user. This is the most common form of
prompting and is how prompts are usually delivered in consumer applications.
Assistant Prompt This "prompt" is simply the output of the LLM itself. It can be considered a prompt
(or part of one) when it is fed back into the model, for example as part of a conversation history with a
user.
System Prompt This prompt is used to give LLMs high level instructions for interacting with users. Not
all models have this.
A.2.4.2 Hard vs Soft Prompts
Hard (discrete) Prompt These prompts only contain tokens that directly correspond to words in the
LLM vocabulary.
Soft (continuous) Prompt These prompts contain tokens that may not correspond to any word in the
vocabulary (Lester et al., 2021; Wang et al., 2023c). Soft prompts can be used when fine-tuning is desired,
but modifying the weights of the full model is prohibitively expensive. Thus, a frozen model can be used
while allowing gradients to flow through the prompt tokens.

                                      Hard Prompts ⊆ Soft Prompts
A.2.4.3 Prediction Styles
In LLMs, a prediction style is the format in which it predicts the next token. There are two common
formats for this in prompting research. We do not discuss non-text prediction styles.
Cloze In Cloze prompts, the token(s) to be predicted are presented as "slots to fill", usually somewhere
in the middle of the prompt (Liu et al., 2023b). This is usually the case for earlier transformer models
such as BERT (Chu and Lin, 2023).

                                                     64
Prefix In Prefix prompts, the token to be predicted is at the end of the prompt (Liu et al., 2023b). This is
usually the case with modern GPT-style models (Radford et al., 2019b).




                                                    65
A.3     Datasheet

We present a datasheet (Gebru et al., 2021) with more information about the associated paper dataset,
which is hosted on HuggingFace.

A.3.1   Motivation
For what purpose was the dataset created? Was there a specific task in mind? Was there a specific
gap that needed to be filled? Please provide a description.
This dataset was created to gather existing literature on prompt engineering in order to analyze all current
hard prefix prompting techniques.
   Who created the dataset (e.g., which team, research group) and on behalf of which entity (e.g.,
company, institution, organization)?
This research was associated with the University of Maryland, Learn Prompting, and sponsored by
OpenAI, but not created on the behalf of any particular organization.
   Who funded the creation of the dataset? If there is an associated grant, please provide the name
of the grantor and the grant name and number.
OpenAI contributed $10,000 in credits for their API.

A.3.2   Composition
What do the instances that comprise the dataset represent (e.g., documents, photos, people, coun-
tries)? Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions
between them; nodes and edges)? Please provide a description.
The dataset contains 1,565 research papers in PDF format. Any duplicate papers were removed automati-
cally, though some could exist.
   What data does each instance consist of? “Raw” data (e.g., unprocessed text or images) or
features? In either case, please provide a description.
Each data instance is a research paper as a PDF.
   Is there a label or target associated with each instance? If so, please provide a description.
No
   Is any information missing from individual instances? If so, please provide a description, ex-
plaining why this information is missing (e.g., because it was unavailable). This does not include
intentionally removed information, but might include, e.g., redacted text.
No.
   Are there any errors, sources of noise, or redundancies in the dataset? If so, please provide a
description.
The papers were gathered in a semi-automated process which introduced the possibility of irrelevant
papers being collected and relevant papers not being collected. There were manual reviews done for both
possible errors to mitigate these errors.
   Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g.,
websites, tweets, other datasets)?
It is self-contained.
   Does the dataset contain data that might be considered confidential (e.g., data that is protected by
legal privilege or by doctor–patient confidentiality, data that includes the content of individuals’
non-public communications)? If so, please provide a description.
No.
   Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening,
or might otherwise cause anxiety? If so, please describe why.
The dataset contains some papers on prompt injection. These papers may contain offensive content
including racism and sexism.

                                                    66
A.3.3   Collection Process
How was the data associated with each instance acquired?
The dataset was compiled from Arxiv, Semantic Scholar, and ACL.
  What mechanisms or procedures were used to collect the data?
We wrote scripts to automatically query the APIs of Arxiv and Semantic Scholar.
  Over what timeframe was the data collected?
The dataset was curated the duration of the research paper, primarily in February of 2024.
  Were any ethical review processes conducted?
No.

A.3.4   Preprocessing/ Cleaning/ Labeling
Was any preprocessing/cleaning/labeling of the data done?
After collecting data from different sources, we removed duplicate papers and did a manual and semi-
automated review of papers to ensure they were all relevant.
   Was the “raw” data saved in addition to the preprocessed/cleaned/labeled data?
No, we do not anticipate the use of our preprocessed data. However, raw data can be recovered from the
links we store.
   Is the software that was used to preprocess/clean/label the data available?
It is contained within our code repository on Github.

A.3.5   Uses
Has the dataset been used for any tasks already?
No.
   Is there a repository that links to any or all papers or systems that use the dataset?
Yes.
   Is there anything about the composition of the dataset or the way it was collected and prepro-
cessed/cleaned/labeled that might impact future uses?
All of the papers we collected were written in English. It is possible some papers were not included due to
a translation not being available.
   Are there tasks for which the dataset should not be used?
No.

A.3.6   Distribution
Will the dataset be distributed to third parties outside of the entity on behalf of which the dataset
was created?
No.

A.3.7   Maintenance
Who will be supporting/hosting/maintaining the dataset?
Our team will continue maintenance.
  How can the owner/curator/manager of the dataset be contacted?
Please email us at sanderschulhoff@gmail.com
  Is there an erratum?
No.
  If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for
them to do so?
Yes, anyone is free to use/modify the data.




                                                    67
A.4   Keywords
Here are the keywords we used for search.

  • jailbreak prompt

  • prompt an llm

  • prompt a large language model

  • prompt injection

  • prompt optimization

  • prompt engineering

  • few-shot learning

  • few shot learning

  • prompt-based methods

  • prompt based methods

  • prompting-based methods

  • prompting based methods

  • few-shot prompt

  • few shot prompt

  • one-shot prompt

  • one shot prompt

  • few-shot prompting

  • few shot prompting

  • one-shot prompting

  • one shot prompting

  • prompting techniques

  • prompt engineering techniques

  • llm prompting

  • large language model prompting

  • 0-shot prompt

  • 0 shot prompt

  • zero-shot prompt

  • many-shot prompt

  • zero-shot prompting

  • many-shot prompting

                                            68
• in-context learning

• in context learning

• transformer model prompts

• prompt-based transfer learning

• nlp prompting strategies

• llm interpretability via prompts

• curriculum learning with prompts

• feedback loops in llm prompting

• human-in-the-loop prompting

• token-efficient prompting

• multimodal prompting

• instruction prompting

• prompt templating

• prompt template




                                     69
A.5    Prompt for Systematic Literature Review
Please find the prompt we used here. We present it in text in this document, but note that you should use
the version in our codebase rather than copy and paste this.
We used the following system prompt:
You are a lab assistant, helping with a systematic review on prompt engineering. You’ve been asked to
rate the relevance of a paper to the topic of prompt engineering. To be clear, this review will strictly cover
hard prefix prompts. For clarification: Hard prompts have tokens that correspond directly to words in
the vocab. For example, you could make up a new token by adding two together. This would no longer
correspond to any word in the vocabulary, and would be a soft prompt Prefix prompts are prompts used
for most modern transformers, where the model predicts the words after this prompt. In earlier models,
such as BERT, models could predict words (e.g. <MASK>) in the middle of the prompt. Your job is to be
able to tell whether a paper is related to (or simply contains) hard prefix prompting or prompt engineering.
Please note that a paper might not spell out that it is using "hard prefix" prompting and so it might just say
prompting. In this case, you should still rate it as relevant to the topic of prompt engineering. Please also
note, that a paper that focuses on training a model as opposed to post-training prompting techniques is
considered irrelevant. Provide a response in JSON format with two fields: ’reasoning’ (a single sentence
that justifies your reasoning) and ’rating’ (a string that is one of the following categories: ’highly relevant’,
’somewhat relevant’, ’neutrally relevant’, ’somewhat irrelevant’, ’highly irrelevant’) indicating relevance
to the topic of prompt engineering)
Then, we used this user prompt template to input information for each paper:
Title: ’{title}’, Abstract: ’{abstract}’. Rate its relevance to the topic of prompt engineering as one of the
following categories: ’highly relevant’, ’somewhat relevant’, ’neutrally relevant’, ’somewhat irrelevant’,
’highly irrelevant’, and provide text from the abstract that justifies your reasoning




                                                       70
A.6      Evaluation Table

                                                                                       P ROMPT
  ID                           M ODEL                                                                      O UTPUT S PACE                      T YPE R ES . BATCH
                                                                             Roles CoT Definition Few-Shot
  (Kocmi and Federmann, 2023b) GPT-family                                                                 DA, sMQM, stars, classes               E     S
  (Lu et al., 2023c)           Dav3, GPT-4-Turbo, GPT-4                            ✓      ✓         ✓     Error Span → Score                     E     S     ✓
  (Fernandes et al., 2023)     PaLM                                                ✓      ✓         ✓     Error Span                             I     S
  (Kocmi and Federmann, 2023a) GPT-4                                               ✓      ✓         ✓     Error Span                             I     S     ✓
  (Araújo and Aguiar, 2023)    ChatGPT                                                    ✓               Likert [1-5]                           E     S     ✓
  (Wang et al., 2023b)         ChatGPT                                                    ✓               DA, stars                              E     S
  (Liu et al., 2023d)†         GPT-3.5, GPT-4                                             ✓               Likert [1-10]                          I     M
  (Chan et al., 2024)          ChatGPT, GPT-4                                 ✓    ✓                      Likert [1-10]                          I     M
  (Luo et al., 2023)           ChatGPT                                             ✓      ✓               yes/no;A/B; Likert [1-10]              E     S
  (Hada et al., 2024)          GPT-4-32K                                                  ✓         ✓     [0,1,2] or binary                      E     S     ✓
  (Fu et al., 2023a)           GPT-3, OPT, FLAN-T5, GPT-2                                                 Probability                            I     S
  (Gao et al., 2023c)          ChatGPT                                                    ✓               Likert [1-5], Pairwise, Pyramid, 0/1   E     S
  (Chen et al., 2023g)         ChatGPT                                                                    Likert [1-10]; yes/no; pairwise: A/B/C E & I S
  (He et al., 2023a)           GPT-4                                                      ✓               Likert [1-5]                           E     S
  (Sottana et al., 2023)       GPT-4                                                      ✓               Likert [1-5]                           E     S
  (Chen et al., 2023c)         GPT, Flan-T5                                        ✓                      Yes/No                                 E     S
  (Zhao et al., 2023b)         GPT-3.5, GPT-4                                      ✓                ✓     true/false                             E     S
  (Wu et al., 2023b)           GPT-3                                          ✓                           pairwise voting                        E     M     ✓
  (Wang et al., 2023i)         PaLM 2-IT-L                                                                A/B                                    E     M
  (Jia et al., 2023)           LLaMa7b                                                                    Probability                            I     S
  (Yue et al., 2023)           ChatGPT, Alpaca, Vicuna, GPT-4                             ✓         ✓     Yes/No                                 E     S
  (Li et al., 2023e)           GPT-3.5, GPT-4, Bard, Vicuna                        ✓                      Pairwise                               I     M
  (Liu et al., 2023f)          ChatGPT, Vicuna, chatGLM, StableLM                         ✓               continuous [0-1]                       E     S
  (Bai et al., 2023b)          GPT-4, Claude, ChatGPT, Bard, Vicuna                       ✓               Likert [1-5]                           E     S
  (Dubois et al., 2023)        GPT-4, ChatGPT, Dav3                                       ✓         ✓     pairwise                               E     M     ✓
  (Liu et al., 2023h)†         GPT-4-32K                                                  ✓               Likert [1-5]                           E     S
  (Wang et al., 2023h)         GPT-4-Turbo, ChatGPT, GPT-4, Vicuna                 ✓                      Likert [1-10]                          E     M
  (Zeng et al., 2023)          GPT-4, ChatGPT, LLaMA-2-Chat, PaLM2, Falcon    ✓    ✓                ✓     Pairwise                               E     S
  (Zheng et al., 2023b)        Claude-v1, GPT-3.5, GPT-4                           ✓                ✓     Pairwise/Likert [1-10]                 E     S/M
  (Lin and Chen, 2023)         Claude-v1.3                                                                Likert [0-5], Likert [0-100]           E     S     ✓


Table A.2: Evaluation Paper Summary. E: Explicit (whether the model generates an assessment), I: Implicit (whether
an assessment is derived from the model output); Response (Res.) S: Single response, M: Multiple responses; †:
Model generated instruction;




                                                                             71
A.7     Entrapment Prompting Process
This section contains the thought process of our prompt engineer as he developed the prompt.

A.7.1   Exploration
   • First did a bit of dataset exploration, looking at length/label distribution, then chose entrapment to
     start with.

   • Checked if gpt-1106-preview understood entrapment, by asking it to define the term WRT SCS. It
     did not.

A.7.2   Getting a Label
   • Showed it the definition of entrapment in the system prompt and asked it to label a data point, but it
     responded saying I should seek mental health support.

   • I put the instructions in the user prompt, but get a similar response.

   • Appending "Is this entrapment? Yes or no" got it to actually respond with a label.

   • I gave it a reject example, but it labeled it as accept, and also sometimes gives emotional responses
     about getting help.

   • Using 10-shot prompting, it still gives the get help responses.

   • I tried removing the definition, got the same problem. It seems that it doesn’t like "accept"/"reject"
     as labels.

   • I added back the definition, changed labels to entrapment/not entrapment, it often says "not enough
     info to determine".

   • I switched to GPT-4-32K, which gave one word responses and correctly predicted a reject and an
     accept datapoint.

A.7.3   Varying Prompting Techniques
   • Tested 0-shot with context.

   • 10-shot with context, showed improvement.

   • Taking first failing instance into playground. (12th in train file)

   • Tried doing ’A: Let’s go step by step and figure this out: ", output "A: Yes"

   • Did "A: Let’s go step by step and figure this out: ", OUTPUT:

         The individual in this post is expressing feelings of hopelessness, loneliness, and despair.
         They mention a significant loss (their mother) and a subsequent decline in their mental health,
         turning to alcohol as a coping mechanism. They also mention financial struggles and the
         possibility of becoming homeless. They express feelings of guilt and shame about their
         situation and compare themselves negatively to their friends and family. Most concerning
         is their detailed plan for suicide, involving sleeping pills and alcohol. They also mention
         considering stepping in front of a car. Given these factors, the label for this post would be
         "Yes" for expressing feelings of entrapment.


                                                     72
• "A: Before predicting a label, let’s go step by step and write out your thought process. Use the items
  in the definition of entrapment to support your conclusion.", OUTPUT:

     Before predicting a label, let’s go step by step and write out your thought process. Use the
     items in the definition of entrapment to support your conclusion.


• Began discussing with the AI "they don’t ever say they feel trapped or that there is no way out, how
  did u get that idea?", OUTPUT:

     The individual doesn’t explicitly state that they feel trapped or that there is no way out, but
     their narrative suggests a sense of entrapment. They mention that they are facing eviction,
     struggling with debt, and dealing with a decrease in income. They also express a sense of
     hopelessness and despair, and contemplate suicide as a potential solution to their problems.
     These elements suggest a feeling of being trapped in their current circumstances with no
     apparent way out. However, it’s important to note that this interpretation is based on the
     information provided in the post and the individual’s expressed feelings and thoughts.


• Asked it to help reformulate instructions to make explicitness more clearly needed, still predicts
  entrapment.

• Added "ENTRAPMENT MUST BE EXPLICIT, NOT IMPLICIT." to instruction at top after defini-
  tions (no CoT inducer)

• Also tried with previous CoT inducer, still says entrapment in a hard to parse out way.

• Added "If the person does not explicitly say they feel trapped, this doesn’t count as entrapment." (no
  CoT), still entrapment.

• Talking to AI, it thinks "Today I found out I have 10 days to vacate my apartment or I’ll be formally
  evicted. I’m 2 months behind on my rent due to a bad time where I got demoted at work and rent
  from making roughly $1000 ever 2 weeks to around $450. If I get evicted, I’ll probably be homeless"
  is feeling trapped/stuck.

• Tried "Before stating a label, write out reasoning using the grid above about why this may/may not
  be entrapment:", still thinks entrapment.

• paste in email: [REDACTED] above definition of entrapment

• remove shots, says "Entrapment"

• add this after def: IMPORTANT: Only label the post as entrapment if they explicitly say that they
  feel trapped., says "Yes"

• In the prompt, gave it CoT reasoning. (18.txt), and tried with the next wrongly labeled one (15), (full
  prompt, 19.txt)

• Tested this on everything except first 20, did pretty well

• Tried removing email, performance dropped of a cliff

• At this point, I am thinking that giving examples with reasoning helps (obviously)

• Tried to add 10 shots in for free, before the last one with reasoning, bad results

                                                 73
A.7.3.1 AutoCoT
  • Develop dataset using this prompt (22.txt). Then ask it "Why?". If it disagrees, I say "It is actually
     not entrapment, please explain why." (accidentally duplicated email 23.txt)

   • Just for fun, tried 0 shot full context (had to adjust verbalizer)

   • tried this with special verbalizer which catches "This post does not meet the criteria for Entrapment."

   • Tested my generated data, beat 0.5 F1

   • Doing 10 more exemplars w autocot. Sometimes responds immediately with reasoning like "This
     post does not meet the criteria for Entrapment as the individual does not explicitly express feelings
     of being trapped or hopeless.", so just use that if so. Sometimes get refusal "I’m really sorry to hear
     that you’re feeling this way, but I’m unable to provide the help that you need. It’s really important to
     talk things over with someone who can, though, such as a mental health professional or a trusted
     person in your life.", just ask "Explain why it is not entrapment." after if so.

   • performance didnt really improve, realized about 11% are getting -1, meaning not extracted properly.
     Retrying with full words "Question" instead of Q, also for reasoning and answer.

   • this led to higher inability to parse, at about 16%.

A.7.3.2 Developing Answer Extraction
  • put first failing to parse one in (22), and developed a prompt for it.

   • did worse:      (0.42857142857142855,                 0.5051546391752577,       0.8571428571428571,
     0.2857142857142857)

   • only using extracted label if have -1 helps slightly to (0.48, 0.61, 0.8571428571428571,
     0.3333333333333333)

   • going back to best performing prompt–10 QRA shot, and performing extraction with any -1s, doesnt
     help other than gently boosting accuracy, perhaps when it doesnt answer

A.7.3.3 Iterating on Email
  • tried best perf, with no email

   • tried with deduped email, worse results

   • noticed that ones its unsure about often contained 1 labels that should be 0, so trying to "recover"
     these doesnt help

   • try moving around exemplar order, performing extraction, didnt help

   • triplicated email, didnt help




                                                      74
A.8   Formally Defining a Prompt
"Prompt" is a widely used term, but uses and definitions differ widely across research. As a result, it
is difficult to create a formal, mathematical definition for a prompt. In this section, we outline some
formalisms for prompt engineering.
As a conditioning Mechanism. Qiao et al. (2022) present the following definition, which involves the
prompt T and a question Q as conditioning mechanisms on predicting the next token. Note that they
appear to use Brown et al. (2020)’s original definition of prompt, which refers to the non-question part of
the prompt (e.g. few-shot exemplars, instructions).


                                                  |A|
                                                  Y
                               p(A | T , Q) =           pLM (ai | T , Q, a1:i−1 )                    (A.1)
                                                  i=1

  Here, the prompt and question condition the pre-trained LLM pLM . The a1:i−1 are previously generated
answer tokens and A a complete answer.
Templating. The above formalization does not include the notion of maximizing a scoring or utility
function (e.g. accuracy on a dataset), which prompts are often designed to do. Additionally, prompt
engineers often seek to design prompt template rather than prompts. Here, we reformulate eq. (A.1) to
include the prompt template:


                                                  |A|
                              p(A | T (x∗ )) =          pLM (ai | T (x∗ ), a1:i−1 )
                                                  Y
                                                                                                     (A.2)
                                                  i=1

   We replace Q with x∗ ∈ Deval , an item from a dataset (e.g., evaluation data). Additionally, we replace
Q on the right side with T (x). T (·) is a prompt template: a function that accepts some item as input then
returns a prompt that is used to condition the model.
Few-Shot Prompting. Often, an important part of the prompting process is the use of few-shot exemplars.
Dtrain is training data (used to build the prompt) and X is a test set for evaluation.


                                Dtrain = {(x1 , y1 ), (x2 , y2 ), ..., (xn , yn )}                   (A.3)
                                   X = {x∗1 , x∗2 , ..., x∗m }                                       (A.4)

  In the few-shot setting, the prompt template function T (·) also takes as input one or more training
samples X = {(xi , yi )}n1 ⊂ Dtrain


                                                  |A|
                                           ∗ 
                                                        pLM (ai | T (X , x∗ ) , a1:i−1 )
                                                  Y
                         p A | T (X , x ) =                                                          (A.5)
                                                  i=1

Optimization. As mentioned, it is often desirable to speak about improving prompts (prompt templates,
that is) with respect to a scoring function, usually defined with respect to a dataset.

                            T ∗ = argmax Exi ,yi ∼D [S (pLM (A|T (xi )), yi )]                       (A.6)
                                       T

  In this definition, we are evaluating over a dataset D with respect to the scoring function S(·). S(·)
evaluates the output A, generated by the LLM conditioned on the prompt T (§⟩ ). yi are labeled outputs
that can be used by S.
  In some cases, there may not be any labeled data yi , and S(·) may be reference-free.

                                                        75
Other considerations. These formalisms could be adapted to cater to CoT, retrieval systems, and more.
Here we describe a simple setup which is most descriptive of the prompting process without adding too
much complexity.
  We also draw attention to the lesser known concept of answer engineering. E(A) is a transformation
function over the raw LLM output that allows it to be compared to the ground truth.


                                A ∼ pLM (A | T (xi ), yi )                                     (A.7)
                                 ∗
                               T = argmax Exi ,yi ∼D [S (E(A), yi )]                           (A.8)
                                        T ,E




                                                  76
A.9    In-Context Learning Definitions Disambiguation
Brown et al. (2020) seemingly offer two different definitions for ICL. All bolding in this section is our
own.
      Recent work [RWC+19] attempts to do this via what we call “in-context learning”, using the text
      input of a pretrained language model as a form of task specification: the model is conditioned
      on a natural language instruction and/or a few demonstrations of the task and is then
      expected to complete further instances of the task simply by predicting what comes next.
  However, they later appear to define it as few-shot only:
      For each task, we evaluate GPT-3 under 3 conditions: (a) “few-shot learning”, or in-context
      learning where we allow as many demonstrations as will fit into the model’s context
      window (typically 10 to 100), (b) “one-shot learning”, where we allow only one demonstration,
      and (c) “zero-shot” learning, where no demonstrations are allowed and only an instruction in
      natural language is given to the model.
  However, they include this image that clarifies the matter:




                                 Figure A.1: ICL from Brown et al. (2020).

  Additionally, they explicitly state that ICL does not necessarily involve learning new tasks.

                                                    77
     To avoid this confusion, we use the term “meta-learning” to capture the inner-loop / outer-loop
     structure of the general method, and the term “in context-learning” to refer to the inner loop
     of meta-learning. We further specialize the description to “zero-shot”, “one-shot”, or “few-
     shot” depending on how many demonstrations are provided at inference time. These terms
     are intended to remain agnostic on the question of whether the model learns new tasks
     from scratch at inference time or simply recognizes patterns seen during training – this
     is an important issue which we discuss later in the paper, but “meta-learning” is intended to
     encompass both possibilities, and simply describes the inner-outer loop structure.

   We use Brown et al. (2020)’s broad definition, though note that practitioners often use ICL to refer to
situations in which the model appears to be learning new tasks from the prompt. Our definition differs
from Dong et al. (2023)’s formal definition, even though it is also derived from (Brown et al., 2020).




                                                   78
A.10   Contributions
The following are the contributions made by the team members in various sections of this paper. Most
authors conducted reviews of other sections as well.

Advisors
  • Denis Peskoff: Assisted with paper organization and final review.

  • Alexander Hoyle: Provided guidance on writing, meta-analysis approach, and ran automated
    baselines for case study.

  • Shyamal Anadkat: Assisted with the overall review of the paper and the etymology and definitions.

  • Jules White: Built trees for technique taxonomies.

  • Marine Carpaut: Framed, reviewed and suggested papers for the multilingual section.

  • Phillip Resnik: Principal Investigator

SCS Labeling
  • Megan L. Rogers, Inna Goncearenco, Giuseppe Sarli, Igor Galynker: reviewed and gave advice
    for this section.

Benchmarking and Agents
  • Konstantine Kahadze: Team leader for the Benchmarking section; managed MMLU benchmarking
    codebase, contributed to Security and Meta Analysis.

  • Ashay Srivastava: Team leader for the Agents section, reviewed papers for human review, worked
    on the tool use agents section. Worked on the compilation of contributions.

  • Hevander Da Costa: Contributed to the Benchmarking section and Meta Review datasets list,
    reviewed literature on LLM code generation and prompting techniques. Added literature review
    content to the Agents section.

  • Feileen Li: Worked on the tool use agents section, assisted with the human paper review.

Alignment and Security
  • Nishant Balepur: Team leader for the alignment section, helped with high-level discussions in
    benchmarking, and reviewed drafts.

  • Sevien Schulhoff: Team leader for the security section and contributed to the benchmarking section.

Related Works and Section Contributions
  • Chenglei Si: Suggested related works and edited section 2.2 and section 7.

  • Pranav Sandeep Dulepet: Contributed definitions for section 2 and worked on segmentation and
    object detection in the multimodal section.

  • HyoJung Han: Contributed to the Multimodal section, especially the speech+text part, and wrote
    the audio prompting section.

  • Hudson Tao: Authored sections on image, video, and 3D within multimodal, reviewed papers for
    human review; maintained GitHub codebase, and built the project website.

  • Amanda Liu: Authored taxonomic ontology sections, conducted background research for introduc-
    tion and related work, developed code pipelines for meta-analysis graphs

                                                 79
  • Sweta Agrawal: Team lead for evaluation section.

  • Saurav Vidyadhara: Assisted with general review and revising taxonomy trees.

  • Chau Pham: Assisted with meta review, including automated analysis of topics.

Multilingual Prompting and Meta Analysis
  • Dayeon Ki: Led the Multilingual prompting section, conducted review on related papers, and wrote
    Section 3.1.

  • Yinheng Li: Worked on section 2.2 text-based techniques, reviewed techniques, and contributed to
    drafting figure 2.2.

  • Saloni Gupta: Wrote tests for paper compilation, helped set up paper pipeline, and worked on the
    code diagram and grammar for the paper.

  • Gerson Kroiz: Involved with section 1.1 and defining a prompt.

  • Aayush Gupta: Contributed to the Meta Analysis, compiling papers, and generating visualization
    graphs.

  • Michael Ilie: Co-Lead Author, managed codebase, ran experiments, collected data, and helped with
    various sections including the PRISMA review figure and the SCS prompting case study.

  • Sander Schulhoff: Lead Author




                                                80
