                                                                                                                  ISSN (Online) 2581-9429
                                                                     IJARSCT
                      International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)
                         International Open-Access, Double-Blind, Peer-Reviewed, Refereed, Multidisciplinary Online Journal
Impact Factor: 7.67                                         Volume 5, Issue 2, March 2025


             A Comprehensive Study on Prompt Engineering
                                     Nihala M S1, Pranav Lal K B1, Rahul Raj PS1, Ms. Siji K B2
                        Students, MCA, Vidya Academy of Science and Technology Thalakkottukara, Thrissur, India1
                                       Assistant Professor, Department of Computer Applications2
                                Vidya Academy of Science and Technology, Thalakkottukara, Thrissur, India

                 Abstract: Prompt engineering has become a vital technique in artificial intelligence (AI), enhancing
                 interactions with large language models (LLMs) and vision-language models (VLMs). By strategically
                 crafting prompts, this approach improves AI performance across domains such as natural language
                 processing (NLP), computer vision (CV), and healthcare. Techniques like zero-shot, few-shot, chain-of-
                 thought (CoT), and retrieval-based prompting refine model responses, increasing accuracy and efficiency.
                 Hard and soft prompting methods play distinct roles, balancing interpretability and customization.
                 Applications range from content generation and conversational AI to medical diagnostics and education.
                 As AI evolves, prompt engineering remains crucial for optimizing model adaptability, ensuring responsible
                 AI usage, and expanding automation. This study provides a comprehensive analysis of methodologies,
                 applications, and future directions in prompt engineering, highlighting its transformative impact on AI-
                 driven solutions.

                 Keywords: Prompt Engineering, AI Optimization, NLP, Chain-of-Thought, Automation

                                                           I. INTRODUCTION
         Prompt engineering has emerged as a crucial field in artificial intelligence (AI), enabling more efficient and accurate
         interactions with large language models (LLMs) and vision-language models (VLMs). With the rapid advancements in
         AI, designing effective prompts has become essential for optimizing model performance across diverse domains such as
         natural language processing (NLP), computer vision (CV), and healthcare applications. The six reviewed documents
         collectively explore the theoretical foundations, methodologies, and applications of prompt engineering, highlighting its
         significance in guiding AI models toward generating more contextually relevant and high-quality outputs.
         Recent developments in prompt engineering have demonstrated its ability to enhance the generalization and adaptability
         of AI models. In the field of NLP, prompt engineering techniques such as zero-shot, few-shot, chain-of-thought (CoT),
         and retrieval-augmented generation (RAG) have significantly improved the quality of responses in tasks like text
         generation, summarization, and question answering. Similarly, in computer vision, visual prompt engineering has been
         instrumental in improving tasks such as image classification, segmentation, and object detection, leveraging models like
         CLIP and SAM to achieve better text-image alignment. Furthermore, in healthcare, prompt engineering is
         revolutionizing AI-driven medical applications, aiding in clinical decision-making, automated diagnosis, and medical
         text processing while addressing challenges related to data privacy, ethical considerations, and domain-specific
         adaptations.
         As AI continues to evolve, prompt engineering is expected to play a pivotal role in refining model interactions,
         increasing efficiency, and expanding the applicability of AI systems. This review provides a comprehensive analysis of
         prompt engineering methodologies, examining how structured prompt design enhances the performance of LLMs and
         VLMs across multiple domains. By synthesizing recent research, this study aims to contribute to the ongoing
         advancements in AI, offering insights into the development and future potential of prompt engineering.

                                               II. WHY PROMPT ENGINEERING ?
         Prompt engineering has emerged as a critical technique in artificial intelligence models, enabling more efficient and
         accurate AI interactions. Rather than fine-tuning entire models, which is costly and time-consuming, prompt
         engineering provides a way to adapt pre-trained systems to new tasks with minimal labeled data


         Copyright to IJARSCT                          DOI: 10.48175/IJARSCT-23769                                                   420
         www.ijarsct.co.in
                                                                                                                  ISSN (Online) 2581-9429
                                                                     IJARSCT
                      International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)
                         International Open-Access, Double-Blind, Peer-Reviewed, Refereed, Multidisciplinary Online Journal
