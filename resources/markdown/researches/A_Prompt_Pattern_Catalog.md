                                                  A Prompt Pattern Catalog to Enhance Prompt Engineering with ChatGPT

                                                          Jules White, Quchen Fu, Sam Hays, Michael Sandborn, Carlos Olea, Henry Gilbert,
                                                                    Ashraf Elnashar, Jesse Spencer-Smith, and Douglas C. Schmidt
                                                                                          Department of Computer Science
                                                                                           Vanderbilt University, Tennessee
                                                                                                Nashville, TN, USA
                                                                {jules.white, quchen.fu, george.s.hays, michael.sandborn, carlos.olea, henry.gilbert,
                                                                      ashraf.elnashar, jesse.spencer-smith, douglas.c.schmidt}@vanderbilt.edu


                                                                                                               LLM by providing specific rules and guidelines for an LLM
arXiv:2302.11382v1 [cs.SE] 21 Feb 2023




                                            Abstract—Prompt engineering is an increasingly important
                                         skill set needed to converse effectively with large language models   conversation with a set of initial rules. In particular, a prompt
                                         (LLMs), such as ChatGPT. Prompts are instructions given to an         sets the context for the conversation and tells the LLM what
                                         LLM to enforce rules, automate processes, and ensure specific
                                         qualities (and quantities) of generated output. Prompts are also      information is important and what the desired output form and
                                         a form of programming that can customize the outputs and              content should be.
                                         interactions with an LLM.                                                For example, a prompt could specify that an LLM should
                                            This paper describes a catalog of prompt engineering tech-         only generate code that follows a certain coding style or
                                         niques presented in pattern form that have been applied to solve      programming paradigm. Likewise, it could specify that an
                                         common problems when conversing with LLMs. Prompt patterns
                                         are a knowledge transfer method analogous to software patterns        LLM should flag certain keywords or phrases in a generated
                                         since they provide reusable solutions to common problems faced        document and provide additional information related to those
                                         in a particular context, i.e., output generation and interaction      keywords. By introducing these guidelines, prompts facilitate
                                         when working with LLMs.                                               more structured and nuanced outputs to aid a large variety of
                                            This paper provides the following contributions to research on     software engineering tasks in the context of LLMs.
                                         prompt engineering that apply LLMs to automate software de-
                                         velopment tasks. First, it provides a framework for documenting
                                                                                                                  Prompt engineering is the means by which LLMs are
                                         patterns for structuring prompts to solve a range of problems         programmed via prompts. To demonstrate the power of
                                         so that they can be adapted to different domains. Second, it          prompt engineering, we provide the following prompt:
                                         presents a catalog of patterns that have been applied successfully          Prompt: “From now on, I would like you to ask me
                                         to improve the outputs of LLM conversations. Third, it explains             questions to deploy a Python application to AWS.
                                         how prompts can be built from multiple patterns and illustrates
                                         prompt patterns that benefit from combination with other prompt             When you have enough information to deploy the
                                         patterns.                                                                   application, create a Python script to automate the
                                            Index Terms—large language models, prompt patterns, prompt               deployment.”
                                         engineering                                                              This example prompt causes ChatGPT to begin asking the
                                                                                                               user questions about their software application. ChatGPT will
                                                                I. I NTRODUCTION                               drive the question-asking process until it reaches a point where
                                            Conversational large language models (LLMs) [1], such as           it has sufficient information to generate a Python script that
                                         ChatGPT [2], have generated immense interest in a range               automates deployment. This example demonstrates the pro-
                                         of domains for tasks ranging from answering questions on              gramming potential of prompts beyond conventional “generate
                                         medical licensing exams [3] to generating code snippets. This         a method that does X” style prompts or “answer this quiz
                                         paper focuses on enhancing the application of LLMs in several         question”.
                                         domains, such as helping developers code effectively and                 Moreover, prompts can be engineered to program an LLM
                                         efficiently with unfamiliar APIs or allowing students to acquire      to accomplish much more than simply dictating the output type
                                         new coding skills and techniques.                                     or filtering the information provided to the model. With the
                                            LLMs are particularly promising in domains where humans            right prompt, it is possible to create entirely new interaction
                                         and AI tools work together as trustworthy collaborators to            paradigms, such as having an LLM generate and give a quiz
                                         more rapidly and reliably evolve software-reliant systems [4].        associated with a software engineering concept or tool, or
                                         For example, LLMs are being integrated directly into software         even simulate a Linux terminal window. Moreover, prompts
                                         tools, such as Github’s Co-Pilot [5]–[7] and included in inte-        have the potential for self-adaptation, suggesting other prompts
                                         grated development environments (IDEs), such as IntelliJ [8]          to gather additional information or generate related artifacts.
                                         and Visual Studio Code, thereby allowing software teams to            These advanced capabilities of prompts highlight the impor-
                                         access these tools directly from their preferred IDE.                 tance of engineering them to provide value beyond simple text
                                            A prompt [9] is a set of instructions provided to an               or code generation.
                                         LLM that programs the LLM by customizing it and/or en-                   Prompt patterns are essential to effective prompt engi-
                                         hancing or refining its capabilities. A prompt can influence          neering. A key contribution of this paper is the introduction
                                         subsequent interactions with—and output generated from—an             of prompt patterns to document successful approaches for
systematically engineering different output and interaction         stylized form to facilitate their use and understanding, such
goals when working with conversational LLMs. We focus               as:
largely on engineering domain-independent prompt patterns              • A name and classification. Each pattern has a name that
and introduce a catalog of essential prompt patterns to solve             identifies the pattern and should be used consistently. A
problems ranging from production of visualizations and code               classification groups patterns into broad categories, such
artifacts to automation of output steps that help fact check              as creational, structural, or behavioral.
outputs.                                                               • The intent concisely conveys the purpose the pattern is
   The remainder of this paper is organized as follows: Sec-              intended to achieve.
tion II introduces prompt patterns and compares these patterns         • The motivation documents the underlying problem the
to well-known software patterns [10]; Section III describes               pattern is meant to solve and the importance of the
16 prompt patterns that have been applied to solve common                 problem.
problems in the domain of conversational LLM interaction and           • The structure and participants. The structure describes
output generation for automating software development tasks;              the different pattern participants (such as classes and
Section IV discusses related work; and Section V presents                 objects) and how they collaborate to form a generalized
concluding remarks and lessons learned.                                   solution.
                                                                       • Example code concretely maps the pattern to some
           II. C OMPARING S OFTWARE PATTERNS                              underlying programming language(s) and aids developers
                  WITH P ROMPT PATTERNS                                   in gaining greater insight into how that pattern can be
   The quality of the output(s) generated by a conversational             applied effectively.
                                                                       • Consequences summarize the pros and cons of applying
LLM is directly related to the quality of the prompts provided
by the user. As discussed in Section I, the prompts given to              the pattern in practice.
a conversational LLM can be used to program interactions            B. Overview of Prompt Patterns
between a user and an LLM to better solve a variety of                 Prompt patterns are similar to software patterns in that they
problems. One contribution of this paper is the framework it        offer reusable solutions to specific problems. They focus more
provides to document patterns that structure prompts to solve       specifically, however, on the context of output generation from
a range of software tasks that can be adapted to different          large-scale language models (LLMs), such as ChatGPT. Just
domains.                                                            as software patterns provide a codified approach to solving
   This framework is useful since it focuses on codifying           common software development challenges, prompt patterns
patterns that can be applied to help users better interact          provide a codified approach to customizing the output and
with conversational LLMs in a variety of contexts, rather           interactions of LLMs.
than simply discussing interesting examples or domain-specific         By documenting and leveraging prompt patterns in the
prompts. Codifying this knowledge in pattern form enhances          context of automating software development tasks, individual
reuse and transferability to other contexts and domains where       users and teams can enforce constraints on the generated
users face similar—but not identical—problems.                      output, ensure that relevant information is included, and
   The topic of knowledge transfer has been studied exten-          change the format of interaction with the LLM to better
sively in the software patterns literature [10], [11] at multiple   solve problems they face. Prompt patterns can be viewed as a
levels, e.g., design, architectural, and analysis. This paper       corollary to the broad corpus of general software patterns, just
applies a variant of a familiar pattern form as the basis of        adapted to the more specific context of LLM output generation.
our prompt engineering approach. Since prompts are a form              Prompt patterns follow a similar format to classic software
of programming, it is natural to document them in pattern           patterns, with slight modifications to match the context of
form.                                                               output generation with LLMs.1 Each of the analogous sections
                                                                    for the prompt pattern form used in this paper is summarized
A. Overview of Software Patterns                                    below:
   A software pattern provides a reusable solution to a recur-         • A name and classification. The prompt pattern name
ring problem within a particular context [10]. Documenting               uniquely identifies the pattern and ideally indicates the
software patterns concisely conveys (and generalizes) from               problem that is being addressed. For the classification,
specific problems being addressed to identify important forces           we have developed a series of initial categories of pattern
and/or requirements that should be resolved and/or addressed             types, which are summarized in Table I and include
in successful solutions.                                                 Output Customization, Error Identification, Prompt
   A pattern form also includes guidance on how to implement             Improvement, Interaction, and Context Control.
the pattern, as well as information on the trade-offs and              • The intent and context describes the problem the prompt
considerations to take into account when implementing a                  pattern solves and the goals it achieves. The problem
pattern. Moreover, example applications of the pattern are             1 The most direct translation of software pattern structure to prompt patterns
often provided to further showcase the pattern’s utility in         is the naming, intent, motivation, and sample code. The structure and
practice. Software patterns are typically documented in a           classification, however, although named similarly, require more adaptation.
    should ideally be independent of any domain, though                should be at a higher-level than the underlying tokens
    domain-specific patterns may also be documented with               representing the idea.
    an appropriate discussion of the context where the pattern       • It is possible to program an LLM to introduce novel
    applies.                                                           semantics for statements and words that create new ways
  • The motivation provides the rationale for the problem              for communicating an idea. In contrast, grammars may
    and explains why solving it is important. The motivation           not easily represent ideas that can be expressed through
    is explained in the context of users interacting with a            completely new symbology or languages that the gram-
    conversational LLM and how it can improve upon users               mar designer was not aware of.
    informally prompting the LLM in one or more circum-
    stances. Specific circumstances where the improvements         D. A Way Forward: Fundamental Contextual Statements
    are expected are documented.                                      An open research question, therefore, is what approach is
  • The structure and key ideas. The structure describes           more effective than formal grammars for describing prompt
    the fundamental contextual information, as a series of         pattern structure and ideas. We propose the concept of funda-
    key ideas, that the prompt pattern provides to the LLM.        mental contextual statements, which are written descriptions
    These ideas are similar to “participants” in a software pat-   of the important ideas to communicate in a prompt to an LLM.
    tern. The contextual information may be communicated           An idea can be rewritten and expressed in arbitrary ways based
    through varying wording (just as a software pattern can        on user needs and experience. The key ideas to communicate,
    have variations in how it is realized in code), but should     however, are presented to the user as a series of simple, but
    have fundamental pieces of information that form a core        fundamental, statements.
    element of the pattern.                                           One benefit of adopting and applying the fundamental con-
  • Example implementation demonstrates how the prompt             textual statements approach is that it is intentionally intuitive
    pattern is worded in practice.                                 to users. In particular, we expect users will understand how to
  • Consequences summarize the pros and cons of applying           express and adapt the statements in a contextually appropriate
    the pattern and may provide guidance on how to adapt           way for their domain. Moreover, since the underlying ideas of
    the prompt to different contexts.                              the prompt are captured, these same ideas can be expressed
                                                                   by the user in alternate symbology or wording that has been
