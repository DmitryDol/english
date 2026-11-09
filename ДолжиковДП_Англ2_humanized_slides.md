# Adaptive-RAG: Slide Plan for the Oral Presentation (Humanized Version)

**Speaker:** Dmitry Dolzhikov  
**Slides:** 13  
**Speech:** 788 words, about 6 minutes at 130 words per minute (the speech is the humanized TASK 3 of `ДолжиковДП_Англ2_humanized.md`, split by slides without changes)

## Instructions for the presentation generator

1. Create a 16:9 presentation in English with exactly 13 slides, in the order given below.
2. Use the slide title and the "On-slide text" as the visible content. Keep the text short. Do not add facts, numbers or claims that are not in this document.
3. Copy the "Speaker notes" of each slide into the notes of that slide exactly as written.
4. Where an image is named, insert the attached file with that name on that slide, together with its caption in small font. Do not redraw, crop or recolour the charts. Where no image is named, do not invent charts or data; a simple layout or a neutral icon is enough.
5. Style: clean academic design, light background, one accent colour, a sans-serif font, large readable text, no more than one image per slide.

Image files to attach (from `articles/article2_figures/` in the repository): `figure2_panels_AB.png`, `figure2_panel_C.png`, `figure1.png`, `figure4.png`, `figure3.png`.

## Slide 1. Adaptive-RAG: Choosing a Retrieval Strategy by Question Complexity

**Time:** about 27 seconds (58 words)

**On-slide text:**

- Dmitry Dolzhikov
- Based on: S. Jeong, J. Baek, S. Cho, S. J. Hwang, J. C. Park. "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity". NAACL 2024, pp. 7036–7050

**Image:** none.

**Layout:** Title slide.

**Speaker notes:**

> Good afternoon, ladies and gentlemen. Thank you all for coming today. My name is Dmitry Dolzhikov. Today I am going to talk about the article "Adaptive-RAG: Learning to Adapt Retrieval-Augmented Large Language Models through Question Complexity". It was written by five researchers from KAIST in Korea and presented at NAACL 2024, a major conference on natural language processing.

## Slide 2. Why Retrieval?

**Time:** about 30 seconds (65 words)

**On-slide text:**

- LLM knowledge is stored in the model parameters
- It can be incomplete or out of date, so models give wrong facts
- Retrieval: search documents (e.g. Wikipedia) before answering
- Every search step costs time and computation

**Image:** none.

**Layout:** Text slide; a simple neutral icon is allowed, no charts.

**Speaker notes:**

> Large language models answer many questions well, but all they know is stored inside the model. That knowledge can be incomplete or out of date, so they sometimes get facts wrong. A common fix is retrieval. Before answering, the system searches a large collection of documents, such as Wikipedia, and gives the useful texts to the model. But every search costs time and computing power.

## Slide 3. Outline

**Time:** about 18 seconds (40 words)

**On-slide text:**

- The problem
- The method
- Experiments and main results
- What the results mean

**Image:** none.

**Layout:** Numbered list.

**Speaker notes:**

> To start with, I'll describe the problem the authors wanted to solve. Then I'll mention the method they propose. Next, I'll discuss their experiments and main results. Finally, I'll summarize what these results mean for people who build such systems.

## Slide 4. The Problem: Questions Differ in Complexity

**Time:** about 41 seconds (88 words)

**On-slide text:**

- Simple: "Paris is the capital of what?" (the model can answer alone)
- Complex: "When did the people who captured Malakoff come to the region where Philipsburg is located?" (4 reasoning steps)
- Single-step search is not enough for complex questions
- Multi-step search wastes time on simple questions

**Image:** `figure2_panels_AB.png` (`articles/article2_figures/figure2_panels_AB.png`). Caption: "Single-step (A) and multi-step (B) approaches. Source: Jeong et al., NAACL 2024, Figure 2."

**Layout:** Image across the top or right side, bullets beside or below it.

**Speaker notes:**

> Let's begin by looking at the problem. Some questions are easy and some are hard. The model can answer "Paris is the capital of what?" on its own. But "When did the people who captured Malakoff come to the region where Philipsburg is located?" takes four reasoning steps and facts from several documents. Most systems handle both questions the same way. Some always search once, and that isn't enough for the second question. Others search again and again, step by step, and waste time on the first one.

## Slide 5. Adaptive-RAG: Match the Effort to the Question

**Time:** about 41 seconds (89 words)

**On-slide text:**

- A: answer without search
- B: search once, then answer
- C: search several times, reasoning between the steps
- A small T5-Large classifier chooses A, B or C before any search

**Image:** `figure2_panel_C.png` (`articles/article2_figures/figure2_panel_C.png`). Caption: "The adaptive approach with a query-complexity classifier. Source: Jeong et al., NAACL 2024, Figure 2 (C)."

**Layout:** Image on the left, the three labels on the right.

**Speaker notes:**

> Where does that lead us? We need a system that decides how much effort each question deserves. That's the main idea of Adaptive-RAG. Well, I've told you about the problem. Now we'll move on to the method. The authors put three strategies together. With strategy A, the model answers without searching. With B, it searches once and then answers. With C, it searches several times and reasons between the steps. Before any search starts, a small classifier based on T5-Large reads the question and picks A, B or C.

## Slide 6. Training the Classifier without Manual Labels

**Time:** about 45 seconds (98 words)

**On-slide text:**

- Run all three strategies on training questions
- Label = the simplest strategy that answers correctly
- No strategy is correct: label by dataset type (single-hop → B, multi-hop → C)
- Example: an unlabelled HotpotQA question gets label C

**Image:** none.

**Layout:** Simple flow diagram drawn from these four points only; no extra facts or numbers.

**Speaker notes:**