Impact Factor: 7.67                                         Volume 5, Issue 2, March 2025

         As AI technologies continue to evolve, prompt engineering is becoming an essential skill for enhancing AI reliability,
         improving adaptability, and ensuring responsible AI usage. Its growing importance highlights the need for continued
         research and development in designing structured, specialized, and automated prompting methods




                                                                  Fig. 1 Prompt

                                            III. METHODS OF PROMPT ENGINEERING
         Prompt engineering refers to the practice of crafting prompts that effectively direct AI models to produce the desired
         outputs. This practice is essential within the field of Natural Language Processing (NLP), as it involves the strategic
         organization of prompt information to bolster the problem-solving abilities of AI systems. A comprehensive
         understanding of these techniques can lead to significant enhancements in the efficacy of NLP models.




                                                   Fig.2 Large Language Model (LLM)
         Prompting can be divided into two main categories: hard prompting and soft prompting. Hard prompting entails the
         manual creation of explicit and structured prompts that utilize clear instructions, examples, or reasoning strategies, all
         without altering the underlying model. This approach is straightforward and does not necessitate additional training.
         Conversely, soft prompting represents a more sophisticated method, wherein prompts are refined through machine-
         learned embeddings or adjustments to model parameters. Unlike hard prompts, soft prompts are not easily interpretable
         by humans and require specialized training to optimize AI performance for particular tasks. While hard prompting
         offers flexibility and ease of use, soft prompting allows for greater customization and efficiency in handling complex
         AI applications.
         Numerous prompting techniques exist, with Sahoo et al. (2024) identifying 29 distinct methods, some of which are
         variations of others, while others are specifically designed for particular tasks. A prominent technique is Few-Shot (FS)
         Prompting, which provides models with examples of similar tasks and their corresponding solutions prior to executing
         the actual task. This method resonates with Bandura and Jeffrey's theory of observational learning, positing that models,
         akin to humans, can acquire knowledge through examples. The array of prompting techniques is crucial for refining AI
         outputs and improving the overall performance of models.

         Hard Prompting :
         1. Task Instruction Prompting
         Task instruction prompting entails clearly defining the actions the model should undertake within the prompt itself.
         These prompts act as explicit directives that shape the model's output. For instance, in a translation scenario, a prompt

         Copyright to IJARSCT                          DOI: 10.48175/IJARSCT-23769                                                   421
         www.ijarsct.co.in
                                                                                                                  ISSN (Online) 2581-9429
                                                                     IJARSCT
                      International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)
                         International Open-Access, Double-Blind, Peer-Reviewed, Refereed, Multidisciplinary Online Journal
Impact Factor: 7.67                                         Volume 5, Issue 2, March 2025

         like “Translate the following sentence into French:” delivers a straightforward instruction that directs the model
         towards the intended task. This method is especially useful for structured problems where the instructions are uniform
         across various inputs. The benefits of task instruction prompting include enhanced clarity and the elimination of the
         need for additional model training. However, it can be somewhat inflexible, as fixed instructions may not encompass all
         task variations and rely on human skill to formulate accurate prompts.

         2. In-Context Learning
         In-context learning improves a model's capacity to recognize patterns and produce responses based on given examples.
         Rather than depending on direct instructions, this technique utilizes a series of input-output pairs within the prompt,
         enabling the model to discern relationships and extrapolate the anticipated output for new inputs. Large language
         models, such as GPT-4, are particularly adept at this method, utilizing their pre-existing knowledge without the need for
         parameter adjustments. A significant benefit of in-context learning is its adaptability, facilitating zero-shot or few-shot
         learning with minimal input. Nonetheless, the model's effectiveness can fluctuate based on the arrangement of examples
         and the length of the prompt, as there is a limit to the amount of context that can be included.

         3. Retrieval-Based Prompting
         Retrieval-based prompting dynamically selects relevant information from an external source or knowledge base to
         enrich the input prompt. Instead of relying solely on pre-defined text, the model retrieves contextual examples or facts
         that enhance its response generation. This method ensures that the model stays up to date with the latest information
         and adapts its output based on the retrieved content. A retrieval function selects the most relevant context based on the
         input query, helping the model produce more precise and task-specific results. This approach is beneficial for real-
         world applications such as question-answering systems and customer support bots. However, its effectiveness depends
         on the quality of the retrieval mechanism and the comprehensiveness of the external database, which can introduce
         additional complexity.

         4. Chain-of-Thought Prompting
         Chain-of-thought prompting is a method of prompting in machine learning (ML) that allows a model to explicitly
         describe the steps leading to a conclusion, enhancing the quality of output. This method, similar to concurrent thinking
         aloud, is useful for tasks that require complex operations on textual information. However, not all tasks require CoT
         prompting, and understanding this method is crucial for users. CoT prompting has sparked research in machine learning
         (PE), with a focus on Graph-of-Thought and X-of-Thought reasoning strategies. The goal is to "interiorize" higher-
         order reasoning in LLM, making it automatically apply the steps without explicitly spelling them out. This approach is
         similar to Vygotsky's concept of interiorization, which suggests that higher psychological functions develop with
         external support in the real world and then become executed internally within the human mind.

         5. Tree of thought Prompting
         Tree-of-thought prompting is a generalization of CoT that has gained prominence due to its non-technical
         implementation. It involves a collaborative brainstorming session among experts, where each expert writes down a step
         in their thinking and shares it with the group. If any expert realizes they are wrong, they leave. This method allows the
         model to fulfill multiple roles and potentially enhances its performance. Self-consistency is another technique used to
         enhance model performance, posing the same question multiple times and determining the most frequently occurring
         response. This concept is similar to the wisdom of crowds, where a collective group of individuals often makes more
         accurate judgments than individual members. In LLMs, the model is treated as if it were a crowd of people, with each
         new attempt acting as an independent opinion. Self-fact-checking is another strategy that helps mitigate LLM
         hallucinations. Originally designed as a chat-bot function, users can manually adopt this technique, which divides
         responses into individual claims, verifies their accuracy separately, and constructs a final response from those which are
         correct. This practice draws strong parallels with retrospective thinking aloud, focusing on the evaluation of
         information rather than its generation.

         Copyright to IJARSCT                          DOI: 10.48175/IJARSCT-23769                                                   422
         www.ijarsct.co.in
                                                                                                                  ISSN (Online) 2581-9429
                                                                     IJARSCT
                      International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)
                         International Open-Access, Double-Blind, Peer-Reviewed, Refereed, Multidisciplinary Online Journal