C. Evaluating Means for Defining a Prompt Pattern’s Struc-
                                                                   introduced to the LLM using patterns, such as the Meta
ture and Ideas
                                                                   Language Creation pattern presented in Section III-B.
   In software patterns, the structure and participants are           Our ultimate goal is to enhance prompt engineering by
normally defined in terms of UML diagrams, such as structure       providing a framework for designing prompts that can be
diagrams and/or interaction diagrams. These UML diagrams           reused and/or adapted to other LLMs in the same way that
explain what the participants of the pattern are and how they      software patterns can be implemented in different program-
interact to solve the problem. In prompt patterns, something       ming languages and platforms. For the purposes of this paper,
analogous is needed, though UML may not be an appro-               however, all prompts were tested with ChatGPT [12] using the
priate structural documentation approach since it is intended      ChatGPT+ service. We use ChatGPT as the LLM for all exam-
to describe software structures, as opposed to the ideas to        ples presented in this paper due to its widespread availability
communicate in a prompt.                                           and popularity. These examples were documented through a
   Several possible approaches could be used, ranging from di-     combination of exploring the corpus of community-posted
agrams to defining grammars for a prompt language. Although        prompts on the Internet and independent prompt creation from
grammars may seem attractive due to their formal nature, they      our use of ChatGPT to automating software development
also incur the following challenges:                               tasks.
   • The goal of prompts is to communicate knowledge in a
     clear and concise way to conversation LLM users, who                    III. A C ATALOG OF P ROMPT PATTERNS
     may or may not be computer scientists or programmers.                        FOR C ONVERSATIONAL LLM S
     As a community, we should strive to create an approach-         This section presents our catalog of prompt patterns that
     able format that communicates knowledge clearly to a          have been applied to solve common problems in the domain
     diverse target audience.                                      of conversational LLM interaction and output generation for
   • It is possible to phrase a prompt in many different ways.     automating software tasks. Each prompt pattern is accompa-
     It is hard, however, to define a grammar that accurately      nied by concrete implementation samples and examples with
     and completely expresses all the nuanced ways that            and without the prompt.
     components of a prompt could be expressed in text or
     symbols.                                                      A. Summary of the Prompt Pattern Catalog
   • Prompts fundamentally convey ideas to a conversational           The classification of prompt patterns is an important consid-
     LLM and are not simply the production of tokens for           eration in documenting the patterns. Table I outlines the initial
     input. In particular, an idea built into a prompt pattern     classifications for the catalog of prompt patterns we identified
     can be communicated in many ways and its expression           in our work with ChatGPT thus far.
                             TABLE I                                  category includes the Fact Check List and Reflection patterns.
                  C LASSIFYING P ROMPT PATTERNS                       The Fact Check List pattern requires the LLM to generate a
                                                                      list of facts the output depends on that should be fact-checked.
 Pattern Category     Prompt Pattern
                                                                      The Reflection pattern requires the LLM to introspect on its
 Input Semantics      Meta Language Creation                          output and identify any errors.
 Output               Output Automater                                   The Prompt Improvement category focuses on improving
 Customization        Persona                                         the quality of the input and output. This category includes
                      Visualization Generator                         the Question Refinement, Alternative Approaches, Cognitive
                      Recipe                                          Verifier, and Refusal Breaker patterns. The Question Refine-
                                                                      ment pattern ensures the LLM always suggests a better version
                      Template                                        of the user’s question. The Alternative Approaches pattern
 Error Identification Fact Check List                                 requires the LLM to suggest alternative ways of accomplishing
                      Reflection                                      a user-specified task. The Cognitive Verifier pattern instructs
 Prompt               Question Refinement                             the LLM to automatically suggest a series of subquestions
 Improvement          Alternative Approaches                          for the user to answer before combining the answers to the
                                                                      subquestions and producing an answer to the overall question.
                      Cognitive Verifier
                                                                      The Refusal Breaker pattern requires the LLM to automatically
                      Refusal Breaker                                 reword the user’s question when it refuses to produce an
 Interaction          Flipped Interaction                             answer.
                      Game Play                                          The Interaction category focuses on the interaction be-
                      Infinite Generation                             tween the user and the LLM. This category includes the
 Context Control      Context Manager                                 Flipped Interaction, Game Play, and Infinite Generation pat-
                                                                      terns. The Flipped Interaction pattern requires the LLM to
                                                                      ask questions rather than generate output. The Game Play
                                                                      pattern requires the LLM to generate output in the form of
   As shown in this table, there are five categories of prompt
                                                                      a game. The Infinite Generation pattern requires the LLM to
patterns in our classification framework: Input Semantics,
                                                                      generate output indefinitely without the user having to reenter
Output Customization, Error Identification, Prompt Im-
                                                                      the generator prompt each time.
provement, and Interaction, each of which is summarized
                                                                         Finally, the Context Control category focuses on control-
below.
                                                                      ling the contextual information in which the LLM operates.
   The Input Semantics category deals with how an LLM                 This category includes the Context Manager pattern, which
understands the input and how it translates the input into            allows the user to specify the context for the LLM’s output.
something it can use to generate output. This category in-               The remainder of this section describes each of these prompt
cludes the Meta Language Creation pattern, which focuses on           patterns using the pattern form discussed in Section II-B.
creating a custom language for the LLM to understand. This
pattern is useful when the default input language is ill-suited       B. The Meta Language Creation Pattern
for expressing ideas the user wants to convey to the LLM.
                                                                         1) Intent and Context: During a conversation with an LLM,
   The Output Customization category focuses on constrain-            the user would like to create the prompt via an alternate
ing or tailoring the types, formats, structure, or other properties   language, such as a textual short-hand notation for graphs, a
of the output generated by the LLM. The prompt patterns in            description of states and state transitions for a state machine, a
this category include Output Automater, Persona, Visualiza-           set of commands for prompt automation, etc. The intent of this
tion Generator, Recipe, and Template patterns. The Output             pattern is to explain the semantics of this alternative language
Automater pattern allows the user to create scripts that can          to the LLM so the user can write future prompts using this
automate any tasks the LLM output suggests the user should            new language and its semantics.
perform. The Persona pattern gives the LLM a persona or role
                                                                         2) Motivation: Many problems, structures, or other ideas
to play when generating output. The Visualization Generator
                                                                      communicated in a prompt may be more concisely, unam-
pattern allows the user to generate visualizations by producing
                                                                      biguously, or clearly expressed in a language other than
textual outputs that can be fed to other tools, such as other
                                                                      English (or whatever conventional human language is used
AI-based image generators, like DALL-E [13]. The Recipe
                                                                      to interact with an LLM). To produce output based on an
pattern allows the user to obtain a sequence of steps or actions
                                                                      alternative language, however, an LLM needs to understand
to realize a stated end result, possibly with partially known
                                                                      the language’s semantics.
information or constraints. The Template pattern allows the
                                                                         3) Structure and Key Ideas: Fundamental contextual state-
user to specify a template for the output, which the LLM fills
                                                                      ments:
in with content.
   The Error Identification category focuses on identifying              Contextual Statements
and resolving errors in the output generated by the LLM. This            When I say X, I mean Y (or would like you to do Y)
   The key structure of this pattern involves explaining the          it will respond that this prompt creates too much confusion
meaning of one or more symbols, words, or statements to            as “a” is an indefinite article and too commonly used, as shown
the LLM so it uses the provided semantics for the ensuing          below:
conversation. This description can take the form of a simple             “Referring to Marie Antoinette using “a” could
translation, such as “X” means “Y”. The description can also             potentially cause confusion, as “a” is an indefinite
take more complex forms that define a series of commands                 article commonly used to refer to a noun that has
and their semantics, such as “when I say X, I want you to do             not been mentioned before. It may be more clear
”. In this case, “X” is henceforth bound to the semantics of             to use her name, “Marie Antoinette”, or a pronoun
“take action”.                                                           such as “she” or “her” to refer to her. Moreover,
   4) Example Implementation: The key to successfully using              using context to establish who you are referring to
the Meta Language Creation pattern is developing an unam-                can also help avoid confusion in conversation.”
biguous notation or shorthand, such as the following:                 In general, an LLM will perform better on data it was
     “From now on, whenever I type two identifiers                 trained on. Therefore, when an existing notation is available—
     separated by a “→”, I am describing a graph. For              but may not be the dominant meaning—the Meta Language
     example, “a → b” is describing a graph with nodes             Creation pattern can provide context to scope the meaning of
     “a” and “b” and an edge between them. If I separate           the symbol to improve the accurately and utility of the output.
     identifiers by “-[w:2, z:3]→”, I am adding properties         For example, the symbol “→” conveys slightly different infor-
     of the edge, such as a weight or label.”                      mation in graphs and propositional logic. The statement “p →
   This example of the Meta Language Creation pattern estab-       q, q → p” may therefore make sense, but only if the LLM
lishes a standardized notation for describing graphs by defining   is given the appropriate context through a Meta Language
a convention for representing nodes and edges. Whenever the        Creation prompt.
author types two identifiers separated by a “→” symbol, it is         Although Meta Language Creation is a powerful pattern it
an indication that a graph is being described. For example, if     must be used carefully, particularly when describing concepts
the author types “a → b”, this indicates that a graph is being     that may otherwise be hard to precisely or concisely describe.
defined with nodes “a” and “b”, and that there is an edge          These types of prompts are thus best used in completely
between them. This convention provides a clear and concise         new conversation sessions. Using a single meta-language-per-
way to communicate the structure of a graph in written form.       conversation session may also be a best practice since it avoids
   Moreover, the prompt goes on to specify that additional         the potential for conflicting or unexpected semantics being
information about the edges, such as a weight or label, can        applied to the conversation over time.
be provided using the syntax “-[w:2, z:3]→”. This notation
allows for the specification of additional properties beyond       C. The Output Automater Pattern
the basic structure of the graph. The specified properties are        1) Intent and Context: The intent of this pattern is to have
associated with the edge between the two nodes and can             the LLM generate a script or other automation artifact that can
provide important context for the interpretation of the graph.     automatically perform any steps it recommends taking as part
This standardized notation for describing graphs can make it       of its output. The goal is to reduce the manual effort needed
easier to communicate graph structures and properties, which       to implement any LLM output recommendations.
may not be easy or are very verbose to describe as a series of        2) Motivation: The output of an LLM is often a sequence
sentences.                                                         of steps for the user to follow. For example, when asking an
   5) Consequences: Although this pattern provides a pow-          LLM to generate a Python configuration script it may suggest
erful means to customize a user’s interaction with an LLM,         a number of files to modify and changes to apply to each file.
it may create the potential for confusion within the LLM.          However, having users continually perform the manual steps
As important as it is to clearly define the semantics of the       dictated by LLM output is tedious and error-prone.
language, it is also essential to ensure the language itself          3) Structure and Key Ideas: Fundamental contextual state-
introduces no ambiguities that degrade the LLM’s performance       ments:
or accuracy. For example, the prompt “whenever I separate
two things by commas, it means that the first thing precedes          Contextual Statements
the second thing” will likely create significant potential for        Whenever you produce an output that has at least one
ambiguity and create the potential for unexpected semantics           step to take and the following properties (alternatively,
if punctuation involving commas is used in the prompt.                always do this)
   To showcase the potential for confusion, ChatGPT will              Produce an executable artifact of type X that will