> Let's consider this in more detail. How do you train such a classifier if no dataset says how complex its questions are? The authors make the labels themselves. They run all three strategies on the training questions, and each question gets the label of the simplest strategy that answers it correctly. If none of them works, the label depends on the dataset: questions from single-hop datasets get B, and questions from multi-hop datasets get C. A good example of this is HotpotQA. Its questions need several documents, so a HotpotQA question that no strategy answered gets label C.

## Slide 7. Experimental Setup

**Time:** about 23 seconds (49 words)

**On-slide text:**

- 6 open-domain QA datasets
- Single-hop: SQuAD, Natural Questions, TriviaQA
- Multi-hop: MuSiQue, HotpotQA, 2WikiMultiHopQA
- 3 LLMs: FLAN-T5-XL (3B), FLAN-T5-XXL (11B), GPT-3.5

**Image:** none.

**Layout:** Two columns: datasets on the left, models on the right.

**Speaker notes:**

> Let me turn now to the experiments. The authors used six well-known question answering datasets. SQuAD, Natural Questions and TriviaQA have simple single-hop questions. MuSiQue, HotpotQA and 2WikiMultiHopQA have complex multi-hop ones. Three language models wrote the answers: two FLAN-T5 models, with three and eleven billion parameters, and GPT-3.5.

## Slide 8. Results with GPT-3.5

**Time:** about 15 seconds (33 words)

**On-slide text:**

- Adaptive-RAG: F1 50.91, relative time 1.46
- Multi-step approach: F1 50.87, relative time 3.33
- The same accuracy in less than half of the time

**Image:** `figure1.png` (`articles/article2_figures/figure1.png`). Caption: "QA performance (F1) against time per query with GPT-3.5. Source: Jeong et al., NAACL 2024, Figure 1."

**Layout:** Large chart, three short lines beside it.

**Speaker notes:**

> What does this mean for accuracy and cost? With GPT-3.5, Adaptive-RAG got an F1 score of about fifty-one. The multi-step method scored practically the same, but it took more than twice as long.

## Slide 9. Results with FLAN-T5-XL (3B)

**Time:** about 24 seconds (53 words)

**On-slide text:**

- Adaptive-RAG: F1 46.94, relative time 3.60
- Multi-step approach: F1 48.85, relative time 8.81
- Adaptive Retrieval: F1 32.24, so Adaptive-RAG is 14.7 points higher

**Image:** `figure4.png` (`articles/article2_figures/figure4.png`). Caption: "QA performance (F1) against time per query with FLAN-T5-XL. Source: Jeong et al., NAACL 2024, Figure 4."

**Layout:** Large chart, three short lines beside it.

**Speaker notes:**

> With the smaller FLAN-T5 model, the one with three billion parameters, Adaptive-RAG was about two points behind the multi-step method and again took less than half of its time. In the same test it was almost fifteen F1 points ahead of Adaptive Retrieval, a method that only decides whether to search at all.

## Slide 10. Example: One Simple Question

**Time:** about 25 seconds (55 words)

**On-slide text:**

- Question: "Which famous corporate logo changed to a flat colour/color sans serif font in its first major change since 1999?"
- Adaptive Retrieval: label B, searched documents, answer "Microsoft" (wrong)
- Adaptive-RAG: label A, no search, answer "Google" (correct)

**Image:** none.

**Layout:** Two-column comparison table built from these lines (based on Table 5 of the article); mark wrong in red and correct in green.

**Speaker notes:**

> To give you an example, take a question about a famous company logo that switched to a flat font in its first big redesign since 1999. Adaptive-RAG decided the model could answer from memory, and the answer was right: Google. Adaptive Retrieval went searching, picked up partly irrelevant text about Microsoft and got it wrong.

## Slide 11. The Weak Point: The Classifier

**Time:** about 21 seconds (46 words)

**On-slide text:**

- Correct label for 54.5% of questions
- Easy questions are often sent to search
- With an ideal (oracle) classifier: F1 62.80 with GPT-3.5

**Image:** `figure3.png` (`articles/article2_figures/figure3.png`). Caption: "Classifier performance with FLAN-T5-XL and XXL (left, centre) and the confusion matrix (right). Source: Jeong et al., NAACL 2024, Figure 3."

**Layout:** Wide image across the slide, bullets under it.

**Speaker notes:**

> The classifier is still the weak point. It picks the right label for only about fifty-five percent of questions, and it often sends easy questions to search when they don't need it. With a perfect classifier, the F1 score with GPT-3.5 would rise to almost sixty-three.

## Slide 12. Conclusions

**Time:** about 32 seconds (70 words)

**On-slide text:**

- Questions differ in complexity: one fixed strategy wastes resources or fails
- Choosing a strategy per question: accuracy close to multi-step search in less than half of the time
- Next steps: better complexity labels and better classifiers

**Image:** none.

**Layout:** Three numbered points.

**Speaker notes:**

> In conclusion, let me sum up the main findings. First, questions differ in difficulty, so one fixed strategy either wastes resources or fails on hard questions. Second, a small classifier that picks a strategy for each question gets almost the accuracy of multi-step search in less than half the time. Third, the classifier is the part that most needs work, and the authors plan better complexity labels and better classifiers.

## Slide 13. Key Message

**Time:** about 20 seconds (44 words)

**On-slide text:**

- Before spending resources on an answer, ask how difficult the question really is
- Thank you! Questions?

**Image:** none.

**Layout:** Large quote in the centre, "Thank you! Questions?" below it.

**Speaker notes:**

> If you take just one thing from this talk, take this: before a system spends resources on an answer, it should ask how difficult the question really is. Many thanks for your attention. Now I'll be glad to answer any questions you may have.