Impact Factor: 7.67                                         Volume 5, Issue 2, March 2025

         Soft Prompting
         1. Prompt Tuning
         Prompt tuning consists of training a collection of soft embeddings that function as an optimized prefix tailored for a
         specific task. These embeddings serve as learned representations that alter the input to improve the model's
         effectiveness for defined tasks. In contrast to conventional fine-tuning, which involves modifying the entire model,
         prompt tuning exclusively adjusts the learned prompt embeddings, leaving the core model intact. This approach
         enhances efficiency and adaptability, particularly for large language models, as it diminishes computational expenses
         while preserving flexibility. Nonetheless, the non-human-readable nature of the learned prompts can pose difficulties
         for debugging or understanding the tuning process.

         2. Prefix Tuning
         Prefix tuning builds upon the concept of prompt tuning by incorporating a trainable sequence of soft tokens into the
         input of the model. Rather than altering the entire architecture of the model, this approach introduces a limited set of
         learnable parameters at the input layer, which directs the generation process. These prefixes act as memory slots that
         modify the model's output while leaving its underlying weights unchanged. This technique is particularly advantageous
         for domain adaptation, allowing a general language model to become specialized in a specific field without
         necessitating complete retraining. While this method is highly efficient, its success is contingent upon the ability of the
         learned prefixes to generalize effectively across various tasks.

         Prompt Engineering for Knowledge Creation: Using Chain-of-Thought to Support Students’ Improvable Ideas
         This study explores the use of prompt engineering in knowledge creation by leveraging the Chain-of-Thought (CoT)
         approach in large language models (LLMs) to support student discourse. The research investigates how CoT-enhanced
         AI prompts can improve idea quality, reasoning depth, and collaborative learning in educational environments.
         A dataset of 721 discourse turns from a student Knowledge Building Design Studio (sKBDS) was analyzed, consisting
         of 272 relevant question–answer pairs and 149 discussion threads. The study compared original student responses with
         those generated by LLMs using CoT prompting. Findings revealed that CoT-enhanced prompts helped students refine
         their ideas by providing more structured reasoning and deeper insights.
         The results indicate that CoT enhances knowledge building by encouraging step-by-step reasoning, leading to more
         meaningful student contributions. This approach supports educational AI applications by allowing students to engage in
         critical thinking and structured problem-solving without requiring extensive AI fine-tuning.
         This study suggests that prompt engineering techniques, particularly CoT prompting, can significantly improve student
         discourse and idea development, making AI-assisted knowledge creation more effective in educational settings.
         EXAMPLE
         Example of Standard Prompting:
         Q: Why do we wear seat belts in a car?
         ANS: To stay safe in case of an accident.
         Q: Why do we wear seat belts in a car? Think step by step.
         ANS:
         When a car stops suddenly, passengers keep moving due to inertia.
         If not restrained, they can hit the dashboard or be thrown out.
         A seat belt holds them in place, preventing serious injuries.
         This reduces the risk of fatal accidents.
         That's why we wear seat belts in a car.

                                          IV. APPLICATIONS IN PROMPT ENGINEERING
         Prompt engineering is integral to enhancing AI interactions across various sectors, facilitating automation, and boosting
         operational efficiency. The following outlines its primary applications:



         Copyright to IJARSCT                          DOI: 10.48175/IJARSCT-23769                                                   423
         www.ijarsct.co.in
                                                                                                                  ISSN (Online) 2581-9429
                                                                     IJARSCT
                      International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)
                         International Open-Access, Double-Blind, Peer-Reviewed, Refereed, Multidisciplinary Online Journal