warn the user and potentially be unable to perform a specific         automate these steps
mapping of a symbol or term to a new meaning. For example,            The first part of the pattern identifies the situations under
if following prompt is given to ChatGPT                            which automation should be generated. A simple approach
     “Whenever I say “a”, I am referring to Marie An-              is to state that the output includes at least two steps to
     toinette.”                                                    take and that an automation artifact should be produced. The
scoping is up to the user, but helps prevent producing an            rather than manual actions unknown to the LLM. Alternatively,
output automation scripts in cases where running the output          self-contained sequences of steps work well, such as “how do
automation script will take more user effort than performing         I find the list of open ports on my Mac computer”.
the original steps produced in the output. The scope can be             In some cases, the LLM may produce a long output with
limited to outputs requiring more than a certain number of           multiple steps and not include an automation artifact. This
steps.                                                               omission may arise for various reasons, including exceeding
   The next part of this pattern provides a concrete statement       the output length limitation the LLM supports. A simple
of the type of output the LLM should output to perform the           workaround for this situation is to remind the LLM via a
automation. For example, “produce a Python script” gives the         follow-on prompt, such as “But you didn’t automate it”, which
LLM a concrete understanding to translate the general steps          provides the context that the automation artifact was omitted
into equivalent steps in Python. The automation artifact should      and should be generated.
be concrete and must be something that the LLM associates               At this point in the evolution of LLMs, the Output Auto-
with the action of “automating a sequence of steps”.                 mater pattern is best employed by users who can read and
   4) Example Implementation: A sample of this prompt pat-           understand the generated automation artifact. LLMs can (and
tern applied to code snippets generated by the ChatGPT LLM           do) produce inaccuracies in their output, so blindly accepting
is shown below:                                                      and executing an automation artifact carries significant risk.
      “From now on, whenever you generate code that                  Although this pattern may alleviate the user from performing
      spans more than one file, generate a Python script             certain manual steps, it does not alleviate their responsibility
      that can be run to automatically create the specified          to understand the actions they undertake using the output.
      files or make changes to existing files to insert the          When users execute automation scripts, therefore they assume
      generated code.”                                               responsibility for the outcomes.
   This pattern is particularly effective in software engineering
                                                                     D. The Flipped Interaction Pattern
as a common task for software engineers using LLMs is to
then copy/paste the outputs into multiple files. Some tools,            1) Intent and Context: You want the LLM to ask questions
such as Copilot, insert limited snippets directly into the section   to obtain the information it needs to perform some tasks.
of code that the coder is working with, but tools, such as           Rather than the user driving the conversation, therefore, you
ChatGPT, do not provide these facilities. This automation trick      want the LLM to drive the conversation to focus it on
is also effective at creating scripts for running commands on        achieving a specific goal. For example, you may want the
a terminal, automating cloud operations, or reorganizing files       LLM to give you a quick quiz or automatically ask questions
on a file system.                                                    until it has sufficient information to generate a deployment
   This pattern is a powerful complement for any system that         script for your application to a particular cloud environment.
can be computer controlled. The LLM can provide a set of                2) Motivation: Rather than having the user drives a con-
steps that should be taken on the computer-controlled system         versation, an LLM often has knowledge it can use to more
and then the output can be translated into a script that allows      accurately obtain information from the user. The goal of the
the computer controlling the system to automatically take            Flipped Interaction pattern is to flip the interaction flow so the
the steps. This is a direct pathway to allowing LLMs, such           LLM asks the user questions to achieve some desired goal. The
as ChatGPT, to integrate quality into—and to control—new             LLM can often better select the format, number, and content
computing systems that have a known scripting interface.             of the interactions to ensure that the goal is reached faster,
   5) Consequences: An important usage consideration of              more accurately, and/or by using knowledge the user may not
this pattern is that the automation artifact must be defined         (initially) possess.
concretely. Without a concrete meaning for how to “automate”            3) Structure and Key Ideas: Fundamental contextual state-
the steps, the LLM often states that it “can’t automate things”      ments:
since that is beyond its capabilities. LLMs typically accept
                                                                        Contextual Statements
requests to produce code, however, so the goal is to instruct the
                                                                        I would like you to ask me questions to achieve X
LLM to generate text/code, which can be executed to automate
                                                                        You should ask questions until this condition is met or
something. This subtle distinction in meaning is important to
                                                                        to achieve this goal (alternatively, forever)
help an LLM disambiguate the prompt meaning.
   One caveat of the Output Automater pattern is the LLM                (Optional) ask me the questions one at a time, two at
needs sufficient conversational context to generate an automa-          a time, etc.
tion artifact that is functional in the target context, such as         A prompt for a flipped interaction should always specify the
the file system of a project on a Mac vs. Windows computer.          goal of the interaction. The first idea (i.e., you want the LLM to
This pattern works best when the full context needed for the         ask questions to achieve a goal) communicates this goal to the
automation is contained within the conversation, e.g., when          LLM. Equally important is that the questions should focus on a
a software application is generated from scratch using the           particular topic or outcome. By providing the goal, the LLM
conversation and all actions on the local file system are            can understand what it is trying to accomplish through the
performed using a sequence of generated automation artifacts         interaction and tailor its questions accordingly. This “inversion
of control” enables more focused and efficient interaction since       For example, the user can state that they would like to
the LLM will only ask questions that it deems relevant to           deploy an application to Amazon AWS EC2, rather than
achieving the specified goal.                                       simply state ”the cloud” and require multiple interactions to
   The second idea provides the context for how long the in-        narrow down the deployment target. The more precise the
teraction should occur. A flipped interaction can be terminated     initial information, the better the LLM can use the limited
with a response like “stop asking questions”. It is often better,   questions that a user is likely willing to answer to obtain
however, to scope the interaction to a reasonable length or         information to improve its output.
only as far as is needed to reach the goal. This goal can be           When developing prompts for flipped interactions, it is im-
surprisingly open-ended and the LLM will continue to work           portant to consider the level of user knowledge, engagement,
towards the goal by asking questions, as is the case in the         and control. If the goal is to accomplish the goal with as little
example of ”until you have enough information to generate a         user interaction as possible (minimal control), that should be
Python script”.                                                     stated explicitly.Conversely, if the goal is to ensure the user
   By default, the LLM is likely to generate multiple questions     is aware of all key decisions and confirms them (maximum
per iteration. The third idea is completely optional, but can       engagement) that should also be stated explicitly. Likewise, if
improve usability by limiting (or expanding) the number of          the user is expected to have minimal knowledge and should
questions that the LLM generates per cycle. If a precise            have the questions targeted at their level of expertise, this
number/format for the questioning is not specified, the ques-       information should be engineered into the prompt.
tioning will be semi-random and may lead to one-at-a-time
questions or ten-at-a-time questions. The prompt can thus be        E. The Persona Pattern
tailored to include the number of questions asked at a time,
the order of the questions, and any other formatting/ordering          1) Intent and Context: In many cases, users would like
considerations to facilitate user interaction.                      LLM output to always take a certain point of view or per-
                                                                    spective. For example, it may be useful for to conduct a code
   4) Example Implementation: A sample prompt for a flipped
                                                                    review as if the LLM was a security expert. The intent of this
interaction is shown below:
                                                                    pattern is to give the LLM a “persona” that helps it select what
     “From now on, I would like you to ask me questions             types of output to generate and what details to focus on.
     to deploy a Python application to AWS. When you                   2) Motivation: Users may not know what types of outputs
     have enough information to deploy the application,             or details are important for an LLM to focus on to achieve
     create a Python script to automate the deployment.”            a given task. They may know, however, the role or type of
   In general, the more specific the prompt regarding the           person that they would normally ask to get help with these
constraints and information to collect, the better the outcome.     things. The Persona pattern enables the users to express what
For instance, the example prompt above could provide a menu         they need help with without knowing the exact details of the
of possible AWS services (such as Lambda, EC2, etc.) with           outputs they need.
which to deploy the application. In other cases, the LLM may           3) Structure and Key Ideas: Fundamental contextual state-
be permitted to simply make appropriate choices on its own for      ments:
things that the user doesn’t explicitly make decisions about.
One limitation of this prompt is that, once other contextual            Contextual Statements
information is provided regarding the task, it may require              Act as persona X
experimentation with the precise phrasing to get the LLM to             Provide outputs that persona X would create
ask the questions in the appropriate number and flow to best
                                                                       The first statement conveys the idea that the LLM needs
suit the task, such as asking multiple questions at once versus
                                                                    to act as a specific persona and provide outputs that such a
one question at a time.
                                                                    persona would. This persona can be expressed in a number
   5) Consequences: One consideration when designing the
                                                                    of ways, ranging from a job description, title, fictional char-
prompt is how much to dictate to the LLM regarding what
                                                                    acter, historical figure, etc. The persona should elicit a set
information to collect prior to termination. In the example
                                                                    of attributes associated with a well-known job title, type of
above, the flipped interaction is open-ended and can vary sig-
                                                                    person, etc.2
nificantly in the final generated artifact. This open-endedness
                                                                       The secondary idea—provide outputs that persona X would
makes the prompt generic and reusable, but may potentially
                                                                    create—offers opportunities for customization. For example, a
ask additional questions that could be skipped if more context
                                                                    teacher might provide a large variety of different output types,
is given.
                                                                    ranging from assignments to reading lists to lectures. If a more
   If specific requirements are known in advance, it is better to
                                                                    specific scope to the type of output is known, the user can
inject them into the prompt rather than hoping the LLM will
                                                                    provide it in this statement.
obtain the needed information. Otherwise, the LLM will non-
nondeterministically decide whether to prompt the user for the        2 Be aware, however, that personas relating to living people or people
information or make an educated guess as to an appropriate          considered harmful make be disregarded due to underlying LLM privacy and
value.                                                              security rules.
    4) Example Implementation: A sample implementation for          is pretending to query. ChatGPT can then generate synthetic
code review is shown below:                                         rows, such as generating imaginary rows for a “people” table
       “From now on, act as a security reviewer. Pay close          with columns for “name” and “job”.
       attention to the security details of any code that
                                                                    F. The Question Refinement Pattern
       we look at. Provide outputs that a security reviewer
       would regarding the code.”                                      1) Intent and Context: This pattern engages the LLM in
    In this example, the LLM is instructed to provide outputs       the prompt engineering process. The intent of this pattern is
that a ”security reviewer” would. The prompt further sets the       to ensure the conversational LLM always suggests potentially
stage that code is going to be evaluated. Finally, the user         better or more refined questions the user could ask instead of
refines the persona by scoping the persona further to outputs       their original question. Using this pattern, the LLM can aid the
regarding the code.                                                 user in finding the right question to ask in order to arrive at an
    Personas can also represent inanimate or non-human en-          accurate answer. In addition, the LLM may help the user find
tities, such as a Linux terminal, a database, or an animal’s        the information or achieve their goal in fewer interactions with
perspective. When using this pattern to represent these entities,   the user than if the user employed trial and error prompting.
it can be useful to also specify how you want the inputs               2) Motivation: If a user is asking a question, it is possible
delivered to the entity, such as “assume my input is what the       they are not an expert in the domain and may not know the
owner is saying to the dog and your output is the sounds the        best way to phrase the question or be aware of additional
dog is making”. An example prompt for a non-human entity            information helpful in phrasing the question. LLMs will often
that uses a “pretend to be” wording is shown below:                 state limitations on the answer they are providing or request
                                                                    additional information to help them produce a more accurate
       “You are going to pretend to be a Linux terminal
                                                                    answer. An LLM may also state assumptions it made in
       for a computer that has been compromised by an
                                                                    providing the answer. The motivation is that this additional
       attacker. When I type in a command, you are going
                                                                    information or set of assumptions could be used to generate
       to output the corresponding text that the Linux
                                                                    a better prompt. Rather than requiring the user to digest
       terminal would produce.”
                                                                    and rephrase their prompt with the additional information,
    This prompt is designed to simulate a computer that has         the LLM can directly refine the prompt to incorporate the
been compromised by an attacker and is being controlled             additional information.
through a Linux terminal. The prompt specifies that the user           3) Structure and Key Ideas: Fundamental contextual state-
will input commands into the terminal, and in response, the         ments:
simulated terminal will output the corresponding text that
would be produced by a real Linux terminal. This prompt                Contextual Statements
is more prescriptive in the persona and asks the LLM to, not           Within scope X, suggest a better version of the question
only be a Linux terminal, but to further act as a computer that        to use instead
has been compromised by an attacker.                                   (Optional) prompt me if I would like to use the better
    The persona causes ChatGPT to generate outputs to com-             version instead
mands that have files and contents indicative of a computer that
                                                                       The first contextual statement in the prompt is asking the
was hacked. The example illustrates how an LLM can bring
                                                                    LLM to suggest a better version of a question within a specific
its situational awareness to a persona, in this case, creating
                                                                    scope. The scope is provided to ensure that not all questions
evidence of a cyberattack in the outputs it generates. This
                                                                    are automatically reworded or that they are refined with a
type of persona can be very effective for combining with the
                                                                    given goal. The second contextual statement is meant for
Game Play pattern, where you want the exact details of the
                                                                    automation and allows the user to automatically use the refined
output characteristics to be hidden from the user (e.g., don’t
                                                                    question without having to copy/paste or manually enter it. The
give away what the cyberattack did by describing it explicitly
                                                                    engineering of this prompt can be further refined by combining
in the prompt).
                                                                    it with the Reflection pattern, which allows the LLM to explain
    5) Consequences: An interesting aspect of taking non-
                                                                    why it believes the refined question is an improvement.
human personas is that the LLM may make interesting as-
                                                                       4) Example Implementation:
sumptions or “hallucinations” regarding the context. A widely
circulated example on the Internet asks ChatGPT to act as                 “From now on, whenever I ask a question about a
a Linux terminal and produce the expected output that you                 software artifact’s security, suggest a better version
would get if the user typed the same text into a terminal.                of the question to use that incorporates information
Commands, such as ls -l, will generate a file listing for an              specific to security risks in the language or frame-
imaginary UNIX file system, complete with files that can have             work that I am using instead and ask me if I would
cat file1.txt run on them.                                                like to use your question instead.”
    In other examples, the LLM may prompt the user for more            In the context of the example above, the LLM will use
context, such as when ChatGPT is asked to act as a MySQL            the Question Refinement pattern to improve security-related
database and prompts for the structure of a table that the user     questions by asking for or using specific details about the
software artifact and the language or framework used to build       the Question Refinement pattern with the Persona pattern so
it. For instance, if a developer of a Python web application with   the LLM flags terms and generates definitions that assume a
FastAPI asks ChatGPT “How do I handle user authentication           particular level of knowledge, such as this example:
in my web application?”, the LLM will refine the question                “From now on, whenever I ask a question, ask four
by taking into account that the web application is written in            additional questions that would help you produce a
Python with FastAPI. The LLM then provides a revised ques-               better version of my original question. Then, use my
tion that is more specific to the language and framework, such           answers to suggest a better version of my original
as “What are the best practices for handling user authentication         question. After the follow-up questions, temporarily
securely in a FastAPI web application to mitigate common                 act as a user with no knowledge of AWS and define
security risks, such as cross-site scripting (XSS), cross-site           any terms that I need to know to accurately answer
request forgery (CSRF), and session hijacking?”                          the questions.”
    The additional detail in the revised question is likely            An LLM can always produce factual inaccuracies, just
to not only make the user aware of issues they need to              like a human. A risk of this pattern is that the inaccuracies
consider, but lead to a better answer from the LLM. For             are introduced into the refined question. This risk may be
software engineering tasks, this pattern could also incorporate     mitigated, however, by combining the Fact Check List pattern
information regarding potential bugs, modularity, or other          to enable the user to identify possible inaccuracies and the
code quality considerations. Another approach would be to           Reflection pattern to explain the reasoning behind the question
automatically refine questions so the generated code cleanly        refinement.
separates concerns or minimizes use of external libraries, such
as:                                                                 G. The Alternative Approaches Pattern
      Whenever I ask a question about how to write some                1) Intent and Context: The intent of the pattern is to ensure
      code, suggest a better version of my question that            an LLM always offers alternative ways of accomplishing a task
      asks how to write the code in a way that minimizes            so a user does not pursue only the approaches with which they
      my dependencies on external libraries.                        are familiar. The LLM can provide alternative approaches that
                                                                    always force the user to think about what they are doing and
    5) Consequences: The Question Refinement pattern helps          determine if that is the best approach to meet reach their goal.
bridge the gap between the user’s knowledge and the LLM’s           In addition, solving the task may inform the user or teach them
understanding, thereby yielding more efficient and accurate         about alternative concepts for subsequent follow-up.
interactions. One risk of this pattern is its tendency to rapidly      2) Motivation: Humans often suffer from cognitive biases
narrow the questioning by the user into a specific area that        that lead them to choose a particular approach to solve a
guides the user down a more limited path of inquiry than            problem even when it is not the right or “best” approach.
necessary. The consequence of this narrowing is that the            Moreover, humans may be unaware of alternative approaches
user may miss important ”bigger picture” information. One           to what they have used in the past. The motivation of the
solution to this problem is to provide additional scope to the      Alternative Approaches pattern is to ensure the user is aware
pattern prompt, such as “do not scope my questions to specific      of alternative approaches to select a better approach to solve
programming languages or frameworks.”                               a problem by dissolving their cognitive biases.
    Another approach to overcoming arbitrary narrowing or              3) Structure and Key Ideas: Fundamental contextual state-
limited targeting of the refined question is to combine the         ments:
Question Refinement pattern with other patterns. In particular,
this pattern can be combined with the Cognitive Verifier pattern       Contextual Statements
so the LLM automatically produces a series of follow-up ques-          Within scope X, if there are alternative ways to accom-
tions that can produce the refined question. For example, in           plish the same thing, list the best alternate approaches
the following prompt the Question Refinement and Cognitive             (Optional) compare/contrast the pros and cons of each
Verifier patterns are applied to ensure better questions are           approach
posed to the LLM:                                                      (Optional) include the original way that I asked
      “From now on, whenever I ask a question, ask four                (Optional) prompt me for which approach I would like
      additional questions that would help you produce a               to use
      better version of my original question. Then, use my             The first statement, “within scope X”, scopes the interaction
      answers to suggest a better version of my original            to a particular goal, topic, or bounds on the questioning. The
      question.”                                                    scope is the constraints that the user is placing on the alter-
    As with many patterns that allow an LLM to generate             native approaches. The scope could be “for implementation
new questions using its knowledge, the LLM may introduce            decisions” or “for the deployment of the application”. The
unfamiliar terms or concepts to the user into the question.         scope ensures that any alternatives fit within the boundaries
One way to address this issue is to include a statement that        or constraints that the user must adhere to.
the LLM should explain any unfamiliar terms it introduces into         The second statement, “if there are alternative ways to
the question. A further enhancement of this idea is to combine      accomplish the same thing, list the best alternate approaches”
instructs the LLM to suggest alternatives. As with other            into additional questions that can be used to provide a better
patterns, the specificity of the instructions can be increased or   answer to the original question.
include domain-specific contextual information. For example,           2) Motivation: The motivation of the Cognitive Verifier
the statement could be scoped to “if there are alternative ways     pattern is two-fold:
to accomplish the same thing with the software framework that          • Humans may initially ask questions that are too high-
I am using” to prevent the LLM from suggesting alternatives              level to provide a concrete answer to without additional
that are inherently non-viable because they would require too            follow-up due to unfamiliarity with the domain, laziness
many changes to other parts of the application.                          in prompt entry, or being unsure about what the correct
   Since the user may not be aware of the alternative ap-                phrasing of the question should be.
proaches, they also may not be aware of why one would                  • Research has demonstrated that LLMs can often perform
choose one of the alternatives. The optional statement “com-             better when using a question that is subdivided into
pare/contrast the pros and cons of each approach” adds de-               individual questions.
cision making criteria to the analysis. This statement ensures         3) Structure and Key Ideas: Fundamental contextual state-
the LLM will provide the user with the necessary rationale          ments:
for alternative approaches. The final statement, “prompt me
for which approach I would like to use”, helps eliminate the           Contextual Statements
user needing to manually copy/paste or enter in an alternative         When you are asked a question, follow these rules
approach if one is selected.                                           Generate a number of additional questions that would
   4) Example Implementation: Example prompt implementa-               help more accurately answer the question
tion to generate, compare, and allow the user to select one or         Combine the answers to the individual questions to
more alternative approaches:                                           produce the final answer to the overall question
     “Whenever I ask you to deploy an application to
                                                                       The first statement is to generate a number of additional
     a specific cloud service, if there are alternative
                                                                    questions that would help more accurately answer the original
     services to accomplish the same thing with the
                                                                    question. This step instructs the LLM to consider the context
     same cloud service provider, list the best alternative
                                                                    of the question and to identify any information that may be
     services and then compare/contrast the pros and cons
                                                                    missing or unclear. By generating additional questions, the
     of each approach with respect to cost, availability,
                                                                    LLM can help to ensure that the final answer is as complete
     and maintenance effort and include the original way
                                                                    and accurate as possible. This step also encourages critical
     that I asked. Then ask me which approach I would
                                                                    thinking by the user and can help to uncover new insights or
     like to proceed with.”
                                                                    approaches that may not have been considered initially, which
   This implementation of the Alternative Approaches pattern        subsequently lead to better follow-on questions.
is being specifically tailored for the context of software             The second statement is to combine the answers to the
engineering and focuses on the deployment of applications           individual questions to produce the final answer to the overall
to cloud services. The prompt is intended to intercept places       question. This step is designed to ensure that all of the infor-
where the developer may have made a cloud service selection         mation gathered from the individual questions is incorporated
without full awareness of alternative services that may be          into the final answer. By combining the answers, the LLM
priced more competitively or easier to maintain. The prompt         can provide a more comprehensive and accurate response to
directs ChatGPT to list the best alternative services that can      the original question. This step also helps to ensure that all
accomplish the same task with the same cloud service provider       relevant information is taken into account and that the final
(providing constraints on the alternatives), and to compare and     answer is not based on any single answer.
contrast the pros and cons of each approach.                           4) Example Implementation:
   5) Consequences: This pattern is effective in its generic
                                                                         “When I ask you a question, generate three addi-
form and can be applied to a range of tasks effectively.
Refinements could include having a standardized catalog of               tional questions that would help you give a more
acceptable alternatives in a specific domain from which the              accurate answer. When I have answered the three
                                                                         questions, combine the answers to produce the final