Impact Factor: 7.67                                         Volume 5, Issue 2, March 2025

         1. Natural Language Processing & Conversational AI
         Prompt engineering is vital for the creation of sophisticated chatbots and virtual assistants. It enhances user engagement
         by producing responses that are more natural and contextually relevant. AI-enabled customer support systems utilize
         prompt engineering to deliver immediate solutions, thereby minimizing the need for human involvement.

         2. Content Generation & Summarization
         By employing meticulously designed prompts, AI models can produce high-quality content, such as articles, reports,
         and creative writing. Furthermore, prompt engineering improves text summarization capabilities, enabling the
         distillation of extensive information into succinct and meaningful summaries, which are particularly beneficial in
         journalism, academia, and research.

         3. Software Development & Code Assistance
         In the realm of software development, prompt engineering is employed to generate, debug, and optimize code. AI-
         driven coding assistants can offer suggestions, rectify errors, and even compose complete scripts, thereby enhancing the
         efficiency of software development processes. Additionally, it facilitates the learning of new programming languages
         and the automation of documentation creation.

         4. Education & Personalized Learning
         AI-enhanced educational tools leverage prompt engineering to customize learning resources for individual students.
         This approach aids in the generation of quizzes, interactive exercises, and comprehensive explanations, making the
         learning experience more engaging and effective. Researchers can also utilize AI to summarize academic papers and
         recommend pertinent literature.

         5. Healthcare & Medical Applications
         In healthcare, prompt engineering underpins AI applications by summarizing patient records, aiding in diagnostic
         processes, and automating medical documentation. AI models can analyze symptoms, propose treatment options, and
         enhance telemedicine services, thereby improving healthcare accessibility.

         6. Legal & Business Automation
         Legal professionals employ AI-driven solutions to streamline various processes.

                                                               V. CONCLUSION
         Prompt engineering serves as an essential methodology for enhancing AI interactions across a multitude of fields,
         including natural language processing, computer vision, healthcare, and education. By utilizing both structured hard and
         soft prompts, AI models can attain improved adaptability, efficiency, and accuracy. Innovative approaches such as
         Chain-of-Thought and Retrieval-Based Prompting significantly bolster model reasoning and the quality of outputs. As
         the field of AI progresses, prompt engineering will be instrumental in advancing AI reliability, addressing ethical
         concerns, and facilitating automation. Future developments in automated and dynamic prompting are expected to
         further elevate AI capabilities, establishing it as a critical competency for developers and researchers.

                                                          REFERENCES
         [1]. Ggaliwango Marvin, Nakayiza Hellen, Daudi Jjingo, Joyce Nakatumba-Nabende, "Prompt Engineering in
         LargeLanguageModels,"2024.
         [2] . Jindong Gu, Zhen Han, Shuo Chen, Ahmad Beirami, Bailan He, Gengyuan Zhang, Ruotong Liao, Yao Qin,
         Volker Tresp, Philip Torr, "A Systematic Survey of Prompt Engineering on Vision-Language Foundation Models,"
         2023.
         [3]. Alwyn Vwen Yen Lee, Chew Lee Teo, Seng Chee Tan, "Prompt Engineering for Knowledge Creation: Using
         Chain-of-ThoughttoSupportStudents'ImprovableIdeas,"2024.
         [4]. Denis Federiakin, Dimitri Molerov, Olga Zlatkin-Troitschanskaia, Andreas Maur, "Prompt Engineering as a New
         Copyright to IJARSCT                          DOI: 10.48175/IJARSCT-23769                                                   424
         www.ijarsct.co.in
                                                                                                                  ISSN (Online) 2581-9429
                                                                     IJARSCT
                      International Journal of Advanced Research in Science, Communication and Technology (IJARSCT)
                         International Open-Access, Double-Blind, Peer-Reviewed, Refereed, Multidisciplinary Online Journal