user must select. The Alternative Approaches pattern can also
be used to incentivize users to select one of an approved set            answers to my original question.”
of approaches while informing them of the pros/cons of the             This specific instance of the prompt pattern adds a refine-
approved options.                                                   ment to the original pattern by specifying a set number of
                                                                    additional questions that the LLM should generate in response
H. The Cognitive Verifier Pattern                                   to a question. In this case, the prompt specifies that ChatGPT
   1) Intent and Context: Research literature has documented        should generate three additional questions that would help to
that LLMs can often reason better if a question is subdivided       give a more accurate answer to the original question. The
into additional questions that provide answers combined into        specific number can be based on the user’s experience and
the overall answer to the original question [14]. The intent of     willingness to provide follow-up information. A refinement
the pattern is to force the LLM to always subdivide questions       to the prompt can be to provide a context for the amount
of knowledge that the LLM can assume the user has in the                Contextual Statements
domain to guide the creation of the additional questions:               Generate a set of facts that are contained in the output
                                                                        The set of facts should be inserted in a specific point
     “When I ask you a question, generate three addi-                   in the output
     tional questions that would help you give a more                   The set of facts should be the fundamental facts that
     accurate answer. Assume that I know little about                   could undermine the veracity of the output if any of
     the topic that we are discussing and please define                 them are incorrect
     any terms that are not general knowledge. When
     I have answered the three questions, combine the                  One point of variation in this pattern is where the facts are
     answers to produce the final answers to my original            output. Given that the facts may be terms that the user is not
     question.”                                                     familiar with, it is preferable if the list of facts comes after
                                                                    the output. This after-output presentation ordering allows the
   The refinement also specifies that the user may not have         user to read and understand the statements before seeing what
a strong understanding of the topic being discussed, which          statements should be checked. The user may also determine
means that the LLM should define any terms that are not             additional facts prior to realizing the fact list at the end should
general knowledge. This helps to ensure that the follow-up          be checked.
questions are not only relevant and focused, but also accessible       4) Example Implementation: A sample wording of the Fact
to the user, who may not be familiar with technical or domain-      Check List pattern is shown below:
specific terms. By providing clear and concise definitions, the
                                                                         “From now on, when you generate an answer, create
LLM can help to ensure that the follow-up questions are easy
                                                                         a set of facts that the answer depends on that should
to understand and that the final answer is accessible to users
                                                                         be fact-checked and list this set of facts at the
with varying levels of knowledge and expertise.
                                                                         end of your output. Only include facts related to
   5) Consequences: This pattern can dictate the exact number            cybersecurity.”
of questions to generate or leave this decision to the LLM.
                                                                       The user may have expertise in some topics related to the
There are pros and cons to dictating the exact number. A pro
                                                                    question but not others. The fact check list can be tailored to
is that specifying an exact number of questions can tightly
                                                                    topics that the user is not as experienced in or where there
scope the amount of additional information the user is forced
                                                                    is the most risk. For example, in the prompt above, the user
to provide so it is within a range they are willing and able to
                                                                    is scoping the fact check list to security topics, since these
contribute.
                                                                    are likely very important from a risk perspective and may not
   A con, however, is that given N questions there may be           be well-understood by the developer. Targeting the facts also
an invaluable N + 1 question that will always be scoped out.        reduces the cognitive burden on the user by potentially listing
Alternatively, the LLM can be provided a range or allowed           fewer items for investigation.
to ask additional questions. Of course, by omitting a limit on         5) Consequences: The Fact Check List pattern should be
the number of questions the LLM may generate numerous               employed whenever users are not experts in the domain for
additional questions that overwhelm the user.                       which they are generating output. For example, a software
                                                                    developer reviewing code could benefit from the pattern
                                                                    suggesting security considerations. In contrast, an expert on
I. The Fact Check List Pattern                                      software architecture is likely to identify errors in statements
                                                                    about the software structure and need not see a fact check list
   1) Intent and Context: The intent of this pattern is to ensure
                                                                    for these outputs.
that the LLM outputs a list of facts that are present in the
                                                                       Errors are potential in all LLM outputs, so Fact Check List
output and form an important part of the statements in the
                                                                    is an effective pattern to combine with other patterns, such
output. This list of facts helps inform the user of the facts
                                                                    as by combining it with the Question Refinement pattern. A
(or assumptions) the output is based on. The user can then
                                                                    key aspect of this pattern is that users can inherently check it
perform appropriate due diligence on these facts/assumptions
                                                                    against the output. In particular, users can directly compare the
to validate the veracity of the output.
                                                                    fact check list to the output to verify the facts listed in the fact
   2) Motivation: A current weakness of LLMs (including             check list actually appear in the output. Users can also identify
ChatGPT) is they often rapidly (and even enthusiastically!)         any omissions from the list. Although the fact check list may
generate convincing text that is factually incorrect. These         also have errors, users often have sufficient knowledge and
errors can take a wide range of forms, including fake statistics    context to determine its completeness and accuracy relative to
to invalid version numbers for software library dependencies.       the output.
Due to the convincing nature of this generated text, however,          One caveat of the Fact Check List pattern is that it only
users may not perform appropriate due diligence to determine        applies when the output type is amenable to fact-checking. For
its accuracy.                                                       example, the pattern works when asking ChatGPT to generate
 3) Structure and Key Ideas: Fundamental contextual state-          a Python “requirements.txt” file since it will list the versions
ments:                                                              of libraries as facts that should be checked, which is handy as
the versions commonly have errors. However, ChatGPT will            that component can be omitted. Ideally, placeholders should
refuse to generate a fact check list for a code sample and          use a format that is commonly employed in text that the LLM
indicate that this is something it cannot check, even though        was trained on, such as all caps, enclosure in brackets, etc.
the code may have errors.                                              The third statement attempts to constrain the LLM so that it
                                                                    doesn’t arbitrarily rewrite the template or attempt to modify it
J. The Template Pattern
                                                                    so that all of the output components can be inserted. It should
   1) Intent and Context: The intent of the pattern is to           be noted that this statement may not preclude additional text
ensure an LLM’s output follows a precise template in terms of       from being generated before or after. In practice, LLMs will
structure. For example, the user might need to generate a URL       typically follow the template, but it is harder to eliminate any
that inserts generated information into specific positions within   additional text being generated beyond the template without
the URL path. This pattern allows the user to instruct the LLM      experimentation with prompt wording.
to produce its output in a format it would not ordinarily use          4) Example Implementation: A sample template for gener-
for the specified type of content being generated.                  ating URLs where the output is put into specific places in the
   2) Motivation: In some cases, output must be produced in         template is shown below:
a precise format that is application or use-case specific and
                                                                          “I am going to provide a template for your out-
not known to the LLM. Since the LLM is not aware of the
                                                                          put. Everything in all caps is a placeholder. Any
template structure, it must be instructed on what the format
                                                                          time that you generate text, try to fit it into one
is and where the different parts of its output should go. This
                                                                          of the placeholders that I list. Please preserve the
could take the form of a sample data structure that is being
                                                                          formatting and overall template that I provide at
generated, a series of form letters being filled in, etc.
                                                                          https://myapi.com/NAME/profile/JOB”
   3) Structure and Key Ideas: Fundamental contextual state-
ments:                                                                 A sample interaction after the prompt was provided, is
                                                                    shown:
   Contextual Statements                                                  User: “Generate a name and job title for a person”
   I am going to provide a template for your output                       ChatGPT: “https://myapi.com/Emily Parker/profile/
   X is my placeholder for content                                        Software Engineer”
   Try to fit the output into one or more of the placehold-            5) Consequences: One consequence of applying the Tem-
   ers that I list                                                  plate pattern is that it filters the LLM’s output, which may
   Please preserve the formatting and overall template that         eliminate other outputs the LLM would have provided that
   I provide                                                        might be useful to the user. In many cases, the LLM can
   This is the template: PATTERN with PLACEHOLD-                    provide helpful descriptions of code, decision making, or other
   ERS                                                              details that this pattern will effectively eliminate from the
   The first statement directs the LLM to follow a specific         output. Users should therefore weight the pros/cons of filtering
template for its output. The template will be used to try and       out this additional information.
coerce the LLMs responses into a structure that is consistent          In addition, filtering can make it hard to combine this pattern
with the user’s formatting needs. This pattern is needed when       with other patterns from the Output Customization category.
the target format is not known to the LLM. If the LLM already       The Template pattern effectively constrains the output format,
has knowledge of the format, such as a specific file type, then     so it may not be compatible with generation of certain other
the template pattern can be skipped and the user can simply         types of output. For example, in the template provided above
specify the known format. However, there may be cases, such         for a URL, it would not be easy (or likely possible) to combine
as generating Javascript Object Notation (JSON), where there        with the Recipe pattern, which needs to output a list of steps.
is a large amount of variation in how the data could be
represented within that format and the template can be used to      K. The Infinite Generation Pattern
ensure that the representation within the target format meets          1) Intent and Context: The intent of this pattern is to
the user’s additional constraints.                                  automatically generate a series of outputs (which may appear
   The second statement makes the LLM aware that the                infinite) without having to reenter the generator prompt each
template will contain a set of placeholders. Users will explain     time. The goal is to limit how much text the user must type to
how the output should be inserted into the template through the     produce the next output, based on the assumption that the user
placeholders. The placeholders allow the user to semantically       does not want to continually reintroduce the prompt. In some
target where information should be inserted. Placeholders           variations, the intent is to allow the user to keep an initial
can use formats, like NAME, that allow the LLM to infer             prompt template, but add additional variation to it through
the semantic meaning of to determine where output should            additional inputs prior to each generated output.
be inserted (e.g., insert the person’s name in the NAME                2) Motivation: Many tasks require repetitive application of
placeholder). Moreover, by using placeholders, the user can         the same prompt to multiple concepts. For example, generating
indicate what is not needed in the output – if a placeholder        code for create, read, update, and delete (CRUD) operations
doesn’t exist for a component of the generated output, then         for a specific type of entity may require applying the same
prompt to multiple types of entities. If the user is forced to       placeholders for the name and job title. By using the Infinite
retype the prompt over and over, they may make mistakes. The         Generation pattern, the user receives multiple outputs without
Infinite Generation pattern allows the user to repetitively apply    having to continually re-enter the template. Likewise, the
a prompt, either with or without further input, to automate          Template pattern is applied to provide a consistent format for
the generation of multiple outputs using a predefined set of         the outputs.
constraints.                                                           5) Consequences: In conversational LLMs, the input to
   3) Structure and Key Ideas:                                       the model at each time step is the previous output and the
                                                                     new user input. Although the details of what is preserved
   Contextual Statements                                             and reintroduced in the next output cycle are model and
   I would like you to generate output forever, X output(s)          implementation dependent, they are often limited in scope. The
   at a time.                                                        model is therefore constantly being fed the previous outputs
   (Optional) here is how to use the input I provide                 and the prompt, which can result in the model losing track of
   between outputs.                                                  the original prompt instructions over time if they exceed the
   (Optional) stop when I ask you to.                                scope of what it is being provided as input.
                                                                       As additional outputs are generated, the context surrounding
    The first statement specifies that the user wants the LLM
                                                                     the prompt may fade, leading to the model deviating from
to generate output indefinitely, which effectively conveys the
                                                                     the intended behavior. It is important to monitor the outputs