Impact Factor: 7.67                                         Volume 5, Issue 2, March 2025

         21stCentury.Skill,"2024.
         [5]. Jiaqi Wang, Zhengliang Liu, Lin Zhao, Zihao Wu, Chong Ma, Sigang Yu, Haixing Dai, Qiushi Yang, Yiheng Liu,
         Songyao Zhang, Enze Shi, Yi Pan, Tuo Zhang, Dajiang Zhu, Xiang Li, Xi Jiang, Bao Ge, Yixuan Yuan, Dinggang
         Shen, Tianming Liu, Shu Zhang, "Review of Large Vision Models and Visual Prompt Engineering," 2023.
         [6]. Jiaqi Wang, Enze Shi, Sigang Yu, Zihao Wu, Chong Ma, Haixing Dai, Qiushi Yang, Yanqing Kang, Jinru Wu,
         Huawen Hu, Chenxi Yue, Haiyang Zhang, Yiheng Liu, Yi Pan, Zhengliang Liu, Lichao Sun, Xiang Li, Bao Ge, Xi
         Jiang, Dajiang Zhu, Yixuan Yuan, Dinggang Shen, Tianming Liu, Shu Zhang, "Prompt Engineering for Healthcare:
         Methodologies and Applications," 2024.
         [7] .Brown, T., Mann, B., Ryder, N., Subbiah, M., Kaplan, J., Dhariwal, P., et al., "Language Models are Few-Shot
         Learners," Advances in Neural Information Processing Systems, 2020.
         [8]. Kirillov, A., Mintun, E., Ravi, N., Mao, H., Rolland, C., Gustafson, L., et al., "Segment Anything," arXiv preprint
         arXiv:2304.02643,2023.
         [9]. Lester, B., Al-Rfou, R., & Constant, N., "The Power of Scale for Parameter-Efficient Prompt Tuning," Proceedings
         of the 2021 Conference on Empirical Methods in Natural Language Processing, 2021.
         [10]. Radford, A., Kim, J. W., Hallacy, C., Ramesh, A., Goh, G., Agarwal, S., et al., "Learning Transferable Visual
         Models from Natural Language Supervision," International Conference on Machine Learning, 2021.
         [11]. Reynolds, L., & McDonell, K., "Prompt Programming for Large Language Models: Beyond the Few-Shot
         Paradigm," arXiv preprint arXiv:2102.07350, 2021.
         [12]. Wei, J., Wang, X., Schuurmans, D., Bosma, M., Chi, E. H., Le, Q. V., et al., "Chain-of-Thought Prompting Elicits
         Reasoning in Large Language Models," Advances in Neural Information Processing Systems, 2022.
         [13]. Mazurowski, M. A., Dong, H., Gu, H., Yang, J., Konz, N., Zhang, Y., Segment Anything Model for Medical
         Image Analysis: An Experimental Study, Medical Image Analysis, vol. 89, pp. 102918, 2023.
         [14]. Wu, J., Fu, R., Fang, H., et al., Medical SAM Adapter: Adapting Segment Anything Model for Medical Image
         Segmentation, arXiv preprint arXiv:2304.12620, 2023.
         [15]. He, S., Bao, R., Li, J., Grant, P. E., Ou, Y., Accuracy of Segment-Anything Model (SAM) in Medical Image
         Segmentation Tasks, arXiv preprint arXiv:2304.09324, 2023.
         [16].Shi, P., Qiu, J., Abaxi, S. M. D., Wei, H., Lo, F. P. W., Yuan, W., Generalist Vision Foundation Models for
         Medical Imaging: A Case Study of Segment Anything Model on Zero-Shot Medical Segmentation, Diagnostics, vol. 13,
         no. 11, pp. 1947, 2023.
         [17].Zhang, Y., Zhou, T., Liang, P., Chen, D. Z., Input Augmentation with SAM: Boosting Medical Image Segmentation
         with Segmentation Foundation Model, International Conference on Medical Image Computing and Computer-Assisted
         Intervention, Cham: Springer Nature Switzerland, pp. 129–139, 2023.
         [18].Chase,        H.,     Welcome        to       LangChain—LangChain            0.0.154      [Online].     Available:
         https://python.langchain.com/en/latest/index.html. Accessed 01 May 2023.
         [19]. Dust, Design and Deploy Large Language Models Apps [Online]. Available: https://dust.tt/. Accessed 01 May
         2023.
         [20]. OpenPrompt, OpenPrompt [Online]. Available: https://openprompt.co/. Accessed 01 May 2023.
         [21]. The Art & Science of AI Prompts, The Art & Science of AI Prompts [Online]. Available:
         https://www.betterprompts.ai/. Accessed 01 May 2023.
         [22].PromptEngines.com,PromptEngines.com[Online].Available:https://www.afternic.com/forsale/promptengines.com.
         Accessed 01 May 2023.




         Copyright to IJARSCT                          DOI: 10.48175/IJARSCT-23769                                                   425
         www.ijarsct.co.in