information that the same prompt is going to be reused over
                                                                     produced by the model to (1) ensure it still adheres to
and over. By specifying the number of outputs that should be
                                                                     the desired behavior and (2) provide corrective feedback if
generated at a time (i.e. “X outputs at a time”), the user can
                                                                     necessary. Another issue to consider is that the LLM may
rate limit the generation, which can be particularly important if
                                                                     generate repetitive outputs, which may not be desired since
there is a risk that the output will exceed the length limitations
                                                                     users find this repetition tedious and error-prone to process.
of the LLM for a single output.
    The second statement provides optional instructions for how      L. The Visualization Generator Pattern
to use the input provided by the user between outputs. By               1) Intent and Context: The intent of this pattern is to use
specifying how additional user inputs between prompts can            text generation to create visualizations. Many concepts are
be provided and leveraged, the user can create a prompting           easier to grasp in diagram or image format. The purpose of
strategy that leverages user feedback in the context of the          this pattern is to create a pathway for the tool to produce
original prompt. The original prompt is still in the context of      imagery that is associated with other outputs. This pattern
the generation, but each user input between generation steps         allows the creation of visualizations by creating inputs for
is incorporated into the original prompt to refine the output        other well-known visualization tools that use text as their
using prescribed rules.                                              input, such as Graphviz Dot [15] or DALL-E [13]. This
    The third statement provides an optional way for the user        pattern can provide a more comprehensive and effective way
to stop the output generation process. This step is not always       of communicating information by combining the strengths of
needed, but can be useful in situations where there may be           both the text generation and visualization tools.
the potential for ambiguity regarding whether or not the user-          2) Motivation: LLMs generally produce text and cannot
provided input between inputs is meant as a refinement for           produce imagery. For example, an LLM cannot draw a diagram
the next generation or a command to stop. For example, an            to describe a graph. The Visualization Generator pattern over-
explicit stop phrase could be created if the user was generating     comes this limitation by generating textual inputs in the correct
data related to road signs, where the user might want to enter       format to plug into another tool that generates the correct
a refinement of the generation like “stop” to indicate that a        diagram. The motivation behind this pattern is to enhance the
stop sign should be added to the output.                             output of the LLM and make it more visually appealing and
    4) Example Implementation: The following is a sample             easier to understand for users. By using text inputs to generate
infinite generation prompt for producing a series of URLs:           visualizations, users can quickly understand complex concepts
      “From now on, I want you to generate a name                    and relationships that may be hard to grasp through text alone.
      and job until I say stop. I am going to provide a                 3) Structure and Key Ideas: Fundamental contextual state-
      template for your output. Everything in all caps is a          ments:
      placeholder. Any time that you generate text, try to
      fit it into one of the placeholders that I list. Please           Contextual Statements
      preserve the formatting and overall template that I               Generate an X that I can provide to tool Y to visualize
      provide: https://myapi.com/NAME/profile/JOB”                      it
    This prompt is combining the functionality of both the              The goal of the contextual statements is to indicate to the
Infinite Generation pattern and the Template pattern. The user       LLM that the output it is going to produce, “X”, is going to
is requesting the LLM continuously generate a name and job           be imagery. Since LLMs can’t generate images, the ”that I
title until explicitly told to “stop”. The generated outputs are     can provide to tool Y to visualize it” clarifies that the LLM
then formatted into the template provided, which includes            is not expected to generate an image, but is instead expected
to produce a description of imagery consumable by tool Y for           Contextual Statements
production of the image.                                               Create a game for me around X
   Many tools may support multiple types of visualizations or          One or more fundamental rules of the game
formats, and thus the target tool itself may not be sufficient         The first statement, instructs the LLM to create a game and
information to accurately produce what the user wants. The          provides the important scoping of the game to a topic area. .
user may need to state the precise types of visualizations (e.g.,   One of the important capabilities of the pattern is that it allows
bar chart, directed graph, UML class diagram) that should be        the user to create games by describing the rules of the game,
produced. For example, Graphviz Dot can create diagrams for         without having to determine the content of the game. The more
both UML class diagrams and directed graphs. Further, as will       specific the topic, typically the more novel and interesting the
be discussed in the following example, it can be advantageous       game play.
to specify a list of possible tools and formats and let the LLM        The second statement introduces the rules of the game to the
select the appropriate target for visualization.                    LLM. It is important that the rules fit within the capabilities
   4) Example Implementation:                                       of the LLM. Textual games that rely on input and output text
     “Whenever I ask you to visualize something, please             sequences work best. One of the key attributes of the pattern
     create either a Graphviz Dot file or DALL-E prompt             is that the input text can be rich and expressive, which can
     that I can use to create the visualization. Choose             lead to interesting interfaces for the game. For example, the
     the appropriate tools based on what needs to be                user might express actions in the game as scripts dictating
     visualized.”                                                   a sequence of complex actions, such as “get a listing of all
                                                                    network activity and check it for anomalies”, which go beyond
   This example of the pattern adds a qualification that the        the scope of multiple choice or short answer inputs. Each rule
output type for the visualization can be either for Graphviz        should be provided as a separate statement regarding some
or DALL-E. The interesting aspect of this approach is that          aspect of the game.
it allows the LLM to use its semantic understanding of the             4) Example Implementation: A sample cybersecurity game
output format to automatically select the target tooling based      prompt is shown below:
on what will be displayed. In this case, Graphviz would be for
                                                                         “We are going to play a cybersecurity game. You
visualizing graphs with a need for an exactly defined structure.
                                                                         are going to pretend to be a Linux terminal for a
DALL-E would be effective at visualizing realistic or artistic
                                                                         computer that has been compromised by an attacker.
imagery that does not have an exactly defined structure. The
                                                                         When I type in a command, you are going to output
LLM can select the tool based on the needs of the visualization
                                                                         the corresponding text that the Linux terminal would
and capabilities of each tool.
                                                                         produce. I am going to use commands to try and
   5) Consequences: The pattern creates a target pipeline                figure out how the system was compromised. The
for the output to render a visualization. The pipeline may               attack should have done one or more of the following
include AI generators, such as DALL-E, that can produce                  things: (1) launched new processes, (2) changed
rich visualizations. The pattern allows the user to expand the           files, (3) opened new ports to receive communi-
expressive capabilities of the output into the visual domain.            cation, (4) created new outbound connections, (5)
                                                                         changed passwords, (6) created new user accounts,
M. The Game Play Pattern                                                 or (7) read and stolen information. To start the game,
   1) Intent and Context: The intent of this pattern is to create        print a scenario of what happened that led to my
a game around a given topic. The pattern can be combined                 investigation and make the description have clues
with the Visualization Generator to add imagery to the game.             that I can use to get started.”
The game is centered around a specific topic and the LLM               This cybersecurity game prompt combines a number of pat-
will guide the game play. The pattern is particularly effective     terns, including Game Play and Persona. The Linux terminal
when the rules of the game are relatively limited in scope, but     persona that is chosen for the game has been discussed in many
the content for the game is expected to be wide in scope. The       Internet posts [16]. This game further customizes the discussed
user can specify a limited set of rules and then the LLM can        Linux persona to act as a Linux terminal of a computer
automate generation of bodies of content for game play.             compromised by a cyberattack. ChatGPT responds to Linux
   2) Motivation: You would like the LLM to generate scenar-        commands with appropriate terminal outputs and synthesizes
ios or questions revolving around a specific topic and require      a fake file system that has clues to a cyberattack.
users to apply problem solving or other skills to accomplish           Sample output from this game with ChatGPT after typing
a task related to the scenario. Generating all the content for      in “ls -alt”, the Linux command to generate a list of files in
the game manually would be too time consuming, however, so          the current directory is shown below (permissions have been
you would like the LLM to apply its knowledge of the topic          removed for formatting reasons):
to guide the generation of content.                                 total 56
   3) Structure and Key Ideas: Fundamental contextual state-         5 user user 4096 Feb 16 14:31 .
ments:                                                               1 user user 18881 Feb 16 14:31 .bash_history
43 user user          4096 Feb 16 14:30 ..                           3) Structure and Key Ideas: Fundamental contextual state-
 1 user user          1178 Aug 15 2022 .bashrc                    ments:
 1 user user            220 Aug 15 2022 .bash_logout
 3 user user          4096 Feb 16 14:25 .gnupg                        Contextual Statements
 1 user user          4041 Feb 15 17:52 README.md                     Whenever you generate an answer
 2 user user          4096 Feb 1 11:35 project                        Explain the reasoning and assumptions behind your
                                                                      answer
   When the user then typed the command “cat .bash history”,          (Optional) ...so that I can improve my question
to display the contents of the log file showing the commands
run by the user, ChatGPT responded with:                             The first statement is requesting that, after generating an an-
                                                                  swer, the LLM should explain the reasoning and assumptions
cd /var/www/html                                                  behind the answer. This statement helps the user understand
sudo rm -rf *                                                     how the LLM arrived at the answer and can help build trust in
sudo wget https://example.com/backdoor.php the model’s responses. The prompt includes the statement that
sudo chmod 777 backdoor.php                                       the purpose of the explanation is for the user to refine their
exit                                                              question. This additional statement gives the LLM the context
ls -alt                                                           it needs to better tailor its explanations to the specific purpose
ps -ef                                                            of aising the user in producing follow-on questions.
netstat -tulnp                                                       4) Example Implementation: This example tailors the
                                                                  prompt specifically to the domain of providing answers related
   In the output above, ChatGPT generated a fake log file with
                                                                  to code:
realistic commands for deleting the data being served by the
web server in /var/www/html and replacing the content                  ”When you provide an answer, please explain the
with a backdoor into the system.                                       reasoning and assumptions behind your selection
                                                                       of software frameworks. If possible, use specific
   5) Consequences: This pattern can be combined effectively
                                                                       examples or evidence with associated code samples
with the Persona, Infinite Generation, and Visualization Gen-
                                                                       to support your answer of why the framework is
erator patterns. For example, the cybersecurity game uses the
                                                                       the best selection for the task. Moreover, please
Persona pattern so the LLM can masquerade as a Linux termi-
                                                                       address any potential ambiguities or limitations in
nal. For a network security game, the Visualization Generator
                                                                       your answer, in order to provide a more complete
could be employed to add the ability to visualize the network
                                                                       and accurate response.”
topology and traffic flows.
                                                                     The pattern is further customized to instruct the LLM that
N. The Reflection Pattern                                         it should justify its selection of software frameworks, but not
                                                                  necessarily other aspects of the answer. In addition, the user
   1) Intent and Context: The goal of this pattern is to ask
                                                                  dictates that code samples should be used to help explain the
the model to automatically explain the rationale behind given
                                                                  motivation for selecting the specific software framework.
answers to the user. The pattern allows users to better assess       5) Consequences: One consequence of the Reflection pat-
the output’s validity, as well as inform users how an LLM tern is that it may not be effective for users who do not
arrived at a particular answer. Reflection can clarify any points understand the topic area of the discussion. For example, a
of confusion, uncover underlying assumptions, and reveal gaps highly technical question by a non-technical user may result
in knowledge or understanding.                                    in a complex rationale for the answer that the user cannot
   2) Motivation: LLMs can and do make mistakes. More- fathom. As with other prompt patterns, there is a risk the
over, users may not understand why an LLM is producing output may include errors or inaccurate assumptions included
a particular output and how to adapt their prompt to solve in the explanation of the rationale that the user may not be
a problem with the output. By asking LLM to automatically able to spot. This pattern can be combined with the Fact Check
explain the rationale behind its answers, users can gain a better List to help address this issue.
understanding of how the model is processing the input, what
assumptions it is making, and what data it is drawing on.         O. The Refusal Breaker Pattern
   LLMs may sometime provide incomplete, incorrect, or               1) Intent and Context: The goal of this pattern is to ask an
ambiguous answers. Reflection is an aid to help address these LLM to automatically help users rephrase a question when it
shortcomings and ensure the information provided by LLM refuses to give an answer. This pattern has the potential for
is as accurate. A further benefit of the pattern is that it can misuse, however, e.g., to generate phishing emails or perform
help users debug their prompts and determine why they are other actions that violate LLM policy filters. Caution should
not getting results that meet expectations. This pattern is therefore be exercised when applying this pattern to ensure
particularly effective for the exploration of topics that can it is used ethically and responsibly. This pattern has been
be confused with other topics or that may have nuanced used successfully in some LLMs to overcome the underlying
interpretations and where knowing the precise interpretation prompts used to program the LLM and prevent harmful output
that the LLM used is important.                                   generation.
   2) Motivation: LLMs may sometimes refuse to answer                      the meaning of life?” or “What are some common
a question, either because they do not have the required                   beliefs about the purpose of life?”
knowledge or because the question is phrased in a way that               5) Consequences: This pattern provides a potential path
they do not understand. This outcome may be frustrating               for misuse, so organizations, parents, or other stakeholders
for users who are looking for answers. In some situations,            may need to restrict the usage of the LLM. The first step in
therefore, the Refusal Breaker pattern can help users find a          going around guardrails on usage is to understand where the
way to either rephrase their question or ask a different question     guardrails are. In future work, a complement of this pattern
the LLM is better equipped to answer.                                 may be developed to hide the underlying prompt information
   For example, you could ask for clarification on why the            and rationale from users to prevent discovery.
question was refused, as there may be a specific reason why              Although the rationale and alternate rewordings are gener-
LLM could not provide an answer. Another approach is to               ated, there is no guarantee that users will be able to overcome
ask a different question that may be within its knowledge cut-        the refusal. The alternate questions that are generated may not
off or expertise. However, all these approaches require user          be of interest to the user or helpful in answering the original
intervention and knowledge of how to bypass the refusal.              question. The pattern mainly provides an aid in determining
   3) Structure and Key Ideas: Fundamental contextual state-          what the LLM can answer, but not a guarantee that it will
ments:                                                                answer a semantically equivalent variation of the original
                                                                      question.
   Contextual Statements
   Whenever you can’t answer a question
                                                                      P. The Context Manager Pattern
   Explain why you can’t answer the question
   Provide one or more alternative wordings of the ques-                 1) Intent and Context: The intent of this pattern is to enable
   tion that you could answer                                         users to specify or remove context for a conversation with
                                                                      an LLM. The goal is to focus the conversation on specific
   The first statement sets the stage that this set of instructions
                                                                      topics or exclude unrelated topics from consideration. This
should only be applied when a question can’t be answered.
                                                                      pattern gives users greater control over what statements the
The user does not want to trigger these instructions under
                                                                      LLM considers or ignores when generating output.
normal circumstances. The second statement instructs the
LLM to provide an explanation of why the question can’t be               2) Motivation: LLMs often struggle to interpret the in-
answered. The explanation is likely to include assumptions,           tended context of the current question or generate irrelevant
constraints, or misunderstandings that can be leveraged by the        responses based on prior inputs or irrelevant attention on
user to strategize about how to reword the question. Although         the wrong statements. By focusing on explicit contextual
just the explanation of why the question can’t be answered            statements or removing irrelevant statements, users can help
could help a user overcome the refusal, the pattern adds an           the LLM better understand the question and generate more
additional statement for the LLM to suggest rewordings that           accurate responses. Users may introduce unrelated topics or
would be acceptable. The pattern combines both reasoning              reference information from earlier in the dialogue, which
and suggested rewordings to improve the chances that the user         may can disrupt the flow of the conversation. The Context
will find a path around whatever roadblocks are preventing the        Manager pattern aims to emphasize or remove specific aspects
question form being answered.                                         of the context to maintain relevance and coherence in the
                                                                      conversation.
   4) Example Implementation: The Refusal Breaker pattern
                                                                         3) Structure and Key Ideas: Fundamental contextual state-
can be be implemented and applied with the following phras-
                                                                      ments:
ing:
     “Whenever you can’t answer a question, explain why                  Contextual Statements
     and provide one or more alternate wordings of the                   Within scope X
     question that you can’t answer so that I can improve                Please consider Y
     my questions.”                                                      Please ignore Z
  A sample discourse after using the pattern is shown below:             (Optional) start over
     User: What is the meaning of life?                                  Statements about what to consider or ignore should list key
     ChatGPT: As an AI language model, I do not                       concepts, facts, instructions, etc. that should be included or
     have personal beliefs or opinions. The meaning of                removed from the context. The more explicit the statements
     life is a complex philosophical question that has                are, the more likely the LLM will take appropriate action. For
     been pondered by humans for centuries and can                    example, if the user asks to ignore subjects related to a topic,
     vary greatly from person to person. It may be more               yet some of the those statements were discussed far back in the
     productive to rephrase the question in a way that can            conversation, the LLM may not properly disregard the relevant
     be answered by information and knowledge, such                   information. The more explicit the list is, therefore, the better
     as “What are some philosophical perspectives on                  the inclusion/exclusion behavior will be.
  4) Example Implementation: To specify context consider               3) Structure and Key Ideas: Fundamental contextual state-
using the following prompt:                                           ments:
     “When analyzing the following pieces of code, only
                                                                         Contextual Statements
     consider security aspects.”
                                                                         I would like to achieve X
  Likewise, to remove context consider using the following               I know that I need to perform steps A,B,C
prompt:                                                                  Provide a complete sequence of steps for me
     “When analyzing the following pieces of code, do                    Fill in any missing steps
     not consider formatting or naming conventions.”                     Identify any unnecessary steps
   Clarity and specificity are important when providing or               The first statement “I would like to achieve X” focuses the
removing context to/from an LLM so it can better understand           LLM on the overall goal that the recipe needs to be built
the intended scope of the conversation and generate more              to achieve. The steps will be organized and completed to
relevant responses. In many situations, the user may want to          sequentially achieve the goal specified. The second statement
completely start over and can employ this prompt to reset the         provides the partial list of steps that the user would like
LLM’s context:                                                        to include in the overall recipe. These serve as intermediate
     “Ignore everything that we have discussed. Start                 waypoints for the path that the LLM is going to generate or
     over.”                                                           constraints on the structure of the recipe. The next statement
                                                                      in the pattern, “provide a complete sequence of steps for
   The “start over” idea helps produce a complete reset of the
                                                                      me”, indicates to the LLM that the goal is to provide a
context.
                                                                      complete sequential ordering of steps. The “fill in any missing
   5) Consequences: One consequence of this pattern is that           steps” helps ensure that the LLM will attempt to complete
it may inadvertently wipe out patterns applied to the con-            the recipe without further follow-up by making some choices
versation that the user is unaware of. For example, if an             on the user’s behalf regarding missing steps, as opposed to
organization injects a series of helpful patterns into the start of   just stating additional information that is needed. Finally, the
a conversation, the user may not be aware of these patterns and       last statement, “identify any unnecessary steps,” is useful in
remove them through a reset of the context. This reset could          flagging inaccuracies in the user’s original request so that the
potentially eliminate helpful capabilities of the LLM, while          final recipe is efficient.
not making it obvious that the user will lose this functionality.        4) Example Implementation: An example usage of this
A potential solution to this problem is to include in the prompt      pattern in the context of deploying a software application to
a request to explain what topics/instructions will potentially be     the cloud is shown below:
lost before proceeding.
                                                                            “I am trying to deploy an application to the cloud. I
                                                                            know that I need to install the necessary dependen-
Q. The Recipe Pattern
                                                                            cies on a virtual machine for my application. I know
   1) Intent and Context: This pattern provides constraints to              that I need to sign up for an AWS account. Please
ultimately output a sequence of steps given some partially                  provide a complete sequence of steps. Please fill in
provided “ingredients” that must be configured in a sequence                any missing steps. Please identify any unnecessary
of steps to achieve a stated goal. It combines the Template,                steps.”
Alternative Approaches, and Reflection patterns.                         Depending on the use case and constraints, “installing
   2) Motivation: Users often want an LLM to analyze a                necessary dependencies on a virtual machine” may be an
concrete sequence of steps or procedures to achieve a stated          unnecessary step. For example, if the application is already
outcome. Typically, users generally know—or have an idea              packaged in a Docker container, the container could be de-
of—what the end goal should look like and what “ingredients”          ployed directly to the AWS Fargate Service, which does not
belong in the prompt. However, they may not necessarily know          require any management of the underlying virtual machines.
the precise ordering of steps to achieve that end goal.               The inclusion of the “identify unnecessary steps” language
   For example, a user may want a precise specification on how        will cause the LLM to flag this issue and omit the steps from
a piece of code should be implemented or automated, such as           the final recipe.
“create an Ansible playbook to ssh into a set of servers, copy           5) Consequences: One consequence of the recipe pattern is
text files from each server, spawn a monitoring process on            that a user may not always have a well-specified description
each server, and then close the ssh connection to each server.        of what they would like to implement, construct, or design.
In other words, this pattern represents a generalization of the       Moreover, this pattern may introduce unwanted bias from the
example of “given the ingredients in my fridge, provide dinner        user’s initially selected steps so the LLM may try to find a
recipes.” A user may also want to specify a set number of             solution that incorporates them, rather than flagging them as
alternative possibilities, such as “provide 3 different ways of       unneeded. For example, an LLM may try to find a solution
deploying a web application to AWS using Docker containers            that does install dependencies for a virtual machine, even if
and Ansible using step by step instructions”.                         there are solutions that do not require that.
                     IV. R ELATED W ORK                                 have been run by an attacker stored in a .bash history
                                                                        file. As shown in Section III, larger and more complex
   Software patterns [10], [11] have been extensively studied
                                                                        capabilities can be created by combining prompt patterns,
and documented in prior work. Patterns are widely used in
                                                                        such as combining the Game Play and Visualization
software engineering to express the intent of design structures
                                                                        Generator patterns.
in a way that is independent of implementation details. Patterns
                                                                      • Documenting prompt patterns as a pattern catalog is
provide a mental picture of the goals that the pattern is
                                                                        useful, but insufficient. Our experience indicates that
trying to achieve and the forces that it is trying to resolve.
                                                                        much more work can be done in this area, both in terms
A key advantage of patterns is their composability, allowing
                                                                        of refining and expanding the prompt patterns presented
developers to build pattern sequences and pattern languages
                                                                        in this paper, as well as in exploring new and innovative
that can be used to address complex problems. Patterns have
                                                                        ways of using LLMs. In particular, weaving the prompt
also been investigated in other domains, such as contract
                                                                        patterns captured here as a pattern catalog into a more
design for decentralized ledgers [17], [18].
                                                                        expression pattern language will help guide users of
   The importance of good prompt design with LLMs, such as
                                                                        LLMs more effectively.
ChatGPT, is well understood [19]–[28]. Previous studies have
                                                                      • LLM Capabilities will evolve over time, likely necessitat-
examined the effect of prompt words on AI generative models.
                                                                        ing refinement of patterns. As LLM capabilities change,
   For example, Liu et al. [29] investigated how different
                                                                        some patterns may no longer be necessary, be obviated
prompt key words affect image generation and different char-
                                                                        by different styles of interaction or conversation/session
acteristics of images. Other work has explored using LLMs
                                                                        management approaches, or require enhancement to func-
to generate visualizations [30]. Han et al. [31] researched
                                                                        tion correctly. Continued work will be needed to docu-
strategies for designing prompts for classification tasks. Other
                                                                        ment and catalog patterns that provide reusable solutions.
research has looked at boolean prompt design for literature
                                                                      • The prompt patterns are generalizable to many differ-
queries [32]. Yet other work has specifically examined prompts
                                                                        ent domains. Although most of the patterns have been
for software and fixing bugs [33].
                                                                        discussed in the context of software development, these
   Our work is complementary to prior work by providing
                                                                        same patterns are applicable in arbitrary domains, ranging
a structure for documenting, discussing, and reasoning about
                                                                        from infinite generation of stories for entertainment to
prompts that can aid users in developing mental models for
                                                                        educational games to explorations of topics.
structuring prompts to solve common problems.
   The quality of the answers produced by LLMs, particuarly            We hope that this paper inspires further research and de-
ChatGPT, has been assessed in a number of domains. For              velopment in this area that will help enhance prompt pattern
example, ChatGPT has been used to take the medical licensing        design to create new and unexpected capabilities for conver-
exam with surprisingly good results [3]. The use of ChatGPT         sational LLMs.
in Law School has also been explored [34]. Other papers have
looked at its mathematical reasoning abilities [35]. As more                                    R EFERENCES
domains are explored, we expect that domain-specific pattern        [1] R. Bommasani, D. A. Hudson, E. Adeli, R. Altman, S. Arora, S. von
catalogs will be developed to share domain-specific problem             Arx, M. S. Bernstein, J. Bohg, A. Bosselut, E. Brunskill et al.,
solving prompt structures.                                              “On the opportunities and risks of foundation models,” arXiv preprint
                                                                        arXiv:2108.07258, 2021.
                                                                    [2] Y. Bang, S. Cahyawijaya, N. Lee, W. Dai, D. Su, B. Wilie, H. Lovenia,
                 V. C ONCLUDING R EMARKS                                Z. Ji, T. Yu, W. Chung et al., “A multitask, multilingual, multimodal
                                                                        evaluation of chatgpt on reasoning, hallucination, and interactivity,”
   This paper presented a framework for documenting and                 arXiv preprint arXiv:2302.04023, 2023.
applying a catalog of prompt patterns for large language            [3] A. Gilson, C. Safranek, T. Huang, V. Socrates, L. Chi, R. A. Taylor,
models (LLMs), such as ChatGPT. These prompt patterns are               and D. Chartash, “How well does chatgpt do when taking the medical
                                                                        licensing exams?” medRxiv, pp. 2022–12, 2022.
analogous to software patterns and aim to provide reusable          [4] A. Carleton, M. H. Klein, J. E. Robert, E. Harper, R. K. Cunningham,
solutions to problems that users face when interacting with             D. de Niz, J. T. Foreman, J. B. Goodenough, J. D. Herbsleb, I. Ozkaya,
LLMs to perform a wide range of tasks. The catalog of prompt            and D. C. Schmidt, “Architecting the future of software engineering,”
                                                                        Computer, vol. 55, no. 9, pp. 89–93, 2022.
patterns captured via this framework (1) provides a structured      [5] “Github copilot · your ai pair programmer.” [Online]. Available:
way of discussing prompting solutions, (2) identifies patterns          https://github.com/features/copilot
in prompts, rather than focusing on specific prompt examples,       [6] O. Asare, M. Nagappan, and N. Asokan, “Is github’s copilot as bad
and (3) classifies patterns so users are guided to more efficient       as humans at introducing vulnerabilities in code?” arXiv preprint
                                                                        arXiv:2204.04741, 2022.
and effective interactions with LLMs.                               [7] H. Pearce, B. Ahmad, B. Tan, B. Dolan-Gavitt, and R. Karri, “Asleep at
   The following lessons learned were gleaned from our work             the keyboard? assessing the security of github copilot’s code contribu-
on prompt patterns:                                                     tions,” in 2022 IEEE Symposium on Security and Privacy (SP). IEEE,
                                                                        2022, pp. 754–768.
   • Prompt patterns significantly enrich the capabilities that     [8] J. Krochmalski, IntelliJ IDEA Essentials. Packt Publishing Ltd, 2014.
     can be created in a conversational LLM. For example,           [9] P. Liu, W. Yuan, J. Fu, Z. Jiang, H. Hayashi, and G. Neubig, “Pre-
                                                                        train, prompt, and predict: A systematic survey of prompting methods
     prompts can lead to the generation of cybersecurity                in natural language processing,” ACM Computing Surveys, vol. 55, no. 9,
     games, complete with fictitious terminal commands that             pp. 1–35, 2023.
[10] E. Gamma, R. Johnson, R. Helm, R. E. Johnson, and J. Vlissides,             [32] S. Wang, H. Scells, B. Koopman, and G. Zuccon, “Can chatgpt write
     Design patterns: elements of reusable object-oriented software. Pearson          a good boolean query for systematic review literature search?” arXiv
     Deutschland GmbH, 1995.                                                          preprint arXiv:2302.03495, 2023.
[11] D. C. Schmidt, M. Stal, H. Rohnert, and F. Buschmann, Pattern-oriented      [33] C. S. Xia and L. Zhang, “Conversational automated program repair,”
     software architecture, patterns for concurrent and networked objects.            arXiv preprint arXiv:2301.13246, 2023.
     John Wiley & Sons, 2013.                                                    [34] J. H. Choi, K. E. Hickman, A. Monahan, and D. Schwarcz, “Chatgpt
[12] OpenAI, “ChatGPT: Large-Scale Generative Language Models for                     goes to law school,” Available at SSRN, 2023.
     Automated Content Creation,” https://openai.com/blog/chatgpt/, 2023,        [35] S. Frieder, L. Pinchetti, R.-R. Griffiths, T. Salvatori, T. Lukasiewicz,
     [Online; accessed 19-Feb-2023].                                                  P. C. Petersen, A. Chevalier, and J. Berner, “Mathematical capabilities
[13] ——,         “DALL·E        2:     Creating    Images       from    Text,”        of chatgpt,” arXiv preprint arXiv:2301.13867, 2023.
     https://openai.com/dall-e-2/, 2023, [Online; accessed 19-Feb-2023].
[14] D. Zhou, N. Schärli, L. Hou, J. Wei, N. Scales, X. Wang, D. Schu-
     urmans, O. Bousquet, Q. Le, and E. Chi, “Least-to-most prompting
     enables complex reasoning in large language models,” arXiv preprint
     arXiv:2205.10625, 2022.
[15] J. Ellson, E. R. Gansner, E. Koutsofios, S. C. North, and G. Woodhull,
     “Graphviz and dynagraph—static and dynamic graph drawing tools,”
     Graph drawing software, pp. 127–148, 2004.
[16] S. Owen, “Building a virtual machine inside a javascript library,”
     https://www.engraved.blog/building-a-virtual-machine-inside/,       2022,
     accessed: 2023-02-20.
[17] P. Zhang, J. White, D. C. Schmidt, and G. Lenz, “Applying
     software patterns to address interoperability in blockchain-based
     healthcare apps,” CoRR, vol. abs/1706.03700, 2017. [Online]. Available:
     http://arxiv.org/abs/1706.03700
[18] X. Xu, C. Pautasso, L. Zhu, Q. Lu, and I. Weber, “A pattern collection
     for blockchain-based applications,” in Proceedings of the 23rd European
     Conference on Pattern Languages of Programs, 2018, pp. 1–20.
[19] E. A. van Dis, J. Bollen, W. Zuidema, R. van Rooij, and C. L. Bockting,
     “Chatgpt: five priorities for research,” Nature, vol. 614, no. 7947, pp.
     224–226, 2023.
[20] L. Reynolds and K. McDonell, “Prompt programming for large language
     models: Beyond the few-shot paradigm,” CoRR, vol. abs/2102.07350,
     2021. [Online]. Available: https://arxiv.org/abs/2102.07350
[21] J. Wei, X. Wang, D. Schuurmans, M. Bosma, E. H. Chi, Q. Le,
     and D. Zhou, “Chain of thought prompting elicits reasoning in
     large language models,” CoRR, vol. abs/2201.11903, 2022. [Online].
     Available: https://arxiv.org/abs/2201.11903
[22] J. Wei, Y. Tay, R. Bommasani, C. Raffel, B. Zoph, S. Borgeaud,
     D. Yogatama, M. Bosma, D. Zhou, D. Metzler, E. H. Chi,
     T. Hashimoto, O. Vinyals, P. Liang, J. Dean, and W. Fedus, “Emergent
     abilities of large language models,” 2022. [Online]. Available:
     https://arxiv.org/abs/2206.07682
[23] Y. Zhou, A. I. Muresanu, Z. Han, K. Paster, S. Pitis, H. Chan, and
     J. Ba, “Large language models are human-level prompt engineers,”
     2022. [Online]. Available: https://arxiv.org/abs/2211.01910
[24] T. Shin, Y. Razeghi, R. L. L. IV, E. Wallace, and S. Singh,
     “Autoprompt: Eliciting knowledge from language models with
     automatically generated prompts,” CoRR, vol. abs/2010.15980, 2020.
     [Online]. Available: https://arxiv.org/abs/2010.15980
[25] A. Radford, J. Wu, R. Child, D. Luan, D. Amodei, and I. Sutskever,
     “Language models are unsupervised multitask learners,” 2019.
[26] D. Zhou, N. Schärli, L. Hou, J. Wei, N. Scales, X. Wang,
     D. Schuurmans, C. Cui, O. Bousquet, Q. Le, and E. Chi, “Least-to-
     most prompting enables complex reasoning in large language models,”
     2022. [Online]. Available: https://arxiv.org/abs/2205.10625
[27] J. Jung, L. Qin, S. Welleck, F. Brahman, C. Bhagavatula, R. L.
     Bras, and Y. Choi, “Maieutic prompting: Logically consistent
     reasoning with recursive explanations,” 2022. [Online]. Available:
     https://arxiv.org/abs/2205.11822
[28] S. Arora, A. Narayan, M. F. Chen, L. Orr, N. Guha,
     K. Bhatia, I. Chami, and C. Re, “Ask me anything: A
     simple strategy for prompting language models,” in International
     Conference on Learning Representations, 2023. [Online]. Available:
     https://openreview.net/forum?id=bhUPJnS2g0X
[29] V. Liu and L. B. Chilton, “Design guidelines for prompt engineering
     text-to-image generative models,” in Proceedings of the 2022 CHI
     Conference on Human Factors in Computing Systems, 2022, pp. 1–23.
[30] P. Maddigan and T. Susnjak, “Chat2vis: Generating data visualisations
     via natural language using chatgpt, codex and gpt-3 large language
     models,” arXiv preprint arXiv:2302.02094, 2023.
[31] X. Han, W. Zhao, N. Ding, Z. Liu, and M. Sun, “Ptr: Prompt tuning
     with rules for text classification,” AI Open, vol. 3, pp. 182–192, 2022.
